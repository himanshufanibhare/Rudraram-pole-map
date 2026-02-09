from app import read_coordinates
import json

coords = read_coordinates()
print(f'Total coordinates: {len(coords)}')
print('\nFirst 5 coordinates:')
for i, coord in enumerate(coords[:5]):
    print(f"{i+1}. {coord}")
