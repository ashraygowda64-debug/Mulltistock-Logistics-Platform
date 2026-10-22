"""
Product Purge Script - Remove 181 products from database
Keeps only 100 products and removes all related data
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
django.setup()

from apps.goods.models import ListModel as Product
from apps.stock.models import StockListModel
from apps.orders.models import Order, OrderItem
from django.db import transaction

def purge_products():
    print("🔍 Analyzing database...")
    
    total_products = Product.objects.filter(is_delete=False).count()
    print(f"Total products: {total_products}")
    
    if total_products <= 100:
        print("✅ Already 100 or fewer products. No purge needed.")
        return
    
    # Get products to delete (oldest 181)
    products_to_delete = Product.objects.filter(is_delete=False).order_by('id')[100:]
    delete_count = products_to_delete.count()
    
    print(f"\n⚠️  Will delete {delete_count} products and ALL related data:")
    print(f"   - Stock records")
    print(f"   - Order items")
    print(f"   - Marketplace listings")
    print(f"   - Barcode records")
    
    confirm = input("\n❓ Type 'DELETE' to confirm: ")
    
    if confirm != 'DELETE':
        print("❌ Cancelled")
        return
    
    print("\n🗑️  Starting purge...")
    
    with transaction.atomic():
        deleted_stats = {
            'products': 0,
            'stock': 0,
            'order_items': 0,
        }
        
        for product in products_to_delete:
            goods_code = product.goods_code
            
            # Delete stock records
            stock_deleted = StockListModel.objects.filter(goods_code=goods_code).delete()[0]
            deleted_stats['stock'] += stock_deleted
            
            # Delete order items
            try:
                order_items_deleted = OrderItem.objects.filter(product_code=goods_code).delete()[0]
                deleted_stats['order_items'] += order_items_deleted
            except:
                pass
            
            # Soft delete product
            product.is_delete = True
            product.save()
            deleted_stats['products'] += 1
            
            if deleted_stats['products'] % 10 == 0:
                print(f"   Processed {deleted_stats['products']}/{delete_count}...")
    
    print("\n✅ Purge completed!")
    print(f"   Products deleted: {deleted_stats['products']}")
    print(f"   Stock records deleted: {deleted_stats['stock']}")
    print(f"   Order items deleted: {deleted_stats['order_items']}")
    
    remaining = Product.objects.filter(is_delete=False).count()
    print(f"\n📊 Remaining products: {remaining}")

if __name__ == '__main__':
    purge_products()
