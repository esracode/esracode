#!/usr/bin/env python3
"""
Generate QR code for the GitHub Pages URL
"""
import qrcode
from PIL import Image

# URL to encode in QR code
url = "https://esracode.github.io/esracode"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(url)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")
print(f"QR code generated successfully for: {url}")

