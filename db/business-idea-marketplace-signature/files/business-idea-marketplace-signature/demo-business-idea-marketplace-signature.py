"""Demo program for the The Business Idea Marketplace Database (Signature) (business-idea-marketplace-signature).
Run: python3 demo-business-idea-marketplace-signature.py
"""
ideas = [
    ("A Signature Soup of the Day Stall", "food"),
    ("A Signature Bicycle Tune-Up Van", "services"),
    ("A Signature Appointment Keeper", "software"),
    ("A Signature Book Exchange Shelf", "retail"),
    ("A Signature Homework Helpers Circle", "education"),
    ("A Signature Morning Walk for Neighbors", "health"),
    ("A Signature Compost-to-Garden Loop", "green"),
    ("A Signature Candle-Making Evening", "crafts"),
    ("A Signature Picnic Basket Service", "food"),
    ("A Signature Window-Cleaning Round", "services"),
    ("A Signature Savings Jar Tracker", "software"),
    ("A Signature Craft Fair Booth", "retail"),
    ("A Signature Science Story Hour", "education"),
    ("A Signature Balance and Breath Class", "health"),
    ("A Signature Cloth Bag Sewing Circle", "green"),
    ("A Signature Wooden Toy Repair Bench", "crafts"),
    ("A Signature Baked Treats Stall", "food"),
    ("A Signature Dog-Walking Club", "services"),
    ("A Signature Neighborhood Notice Board", "software"),
    ("A Signature Seed Library", "retail"),
    ("A Signature Cooking Basics Class", "education"),
    ("A Signature Restful Evening Routine Guide", "health"),
    ("A Signature Solar Lantern Workshop", "green"),
]
for title, category in ideas:
    print(f"{title} [{category}]")
print(f"Total ideas: {len(ideas)} (fictional catalog examples only)")
