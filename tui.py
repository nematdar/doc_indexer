from textual.app import ComposeResult, RenderableType
from textual.containers import Container, Vertical, Horizontal, ScrollableContainer
from textual.widgets import Header, Footer, Input, Button, Static, RichLog
from textual.reactive import reactive
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin
from textual.app import App


class InputBox(Static):
    """A styled input box with a label and textbox."""
    
    DEFAULT_CSS = """
    InputBox {
        height: auto;
    }
    """
    
    def __init__(self, label: str, placeholder: str, input_id: str):
        super().__init__()
        self.label_text = label
        self.placeholder = placeholder
        self.input_id = input_id
    
    def compose(self) -> ComposeResult:
        yield Static(self.label_text, classes="input_label")
        yield Input(
            placeholder=self.placeholder,
            id=self.input_id,
            classes="text_input"
        )


class StatusPanel(Static):
    """Displays status and progress information."""
    
    status_text = reactive("Ready")
    progress = reactive(0)
    
    def render(self) -> RenderableType:
        from rich.panel import Panel
        from rich.text import Text
        
        status = Text(self.status_text, style="cyan")
        
        if self.progress > 0:
            # Simple progress bar using text
            bar_length = 40
            filled = int((self.progress / 100) * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            progress_text = f"[{bar}] {self.progress}%"
            
            return Panel(
                f"{status}\n\n{progress_text}",
                title="[bold]Status[/bold]",
                border_style="blue",
                expand=False
            )
        else:
            return Panel(status, title="[bold]Status[/bold]", border_style="blue")


class DocIndexerApp(App):
    """TUI for doc-indexer - Convert API docs to Markdown for LLMs."""
    
    BINDINGS = [("q", "quit", "Quit")]
    CSS = """
    Screen {
        layout: vertical;
        background: $surface;
    }
    
    #title {
        width: 100%;
        text-align: center;
        color: $accent;
        text-style: bold;
        margin-bottom: 1;
    }
    
    #subtitle {
        width: 100%;
        text-align: center;
        color: $text-muted;
        margin-bottom: 2;
    }
    
    .input_label {
        color: $text;
        text-style: bold;
        margin-bottom: 1;
        width: 100%;
        margin-top: 1;
    }
    
    .text_input {
        width: 100%;
        height: 3;
        border: solid $primary;
        margin-bottom: 2;
    }
    
    #input_container {
        width: 100%;
        height: auto;
        border: solid $accent;
        padding: 2 2;
        margin-bottom: 2;
    }
    
    #button_container {
        height: auto;
        margin-bottom: 2;
        width: 100%;
    }
    
    Button {
        margin-right: 2;
    }
    
    #status_panel {
        height: auto;
        margin-bottom: 2;
        width: 100%;
    }
    
    #log_area {
        border: solid $primary;
        width: 100%;
        height: 1fr;
    }
    """
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=False)
        
        with ScrollableContainer():
            yield Static("📚 Doc Indexer By @Nematdar", id="title")
            yield Static("Convert API documentation to Markdown for LLM consumption", id="subtitle")
            
            # Input container with border
            with Vertical(id="input_container"):
                yield InputBox(
                    "🔗 Documentation URL",
                    "https://numpy.org/doc/stable/reference/",
                    "url_input"
                )
                yield InputBox(
                    "📁 Output File Path",
                    "numpy_api_reference.md",
                    "output_input"
                )
            
            # Buttons
            with Horizontal(id="button_container"):
                yield Button("🚀 Start Scraping", id="start_btn", variant="primary")
                yield Button("✕ Reset", id="reset_btn")
            
            # Status panel
            yield StatusPanel(id="status_panel")
            
            # Log area
            yield RichLog(id="log_area", markup=True)
        
        yield Footer()
    
    def on_mount(self) -> None:
        """Handle mount event."""
        self.title = "doc-indexer"
        self.sub_title = "API Documentation to Markdown Converter"
        
        # Focus on URL input
        self.query_one("#url_input", Input).focus()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "start_btn":
            self.start_scraping()
        elif event.button.id == "reset_btn":
            self.reset_form()
    
    def reset_form(self) -> None:
        """Reset the form."""
        self.query_one("#url_input", Input).value = ""
        self.query_one("#output_input", Input).value = ""
        status_panel = self.query_one("#status_panel", StatusPanel)
        status_panel.status_text = "Ready"
        status_panel.progress = 0
        log = self.query_one("#log_area", RichLog)
        log.clear()
        self.query_one("#url_input", Input).focus()
    
    def start_scraping(self) -> None:
        """Start the scraping process."""
        url = self.query_one("#url_input", Input).value.strip()
        output = self.query_one("#output_input", Input).value.strip()
        
        log = self.query_one("#log_area", RichLog)
        status_panel = self.query_one("#status_panel", StatusPanel)
        
        # Validation
        if not url:
            log.write("[red]Error: Please enter a URL[/red]")
            return
        
        if not output:
            log.write("[red]Error: Please enter an output file path[/red]")
            return
        
        if not url.startswith(("http://", "https://")):
            log.write("[red]Error: URL must start with http:// or https://[/red]")
            return
        
        log.clear()
        log.write(f"[cyan]Source URL:[/cyan] {url}")
        log.write(f"[cyan]Output file:[/cyan] {output}\n")
        
        status_panel.status_text = "Discovering pages..."
        status_panel.progress = 5
        
        # Disable buttons during scrape
        self.query_one("#start_btn", Button).disabled = True
        
        # Start background worker
        self.run_scraper(url, output)

    def update_status(self, text: str, progress: int, log_msg: str = None, log_style: str = "white"):
        """Update UI elements safely from the worker thread."""
        status_panel = self.query_one("#status_panel", StatusPanel)
        status_panel.status_text = text
        status_panel.progress = progress
        if log_msg:
            self.query_one("#log_area", RichLog).write(f"[{log_style}]{log_msg}[/{log_style}]")

    def finish_scraping(self, success: bool, message: str) -> None:
        """Handle scraping completion safely from the worker thread."""
        self.query_one("#start_btn", Button).disabled = False
        status_panel = self.query_one("#status_panel", StatusPanel)
        log = self.query_one("#log_area", RichLog)
        
        if success:
            status_panel.status_text = "Complete!"
            status_panel.progress = 100
            log.write(f"[green]✓ {message}[/green]")
        else:
            status_panel.status_text = "Error"
            log.write(f"[red]❌ Error: {message}[/red]")

    from textual import work

    @work(thread=True)
    def run_scraper(self, base_url: str, output_path: str) -> None:
        """The actual scraping logic running in a background thread."""
        try:
            self.call_from_thread(self.update_status, "Fetching index...", 10, "Fetching index page...", "yellow")
            
            response = requests.get(base_url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            main_content = (
                soup.find(itemprop="articleBody") or 
                soup.find('main') or 
                soup.find(role="main") or 
                soup 
            )
            
            links = main_content.find_all('a', href=True)
            urls_to_scrape = [base_url]
            
            for link in links:
                href = link['href']
                if not href.startswith('#') and not href.startswith('http'):
                    full_url = urljoin(base_url, href)
                    if full_url not in urls_to_scrape:
                        urls_to_scrape.append(full_url)
                        
            total_urls = len(urls_to_scrape)
            self.call_from_thread(self.update_status, f"Found {total_urls} pages", 15, f"Found {total_urls} pages to scrape", "green")
            
            all_markdown_sections = []
            
            for i, url in enumerate(urls_to_scrape):
                progress = 15 + int((i / total_urls) * 80) # Progress from 15% to 95%
                self.call_from_thread(self.update_status, f"Fetching page {i+1}/{total_urls}", progress, f"Fetching sub-page: {url}", "cyan")
                
                try:
                    res = requests.get(url, timeout=15)
                    res.raise_for_status()
                    page_soup = BeautifulSoup(res.text, 'html.parser')
                    
                    page_content = (
                        page_soup.find(itemprop="articleBody") or 
                        page_soup.find('main') or 
                        page_soup.find(role="main") or
                        page_soup
                    )
                    
                    if page_content:
                        md_text = f"<!-- Source: {url} -->\n"
                        md_text += md(
                            str(page_content), 
                            heading_style="ATX", 
                            strip=['script', 'style']
                        )
                        all_markdown_sections.append(md_text)
                except Exception as e:
                    self.call_from_thread(self.update_status, f"Error on {url}", progress, f"Failed to fetch {url}: {e}", "red")

            self.call_from_thread(self.update_status, "Compiling Markdown...", 95, "Compiling and cleaning Markdown...", "yellow")
            
            final_markdown = "\n\n---\n\n".join(all_markdown_sections)
            cleaned_markdown = "\n".join([line for line in final_markdown.splitlines() if line.strip() != ""])
            
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_markdown)
                
            self.call_from_thread(self.finish_scraping, True, f"Saved to {output_file.absolute()} ({len(cleaned_markdown)} characters)")
            
        except requests.exceptions.Timeout:
            self.call_from_thread(self.finish_scraping, False, "Request timed out (15s)")
        except requests.exceptions.ConnectionError:
            self.call_from_thread(self.finish_scraping, False, "Could not connect to the URL")
        except Exception as e:
            self.call_from_thread(self.finish_scraping, False, str(e))


if __name__ == "__main__":
    app = DocIndexerApp()
    app.run()
