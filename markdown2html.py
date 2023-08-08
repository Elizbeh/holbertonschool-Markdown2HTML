#!/usr/bin/python3
"""
This script converts a markdown file to HTML format.
Reads a markdown file and writes an HTML file with
the same content but formatted as HTML.
"""

import os
import sys
import markdown


def markdown_to_html(markdown_file, output_file):   
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        s
        ys.exit(1)

    with open(markdown_file, "r") as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    with open(output_file, "w") as f:
        f.write(html_content)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.stderr.write(f"Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    markdown_to_html(markdown_file, output_file)

    sys.exit(0)
