from gps_data_dict import gps_data
import re

# Test the regex on R0 labels
test_labels = [
    'VC-XX-R0-PWL-01',
    'VC-XX-R00-CPT-01',
    'VC-XX-R03-PWL-01'
]

for label in test_labels:
    ref_match = re.search(r'R(\d+|XX)', label, re.IGNORECASE)
    ref_group = ref_match.group(0).upper() if ref_match else 'UNKNOWN'
    print(f"{label} -> {ref_group}")

print("\nActual R0 poles in data:")
for pole_id, data in gps_data.items():
    label = data.get('label', '')
    if 'R0-' in label or '-R0-' in label:
        ref_match = re.search(r'R(\d+|XX)', label, re.IGNORECASE)
        ref_group = ref_match.group(0).upper() if ref_match else 'UNKNOWN'
        print(f"  ID {pole_id}: {label} -> ref_group: {ref_group}")
