# Analytics Dashboard Implementation Guide

## ✅ Completed: Coupons Module
- Analytics page: `/coupons/analytics/`
- Metrics: Total, Active, Redemptions, Savings
- Charts: Trend line chart, Status doughnut chart
- Tables: Top performers, Recent activity

## 🔧 Quick Implementation for Remaining Modules

### 1. Customers Analytics (`/customers/analytics/`)
**Metrics:**
- Total Customers
- Active Customers
- New This Month
- Total Revenue

**View Code:**
```python
@login_required
def customer_analytics(request):
    from customer.models import ListModel as Customer
    total = Customer.objects.count()
    active = Customer.objects.filter(is_active=True).count()
    context = {'total_customers': total, 'active_customers': active}
    return render(request, 'customers/analytics.html', context)
```

### 2. Suppliers Analytics (`/suppliers/analytics/`)
**Metrics:**
- Total Suppliers
- Active Suppliers
- Total Orders
- Total Value

### 3. Team Analytics (`/team/analytics/`)
**Metrics:**
- Total Members
- Active Members
- Roles Distribution
- Performance Score

### 4. Rentals Analytics (`/rentals/analytics/`)
**Metrics:**
- Total Items
- Available Items
- Total Bookings
- Revenue

### 5. Storage Analytics (`/storage/analytics/`)
**Metrics:**
- Total Units
- Occupied Units
- Utilization Rate
- Revenue

### 6. Lockers Analytics (`/lockers/analytics/`)
**Metrics:**
- Total Lockers
- Available Lockers
- Bookings Today
- Occupancy Rate

### 7. Warehouse Analytics (Already Exists)
- Page: `/warehouses/`
- Has metrics cards and charts

## 📋 Implementation Steps

1. **Create analytics.html** in module's templates folder
2. **Add URL route** in module's urls.py: `path('analytics/', views.module_analytics, name='analytics')`
3. **Add view function** in module's views.py with database queries
4. **Add navigation link** in sidebar or module page

## 🎨 Template Structure

```html
{% extends 'base.html' %}
{% block content %}
<div class="container-fluid py-4">
    <!-- Metrics Cards -->
    <div class="row mb-4">
        <div class="col-md-3">
            <div class="card border-0 shadow-sm">
                <div class="card-body text-center">
                    <i class="fas fa-icon fa-2x mb-2" style="color:#0014A8"></i>
                    <h6 class="text-muted">Metric Label</h6>
                    <h3>{{ value }}</h3>
                </div>
            </div>
        </div>
        <!-- Repeat for 4 metrics -->
    </div>
    
    <!-- Charts -->
    <div class="row mb-4">
        <div class="col-lg-8">
            <div class="card">
                <div class="card-header"><h5>Trend Chart</h5></div>
                <div class="card-body">
                    <canvas id="trendChart" style="max-height:300px"></canvas>
                </div>
            </div>
        </div>
        <div class="col-lg-4">
            <div class="card">
                <div class="card-header"><h5>Distribution</h5></div>
                <div class="card-body">
                    <canvas id="pieChart" style="max-height:300px"></canvas>
                </div>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
// Chart.js initialization code
</script>
{% endblock %}
```

## 🚀 Access URLs

- Coupons: http://127.0.0.1:8000/coupons/analytics/
- Customers: http://127.0.0.1:8000/customers/analytics/ (to be created)
- Suppliers: http://127.0.0.1:8000/suppliers/analytics/ (to be created)
- Team: http://127.0.0.1:8000/team/analytics/ (to be created)
- Rentals: http://127.0.0.1:8000/rentals/analytics/ (to be created)
- Storage: http://127.0.0.1:8000/storage/analytics/ (to be created)
- Lockers: http://127.0.0.1:8000/lockers/analytics/ (to be created)
- Warehouse: http://127.0.0.1:8000/warehouses/ (already has analytics)

## 📊 Chart.js Integration

All pages use Chart.js 4.4.0 from CDN for:
- Line charts (trends)
- Doughnut charts (distribution)
- Bar charts (comparisons)

Colors: Zaffre Blue (#0014A8), Green (#28a745), Yellow (#ffc107), Cyan (#17a2b8)
