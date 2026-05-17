@echo off
cd /d %~dp0

py -m PyInstaller --onefile ^
--icon=assets/ntsl_icon.ico ^
--name ntsl_1.6.0 ^
ntsl_main.py

pause