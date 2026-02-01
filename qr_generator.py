"""
QR Code Generator without using Pillow
Generates an SVG QR Code instead of PNG
"""

import qrcode
import qrcode.image.svg
import re

def is_valid_url(url: str) -> bool:
    """
    Validate URL format
    """
    pattern = re.compile(r"^(https?://)")
    return bool(pattern.match(url))


def generate_qr_svg(url: str, output_file="qr_code.svg"):
    """
    Generate QR code as SVG (no Pillow required)
    """
    if not is_valid_url(url):
        raise ValueError("Invalid URL! Must start with http:// or https://")

    # Use SVG image factory
    factory = qrcode.image.svg.SvgImage

    img = qrcode.make(url, image_factory=factory)

    with open(output_file, "wb") as f:
        img.save(f)

    return output_file


def main():
    print("=== Biox Systems – QR Code Generator (SVG Version) ===")
    url = input("Enter a valid URL: ")

    try:
        path = generate_qr_svg(url)
        print(f"QR code SVG generated successfully at: {path}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
