import re

points = {}

with open("gps_data.pdf", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("Image"):
            continue

        parts = line.split()

        # Expect at least: image lat lon label
        if len(parts) < 4:
            continue

        image = parts[0]

        # extract numeric key from image like 5a.jpg → 5
        match = re.match(r"(\d+)a\.jpg", image)
        if not match:
            continue

        key = int(match.group(1))

        try:
            latitude = float(parts[1])
            longitude = float(parts[2])
        except ValueError:
            # invalid lat/lon (you have these)
            continue

        label = " ".join(parts[3:])

        points[key] = {
            "latitude": latitude,
            "longitude": longitude,
            "label": label
        }

print(f"Total valid points: {len(points)}")
