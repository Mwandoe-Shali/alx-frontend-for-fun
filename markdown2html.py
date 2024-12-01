#!/usr/bin/python3

import sys
import os

def convert_markdown_to_html(markdown_content):
    """
    Converts Markdown content to HTML.

    Args:
        markdown_content (str): The Markdown content to convert.

    Returns:
        str: The converted HTML content.
    """
    html_lines = []
    for line in markdown_content.split('\n'):
        if line.startswith('#'):
            heading_level = len(line.split(' ')[0])
            heading_text = ' '.join(line.split(' ')[1:])
            html_line = f'<h{heading_level}>{heading_text}</h{heading_level}>'
            html_lines.append(html_line)
        else:
            html_lines.append(line)
    return '\n'.join(html_lines)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as md:
        markdown_content = md.read()

    html_content = convert_markdown_to_html(markdown_content)

    with open(output_file, 'w') as html:
        html.write(html_content)

    sys.exit(0)
