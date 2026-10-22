"""
Guest Pages Test Script
Run this to verify all guest pages load without errors
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

def test_guest_pages():
    """Test all guest pages"""
    client = Client()
    
    test_results = []
    
    # Test URLs
    guest_urls = [
        ('/', 'Home Page'),
        ('/guest/dashboard/', 'Guest Dashboard'),
        ('/guest/marketplace/', 'Guest Marketplace'),
        ('/guest/auctions/', 'Guest Auctions'),
        ('/guest/forums/', 'Guest Forums'),
        ('/guest/about/', 'Guest About'),
    ]
    
    print("=" * 60)
    print("GUEST PAGES TEST REPORT")
    print("=" * 60)
    print()
    
    for url, name in guest_urls:
        try:
            response = client.get(url, follow=True)
            status = response.status_code
            
            if status == 200:
                result = "✅ PASS"
                # Check for template errors
                content = response.content.decode('utf-8')
                if 'FieldError' in content or 'DoesNotExist' in content or 'Exception' in content:
                    result = "⚠️  WARNING - Possible error in content"
            else:
                result = f"❌ FAIL (Status: {status})"
            
            test_results.append((name, url, result))
            print(f"{result:30} | {name:25} | {url}")
            
        except Exception as e:
            result = f"❌ ERROR: {str(e)[:50]}"
            test_results.append((name, url, result))
            print(f"{result:30} | {name:25} | {url}")
    
    print()
    print("=" * 60)
    
    # Summary
    passed = sum(1 for _, _, r in test_results if '✅' in r)
    failed = sum(1 for _, _, r in test_results if '❌' in r)
    warnings = sum(1 for _, _, r in test_results if '⚠️' in r)
    
    print(f"SUMMARY: {passed} Passed | {failed} Failed | {warnings} Warnings")
    print("=" * 60)
    
    return all('✅' in r for _, _, r in test_results)

if __name__ == '__main__':
    success = test_guest_pages()
    exit(0 if success else 1)
