from app import read_coordinates
import json

coords = read_coordinates()
print(f"Total coordinates read: {len(coords)}")
print("\nFirst 5 coordinates:")
for i in range(min(5, len(coords))):
    print(f"{i+1}. {coords[i]}")

print(f"\nAll coordinates valid: {all('lat' in c and 'lon' in c for c in coords)}")
print(f"Sample coordinate types: lat={type(coords[0]['lat'])}, lon={type(coords[0]['lon'])}")
