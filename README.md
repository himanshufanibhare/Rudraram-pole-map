# TTDF Rudraram Map - GPS Pole Mapping System

A comprehensive web-based GPS mapping application for tracking and managing street light poles in the Rudraram area. This interactive map system visualizes 359 pole locations with detailed information about control points, dependent poles, and high mast lights.

![Map Application](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Leaflet](https://img.shields.io/badge/Leaflet-1.9.4-brightgreen.svg)

## 🌟 Features

### Core Functionality
- **Interactive Map Display**: Powered by Leaflet.js with OpenStreetMap tiles
- **359 GPS Pole Locations**: Accurately plotted control points and dependent poles
- **Smart Filtering System**: 
  - Filter by control points (CPT/CPM/CPTHM/CPMHM)
  - Filter by dependent poles (PWL/PNL)
  - Toggle pole ID number visibility
  - Multi-select control point filtering with reference groups

### Visual Features
- **Color-Coded Markers**:
  - 🟡 **Yellow** - High Mast Light poles
  - 🟢 **Green** - Control Points (CPT/CPM)
  - 🔴 **Red** - Dependent Poles (PWL/PNL)
- **Dynamic Legend**: Shows pole type classifications
- **Collapsible Filter Panel**: Expandable/collapsible side panel for better map visibility
- **Pole ID Labels**: Numbered badges on markers for easy identification

### Advanced Features
- **Distance Measurement**: 
  - Select any two poles to measure distance
  - Haversine formula for accurate calculations
  - Visual line drawing between selected poles
  - Distance displayed in meters
- **Pole Images**: 
  - View pole photographs (a/b views)
  - Lightbox modal for image viewing
  - Supports multiple image formats (jpg, jpeg, png, webp)
- **Location Names**: Custom location labels for control points (e.g., "GP Office", "MPPH School NH9")
- **Reference Group Sorting**: Control points organized by reference groups (R01, R10, R17, etc.)
- **Lighting Information**:
  - Number of lights per pole
  - Light type (LED/NA)
  - Working status indicator

### User Interface
- **Responsive Design**: Works on desktop and mobile devices
- **Multiple Map Layers**: Switch between different tile providers
- **Quick Navigation**: "Go to Location" button for specific coordinates
- **Statistics Display**: Shows visible poles vs total poles count
- **Clear All / Show All**: Quick filter reset buttons

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Installation

### 1. Clone or Download the Project

```bash
cd D:\Himanshu\TTDF_RUDRARAM_MAP\TTDF_RUDRARAM_MAP
```

### 2. Create Virtual Environment

```powershell
# Windows PowerShell
python -m venv .venv

# Activate the virtual environment
.\.venv\Scripts\Activate
```

```bash
# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- Flask==3.0.0
- pandas==2.1.4
- openpyxl==3.1.2
- Werkzeug==3.0.1

### 4. Verify Project Structure

Ensure the following structure exists:

```
TTDF_RUDRARAM_MAP/
├── app.py                      # Flask application
├── gps_data_dict.py           # GPS coordinates database
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── Pole_image/               # Pole photographs (optional)
│   ├── 1a.jpg
│   ├── 1b.jpg
│   └── ...
├── static/
│   └── style.css             # Application styles
└── templates/
    └── index.html            # Main HTML template
```

## 🎯 Usage

### Starting the Application

1. **Activate virtual environment** (if not already activated):
   ```bash
   .\.venv\Scripts\Activate
   ```

2. **Run the Flask server**:
   ```bash
   python app.py
   ```

3. **Open in browser**:
   - Local: http://127.0.0.1:5000
   - Network: http://10.2.16.104:5000 (or your machine's IP)

### Using the Map

#### Filtering Poles
1. **Control Points Filter**:
   - Uncheck/check the "Control Points (CPT/CPM)" checkbox
   - Use the control point list to filter by specific reference groups
   - "Select All" checkbox to toggle all control points

2. **Dependent Poles Filter**:
   - Uncheck/check "Dependent Poles (PWL/PNL)" to show/hide all dependent poles

3. **Pole ID Numbers**:
   - Toggle "Show Pole ID Numbers" to display/hide numeric labels

#### Measuring Distance
1. Click on any pole marker to open its popup
2. Check the "Measure Distance" checkbox
3. Click on a second pole and check its "Measure Distance" checkbox
4. The distance will be calculated and displayed in the Distance Measurement section
5. A line will be drawn between the two poles
6. Click "Clear Selection" to reset

#### Viewing Pole Images
1. Click on a pole marker that has images (View Images button will appear)
2. Click "View Images" button
3. Images will open in a modal/lightbox viewer
4. Click the close button (✕) or click outside to close

#### Navigation
- **Pan**: Click and drag the map
- **Zoom**: Use mouse wheel or +/- buttons
- **Go to Location**: Click the "📍 Go to Location" button for quick navigation

## 📁 Project Structure

### Backend Files

#### `app.py`
Main Flask application with routes:
- `/` - Main map page
- `/api/coordinates` - JSON API for GPS data
- `/pole_image/<filename>` - Image serving endpoint

Key functions:
- `read_coordinates()` - Loads and processes GPS data
- Determines pole types (control/dependent/high mast light)
- Attaches image URLs if available

#### `gps_data_dict.py`
Database of 359 poles with structure:
```python
gps_data = {
    1: {
        'latitude': '17.546980',
        'longitude': '78.15911',
        'label': 'WC-S01-R10-PWL-01',
        'high-mast-light': 'NO',
        'no of lights': '3',
        'light type': 'LED',
        'working': 'YES',
        'location': ''  # Optional location name
    },
    # ... 358 more entries
}
```

### Frontend Files

#### `templates/index.html`
Single-page application with:
- Leaflet.js map initialization
- Filter panel with checkboxes
- Distance measurement logic
- Image modal/lightbox
- Popup content generation

#### `static/style.css`
Comprehensive styling for:
- Map container and overlays
- Filter panel and controls
- Marker styles and labels
- Popup content layout
- Modal/lightbox styles
- Responsive design

## 🔧 Configuration

### Adding New Poles

Edit `gps_data_dict.py`:

```python
360: {
    'latitude': '17.123456',
    'longitude': '78.123456',
    'label': 'WC-XX-R25-CPT-01',
    'high-mast-light': 'NO',
    'no of lights': '2',
    'light type': 'LED',
    'working': 'YES',
    'location': 'New Location Name'
}
```

### Adding Pole Images

1. Place images in the `Pole_image/` folder
2. Name format: `<pole_id>a.<ext>` and `<pole_id>b.<ext>`
   - Example: For pole ID 27: `27a.jpg` and `27b.jpg`
3. Supported formats: jpg, jpeg, png, webp

### Pole Type Classification

The system automatically classifies poles based on label patterns:
- **Control Points**: Labels containing `-CPT-`, `-CPM-`, `-CPTHM-`, `-CPMHM-`
- **High Mast Light**: Labels containing `-HML-` OR having `'high-mast-light': 'YES'`
- **Dependent Poles**: All other poles (PWL, PNL, etc.)

### Map Customization

#### Change Default Center/Zoom
Edit in `templates/index.html`:
```javascript
const map = L.map('map').setView([17.555, 78.165], 15);
```

#### Add Map Tile Layers
```javascript
const osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
});
```

## 🎨 Color Scheme

| Element | Color | Hex Code |
|---------|-------|----------|
| High Mast Light Poles | Yellow | #FFD700 |
| Control Points | Green | #4CAF50 |
| Dependent Poles | Red | #ff4444 |
| Primary Accent | Blue | #667eea |
| Distance Measurement | Blue | #3b82f6 |

## 🗺️ Reference Groups

The system organizes poles by reference groups extracted from labels:
- **R00** - Special reference group
- **R01** through **R27** - Standard reference groups
- **RXX** - Miscellaneous/unclassified

Control points are automatically sorted by reference group number (R01, R02, ... R27).

## 📊 Data Statistics

- **Total Poles**: 359
- **Control Points**: ~50+ (CPT/CPM types)
- **Dependent Poles**: ~300+ (PWL/PNL types)
- **High Mast Lights**: 6 poles
- **Reference Groups**: 22 groups (R00-R27, RXX)
- **Poles with Images**: Variable (based on Pole_image folder)
- **Poles with Location Names**: Variable (user-defined)

## 🛠️ Troubleshooting

### Map Not Loading
- Check if Flask server is running
- Verify port 5000 is not blocked
- Check browser console for JavaScript errors
- Ensure internet connection for map tiles

### Images Not Displaying
- Verify `Pole_image/` folder exists
- Check image file naming convention: `<id>a.jpg`, `<id>b.jpg`
- Ensure file extensions are lowercase
- Check browser console for 404 errors

### Poles Not Showing
- Check `gps_data_dict.py` for syntax errors
- Verify latitude/longitude are valid numbers
- Check filter settings (all controls unchecked will hide poles)
- Open browser console to see error messages

### Distance Measurement Not Working
- Only works between two poles
- Must check the "Measure Distance" checkbox in both popups
- Clear previous selection before measuring new distance

### Performance Issues
- Large number of poles may slow older browsers
- Try closing unused browser tabs
- Clear browser cache
- Disable pole ID labels if map is slow

## 🔐 Security Notes

- This application runs in debug mode by default
- For production deployment:
  - Set `debug=False` in `app.py`
  - Use a production WSGI server (Gunicorn, uWSGI)
  - Configure proper firewall rules
  - Add authentication if needed

## 🚀 Advanced Features (Future)

Potential enhancements:
- [ ] Export pole data to CSV/Excel
- [ ] Import GPS data from external files
- [ ] User authentication and roles
- [ ] Pole maintenance history tracking
- [ ] Mobile app version
- [ ] Offline map caching
- [ ] Route planning between poles
- [ ] Area/zone management
- [ ] Reporting and analytics dashboard

## 📝 Development Notes

### Technology Stack
- **Backend**: Python 3.10+, Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Mapping**: Leaflet.js 1.9.4
- **Map Tiles**: OpenStreetMap, CartoDB
- **Data Format**: Python dictionary (in-memory)
- **Styling**: Custom CSS with flexbox/grid layouts

### Code Organization
- Modular JavaScript functions for map operations
- Separation of concerns (data, presentation, logic)
- Responsive CSS with mobile-first approach
- RESTful API design for coordinates endpoint

## 📄 License

[Specify your license here - MIT, Apache 2.0, etc.]

## 👥 Contributors

Himanshu Fanibhare

## 📞 Support

For issues or questions:
- Create an issue in the repository
- Contact: [Your contact information]

## 🔄 Version History

### v1.0.0 (Current)
- Initial release
- 359 GPS pole locations
- Interactive filtering and distance measurement
- Image viewing capability
- Collapsible filter panel
- High mast light support
- Location name display
- Reference group organization

---

**Note**: This application is designed for managing street light infrastructure in the Rudraram area. Ensure GPS coordinates are accurate before deployment.
