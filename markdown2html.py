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
    """ Check if the input markdown file exists
    """
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    """ Read the contents of the markdown file"""
    with open(markdown_file, "r") as f:
        markdown_content = f.read()

    """ Convert markdown content to HTML"""
    html_content = markdown.markdown(markdown_content)

    """ Write HTML content to the output file"""
    with open(output_file, "w") as f:
        f.write(html_content)


if __name__ == "__main__":
    """ Check if the correct number of arguments is provided"""
    if len(sys.argv) < 3:
        sys.stderr.write(f"Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    """ Get input markdown file and
    output HTML file from command line arguments"""
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    """Convert markdown to HTML and save to the output file"""
    markdown_to_html(markdown_file, output_file)

    """ Exit with a success status code"""
    sys.exit(0)
