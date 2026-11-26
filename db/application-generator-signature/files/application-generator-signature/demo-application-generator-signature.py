"""Demo program for the Application Generator Database (application-generator-signature).
Run: python3 demo-application-generator-signature.py
"""
templates = ["blog", "shop", "notes"]
fields = 4
print(f"The generator builds {len(templates)} apps from {len(templates)} templates with {fields} fields each")
