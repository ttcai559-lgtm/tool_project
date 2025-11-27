@echo off
echo Stopping backend service...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
)
timeout /t 2 /nobreak >nul

echo Starting backend service...
cd testforge
start "TestForge Backend" cmd /k "python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload"

timeout /t 3 /nobreak >nul
echo.
echo Backend service restarted!
echo Testing API...
curl -s http://localhost:8000/
echo.
echo.
echo Backend is ready at http://localhost:8000
pause
