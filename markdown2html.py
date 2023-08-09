#!/usr/bin/python3
"""
This script converts a markdown file to HTML format.
Reads a markdown file and writes an HTML file with
the same content but formatted as HTML.
"""

import os
import sys
import markdown

class MarkdownToHTMLConverter:
    def __init__(self, markdown_file, output_file):
        """
        Initialize the MarkdownToHTMLConverter with input and output file paths.
        
        :param markdown_file: Path to the input Markdown file.
        :param output_file: Path to the output HTML file.
        """
        self.markdown_file = markdown_file
        self.output_file = output_file
    
    def convert(self):
        """
        Convert the input Markdown file to HTML and write it to the output file.
        """
        if not os.path.exists(self.markdown_file):
            sys.stderr.write(f"Missing {self.markdown_file}\n")
            sys.exit(1)

        # Read the content of the input Markdown file
        with open(self.markdown_file, "r") as f:
            markdown_content = f.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Write the HTML content to the output file
        with open(self.output_file, "w") as f:
            f.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        # Print usage information if incorrect arguments provided
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    converter = MarkdownToHTMLConverter(markdown_file, output_file)
    converter.convert()

