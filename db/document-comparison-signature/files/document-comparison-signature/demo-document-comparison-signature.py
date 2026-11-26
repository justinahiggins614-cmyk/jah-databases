"""Demo program for the Document Comparison Database (document-comparison-signature).
Run: python3 demo-document-comparison-signature.py
"""
doc_a = "The cat sat.\nThe dog ran.\nThe bird sang.\nThe sun shone."
doc_b = "The cat sat.\nThe dog slept.\nThe bird sang.\nThe rain fell."
a = doc_a.split("\n")
b = doc_b.split("\n")
print(f"Two documents of {len(a)} lines each, compared line by line")
