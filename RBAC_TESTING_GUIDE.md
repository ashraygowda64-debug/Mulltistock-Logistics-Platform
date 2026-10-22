# RBAC Testing Guide - Verify Role-Based Access Control

## 🎯 Purpose
This guide helps you verify that the Role-Based Access Control (RBAC) system works correctly across both frontend and backend.

---

## 🚀 Quick Setup

### Step 1: Create Test Users
Run this in Django shell (`python manage.py shell`):

```python
from django.contrib.auth.models import User
from apps.permissions.models import UserRole

# Create test users for each role
users_to_create = [
    ('testadmin', 'admin'),
    ('testsubadmin', 'subadmin'),
    ('testsupervisor', 'supervisor'),
    ('teststaff', 'staff'),
    ('testcustomer', 'customer'),
    ('testseller', 'customer_seller'),
]

for username, role in users_to_create:
    # Create user
    user, created = User.objects.get_or_create(
        username=username,
        defaults={'email': f'{username}@test.com'}
    )
    if created:
        user.set_password('test123')
        user.save()
        print(f"✅ Created user: {username}")
    
    # Assign role
    user_role, created = UserRole.objects.get_or_create(
        user=user,
        defaults={'role': role}
    )
    if created:
        print(f"✅ Assigned role: {role} to {username}")

print("\n✅ All test users created!")
print("Password for all: test123")
```

---

## 📋 Test Cases

### Test 1: SuperAdmin Access (admin/admin123)

#### Backend Tests
1. **Login:** http://127.0.0.1:8000/auth/team-login/
   - Username: `admin`
   - Password: `admin123`
   - ✅ Should login successfully

2. **Dashboard:** http://127.0.0.1:8000/dashboard/
   - ✅ Should see full dashboard with all metrics
   - ✅ Should see "SuperAdmin Dashboard" title

3. **Products:** http://127.0.0.1:8000/products/
   - ✅ Should see "Add Product" button
   - ✅ Should see "Bulk Import" button
   - ✅ Should see "Export" button
   - ✅ Should see edit/delete icons on products

4. **Customers:** http://127.0.0.1:8000/customers/
   - ✅ Should see "Add Customer" button
   - ✅ Should see all customers
   - ✅ Should see export button

5. **Analytics:** http://127.0.0.1:8000/analytics/advanced/
   - ✅ Should have full access
   - ✅ Should see all charts and metrics

6. **Permissions:** http://127.0.0.1:8000/permissions/
   - ✅ Should have access
   - ✅ Should see permission management

7. **Admin Panel:** http://127.0.0.1:8000/admin/
   - ✅ Should have access
   - ✅ Should see all models

8. **Data Purge:** http://127.0.0.1:8000/admin/purge/
   - ✅ Should have access (superuser only)

#### Frontend Tests
- ✅ Sidebar shows all modules
- ✅ All navigation links visible
- ✅ No "Permission Denied" messages
- ✅ All buttons and actions enabled

---

### Test 2: Admin Access (testadmin/test123)

#### Backend Tests
1. **Login:** http://127.0.0.1:8000/auth/team-login/
   - Username: `testadmin`
   - Password: `test123`
   - ✅ Should login successfully

2. **Dashboard:** http://127.0.0.1:8000/dashboard/
   - ✅ Should see admin dashboard
   - ✅ Should see business metrics

3. **Products:** http://127.0.0.1:8000/products/
   - ✅ Should see "Add Product" button
   - ✅ Should see edit/delete icons
   - ✅ Can create, edit, delete products

4. **Permissions:** http://127.0.0.1:8000/permissions/
   - ✅ Should have limited access
   - ✅ Can grant permissions
   - ❌ Cannot create new permission types

5. **Data Purge:** http://127.0.0.1:8000/admin/purge/
   - ❌ Should get "Permission Denied"

#### Frontend Tests
- ✅ Sidebar shows most modules
- ✅ No "Data Purge" link
- ✅ Can perform most operations
- ❌ Cannot access superadmin-only features

---

### Test 3: SubAdmin Access (testsubadmin/test123)

#### Backend Tests
1. **Login:** http://127.0.0.1:8000/auth/team-login/
   - Username: `testsubadmin`
   - Password: `test123`
   - ✅ Should login successfully

2. **Products:** http://127.0.0.1:8000/products/
   - ❌ Should NOT see "Add Product" button
   - ✅ Should see edit icon
   - ❌ Should NOT see delete icon
   - ✅ Can edit existing products
   - ❌ Cannot create new products
   - ❌ Cannot delete products

3. **Orders:** http://127.0.0.1:8000/orders/sales/
   - ✅ Should see "Create Order" button
   - ✅ Can create and manage orders
   - ✅ Can approve orders

4. **Customers:** http://127.0.0.1:8000/customers/
   - ✅ Should see "Add Customer" button
   - ✅ Can add/edit customers
   - ❌ Cannot delete customers

5. **Analytics:** http://127.0.0.1:8000/analytics/advanced/
   - ✅ Should have access
   - ✅ Can view reports
   - ❌ Cannot configure analytics

6. **Permissions:** http://127.0.0.1:8000/permissions/
   - ❌ Should get "Permission Denied"

#### Frontend Tests
- ✅ Sidebar shows operational modules
- ❌ No "Add Product" button
- ❌ No delete buttons on products
- ✅ Edit buttons visible
- ❌ No permission management link

---

### Test 4: Supervisor Access (testsupervisor/test123)

#### Backend Tests
1. **Login:** http://127.0.0.1:8000/auth/team-login/
   - Username: `testsupervisor`
   - Password: `test123`
   - ✅ Should login successfully

2. **Products:** http://127.0.0.1:8000/products/
   - ❌ Should NOT see "Add Product" button
   - ❌ Should NOT see edit icon
   - ❌ Should NOT see delete icon
   - ✅ Can view products
   - ❌ Cannot edit products

3. **Orders:** http://127.0.0.1:8000/orders/sales/
   - ✅ Should see "Create Order" button
   - ✅ Can create orders
   - ✅ Can edit orders
   - ❌ Cannot approve orders

4. **Customers:** http://127.0.0.1:8000/customers/
   - ✅ Should see "Add Customer" button
   - ✅ Can add/edit customers
   - ❌ Cannot delete customers

5. **Analytics:** http://127.0.0.1:8000/analytics/advanced/
   - ✅ Should have basic access
   - ✅ Can view operational reports
   - ❌ Cannot export

6. **Stock:** http://127.0.0.1:8000/stock/
   - ✅ Can view stock
   - ✅ Can adjust stock
   - ❌ Cannot transfer between warehouses

#### Frontend Tests
- ✅ Sidebar shows operational modules
- ❌ No product edit buttons
- ✅ Order management visible
- ❌ No analytics configuration
- ❌ No user management

---

### Test 5: Staff Access (teststaff/test123)

#### Backend Tests
1. **Login:** http://127.0.0.1:8000/auth/team-login/
   - Username: `teststaff`
   - Password: `test123`
   - ✅ Should login successfully

2. **Products:** http://127.0.0.1:8000/products/
   - ✅ Can view products
   - ❌ No action buttons visible
   - ❌ Cannot edit/delete

3. **Orders:** http://127.0.0.1:8000/orders/sales/
   - ✅ Should see "Create Order" button
   - ✅ Can create orders
   - ❌ Cannot edit orders
   - ❌ Cannot cancel orders

4. **Customers:** http://127.0.0.1:8000/customers/
   - ❌ Should get "Permission Denied" or limited view
   - ✅ Can view customer info during order
   - ❌ Cannot manage customers

5. **Analytics:** http://127.0.0.1:8000/analytics/advanced/
   - ❌ Should get "Permission Denied"

6. **Stock:** http://127.0.0.1:8000/stock/
   - ❌ Should get "Permission Denied" or view-only

#### Frontend Tests
- ✅ Sidebar shows minimal modules
- ❌ No edit/delete buttons
- ✅ Can create orders
- ❌ No analytics access
- ❌ No management features

---

### Test 6: Customer Access (testcustomer/test123)

#### Backend Tests
1. **Login:** http://127.0.0.1:8000/auth/customer-login/
   - Username: `testcustomer`
   - Password: `test123`
   - ✅ Should login successfully

2. **Dashboard:** http://127.0.0.1:8000/dashboard/customer/
   - ✅ Should see customer dashboard
   - ✅ Should see own orders
   - ✅ Should see loyalty points

3. **Products:** http://127.0.0.1:8000/products/
   - ✅ Can browse products
   - ❌ No management buttons
   - ❌ Cannot edit anything

4. **Marketplace:** http://127.0.0.1:8000/multistock/marketplace/
   - ✅ Can browse marketplace
   - ✅ Can add to cart
   - ✅ Can place orders

5. **Orders:** http://127.0.0.1:8000/orders/my-orders/
   - ✅ Can view own orders
   - ❌ Cannot view other customers' orders
   - ❌ Cannot access order management

6. **Customers:** http://127.0.0.1:8000/customers/
   - ❌ Should get "Permission Denied"

7. **Analytics:** http://127.0.0.1:8000/analytics/advanced/
   - ❌ Should get "Permission Denied"

#### Frontend Tests
- ✅ Customer sidebar visible
- ✅ Shows marketplace, orders, profile
- ❌ No backend management links
- ❌ No analytics or reports
- ✅ Can participate in forums/auctions

---

### Test 7: Customer Seller Access (testseller/test123)

#### Backend Tests
1. **Login:** http://127.0.0.1:8000/auth/customer-login/
   - Username: `testseller`
   - Password: `test123`
   - ✅ Should login successfully

2. **Products:** http://127.0.0.1:8000/products/
   - ✅ Should see "Add Product" button
   - ✅ Can create own listings
   - ✅ Can edit own products
   - ✅ Can delete own products
   - ❌ Cannot edit other sellers' products

3. **Marketplace:** http://127.0.0.1:8000/multistock/marketplace/
   - ✅ Can manage own listings
   - ✅ Can feature products
   - ❌ Cannot moderate marketplace

4. **Orders:** http://127.0.0.1:8000/orders/sales/
   - ✅ Can view own sales
   - ✅ Can process own orders
   - ❌ Cannot view other sellers' orders

5. **Analytics:** http://127.0.0.1:8000/analytics/advanced/
   - ✅ Can view own sales analytics
   - ✅ Can export own reports
   - ❌ Cannot view platform analytics

6. **Seller Dashboard:** http://127.0.0.1:8000/multistock/seller-dashboard/
   - ✅ Should have access
   - ✅ Can see earnings
   - ✅ Can manage listings

#### Frontend Tests
- ✅ Enhanced customer sidebar
- ✅ Shows seller-specific options
- ✅ Can create product listings
- ✅ Can view own analytics
- ❌ No access to other sellers' data

---

### Test 8: Guest Access (Not logged in)

#### Backend Tests
1. **Home:** http://127.0.0.1:8000/
   - ✅ Should see landing page
   - ✅ Should see login options

2. **Products:** http://127.0.0.1:8000/products/
   - ✅ Can browse products (if public)
   - ❌ No action buttons
   - ❌ Cannot add to cart

3. **Marketplace:** http://127.0.0.1:8000/multistock/marketplace/
   - ✅ Can view marketplace
   - ❌ Cannot buy
   - ❌ Cannot bid

4. **Forums:** http://127.0.0.1:8000/multistock/forums/
   - ✅ Can view forums
   - ❌ Cannot post
   - ❌ Cannot reply

5. **Dashboard:** http://127.0.0.1:8000/dashboard/
   - ❌ Should redirect to login

6. **Orders:** http://127.0.0.1:8000/orders/sales/
   - ❌ Should redirect to login

#### Frontend Tests
- ✅ Guest navbar visible
- ✅ Shows login/register buttons
- ❌ No sidebar
- ❌ No action buttons
- ✅ Can browse public content

---

## 🔍 API Testing

### Test API Permissions

#### Products API
```bash
# Without authentication
curl http://127.0.0.1:8000/products/api/
# ✅ Should return products (public read)

# Try to create (should fail)
curl -X POST http://127.0.0.1:8000/products/api/create/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","sku":"TEST-001","price":99}'
# ❌ Should return 401 Unauthorized

# With authentication (as admin)
curl -X POST http://127.0.0.1:8000/products/api/create/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{"name":"Test","sku":"TEST-001","price":99}'
# ✅ Should create product
```

---

## ✅ Verification Checklist

### Backend Verification
- [ ] SuperAdmin can access everything
- [ ] Admin cannot purge data
- [ ] SubAdmin cannot create/delete products
- [ ] Supervisor cannot edit products
- [ ] Staff cannot access analytics
- [ ] Customer cannot access backend
- [ ] Seller can only manage own products
- [ ] Guest cannot create orders

### Frontend Verification
- [ ] Buttons hidden based on permissions
- [ ] Sidebar shows correct modules per role
- [ ] Customer sees customer sidebar
- [ ] Staff sees staff sidebar
- [ ] Permission denied shows proper message
- [ ] No broken links or 404 errors

### Integration Verification
- [ ] Login redirects to correct dashboard
- [ ] Logout clears permissions
- [ ] API returns 403 for unauthorized
- [ ] Forms disabled for unauthorized actions
- [ ] Audit logs track all actions

---

## 🐛 Common Issues

### Issue: "Permission Denied" but user should have access
**Check:**
1. User role assigned correctly in database
2. Permission matrix includes the module/action
3. View has correct decorator
4. User is logged in

### Issue: Button visible but action fails
**Check:**
1. Frontend template has permission check
2. Backend view has permission decorator
3. API endpoint has permission class

### Issue: Wrong sidebar showing
**Check:**
1. `base.html` checks `user.is_staff`
2. Correct sidebar template included
3. User role set correctly

---

## 📊 Expected Results Summary

| Role | Products | Orders | Customers | Analytics | Permissions | Admin Panel |
|------|----------|--------|-----------|-----------|-------------|-------------|
| SuperAdmin | Full | Full | Full | Full | Full | Full |
| Admin | Full | Full | Full | Full | Limited | Limited |
| SubAdmin | Edit Only | Full | Add/Edit | View | None | None |
| Supervisor | View Only | Create/Edit | Add/Edit | Basic | None | None |
| Staff | View Only | Create | View | None | None | None |
| Customer | Browse | Own Only | Own Only | None | None | None |
| Seller | Own Products | Own Sales | Own Data | Own Stats | None | None |
| Guest | Browse | None | None | None | None | None |

---

## 🎯 Success Criteria

✅ **RBAC System is Working if:**
1. Each role can only access permitted modules
2. Action buttons hidden for unauthorized users
3. API returns 403 for unauthorized requests
4. Permission denied shows proper error message
5. Audit logs track all permission checks
6. No security bypasses possible

---

**Status:** Ready for testing
**Last Updated:** 2024
**Platform:** MultiStock v1.0
