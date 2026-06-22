# doc-indexer

Convert Python library API reference documentation to clean Markdown for LLM consumption.

## Why

LLMs work best with current, clean documentation. This tool fetches API reference pages, extracts the content (skipping navbars and footers), and converts them to Markdown. Great for feeding library docs into LLM-powered workflows or keeping your AI tools up-to-date with the latest library versions.

## Features

- **Single-page scraping**: Fetch a docs URL and save as Markdown
- **Full API index crawling**: Crawl an API index, follow all links, and compile into one `.md` file
- **Clean extraction**: Targets main content areas, ignores navigation chrome
- **LLM-ready output**: Clean Markdown that's ready to paste into prompts or pipelines

## Requirements & Installation

You can run `doc-indexer` either via its interactive Terminal UI (TUI) or by using the Python script directly.

### Core Dependencies (For Script/CLI use)

- Python 3.10+
- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing
- `markdownify` — HTML to Markdown conversion

```bash
pip install requests beautifulsoup4 markdownify
```

### TUI Dependencies (For GUI mode)

If you want to use the interactive Terminal UI, you also need the `textual` framework.

```bash
pip install textual
```

*(You can install everything at once with: `pip install requests beautifulsoup4 markdownify textual`)*

## Usage

### Method 1: Interactive TUI (Recommended) 🎨

Launch the beautiful terminal interface:

```bash
python tui.py
```

1. Enter a documentation URL (e.g., `https://numpy.org/doc/stable/reference/`)
2. Enter an output filename (e.g., `numpy_api_reference.md`)
3. Click **Start Scraping**
4. Watch the progress and live logs as it discovers, fetches, and compiles subpages!

### Method 2: Script / Code Mode 💻

If you prefer writing code or integrating it into another pipeline, edit `doc_indexer.py` directly:

```python
if __name__ == "__main__":
    TARGET_URL = "https://numpy.org/doc/stable/reference/"
    OUTPUT_FILE = "numpy_api_reference.md"
    
    scrape_full_api_reference(TARGET_URL, OUTPUT_FILE)
```

Then run:

```bash
python doc_indexer.py
```

### Available Functions

**`scrape_docs_to_markdown(url, output_path)`**

Fetch a single documentation page and save as Markdown.

```python
scrape_docs_to_markdown(
    "https://scipy.org/doc/scipy/reference/",
    "scipy_api_reference.md"
)
```

**`scrape_full_api_reference(base_url, output_path)`**

Crawl an API index page, discover linked subpages, and compile them into a single Markdown file. Useful for comprehensive API references.

```python
scrape_full_api_reference(
    "https://zarr.readthedocs.io/en/stable/api/zarr/",
    "zarr_api_reference.md"
)
```

## Output Examples

This repo includes pre-scraped references:

- `numpy_api_reference.md` — NumPy 2.4 API reference
- `scipy_api_reference.md` — SciPy API reference
- `zarr_api_reference.md` — Zarr API reference
- `dask_api_reference.md` — Dask API reference
- `cupy_api_reference.md` — CuPy API reference
- `napari_api_reference.md` — Napari API reference
- `qt_pyside6_api_reference.md` — PySide6 API reference

These are ready to use with LLMs or as examples.

## Use Cases

- **Prompt Engineering**: Paste library docs directly into your LLM prompts
- **AI Code Assistants**: Feed into custom AI workflows for code generation
- **Documentation Sync**: Periodically regenerate to keep docs in sync with library releases
- **Offline Reference**: Get clean, searchable Markdown versions of web-hosted docs
