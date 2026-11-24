"""Demo program for the Image Resizer Database (image-resizer).
Run: python3 demo-image-resizer.py
"""
old_w, old_h = 800, 600
new_w = 400
new_h = round(new_w * old_h / old_w)
print(f'{old_w}x{old_h} -> {new_w}x{new_h}; pixels {old_w*old_h} -> {new_w*new_h}')
