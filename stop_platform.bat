@echo off
echo ========================================
echo   TestForge Platform - Stopping...
echo ========================================
echo.

echo [1/4] Stopping services by window title...
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
echo [2/4] Stopping Backend API (port 8000)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8000" ^| findstr "LISTENING"') do (
    echo   Killing backend PID: %%a
    taskkill /PID %%a /F /T 2>nul
    if %errorlevel% equ 0 (
        echo   [OK] Backend stopped
    )
)

echo.
echo [3/4] Stopping Frontend UI (port 8080)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8080" ^| findstr "LISTENING"') do (
    echo   Killing frontend PID: %%a
    taskkill /PID %%a /F /T 2>nul
    if %errorlevel% equ 0 (
        echo   [OK] Frontend stopped
    )
)

echo.
echo ========================================
echo   All TestForge Services Stopped
echo ========================================
echo.
echo   Services stopped:
echo   - Backend API (port 8000)
echo   - Frontend UI with AI (port 8080)
echo.
echo   Note: If ports still occupied, reboot PC
echo.
pause
