from gps_data_dict import gps_data

# Create the reformatted file content
output = "gps_data = {\n"

for pole_id, data in gps_data.items():
    lat = data.get('latitude', '')
    lon = data.get('longitude', '')
    label = data.get('label', '')
    
    output += f"    {pole_id}: {{\n"
    output += f"        'latitude': '{lat}',\n"
    output += f"        'longitude': '{lon}',\n"
    output += f"        'label': '{label}'\n"
    output += "    },\n"

output += "}\n"

# Write to file
with open('gps_data_dict.py', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Reformatted {len(gps_data)} entries successfully!")
