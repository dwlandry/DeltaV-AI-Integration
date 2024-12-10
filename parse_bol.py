import os
import json
from bs4 import BeautifulSoup

# Path to your BOL HTML directory
BOL_HTML_DIR = r"C:\Users\dlandry\OneDrive - Scallon Controls, Inc\Desktop\BOL v14.3 Web Based" # os.path.expanduser("~/Desktop/BOL_v14.3_Web_Based")
# Output directory for parsed JSON files
OUTPUT_DIR = r"C:\Users\dlandry\OneDrive - Scallon Controls, Inc\Desktop\BOL_parsed"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def parse_html_file(filepath):
    """
    Parse a single BOL HTML file and extract relevant text.
    Returns a dictionary with filename, title, headings, and body_text.
    """
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title (from <title> tag)
    title_tag = soup.find('title')
    title = title_tag.get_text().strip() if title_tag else ""

    # Attempt to find main heading (often <h1 class="topictitle1">)
    h1_tag = soup.find('h1', class_='topictitle1')
    main_heading = h1_tag.get_text().strip() if h1_tag else ""

    # Extract main article body
    # Often the main content is within <article> or main <div id="center">
    article = soup.find('article')
    if article:
        # Remove script, style, nav, and non-content elements
        for tag in article(['script', 'style', 'nav', 'form', 'noscript']):
            tag.decompose()
        body_text = article.get_text(separator=' ', strip=True)
    else:
        # If no <article> tag, fallback to main content div
        center_div = soup.find('div', id='center')
        if center_div:
            for tag in center_div(['script', 'style', 'nav', 'form', 'noscript']):
                tag.decompose()
            body_text = center_div.get_text(separator=' ', strip=True)
        else:
            body_text = ""

    # Clean and trim body_text
    body_text = ' '.join(body_text.split())

    return {
        "filename": os.path.basename(filepath),
        "title": title,
        "main_heading": main_heading,
        "body_text": body_text
    }

parsed_docs = []

# Traverse the BOL directory and parse HTML files
for root, dirs, files in os.walk(BOL_HTML_DIR):
    for file in files:
        if file.lower().endswith('.html'):
            full_path = os.path.join(root, file)
            doc_data = parse_html_file(full_path)
            parsed_docs.append(doc_data)

# Store all parsed documents in a single JSON file or multiple files
# Option 1: single JSON file with a list of documents
output_file = os.path.join(OUTPUT_DIR, "parsed_bol_documents.json")
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(parsed_docs, outfile, indent=2, ensure_ascii=False)

print(f"Parsing complete. Output saved to {output_file}")
