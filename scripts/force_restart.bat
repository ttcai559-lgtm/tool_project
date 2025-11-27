@echo off
echo ========================================
echo Force Restarting Backend Service
echo ========================================
echo.

echo Step 1: Killing process on port 8000...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000 ^| findstr LISTENING') do (
    echo Killing PID %%a
    taskkill /F /PID %%a
)

echo.
echo Step 2: Waiting 3 seconds...
timeout /t 3 /nobreak

echo.
echo Step 3: Starting new backend service...
cd testforge
start "TestForge Backend" python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload

echo.
echo Step 4: Waiting 5 seconds for service to start...
timeout /t 5 /nobreak

echo.
echo Step 5: Testing API endpoint...
curl -s http://localhost:8000/
echo.
echo.
echo ========================================
echo Backend service restarted!
echo ========================================
