import csv
import json
from pathlib import Path

# This script reads the guest messages saved in the browser localStorage
# and exports them to an Excel-friendly CSV file.

storage_path = Path("guest_messages_export.csv")

# The browser stores entries in localStorage under this key.
# If you want to import from a JSON file instead, replace this with that file path.
try:
    with open("guest_messages.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

if not isinstance(data, list):
    raise ValueError("Expected a list of guest messages in guest_messages.json")

with open(storage_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Message", "Date"])
    for item in data:
        writer.writerow([item.get("name", ""), item.get("message", ""), item.get("createdAt", "")])

print(f"Exported {len(data)} message(s) to {storage_path}")
