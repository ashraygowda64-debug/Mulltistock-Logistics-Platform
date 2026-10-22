@echo off
REM MultiStock - Main Startup Script (New Consolidated Structure)
echo ========================================
echo      MultiStock - Starting System
echo      (Consolidated Structure v2.0)
echo ========================================
echo.

echo [1/4] Installing dependencies...
pip install -r config\requirements.txt

echo.
echo [2/4] Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo [3/4] Creating superuser (if needed)...
echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@multistock.com', 'admin123') | python manage.py shell

echo.
echo [4/4] Starting development server...
echo.
echo ========================================
echo   MultiStock Platform: http://127.0.0.1:8000
echo   Admin Panel: http://127.0.0.1:8000/admin
echo   Username: admin ^| Password: admin123
echo.
echo   New Structure:
echo   - Apps: apps/
echo   - Scripts: scripts/
echo   - Tests: tests/
echo   - Docs: docs/
echo   - Config: config/
echo ========================================
echo.
python manage.py runserver
