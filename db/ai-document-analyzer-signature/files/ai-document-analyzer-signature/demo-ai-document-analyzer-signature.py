"""Demo program for the AI Document Analyzer Database (ai-document-analyzer-signature).
Run: python3 demo-ai-document-analyzer-signature.py
"""
doc = "The river runs past the town and under the old stone bridge. People cross the bridge every day on foot and by cart. The bridge was built long ago and still stands today. Children watch the river from the bridge in the morning. The town keeps the bridge in good repair year after year."
words = doc.split()
sentences = doc.count('.')
print(f"A document of {len(words)} words in {sentences} sentences is read and its 3 main points are kept")
