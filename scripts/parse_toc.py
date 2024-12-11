from bs4 import BeautifulSoup

def get_toc_lines(li, depth=0):
    """
    Recursively traverse the nested <li> elements, extract their text and href 
    (if available), and return a list of lines (strings) representing 
    a Markdown bullet list with links.
    """
    lines = []

    # First, try to find an <a> element
    anchor = li.find('a', recursive=False)
    if anchor:
        # If there's an anchor, use its text and href
        text = anchor.get_text(strip=True)
        href = anchor.get('href', '')
        line = ('  ' * depth) + f'- [{text}]({href})'
    else:
        # If no anchor, fall back to a <span> or other text element
        text_el = li.find('span', recursive=False)
        if not text_el:
            # If there's no span, try the direct text of the li
            text = li.get_text(strip=True)
        else:
            text = text_el.get_text(strip=True)
        line = ('  ' * depth) + '- ' + text

    lines.append(line)

    # Check for nested <ul>
    nested_ul = li.find('ul', recursive=False)
    if nested_ul:
        for child_li in nested_ul.find_all('li', recursive=False):
            lines.extend(get_toc_lines(child_li, depth+1))

    return lines

def main():
    # Load the HTML file
    with open('toc.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the main navigation element
    toc_nav = soup.find('nav', id='toc_nav')
    if not toc_nav:
        print("Could not find nav with id='toc_nav'.")
        return

    # Find top-level <ul>
    main_ul = toc_nav.find('ul')
    if not main_ul:
        print("Could not find top-level <ul> inside #toc_nav.")
        return

    # Extract lines
    all_lines = []
    for li in main_ul.find_all('li', recursive=False):
        all_lines.extend(get_toc_lines(li, depth=0))

    # Write to TOC.md
    with open('TOC.md', 'w', encoding='utf-8') as md_file:
        md_file.write('# Table of Contents\n\n')
        for line in all_lines:
            md_file.write(line + '\n')

    print("TOC with links has been written to TOC.md")

if __name__ == '__main__':
    main()
