"""
Test script to verify guest templates are being used correctly
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
django.setup()

from django.contrib.auth.models import User
from django.test import RequestFactory, Client
from django.contrib.sessions.middleware import SessionMiddleware

print("=" * 80)
print("GUEST TEMPLATE VERIFICATION TEST")
print("=" * 80)

# Check if guest templates exist
template_dir = "templates/multistock/"
guest_templates = [
    'guest_marketplace.html',
    'guest_forums.html', 
    'guest_auctions.html'
]

print("\n1. Checking Guest Template Files:")
print("-" * 80)
for template in guest_templates:
    template_path = os.path.join(template_dir, template)
    if os.path.exists(template_path):
        size = os.path.getsize(template_path)
        print(f"✅ {template:<30} EXISTS ({size:,} bytes)")
    else:
        print(f"❌ {template:<30} MISSING")

# Test guest user session
print("\n2. Testing Guest User Session:")
print("-" * 80)
try:
    guest_user = User.objects.get(username='guest_user')
    print(f"✅ Guest user exists: {guest_user.username}")
    print(f"   - Email: {guest_user.email}")
    print(f"   - Is Staff: {guest_user.is_staff}")
    print(f"   - Is Active: {guest_user.is_active}")
except User.DoesNotExist:
    print("❌ Guest user does NOT exist")

# Test view routing with Django test client
print("\n3. Testing View Routing with Guest Session:")
print("-" * 80)

client = Client()

# Simulate guest access
response = client.get('/auth/guest-access/', follow=True)
print(f"Guest Access Response: {response.status_code}")
print(f"Redirected to: {response.redirect_chain if hasattr(response, 'redirect_chain') else 'N/A'}")

# Check session flags
session = client.session
print(f"\nSession Flags:")
print(f"  - is_guest: {session.get('is_guest', False)}")
print(f"  - guest_mode: {session.get('guest_mode', False)}")
print(f"  - login_verified: {session.get('login_verified', False)}")

# Test marketplace with guest session
print("\n4. Testing Marketplace View:")
print("-" * 80)
response = client.get('/multistock/marketplace/')
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    template_names = [t.name for t in response.templates if t.name]
    print(f"Templates Used: {template_names}")
    if 'multistock/guest_marketplace.html' in template_names:
        print("✅ CORRECT: Using guest_marketplace.html")
    elif 'multistock/marketplace.html' in template_names:
        print("❌ WRONG: Using regular marketplace.html instead of guest template")
    else:
        print(f"⚠️  UNKNOWN: Using template: {template_names}")

# Test forums with guest session
print("\n5. Testing Forums View:")
print("-" * 80)
response = client.get('/multistock/forums/')
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    template_names = [t.name for t in response.templates if t.name]
    print(f"Templates Used: {template_names}")
    if 'multistock/guest_forums.html' in template_names:
        print("✅ CORRECT: Using guest_forums.html")
    elif 'multistock/forums.html' in template_names:
        print("❌ WRONG: Using regular forums.html instead of guest template")
    else:
        print(f"⚠️  UNKNOWN: Using template: {template_names}")

# Test auctions with guest session
print("\n6. Testing Auctions View:")
print("-" * 80)
response = client.get('/multistock/auctions/')
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    template_names = [t.name for t in response.templates if t.name]
    print(f"Templates Used: {template_names}")
    if 'multistock/guest_auctions.html' in template_names:
        print("✅ CORRECT: Using guest_auctions.html")
    elif 'multistock/auctions.html' in template_names:
        print("❌ WRONG: Using regular auctions.html instead of guest template")
    else:
        print(f"⚠️  UNKNOWN: Using template: {template_names}")

# Test view logic directly
print("\n7. Testing View Logic Directly:")
print("-" * 80)
from apps.multistock.views import marketplace_view, forums_view, auctions_view

factory = RequestFactory()

# Create request with guest session
request = factory.get('/multistock/marketplace/')
middleware = SessionMiddleware(lambda x: x)
middleware.process_request(request)
request.session['is_guest'] = True
request.session['guest_mode'] = True
request.session.save()

# Mock user
request.user = guest_user

print(f"Session flags: is_guest={request.session.get('is_guest')}, guest_mode={request.session.get('guest_mode')}")
print(f"User authenticated: {request.user.is_authenticated}")
print(f"User: {request.user.username}")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
