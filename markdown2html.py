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
        # Initialize the MarkdownToHTMLConverter with input and output file paths
        self.markdown_file = markdown_file
        self.output_file = output_file

    def convert(self):
        # Convert the input Markdown file to HTML and write it to the output file
        # Check if the Markdown file exists
        if not os.path.exists(self.markdown_file):
            # Print an error message and exit if the file is missing
            sys.stderr.write(f"Missing {self.markdown_file}\n")
            sys.exit
