import csv
import re

def convert_csv_to_dict(csv_file):
    """Convert CSV to dictionary and replace spaces in labels with XX"""
    data_dict = {}
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            image = row['Image']
            latitude = row['Latitude']
            longitude = row['Longitude']
            label = row['lables']  # Note: CSV has 'lables' typo
            
            # Skip if label is empty
            if not label or label.strip() == '':
                continue
            
            # Replace multiple spaces between hyphens with 'XX'
            # Pattern: finds spaces between hyphens (e.g., "-      -" becomes "-XX-")
            cleaned_label = re.sub(r'-\s+(-)', r'-XX\1', label)
            
            # Extract number from image filename (e.g., '1a.jpg' -> 1)
            image_num = int(re.sub(r'[^\d]', '', image.split('.')[0]))
            
            # Store in dictionary
            data_dict[image_num] = {
                'latitude': latitude if latitude else 'XX',
                'longitude': longitude if longitude else 'XX',
                'label': cleaned_label
            }
    
    return data_dict

if __name__ == "__main__":
    # Convert CSV to dictionary
    result = convert_csv_to_dict('gps_coordinates - Sheet1.csv')
    
    # Print the dictionary
    print("gps_data = {")
    for key, value in sorted(result.items()):
        print(f"    {key}: {{'latitude': '{value['latitude']}', 'longitude': '{value['longitude']}', 'label': '{value['label']}'}},")
    print("}")
    
    # Also save to a file
    with open('gps_data_dict.py', 'w', encoding='utf-8') as f:
        f.write("gps_data = {\n")
        for key, value in sorted(result.items()):
            f.write(f"    {key}: {{'latitude': '{value['latitude']}', 'longitude': '{value['longitude']}', 'label': '{value['label']}'}},\n")
        f.write("}\n")
    
    print("\n✓ Dictionary saved to 'gps_data_dict.py'")
    print(f"✓ Total entries: {len(result)}")
