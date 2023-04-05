#!/usr/bin/python3
"""
This script Convert a markdown file to HTML format.

Usage: ./markdown2html.py input.md output.html

markdown2html.py reads a markdown file and writes an HTML file with the same content
but formatted as HTML..
"""

from sys import argv, stderr
from os.path import exists

if __name__ == "__main__":
    
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    
    if not exists(argv[1]):
        print(f"Missing {argv[1]}", file=stderr)
        exit(1)
        
    with open(argv[1], "r", encoding='utf-8') as file:
        with open(argv[2], "w", encoding='utf-8') as html:
            followline = file.readline()
            while followline:
                title_hash = followline.count("#")
                unordered = followline.strip("- ").rstrip()
                ordered = followline.strip("* ").rstrip()
                if title_hash != 0:
                    line = followline.lstrip('# ').lstrip('/n')
                    html.write(f"<h{title_hash}>{line.rstrip()}</h{title_hash}>\n")
                if '-' in followline:
                    html.write('<ul>\n')
                    html.write(f"<li>{unordered}</li>\n")
                    file.readline()
                    while followline.startswith("-"):
                        html.write(f'<li>{followline.strip("- ").rstrip()}</'
                                   f'li>\n')
                        followline = file.readline()
                    html.write('</ul>\n')
                if '*' in followline:
                    html.write('<ol>\n')
                    html.write(f'<li>{followline.strip("* ").rstrip()}</'f'li>\n')
                    file.readline()
                    while followline.startswith("*"):
                        html.write(f'<li>{followline.strip("* ").rstrip()}</'
                                   f'li>\n')
                        followline = file.readline()
                        html.write('</ol>\n')
                else:
                    followline = file.readline()
        exit(0)