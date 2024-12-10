# Parsing HTML Files

Process:
1. Use Python with `BeautifulSoup` to parse HTML.
2. Extract `<title>`, main `<h1>` headings, and main text content.
3. Ignore navigation bars and search panels.

See also:
- [[Structuring-Documentation-Data]]


**Date:** 2024-12-10

**Progress:**
- Implemented a Python script (`parse_bol.py`) that:
  - Recursively walks through `C:\Users\dlandry\OneDrive - Scallon Controls, Inc\Desktop\BOL v14.3 Web Based`.
  - Uses BeautifulSoup to parse each `.html` file.
  - Extracts `title`, `main_heading`, and main `body_text`.

**Code Snippet:**
```python
# See attached `parse_bol.py` file for full code
