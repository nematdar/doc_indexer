import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from urllib.parse import urljoin
# high-level summary
def scrape_docs_to_markdown(url: str, output_path: str) -> None:
    """
    Fetches an HTML documentation page, extracts the main content, 
    and saves it as a clean Markdown file.
    """
    print(f"Fetching: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Target the main content area to avoid scraping navbars and footers.
    # Sphinx/ReadTheDocs typically uses itemprop="articleBody", role="main", or a <main> tag.
    main_content = (
        soup.find(itemprop="articleBody") or 
        soup.find('main') or 
        soup.find(role="main") or 
        soup.find('article') or 
        soup 
    )

    print("Converting HTML to Markdown...")
    # Convert the extracted HTML to Markdown
    # We use ATX heading style (###) and strip out any residual scripts/styles
    markdown_text = md(
        str(main_content), 
        heading_style="ATX", 
        strip=['script', 'style']
    )

    # Clean up excess blank lines that markdownify sometimes leaves behind
    cleaned_markdown = "\n".join([line for line in markdown_text.splitlines() if line.strip() != ""])

    # Save to the specified output path
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_markdown)
        
    print(f"Success! Documentation saved to: {output_file.absolute()}")

# if __name__ == "__main__":
#     # Your requested parameters
#     TARGET_URL = "https://zarr.readthedocs.io/en/stable/api/zarr/"
#     OUTPUT_FILE = "zarr_api_reference.md"
#     scrape_docs_to_markdown(TARGET_URL, OUTPUT_FILE)
    

def scrape_full_api_reference(base_url: str, output_path: str) -> None:
    """
    Fetches the main API index, finds all sub-pages, extracts their content, 
    and concatenates them into a single Markdown file.
    """
    print(f"Fetching index page: {base_url}")
    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the index URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Target the main content area of the index page
    main_content = (
        soup.find(itemprop="articleBody") or 
        soup.find('main') or 
        soup.find(role="main") or 
        soup 
    )

    # Find all sub-links within the index content
    links = main_content.find_all('a', href=True)
    urls_to_scrape = [base_url] # Start with the index page itself
    
    for link in links:
        href = link['href']
        # Ignore anchor links to the same page and external links
        if not href.startswith('#') and not href.startswith('http'):
            full_url = urljoin(base_url, href)
            if full_url not in urls_to_scrape:
                urls_to_scrape.append(full_url)

    all_markdown_sections = []

    # Scrape each URL we found
    for url in urls_to_scrape:
        print(f"Fetching sub-page: {url}")
        try:
            res = requests.get(url)
            res.raise_for_status()
            page_soup = BeautifulSoup(res.text, 'html.parser')
            
            page_content = (
                page_soup.find(itemprop="articleBody") or 
                page_soup.find('main') or 
                page_soup.find(role="main")
            )
            
            if page_content:
                # Add a Markdown header indicating the source URL for LLM context
                md_text = f"<!-- Source: {url} -->\n"
                md_text += md(
                    str(page_content), 
                    heading_style="ATX", 
                    strip=['script', 'style']
                )
                all_markdown_sections.append(md_text)
                
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

    print("\nCompiling and cleaning Markdown...")
    
    # Join all pages with a horizontal rule separator
    final_markdown = "\n\n---\n\n".join(all_markdown_sections)
    
    # Clean up excess blank lines
    cleaned_markdown = "\n".join([line for line in final_markdown.splitlines() if line.strip() != ""])

    # Save to the specified output path
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_markdown)
        
    print(f"\nSuccess! Full API Reference compiled and saved to: {output_file.absolute()}")

# if __name__ == "__main__":
#     TARGET_URL = "https://zarr.readthedocs.io/en/stable/api/zarr/"
#     OUTPUT_FILE = "zarr_api_reference.md"
#     scrape_full_api_reference(TARGET_URL, OUTPUT_FILE)