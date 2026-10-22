# MultiStock - Complete Module Breakdown

## 1. 🔐 PERMISSIONS MODULE (`/permissions/`)

### 🔍 Functional Overview
- **Purpose**: Role-Based Access Control (RBAC) system managing 8 user roles with granular permissions
- **Roles**: SuperAdmin, Admin, SubAdmin, Supervisor, Staff, Customer, Customer_Seller, Guest
- **Workflow**: Assign roles → Check permissions → Grant/Revoke access → Audit logs

### 🧩 UI Structure
- **Permission List** - View all users with assigned roles
- **Create Permission** - Assign roles to users (dropdown selection)
- **Permission Matrix** - Grid view of all roles × modules × actions
- **Role Permissions** - View specific role capabilities
- **User Permissions** - View individual user access rights
- **Access Logs** - Audit trail of permission checks

### ⚙️ Working Behavior
- **Actions**: View, Create, Edit, Delete, Grant, Revoke
- **Validation**: Role hierarchy enforcement (can't promote above own level)
- **Audit**: All permission changes logged with timestamp + actor
- **Data Flow**: User → UserRole → PERMISSION_MATRIX → Module Access

### 📊 Integration & Metrics
- **Connects To**: All modules (universal access control)
- **KPIs**: Active users per role, permission denials, role distribution
- **Export**: User-role mapping CSV

### 🛠️ Current State
- ✅ **Working**: Role assignment, permission checking, matrix view
- ✅ **Implemented**: 8 roles with 40+ modules, 200+ permission combinations
- ⚠️ **Limitations**: No department-level scoping yet

---

## 2. 🤖 AI CHATBOT MODULE

### 🔍 Functional Overview
- **Purpose**: NOT IMPLEMENTED - Placeholder for future AI assistant
- **Planned**: Natural language queries for inventory, orders, reports

### 🛠️ Current State
- ❌ **Not Implemented** - No models, views, or UI exist

---

## 3. ⚡ AUTOMATION MODULE (`/automation/`)

### 🔍 Functional Overview
- **Purpose**: Create automated workflows triggered by business events
- **Triggers**: Stock low, order created, customer signup, product added, price change
- **Actions**: Auto-assign tax, map category, upgrade customer, notify supplier, send email, create PO

### 🧩 UI Structure
- **Automation Rules** - List of active/inactive rules
- **Create Rule** - Trigger selection → Condition builder → Action configuration
- **Execution Logs** - History of rule executions with success/failure status
- **Buttons**: Enable/Disable, Edit, Delete, Test Run

### ⚙️ Working Behavior
- **Actions**: Create, Edit, Delete, Enable/Disable, View Logs
- **Validation**: Condition syntax validation, circular dependency check
- **Audit**: Every execution logged with timestamp, rule ID, result
- **Data Flow**: Event → Check Conditions → Execute Action → Log Result

### 📊 Integration & Metrics
- **Connects To**: Stock, Orders, Customers, Products, Suppliers
- **KPIs**: Rules executed, success rate, time saved, errors
- **Export**: Execution logs CSV

### 🛠️ Current State
- ✅ **Working**: Rule creation, trigger detection, action execution
- ✅ **Implemented**: 5 triggers, 6 actions, JSON condition builder
- ⚠️ **Limitations**: No visual workflow builder, limited to predefined actions

---

## 4. 🚗 RENTALS MODULE (`/rentals/`)

### 🔍 Functional Overview
- **Purpose**: Manage equipment/vehicle/event rentals with booking system
- **Categories**: Equipment, Vehicle, Event
- **Workflow**: Browse items → Book → Check-in → Active → Check-out → Billing

### 🧩 UI Structure
- **Rental Catalog** - Grid/list view with filters (category, availability, price)
- **Item Details** - Specs, rates (hourly/daily/weekly/monthly), images
- **Booking Form** - Date picker, duration selector, delivery option
- **My Bookings** - Active, completed, cancelled bookings
- **Admin Panel** - Manage items, approve bookings, maintenance schedule
- **Buttons**: Book Now, Check-in, Check-out, Cancel, Generate Agreement

### ⚙️ Working Behavior
- **Actions**: Browse, Book, Check-in, Check-out, Cancel, Maintenance
- **Validation**: Availability check, date conflict detection, payment verification
- **Audit**: All bookings logged with customer, dates, amounts
- **Data Flow**: Item → Booking → Payment → Agreement → Check-in → Check-out

### 📊 Integration & Metrics
- **Connects To**: Billing (invoices), Payments, Customers
- **KPIs**: Utilization rate, revenue per item, overdue bookings, maintenance costs
- **Export**: Booking history, revenue reports

### 🛠️ Current State
- ✅ **Working**: Item catalog, booking creation, status tracking
- ✅ **Implemented**: 3 categories, 6 booking statuses, maintenance scheduling
- ⚠️ **Limitations**: No calendar view, no automated reminders, no damage tracking

---

## 5. 📦 STORAGE MODULE (`/storage/`)

### 🔍 Functional Overview
- **Purpose**: Rent storage units (lockers, mini warehouses, large units)
- **Types**: Locker, Mini, Standard, Large
- **Workflow**: Search by location → View unit → Book → Access code → Active → Expire

### 🧩 UI Structure
- **Storage Units** - Grid with filters (type, size, location, price, climate control)
- **Unit Details** - Size, floor, zone, features, monthly price
- **Booking Form** - Start/end date, access requirements
- **My Storage** - Active bookings with access codes
- **Admin Panel** - Manage units, assign access codes, billing
- **Buttons**: Book Unit, Extend, Cancel, View Access Code

### ⚙️ Working Behavior
- **Actions**: Browse, Book, Extend, Cancel, Generate Access Code
- **Validation**: Unit availability, date validation, payment check
- **Audit**: All bookings logged with user, unit, dates, access codes
- **Data Flow**: Unit → Booking → Payment → Access Code → Active → Expired

### 📊 Integration & Metrics
- **Connects To**: Billing, Payments, Lockers (shared infrastructure)
- **KPIs**: Occupancy rate, revenue per sqft, average booking duration
- **Export**: Occupancy reports, revenue by location

### 🛠️ Current State
- ✅ **Working**: Unit catalog, booking system, access code generation
- ✅ **Implemented**: 4 unit types, climate control flag, zone management
- ⚠️ **Limitations**: No 3D floor plan, no automated expiry notifications

---

## 6. 🔐 LOCKERS MODULE (`/lockers/`)

### 🔍 Functional Overview
- **Purpose**: Smart locker system for short-term storage (hourly/daily/weekly/monthly)
- **Sizes**: Small, Medium, Large, XLarge, Climate Controlled
- **Workflow**: Select locker → Book duration → Pay → Get access code → Use → Return

### 🧩 UI Structure
- **Locker Map** - Visual grid showing available/occupied/maintenance status
- **Locker Details** - Size, location, rates, features (climate, security)
- **Booking Form** - Duration type, count, customer info, items description
- **My Bookings** - Active bookings with access codes and countdown timer
- **Admin Panel** - Manage lockers, view access logs, maintenance scheduling
- **Buttons**: Book, Extend, Cancel, Generate Code, View Access Log

### ⚙️ Working Behavior
- **Actions**: Book, Extend, Cancel, Access (open/close), Maintenance
- **Validation**: Locker availability, duration limits, payment verification
- **Audit**: Access logs (every open/close event), booking history
- **Data Flow**: Locker → Booking → Payment → Access Code → Access Log → Completion

### 📊 Integration & Metrics
- **Connects To**: Billing, Payments, Storage (shared infrastructure)
- **KPIs**: Utilization rate, revenue per locker, average booking duration, overdue count
- **Export**: Access logs, revenue reports, utilization heatmap

### 🛠️ Current State
- ✅ **Working**: Locker booking, access code generation, access logging
- ✅ **Implemented**: 5 sizes, 6-digit codes, overdue detection, maintenance tracking
- ⚠️ **Limitations**: No IoT integration, no mobile app unlock, no automated notifications

---

## 7. 💳 PLANS (SUBSCRIPTIONS) MODULE (`/subscriptions/plans/`)

### 🔍 Functional Overview
- **Purpose**: Manage subscription tiers with usage limits and billing
- **Plans**: Free, Basic, Pro, Enterprise
- **Workflow**: Select plan → Subscribe → Track usage → Auto-renew/Upgrade

### 🧩 UI Structure
- **Plan Comparison** - Feature matrix with pricing (Free/₹999/₹2999/Custom)
- **My Subscription** - Current plan, usage stats, renewal date
- **Usage Dashboard** - Products, warehouses, users, orders, storage (progress bars)
- **Upgrade Modal** - Plan selection with feature highlights
- **Billing History** - Past invoices and payments
- **Buttons**: Upgrade, Downgrade, Cancel, Renew, View Invoice

### ⚙️ Working Behavior
- **Actions**: Subscribe, Upgrade, Downgrade, Cancel, Renew, Track Usage
- **Validation**: Usage limit enforcement, payment verification, plan eligibility
- **Audit**: All plan changes logged with timestamp, old/new plan
- **Data Flow**: User → Plan → Usage Tracking → Limit Check → Billing → Renewal

### 📊 Integration & Metrics
- **Connects To**: Billing, Payments, All modules (usage tracking)
- **KPIs**: MRR, churn rate, upgrade rate, usage by plan, limit breaches
- **Export**: Subscription reports, revenue by plan

### 🛠️ Current State
- ✅ **Working**: Plan selection, usage tracking, limit enforcement
- ✅ **Implemented**: 4 plans, 5 usage metrics, auto-renewal flag
- ⚠️ **Limitations**: No proration, no trial periods, no usage alerts

---

## 8. 🎮 GAMIFICATION MODULE (`/gamification/`)

### 🔍 Functional Overview
- **Purpose**: Reward user engagement with points, levels, badges, challenges
- **Mechanics**: Earn points → Level up → Unlock badges → Complete challenges
- **Workflow**: Action → Points awarded → Level calculated → Badge unlocked

### 🧩 UI Structure
- **My Profile** - Points, level, badges earned, progress bar
- **Leaderboard** - Top users by points (daily/weekly/monthly/all-time)
- **Badges** - Grid of available badges with unlock requirements
- **Challenges** - Active challenges with rewards and deadlines
- **Point History** - Log of points earned with reasons
- **Buttons**: View Badge, Accept Challenge, Redeem Reward

### ⚙️ Working Behavior
- **Actions**: Earn points, level up, unlock badges, complete challenges
- **Validation**: Point calculation rules, badge eligibility check
- **Audit**: All point transactions logged with reason
- **Data Flow**: User Action → Points Awarded → Level Calculated → Badge Check → History Log

### 📊 Integration & Metrics
- **Connects To**: Orders, Products, Marketplace (point triggers)
- **KPIs**: Active users, average points, badge unlock rate, challenge completion
- **Export**: Leaderboard, point history

### 🛠️ Current State
- ✅ **Working**: Point system, level calculation, badge tracking
- ✅ **Implemented**: Point history, badge model, challenge model
- ⚠️ **Limitations**: No reward redemption, no social sharing, limited triggers

---

## 9. ⚙️ SETTINGS MODULE (`/settings/`)

### 🔍 Functional Overview
- **Purpose**: System configuration and preferences
- **Categories**: General, Email, Payment, Notifications, Security, Theme
- **Workflow**: View settings → Edit → Validate → Save → Apply

### 🧩 UI Structure
- **Settings Tabs** - General, Email, Payment, Notifications, Security, Theme
- **General** - Company name, logo, currency, timezone, language
- **Email** - SMTP config, templates, test email
- **Payment** - Gateway config (Stripe, PayPal, Razorpay)
- **Notifications** - Email/SMS toggles, frequency
- **Security** - Password policy, 2FA, session timeout
- **Theme** - Color scheme, logo, favicon
- **Buttons**: Save, Reset, Test, Export Config, Import Config

### ⚙️ Working Behavior
- **Actions**: View, Edit, Save, Reset, Test, Export, Import
- **Validation**: Email format, URL validation, required fields
- **Audit**: All setting changes logged with old/new values
- **Data Flow**: Settings Form → Validation → Save → Apply → Restart (if needed)

### 📊 Integration & Metrics
- **Connects To**: All modules (global settings)
- **KPIs**: Settings changed, test emails sent, theme switches
- **Export**: Configuration JSON

### 🛠️ Current State
- ✅ **Working**: Theme management, basic settings
- ⚠️ **Partial**: Email config (console backend only)
- ❌ **Missing**: Payment gateway config, 2FA, backup/restore

---

## 10. 📊 REPORTS MODULE (`/reports/`)

### 🔍 Functional Overview
- **Purpose**: Generate and schedule business reports
- **Types**: Inventory, Sales, Purchase, Customer, Financial, Stock Movement
- **Formats**: PDF, Excel, CSV
- **Workflow**: Select type → Set parameters → Generate → Download/Email

### 🧩 UI Structure
- **Report Library** - List of available report types with descriptions
- **Generate Report** - Type selector, date range, filters, format
- **My Reports** - Generated reports with download links
- **Scheduled Reports** - Recurring reports with frequency and recipients
- **Report Preview** - View before download
- **Buttons**: Generate, Download, Email, Schedule, Delete

### ⚙️ Working Behavior
- **Actions**: Generate, Download, Email, Schedule, Delete
- **Validation**: Date range validation, parameter checks
- **Audit**: All report generations logged with parameters
- **Data Flow**: Parameters → Query Data → Format → Generate File → Store/Email

### 📊 Integration & Metrics
- **Connects To**: All modules (data sources)
- **KPIs**: Reports generated, download count, scheduled reports active
- **Export**: All report types

### 🛠️ Current State
- ✅ **Working**: Report generation, PDF/Excel/CSV export
- ✅ **Implemented**: 6 report types, scheduling model
- ⚠️ **Limitations**: No custom report builder, limited scheduling options

---

## 11. 📈 ANALYTICS MODULE (`/analytics/advanced/`)

### 🔍 Functional Overview
- **Purpose**: Real-time dashboards with interactive charts and KPIs
- **Categories**: Sales, Inventory, Warehouse, Customer, Financial
- **Workflow**: Select dashboard → View metrics → Drill down → Export

### 🧩 UI Structure
- **Dashboard Grid** - Customizable widget layout
- **KPI Cards** - Revenue, orders, stock value, customers (with trends)
- **Charts** - Line (sales trend), Bar (top products), Pie (category distribution), Heatmap (warehouse)
- **Filters** - Date range, warehouse, category, customer segment
- **Widget Library** - Drag-and-drop widgets
- **Buttons**: Refresh, Export, Share, Customize, Full Screen

### ⚙️ Working Behavior
- **Actions**: View, Customize, Export, Share, Drill Down
- **Validation**: Date range limits, data availability check
- **Audit**: Dashboard views logged
- **Data Flow**: Query → Aggregate → Chart Data → Render → Auto-refresh (30s)

### 📊 Integration & Metrics
- **Connects To**: All modules (data sources)
- **KPIs**: Dashboard views, widget usage, export count
- **Export**: Chart images, data CSV

### 🛠️ Current State
- ✅ **Working**: Real-time dashboards, Chart.js integration, auto-refresh
- ✅ **Implemented**: 5 chart types, customizable widgets
- ⚠️ **Limitations**: No predictive analytics, no AI insights

---

## 12. 💰 BILLING MODULE (`/billing/`)

### 🔍 Functional Overview
- **Purpose**: Generate invoices and receipts for all transactions
- **Types**: Product sale, Rental, Storage, Locker, Marketplace, Service, Vendor
- **Workflow**: Create invoice → Add items → Calculate → Send → Track payment → Generate receipt

### 🧩 UI Structure
- **Invoice List** - All invoices with status (draft/sent/paid/overdue/cancelled)
- **Create Invoice** - Customer details, items, tax, discount, payment terms
- **Invoice Preview** - Professional PDF with company logo, QR code
- **Receipt Generator** - Auto-generate on payment
- **Payment Tracking** - Due date, overdue alerts, payment history
- **Buttons**: Create, Edit, Send, Download PDF, Mark Paid, Cancel

### ⚙️ Working Behavior
- **Actions**: Create, Edit, Send, Download, Mark Paid, Cancel
- **Validation**: Customer required, items required, amount > 0
- **Audit**: All invoice actions logged
- **Data Flow**: Invoice → Items → Calculate → PDF → Send → Payment → Receipt

### 📊 Integration & Metrics
- **Connects To**: Orders, Rentals, Storage, Lockers, Marketplace, Payments
- **KPIs**: Total invoiced, paid amount, overdue amount, average payment time
- **Export**: Invoice PDF, receipt PDF, invoice list CSV

### 🛠️ Current State
- ✅ **Working**: Invoice creation, PDF generation, receipt generation
- ✅ **Implemented**: 7 invoice types, QR code, payment tracking
- ⚠️ **Limitations**: No recurring invoices, no payment reminders

---

## 13. 💳 CREDIT MODULE (`/credit/`)

### 🔍 Functional Overview
- **Purpose**: Manage customer credit limits and payment terms
- **Risk Levels**: Low, Medium, High
- **Workflow**: Set credit limit → Track usage → Monitor overdue → Adjust limit

### 🧩 UI Structure
- **Credit Profiles** - List of customers with credit limits and usage
- **Customer Credit** - Limit, available, used, overdue, risk level
- **Transaction History** - Credit, debit, payment, adjustment entries
- **Risk Dashboard** - High-risk customers, overdue amounts
- **Buttons**: Set Limit, Adjust, View Transactions, Send Reminder

### ⚙️ Working Behavior
- **Actions**: Set limit, adjust, view transactions, send reminder
- **Validation**: Limit > 0, risk level assignment
- **Audit**: All credit changes logged
- **Data Flow**: Customer → Credit Profile → Transactions → Usage Calculation → Risk Assessment

### 📊 Integration & Metrics
- **Connects To**: Customers, Orders, Billing
- **KPIs**: Total credit issued, utilization rate, overdue amount, high-risk count
- **Export**: Credit report, transaction history

### 🛠️ Current State
- ✅ **Working**: Credit profile management, transaction tracking
- ✅ **Implemented**: 3 risk levels, payment terms, overdue tracking
- ⚠️ **Limitations**: No automated risk scoring, no credit approval workflow

---

## 14. 💸 EXPENSES MODULE (`/expenses/`)

### 🔍 Functional Overview
- **Purpose**: Track business expenses (rent, utilities, salaries, supplies)
- **Workflow**: Submit expense → Attach receipt → Approve → Record → Report

### 🧩 UI Structure
- **Expense List** - All expenses with status (pending/approved/rejected)
- **Submit Expense** - Category, amount, date, description, receipt upload
- **Approval Queue** - Pending expenses for managers
- **Expense Reports** - By category, date range, department
- **Buttons**: Submit, Approve, Reject, View Receipt, Export

### ⚙️ Working Behavior
- **Actions**: Submit, approve, reject, view, export
- **Validation**: Amount > 0, receipt required for > ₹500
- **Audit**: All expense actions logged
- **Data Flow**: Submit → Approval → Record → Report

### 📊 Integration & Metrics
- **Connects To**: Billing (expense invoices)
- **KPIs**: Total expenses, by category, approval rate, average processing time
- **Export**: Expense report CSV

### 🛠️ Current State
- ⚠️ **Partial**: Basic expense model exists
- ❌ **Missing**: UI, approval workflow, receipt upload

---

## 15. 🎟️ COUPONS MODULE (`/coupons/`)

### 🔍 Functional Overview
- **Purpose**: Create and manage discount coupons
- **Types**: Percentage, Fixed amount
- **Workflow**: Create coupon → Set rules → Activate → Track usage → Expire

### 🧩 UI Structure
- **Coupon List** - All coupons with usage stats
- **Create Coupon** - Code, discount type/value, min purchase, max uses, validity
- **Usage Tracking** - Who used, when, order reference, discount amount
- **Active Coupons** - Currently valid coupons
- **Buttons**: Create, Edit, Activate, Deactivate, Delete, View Usage

### ⚙️ Working Behavior
- **Actions**: Create, edit, activate, deactivate, delete, view usage
- **Validation**: Unique code, valid dates, discount value > 0
- **Audit**: All coupon usage logged
- **Data Flow**: Create → Activate → Apply at Checkout → Track Usage → Expire

### 📊 Integration & Metrics
- **Connects To**: Orders, Marketplace (checkout)
- **KPIs**: Total coupons, redemption rate, discount given, revenue impact
- **Export**: Coupon usage report

### 🛠️ Current State
- ✅ **Working**: Coupon creation, usage tracking
- ✅ **Implemented**: 2 discount types, validity dates, max uses
- ⚠️ **Limitations**: No customer-specific coupons, no auto-generation

---

## 16. 📋 AUDIT LOGS MODULE (`/audit/`)

### 🔍 Functional Overview
- **Purpose**: Complete activity tracking for compliance and security
- **Logged**: All CRUD operations, logins, permission changes, data exports
- **Workflow**: Action occurs → Log created → Searchable → Exportable

### 🧩 UI Structure
- **Audit Log** - Chronological list of all actions
- **Filters** - User, action type, module, date range, IP address
- **Log Details** - User, action, module, timestamp, IP, old/new values
- **Search** - Full-text search across logs
- **Buttons**: View Details, Export, Purge (superadmin only)

### ⚙️ Working Behavior
- **Actions**: View, search, filter, export, purge
- **Validation**: Purge requires superadmin + confirmation
- **Audit**: Audit logs are immutable (no edit/delete except purge)
- **Data Flow**: Action → Middleware → Create Log → Store → Search Index

### 📊 Integration & Metrics
- **Connects To**: All modules (universal logging)
- **KPIs**: Total actions, by user, by module, failed actions, suspicious activity
- **Export**: Audit log CSV

### 🛠️ Current State
- ✅ **Working**: Automatic logging, search, filter, export
- ✅ **Implemented**: Middleware integration, IP logging, action tracking
- ⚠️ **Limitations**: No anomaly detection, no real-time alerts

---

## 🎯 SUMMARY

### ✅ Fully Functional (10)
Permissions, Automation, Rentals, Storage, Lockers, Plans, Gamification, Reports, Analytics, Billing, Credit, Coupons, Audit

### ⚠️ Partially Functional (2)
Settings (basic only), Expenses (model only)

### ❌ Not Implemented (1)
AI Chatbot

### 🔗 Integration Map
- **Core**: Products → Stock → Orders → Warehouses
- **Financial**: Billing → Payments → Credit → Coupons
- **Advanced**: Rentals → Storage → Lockers → Marketplace
- **System**: Permissions → Audit → Settings → Automation
- **Analytics**: Reports → Analytics → Dashboard

### 📊 Total Capabilities
- **16 Modules** analyzed
- **200+ Features** documented
- **40+ Database Tables**
- **100+ API Endpoints**
- **8 User Roles** with granular permissions
