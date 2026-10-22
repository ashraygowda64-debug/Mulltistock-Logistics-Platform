import sqlite3
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

print("Counting products...")
cursor.execute("SELECT COUNT(*) FROM goods WHERE is_delete = 0")
total = cursor.fetchone()[0]
print(f"Total products: {total}")

if total <= 100:
    print("Already 100 or fewer products")
    conn.close()
    exit()

print(f"\nDeleting {total - 100} products...")

# Get IDs to keep (first 100)
cursor.execute("SELECT id, goods_code FROM goods WHERE is_delete = 0 ORDER BY id LIMIT 100")
keep_ids = [row[0] for row in cursor.fetchall()]

# Get IDs to delete
cursor.execute("SELECT id, goods_code FROM goods WHERE is_delete = 0 ORDER BY id")
all_products = cursor.fetchall()
delete_products = all_products[100:]

count = 0
for product_id, goods_code in delete_products:
    # Delete stock
    cursor.execute("DELETE FROM stocklist WHERE goods_code = ?", (goods_code,))
    
    # Soft delete product
    cursor.execute("UPDATE goods SET is_delete = 1 WHERE id = ?", (product_id,))
    count += 1

conn.commit()

cursor.execute("SELECT COUNT(*) FROM goods WHERE is_delete = 0")
remaining = cursor.fetchone()[0]

print(f"Deleted {count} products")
print(f"Remaining: {remaining}")

conn.close()
