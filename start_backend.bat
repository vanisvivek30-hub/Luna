@echo off
REM Start Backend Server on Port 5000
REM Make sure you have Python 3 installed

cd /d "%~dp0"
cd backend

echo.
echo Starting IndustrySolve Backend Server...
echo.
echo 🔧 Backend will be available at: http://localhost:5000
echo 📚 API Documentation: http://localhost:5000/api/health
echo 💾 Database: industrysolve.db
echo.

python app.py

pause
