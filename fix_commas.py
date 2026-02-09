import re

# Read the file
with open('gps_data_dict.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix missing commas after any dictionary value lines that end with a string
fixed_lines = []
for line in lines:
    stripped = line.rstrip()
    # Check if this is a dictionary key-value line ending with a string but no comma
    # Pattern: whitespace + 'key': + 'value' (no comma at the end)
    if re.match(r"^\s+'\w[\w\s-]*':\s*'[^']*'$", stripped):
        # Add comma before the newline
        fixed_lines.append(stripped + ',\n')
    else:
        fixed_lines.append(line)

# Write the fixed content back
with open('gps_data_dict.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("Fixed all missing commas")
