@echo off
echo ========================================
echo   TestForge Platform - Stopping...
echo ========================================
echo.

echo [1/3] Stopping services by window title...
taskkill /FI "WINDOWTITLE eq TestForge Backend*" /T /F 2>nul
if %errorlevel% equ 0 (
    echo   [OK] Backend window closed
) else (
    echo   [-] Backend window not found
)

taskkill /FI "WINDOWTITLE eq TestForge Frontend*" /T /F 2>nul
if %errorlevel% equ 0 (
    echo   [OK] Frontend window closed
) else (
    echo   [-] Frontend window not found
)

echo.
echo [2/3] Force stopping backend service on port 8000...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8000" ^| findstr "LISTENING"') do (
    echo   Killing process PID: %%a
    taskkill /PID %%a /F /T 2>nul
    if %errorlevel% equ 0 (
        echo   [OK] Backend service stopped
    )
)

echo.
echo [3/3] Force stopping frontend service on port 8080...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8080" ^| findstr "LISTENING"') do (
    echo   Killing process PID: %%a
    taskkill /PID %%a /F /T 2>nul
    if %errorlevel% equ 0 (
        echo   [OK] Frontend service stopped
    )
)

echo.
echo ========================================
echo   All Services Stopped
echo ========================================
echo.
echo   Note: If ports still occupied, reboot PC
echo.
pause
