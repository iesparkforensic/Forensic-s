@echo off
rem Windows: double-click to open every site in sites.txt, 10 seconds apart.
rem Optional: run "open_sites.bat 5" from a command prompt for a 5-second interval.
setlocal EnableDelayedExpansion
cd /d "%~dp0"

set INTERVAL=10
if not "%~1"=="" set INTERVAL=%~1

if not exist "sites.txt" (
  echo sites.txt was not found next to this file.
  pause
  exit /b 1
)

echo Opening sites from sites.txt, %INTERVAL% seconds apart. Close this window to stop.
set COUNT=0
for /f "usebackq eol=# delims=" %%U in ("sites.txt") do (
  set "URL=%%U"
  if "!URL:://=!"=="!URL!" set "URL=https://!URL!"
  set /a COUNT+=1
  if !COUNT! gtr 1 timeout /t %INTERVAL% /nobreak >nul
  echo [!COUNT!] !URL!
  start "" "!URL!"
)

echo Done.
pause
