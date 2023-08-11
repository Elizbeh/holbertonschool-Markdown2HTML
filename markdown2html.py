#!/usr/bin/python3
"""
This script converts a markdown file to HTML format.
"""
import os
import sys
import markdown


# Define a class for converting Markdown to HTML
class MarkdownToHTMLConverter:
    def __init__(self, markdown_file, output_file):
        """
        Initialize the MarkdownToHTMLConverter
        with input and output file paths
        """
        self.markdown_file = markdown_file
        self.output_file = output_file

    def convert(self):
        """
        Convert the input Markdown file to HTML
        and write it to the output file
        Check if the Markdown file exists
        """
        if not os.path.exists(self.markdown_file):
            sys.stderr.write(f"Missing {self.markdown_file}\n")
            sys.exit(1)

        with open(self.markdown_file, "r") as f:
            markdown_content = f.read()

        html_content = markdown.markdown(markdown_content)

        with open(self.output_file, "w") as f:
            f.write(html_content)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    converter = MarkdownToHTMLConverter(markdown_file, output_file)
    converter.convert()
