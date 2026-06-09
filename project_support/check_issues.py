from gps_data_dict import gps_data
import re

print("Checking for issues in GPS data...")
print("=" * 60)

issues = []
for pole_id, data in gps_data.items():
    label = data.get('label', '')
    lat = data.get('latitude', '')
    lon = data.get('longitude', '')
    
    # Check for missing or invalid data
    problems = []
    
    if not label:
        problems.append("Missing label")
    elif not re.match(r'[A-Z]{2}-[A-Z\d]{2,3}-R\d{2}-[A-Z]{3}-\d+', label):
        problems.append(f"Non-standard label format: {label}")
    
    try:
        lat_float = float(lat)
        if not (17 < lat_float < 18):
            problems.append(f"Latitude out of range: {lat}")
    except (ValueError, TypeError):
        problems.append(f"Invalid latitude: {lat}")
    
    try:
        lon_float = float(lon)
        if not (78 < lon_float < 79):
            problems.append(f"Longitude out of range: {lon}")
    except (ValueError, TypeError):
        problems.append(f"Invalid longitude: {lon}")
    
    if problems:
        issues.append((pole_id, problems))

if issues:
    print(f"Found {len(issues)} poles with issues:\n")
    for pole_id, problems in issues:
        data = gps_data[pole_id]
        print(f"Pole ID {pole_id}:")
        print(f"  Label: {data.get('label', 'N/A')}")
        print(f"  Lat: {data.get('latitude', 'N/A')}, Lon: {data.get('longitude', 'N/A')}")
        for problem in problems:
            print(f"  ⚠ {problem}")
        print()
else:
    print("✓ All poles have valid data!")
    print(f"Total poles: {len(gps_data)}")
