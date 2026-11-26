"""Demo program for the Genome Comparison Tool Database (genome-comparison-tool-signature).
Run: python3 demo-genome-comparison-tool-signature.py
"""
a = "ACGTACGTAC"
b = "ACGTACGTTC"
matches = sum(1 for x, y in zip(a, b) if x == y)
print(f"Two sequences of 10 bases match at {matches}: {round(matches / len(a) * 100, 1)} percent identical")
