@echo off
set "PYTHON_EXE=C:\Users\ELUCY\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
set "SITE_DIR=%~dp0"

echo Starting ELUCY design preview...
echo.
echo Open this address in your browser:
echo http://127.0.0.1:5175
echo http://127.0.0.1:5175/konfigurator.html
echo.

cd /d "%SITE_DIR%"
"%PYTHON_EXE%" "%SITE_DIR%preview-server.py"

pause
