# Guest Access - Testing Checklist

## 🧪 Complete Testing Guide

Use this checklist to verify all guest pages work correctly.

---

## ⚡ Quick Start

```bash
# 1. Start the server
cd GreaterWMS
.\start.bat

# 2. Open browser to:
http://127.0.0.1:8000/
```

---

## 📋 Testing Checklist

### 1. Home Page & Guest Entry
- [ ] Visit `http://127.0.0.1:8000/`
- [ ] Verify login selection page loads
- [ ] Click "Browse as Guest" button
- [ ] Verify redirect to `/guest/dashboard/`
- [ ] Check guest badge appears in navbar

**Expected Result:** Smooth redirect to guest dashboard with guest badge visible

---

### 2. Guest Dashboard (`/guest/dashboard/`)
- [ ] Page loads without errors
- [ ] Animated stat cards display
- [ ] Marketplace count shows (number or 0)
- [ ] Auctions count shows (number or 0)
- [ ] Forums count shows (number or 0)
- [ ] About card displays
- [ ] Hover effects work on cards
- [ ] Click "Marketplace" card → redirects to `/guest/marketplace/`
- [ ] Click "Auctions" card → redirects to `/guest/auctions/`
- [ ] Click "Forums" card → redirects to `/guest/forums/`
- [ ] Click "About" card → redirects to `/guest/about/`
- [ ] "Create Account" button works
- [ ] "Sign In" button works

**Expected Result:** All cards clickable, counts accurate, no errors

---

### 3. Guest Marketplace (`/guest/marketplace/`)
- [ ] Page loads without errors
- [ ] Product grid displays
- [ ] Each product shows:
  - [ ] Product title (not "None" or blank)
  - [ ] Product price (formatted as $XX.XX)
  - [ ] Product category
  - [ ] Product icon/image placeholder
- [ ] "View Details" button on each product
- [ ] Click "View Details" → shows login prompt
- [ ] Confirm login prompt → redirects to register page
- [ ] If no products: "No Products Available" message shows

**Expected Result:** Products display correctly with titles and prices

---

### 4. Guest Auctions (`/guest/auctions/`)
- [ ] Page loads without errors
- [ ] Auction grid displays
- [ ] Category chips display at top
- [ ] Each auction shows:
  - [ ] Auction title (not "None" or blank)
  - [ ] Current price (formatted as $XXX)
  - [ ] "LIVE" badge (red, pulsing)
  - [ ] Time left display
  - [ ] Auction icon
- [ ] "Place Bid" button on each auction
- [ ] Click "Place Bid" → shows login prompt
- [ ] Confirm login prompt → redirects to register page
- [ ] If no auctions: "No Active Auctions" message shows

**Expected Result:** Auctions display with correct current_price values

---

### 5. Guest Forums (`/guest/forums/`)
- [ ] Page loads without errors
- [ ] Forum categories display (4 cards)
- [ ] Each category shows:
  - [ ] Category name
  - [ ] Category icon
  - [ ] Description
  - [ ] Topic count
  - [ ] Post count
  - [ ] Latest activity
- [ ] Recent discussions section displays
- [ ] Each post shows:
  - [ ] Author username (not "User object")
  - [ ] Forum title (not "None")
  - [ ] Post content (truncated)
  - [ ] Timestamp (e.g., "2 hours ago")
- [ ] Click forum category → shows login prompt
- [ ] "Create Account" and "Sign In" buttons work
- [ ] If no posts: Sample post displays

**Expected Result:** Forum posts show author.username and forum.title correctly

---

### 6. Guest About (`/guest/about/`)
- [ ] Page loads without errors
- [ ] Platform features section displays (6 cards)
- [ ] Statistics section displays (4 stats)
- [ ] Technology stack section displays (6 tech cards)
- [ ] FAQ section displays (5 questions)
- [ ] Click FAQ question → answer toggles
- [ ] Chevron icon rotates on toggle
- [ ] "Create Account" button works
- [ ] "Sign In" button works

**Expected Result:** All sections render, FAQ toggle works

---

### 7. Navigation & UI
- [ ] Navbar displays on all pages
- [ ] "GUEST" badge visible in navbar
- [ ] Active page highlighted in navbar
- [ ] All navbar links work:
  - [ ] Dashboard
  - [ ] Marketplace
  - [ ] Auctions
  - [ ] Forums
  - [ ] About
- [ ] "Register" button in navbar works
- [ ] "Login" button in navbar works
- [ ] "Exit" button in navbar works
- [ ] Footer displays on all pages
- [ ] Footer links work
- [ ] Background particles animate

**Expected Result:** Smooth navigation, all links functional

---

### 8. Exit Guest Mode
- [ ] Click "Exit" button in navbar
- [ ] Verify redirect to home page (`/`)
- [ ] Verify guest session cleared
- [ ] Verify back to login selection page

**Expected Result:** Clean exit, session cleared

---

### 9. Responsive Design
- [ ] Test on desktop (1920x1080)
- [ ] Test on tablet (768x1024)
- [ ] Test on mobile (375x667)
- [ ] Navbar collapses on mobile
- [ ] Cards stack properly on mobile
- [ ] Text remains readable
- [ ] Buttons remain clickable

**Expected Result:** Works on all screen sizes

---

### 10. Error Handling
- [ ] No "FieldError" messages
- [ ] No "DoesNotExist" exceptions
- [ ] No template syntax errors
- [ ] No broken images (placeholders OK)
- [ ] No console JavaScript errors
- [ ] Empty states display properly

**Expected Result:** No errors in browser or console

---

## 🔍 Common Issues to Check

### ❌ What NOT to See:
- "FieldError: Cannot resolve keyword 'name'"
- "FieldError: Cannot resolve keyword 'current_bid'"
- "FieldError: Cannot resolve keyword 'is_active' on model 'Forum'"
- "User object (1)" instead of username
- "None" instead of actual values
- Template syntax errors like `{ % block %}`

### ✅ What TO See:
- Actual product titles (e.g., "Premium Laptop")
- Actual prices (e.g., "$999.99")
- Usernames (e.g., "john_doe")
- Forum titles (e.g., "General Discussion")
- Proper timestamps (e.g., "2 hours ago")

---

## 🤖 Automated Testing

Run the automated test script:

```bash
python test_guest_pages.py
```

**Expected Output:**
```
============================================================
GUEST PAGES TEST REPORT
============================================================

✅ PASS                        | Home Page                 | /
✅ PASS                        | Guest Dashboard           | /guest/dashboard/
✅ PASS                        | Guest Marketplace         | /guest/marketplace/
✅ PASS                        | Guest Auctions            | /guest/auctions/
✅ PASS                        | Guest Forums              | /guest/forums/
✅ PASS                        | Guest About               | /guest/about/

============================================================
SUMMARY: 6 Passed | 0 Failed | 0 Warnings
============================================================
```

---

## 📊 Test Results Template

Copy and fill this out:

```
GUEST ACCESS TEST RESULTS
Date: _______________
Tester: _______________

[ ] Home Page - PASS / FAIL
[ ] Guest Dashboard - PASS / FAIL
[ ] Guest Marketplace - PASS / FAIL
[ ] Guest Auctions - PASS / FAIL
[ ] Guest Forums - PASS / FAIL
[ ] Guest About - PASS / FAIL
[ ] Navigation - PASS / FAIL
[ ] Exit Guest Mode - PASS / FAIL
[ ] Responsive Design - PASS / FAIL
[ ] Error Handling - PASS / FAIL

Issues Found:
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

Overall Status: PASS / FAIL
Notes: _______________________________________________
```

---

## 🐛 Troubleshooting

### Issue: "FieldError: Cannot resolve keyword 'name'"
**Solution:** Already fixed - template uses `listing.title` now

### Issue: "FieldError: Cannot resolve keyword 'current_bid'"
**Solution:** Already fixed - template uses `auction.current_price` now

### Issue: Forum posts show "User object (1)"
**Solution:** Already fixed - template uses `post.author.username` now

### Issue: No data displays
**Solution:** 
1. Check if database has data
2. Run migrations: `python manage.py migrate`
3. Create test data via admin panel

### Issue: Page returns 404
**Solution:** 
1. Verify URL is correct
2. Check `urls.py` has guest paths
3. Restart server

---

## ✅ Sign-Off

Once all tests pass:

```
✅ All guest pages tested and working
✅ No errors or exceptions
✅ Data displays correctly
✅ Navigation works smoothly
✅ Ready for production

Tested by: _______________
Date: _______________
Signature: _______________
```

---

**Happy Testing! 🎉**
