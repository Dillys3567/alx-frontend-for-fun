#!/usr/bin/python3
import sys
import os
import markdown

"""A script that takes 2 strings,the name of the Markdown file
and the output file name
"""

def convertHTMLToMarkdown(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            markdown_text = f.read()
            html_content = markdown.markdown(markdown_text)
        with open(output_file, 'w') as f:
            f.write(html_content)
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    convertHTMLToMarkdown(input_file, output_file)
