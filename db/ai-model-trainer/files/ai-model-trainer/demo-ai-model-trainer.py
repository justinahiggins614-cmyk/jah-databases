"""Demo program for the AI Model Trainer Database (ai-model-trainer).
Run: python3 demo-ai-model-trainer.py
"""
points = [(1, 3), (2, 5), (3, 7), (4, 9)]
w, b = 0.0, 0.0
loss = sum((w * x + b - y) ** 2 for x, y in points) / len(points)
print(f"Starting at w of {w}, the loss is {round(loss, 1)}")
