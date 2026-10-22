"""Auto Purge - Remove 181 products automatically"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
django.setup()

from apps.goods.models import ListModel as Product
from apps.stock.models import StockListModel
from django.db import transaction

print("🔍 Starting auto purge...")

with transaction.atomic():
    total = Product.objects.filter(is_delete=False).count()
    print(f"Total products: {total}")
    
    if total <= 100:
        print("✅ Already 100 or fewer products")
    else:
        to_delete = Product.objects.filter(is_delete=False).order_by('id')[100:]
        count = 0
        
        for product in to_delete:
            StockListModel.objects.filter(goods_code=product.goods_code).delete()
            product.is_delete = True
            product.save()
            count += 1
        
        print(f"✅ Deleted {count} products")
        print(f"📊 Remaining: {Product.objects.filter(is_delete=False).count()}")
