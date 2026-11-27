"""Demo program for the The Business Idea Marketplace Database (business-idea-marketplace).
Run: python3 demo-business-idea-marketplace.py
"""
ideas = [
    ("A Neighborhood Soup Stall", "food"),
    ("A Mobile Bicycle Repair Visit", "services"),
    ("A Simple Appointment Reminder", "software"),
    ("A Corner Secondhand Book Nook", "retail"),
    ("An After-School Tutoring Circle", "education"),
    ("A Guided Walking Club for Seniors", "health"),
    ("A Community Compost Collection Round", "green"),
    ("A Handmade Soap Workshop", "crafts"),
    ("A Lunch Delivery Round for Offices", "food"),
    ("A Home Garden Watering Service", "services"),
    ("A Household Budget Tracker", "software"),
    ("A Seasonal Stall for Local Growers", "retail"),
    ("A Storytelling Evening for Children", "education"),
    ("A Gentle Stretch Class in the Park", "health"),
    ("A Reusable Bottle Refill Station", "green"),
    ("A Knitted Goods Repair Service", "crafts"),
    ("A Harvest Jam and Preserve Stall", "food"),
    ("A Pet Sitting Visit Service", "services"),
    ("A Local Events Notice Board", "software"),
    ("A Tool Lending Library", "retail"),
    ("A Language Practice Café", "education"),
    ("A Sleep Routine Coaching Session", "health"),
    ("A Rainwater Barrel Fitting Service", "green"),
]
for title, category in ideas:
    print(f"{title} [{category}]")
print(f"Total ideas: {len(ideas)} (fictional catalog examples only)")
