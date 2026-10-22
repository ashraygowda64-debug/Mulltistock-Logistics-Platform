@echo off
echo ================================================================================
echo                    MULTISTOCK PLATFORM - STARTUP VERIFICATION
echo ================================================================================
echo.

echo [1/4] Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)
echo OK - Python found
echo.

echo [2/4] Verifying database...
python manage.py check --database default
if %errorlevel% neq 0 (
    echo ERROR: Database check failed!
    pause
    exit /b 1
)
echo OK - Database ready
echo.

echo [3/4] Running feature verification...
python test_new_features.py
if %errorlevel% neq 0 (
    echo ERROR: Feature verification failed!
    pause
    exit /b 1
)
echo.

echo [4/4] Starting Django server...
echo.
echo ================================================================================
echo                         SERVER STARTING...
echo ================================================================================
echo.
echo Access the platform at: http://127.0.0.1:8000/
echo.
echo Login Credentials:
echo   Admin:    admin / admin123
echo   Customer: customer1 / customer123
echo.
echo New Features:
echo   - Subscriptions: /subscriptions/plans/
echo   - Storage:       /storage/
echo   - Coupons:       /coupons/
echo   - Credit:        /credit/ (Staff only)
echo   - Audit:         /audit/ (Staff only)
echo.
echo Press Ctrl+C to stop the server
echo ================================================================================
echo.

python manage.py runserver
