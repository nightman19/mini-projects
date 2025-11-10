#!/usr/bin/env python3
"""
HTML to PDF Converter Script
Converts HTML files to PDF format using WeasyPrint
"""
import os
import sys
from pathlib import Path

try:
    from weasyprint import HTML
except:
    print("Error: weayprint library not found.")
    print("Please install it using: pip install weasyprint")
    sys.exit(1)


def convert_html_to_pdf(html_file, pdf_file=None):
    """
    Convert an HTML file to PDF.

    Args:
        html_file (str): Path to the input HTML file
        pdf_file(str, optional): Path to the output PDF file. If None, uses same name as HTML with .pdf extension

    Returns:
        str: Path to the generated PDF file
    """
    # Validate input file
    if not os.path.exists(html_file):
        raise FileNotFoundError(f"HTML file not found: {html_file}")

    # Determine output file name
    if pdf_file is None:
        pdf_file = Path(html_file).with_suffix('.pdf')

    # Convert HTML to PDF
    print(f"Converting {html_file} to PDF...")
    HTML(filename=html_file).write_pdf(pdf_file)
    print(f"Successfully created: {pdf_file}")

    return pdf_file


def main():
    """Main function to handle command-line arguments"""
    if len(sys.argv) < 2:
        print("Usage: python html_to_pdf.py <input.html> [output.pdf]")
        print("\Example:")
        print("  python html_to_pdf.py myfile.html")
        print("  python html_to_pdf.py myfile.html output.pdf")
        sys.exit(1)

    html_file = sys.argv[1]
    pdf_file = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        convert_html_to_pdf(html_file, pdf_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()