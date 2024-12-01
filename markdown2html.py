#!/usr/bin/python3

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # No conversion logic yet, just confirming file exists
    with open(markdown_file, 'r') as md:
        markdown_content = md.read()

    with open(output_file, 'w') as html:
        html.write(markdown_content)

    sys.exit(0)
