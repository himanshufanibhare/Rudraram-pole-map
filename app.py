from flask import Flask, render_template, jsonify
from flask import send_from_directory
import re
import os

app = Flask(__name__)

def read_coordinates():
    """Read coordinates from gps_data_dict.py"""
    try:
        from gps_data_dict import gps_data
        
        coordinates = []
        reference_groups = set()
        
        for pole_id, data in gps_data.items():
            try:
                lat = float(data.get('latitude', ''))
                lon = float(data.get('longitude', ''))
                label = data.get('label', f'Pole-{pole_id}')
                
                # Skip invalid coordinates
                if not lat or not lon or lat == 0 or lon == 0:
                    continue
                
                # Check if point_type is explicitly defined in data
                if 'point_type' in data:
                    point_type = data.get('point_type')
                    ref_group = 'NA'
                else:
                    # Extract reference group (RXX pattern)
                    ref_match = re.search(r'R(\d+|XX)', label, re.IGNORECASE)
                    ref_group = ref_match.group(0).upper() if ref_match else 'UNKNOWN'
                    reference_groups.add(ref_group)
                    
                    # Determine point type
                    point_type = 'dependent'  # Default: PWL, PNL, etc.
                    if re.search(r'-(CPT|CPM|CPTHM|CPMHM)-', label, re.IGNORECASE):
                        point_type = 'control'
                
                # Get additional lighting information
                high_mast_light = data.get('high-mast-light', 'NO').upper()
                no_of_lights = data.get('no of lights', '0')
                light_type = data.get('light type', 'NA')
                working = data.get('working', 'NO').upper()
                location = data.get('location', '')
                
                coord = {
                    'id': pole_id,
                    'lat': lat,
                    'lon': lon,
                    'label': label,
                    'ref_group': ref_group,
                    'type': point_type,
                    'high_mast_light': high_mast_light,
                    'no_of_lights': no_of_lights,
                    'light_type': light_type,
                    'working': working,
                    'location': location,
                    'images': []
                }

                # Attach image URLs if images exist in Pole_image folder (named like '27a.jpg','27b.jpg')
                try:
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    img_folder = os.path.join(base_dir, 'Pole_image')
                    if os.path.isdir(img_folder):
                        # check common extensions
                        for suffix in ['a', 'b']:
                            for ext in ['jpg', 'jpeg', 'png', 'webp']:
                                fname = f"{pole_id}{suffix}.{ext}"
                                fpath = os.path.join(img_folder, fname)
                                if os.path.exists(fpath):
                                    coord['images'].append(f"/pole_image/{fname}")
                                    break
                except Exception:
                    pass
                
                coordinates.append(coord)
                
            except (ValueError, TypeError) as e:
                print(f"Skipping pole {pole_id}: {e}")
                continue
        
        return coordinates, sorted(list(reference_groups))
        
    except Exception as e:
        print(f"Error reading GPS data: {e}")
        return [], []

@app.route('/')
def index():
    """Render the main map page"""
    return render_template('index.html')

@app.route('/api/coordinates')
def get_coordinates():
    """API endpoint to get coordinates as JSON"""
    try:
        coordinates, ref_groups = read_coordinates()
        print(f"Sending {len(coordinates)} coordinates with {len(ref_groups)} reference groups")
        return jsonify({
            'coordinates': coordinates,
            'reference_groups': ref_groups
        })
    except Exception as e:
        print(f"Error in get_coordinates: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/pole_image/<path:filename>')
def serve_pole_image(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_folder = os.path.join(base_dir, 'Pole_image')
    return send_from_directory(img_folder, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
