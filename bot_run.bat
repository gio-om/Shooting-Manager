@echo off

call %~dp0ShootingManagerBot\venv\Scripts\activate

cd %~dp0ShootingManagerBot

set TOKEN=5141468385:AAEis82dot0kanavhNHz_7cJC7Lqf6EGr4U
set MANAGER_ID=368234011

python shooting_bot.py

pause