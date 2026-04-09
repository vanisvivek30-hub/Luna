@echo off
REM Start Frontend Server on Port 8000
REM Make sure you have Python 3 installed

cd /d "%~dp0"
cd frontend

echo.
echo Starting IndustrySolve Frontend Server...
echo.
echo 🌐 Frontend will be available at: http://localhost:8000
echo 🚀 Make sure backend is running on port 5000
echo.

python -m http.server 8000

pause
