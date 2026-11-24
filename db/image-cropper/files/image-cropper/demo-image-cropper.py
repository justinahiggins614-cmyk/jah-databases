"""Demo program for the Image Cropper Database (image-cropper).
Run: python3 demo-image-cropper.py
"""
w, h = 800, 600
cw, ch = 400, 300
x, y = (w - cw) // 2, (h - ch) // 2
print(f'Crop ({x}, {y}, {cw}, {ch}) of {w}x{h} keeps the middle {cw} by {ch}')
