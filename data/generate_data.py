import pandas as pd
import numpy as np

np.random.seed(42)

rows = 5000  # you can increase later

area = np.random.randint(500, 5000, rows)
floors = np.random.randint(1, 5, rows)
location_index = np.random.randint(0, 3, rows)
material_quality = np.random.randint(0, 3, rows)
labor_cost_index = np.random.uniform(0.8, 1.5, rows)
building_type = np.random.randint(0, 2, rows)
parking = np.random.randint(0, 2, rows)
basement = np.random.randint(0, 2, rows)
year = np.random.randint(2015, 2028, rows)


# Cost calculation logic (important!)
cost = (
    area * 1200 +
    floors * 200000 +
    location_index * 300000 +
    material_quality * 250000 +
    labor_cost_index * 150000 +
    building_type * 400000 +
    parking * 100000 +
    basement * 150000 +
    (year - 2015) * 50000 +
    np.random.randint(-50000, 50000, rows)
)

data = pd.DataFrame({
    "area": area,
    "floors": floors,
    "location_index": location_index,
    "material_quality": material_quality,
    "labor_cost_index": labor_cost_index,
    "building_type": building_type,
    "parking": parking,
    "basement": basement,
    "year": year,
    "cost": cost
})

data.to_csv("building_data.csv", index=False)

print("✅ Dataset generated successfully!")