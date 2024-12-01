#!/usr/bin/python3

import sys
import os
import re

def convert_markdown_to_html(markdown_content):
    """
    Converts Markdown content to HTML.

    Args:
        markdown_content (str): The Markdown content to convert.

    Returns:
        str: The converted HTML content.
    """
    html_lines = []
    in_ul_list = False
    in_ol_list = False
    in_paragraph = False

    def convert_bold_and_emphasis(text):
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)  # bold
        text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)    # emphasis
        return text

    for line in markdown_content.split('\n'):
        line = convert_bold_and_emphasis(line)
        if line.startswith('#'):
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            heading_level = len(line.split(' ')[0])
            heading_text = ' '.join(line.split(' ')[1:])
            html_line = f'<h{heading_level}>{heading_text}</h{heading_level}>'
            html_lines.append(html_line)
        elif line.startswith('- '):
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            if in_ol_list:
                html_lines.append('</ol>')
                in_ol_list = False
            if not in_ul_list:
                html_lines.append('<ul>')
                in_ul_list = True
            list_item = line[2:].strip()
            html_lines.append(f'  <li>{list_item}</li>')
        elif line.startswith('* '):
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            if in_ul_list:
                html_lines.append('</ul>')
                in_ul_list = False
            if not in_ol_list:
                html_lines.append('<ol>')
                in_ol_list = True
            list_item = line[2:].strip()
            html_lines.append(f'  <li>{list_item}</li>')
        else:
            if in_ul_list:
                html_lines.append('</ul>')
                in_ul_list = False
            if in_ol_list:
                html_lines.append('</ol>')
                in_ol_list = False
            if line.strip() == "":
                if in_paragraph:
                    html_lines.append('</p>')
                    in_paragraph = False
            else:
                if not in_paragraph:
                    html_lines.append('<p>')
                    in_paragraph = True
                html_lines.append(line.replace('\n', '<br/>'))

    if in_ul_list:
        html_lines.append('</ul>')
    if in_ol_list:
        html_lines.append('</ol>')
    if in_paragraph:
        html_lines.append('</p>')

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
