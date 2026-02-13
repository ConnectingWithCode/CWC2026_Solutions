import json

# Load words from JSON
with open('wordles.json', 'r') as f:
    words = json.load(f)

# Sort alphabetically
words_sorted = sorted(words)

# Save back to JSON
with open('wordles.json', 'w') as f:
    json.dump(words_sorted, f, indent=4)

print(f"✅ Sorted {len(words_sorted)} words alphabetically in wordles.json")
