"""Demo program for the File Extractor Database (file-extractor-signature).
Run: python3 demo-file-extractor-signature.py
"""
import io, zipfile
buf = io.BytesIO()
with zipfile.ZipFile(buf, "w") as z:
    z.writestr("hello.txt", "hello world")
    z.writestr("notes.txt", "some notes")
buf.seek(0)
with zipfile.ZipFile(buf) as z:
    names = z.namelist()
print(f"An archive holds {len(names)} entries: {names[0]} and {names[1]}")
