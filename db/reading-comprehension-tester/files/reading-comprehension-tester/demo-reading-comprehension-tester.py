"""Demo program for the Reading Comprehension Tester Database (reading-comprehension-tester).
Run: python3 demo-reading-comprehension-tester.py
"""
passage = "The river flows past the old mill and under the stone bridge."
questions, right = 5, 4
print(f"A passage of {len(passage.split())} words with {questions} questions: {right} right")
