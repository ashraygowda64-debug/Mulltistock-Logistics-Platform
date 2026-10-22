import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Add sample images to warehouses
sample_images = [
    'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=400',
    'https://images.unsplash.com/photo-1553413077-190dd305871c?w=400',
    'https://images.unsplash.com/photo-1565610222536-ef1d8b5d7e5c?w=400',
]

cursor.execute("SELECT id FROM warehouse WHERE is_delete = 0 LIMIT 3")
warehouses = cursor.fetchall()

for idx, (wh_id,) in enumerate(warehouses):
    if idx < len(sample_images):
        cursor.execute("UPDATE warehouse SET warehouse_image = ? WHERE id = ?", (sample_images[idx], wh_id))
        print(f"Updated warehouse {wh_id} with image")

conn.commit()
conn.close()
print("Done!")
