import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
django.setup()

from goods.models import ListModel as Product
from stock.models import StockListModel, StockMovement
from django.contrib.auth.models import User

print("Creating real stock data...")

# Get admin user
admin = User.objects.get(username='admin')

# Get all products
products = Product.objects.all()

if not products:
    print("No products found. Run populate_complete_data.py first.")
    exit()

# Create stock entries for each product
for product in products:
    stock_qty = random.randint(50, 500)
    
    # Create or update stock
    stock, created = StockListModel.objects.update_or_create(
        goods_code=product.goods_code,
        defaults={
            'goods_desc': product.goods_desc,
            'goods_qty': stock_qty,
            'onhand_stock': stock_qty,
            'can_order_stock': stock_qty,
            'ordered_stock': 0,
            'damage_stock': 0,
            'supplier': product.goods_supplier,
            'openid': 'admin'
        }
    )
    
    # Create stock movements (last 30 days)
    for i in range(random.randint(5, 15)):
        movement_type = random.choice(['in', 'in', 'out', 'adjust'])
        qty = random.randint(5, 50)
        
        reasons = {
            'in': ['Purchase Order', 'Stock Replenishment', 'Return from Customer', 'Transfer In'],
            'out': ['Sales Order', 'Damaged Goods', 'Transfer Out', 'Sample'],
            'adjust': ['Stock Count Adjustment', 'Correction', 'Audit Adjustment']
        }
        
        StockMovement.objects.create(
            goods_code=product.goods_code,
            movement_type=movement_type,
            quantity=qty if movement_type == 'in' else -qty,
            reason=random.choice(reasons[movement_type]),
            user=admin,
            created_at=datetime.now() - timedelta(days=random.randint(0, 30))
        )

print(f"Created stock data for {products.count()} products")
print(f"Created {StockMovement.objects.count()} stock movements")
print("Done!")
