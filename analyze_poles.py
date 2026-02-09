from gps_data_dict import gps_data
import re

types = {}
for pole_id, data in gps_data.items():
    label = data.get('label', '')
    match = re.findall(r'-([A-Z]{3})-', label)
    pole_type = match[0] if match else 'UNKNOWN'
    if pole_type not in types:
        types[pole_type] = []
    types[pole_type].append(pole_id)

print('Pole types and counts:')
print('-' * 40)
total = 0
for pole_type in sorted(types.keys()):
    count = len(types[pole_type])
    total += count
    print(f'{pole_type}: {count} poles')
    
print('-' * 40)
print(f'Total: {total} poles')

# Check which are control vs dependent according to current logic
control_count = 0
dependent_count = 0
for pole_type in types:
    if pole_type in ['CPT', 'CPM', 'CPL']:
        control_count += len(types[pole_type])
    else:
        dependent_count += len(types[pole_type])

print(f'\nCurrent categorization:')
print(f'Control points (CPT/CPM/CPL): {control_count}')
print(f'Dependent poles (PWL/PNL): {dependent_count}')
