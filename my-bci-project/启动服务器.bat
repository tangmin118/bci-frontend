@echo off
cd /d "%~dp0"
echo 正在启动本地服务器...
echo 启动后请访问: http://localhost:8080/index.html
echo 关闭此窗口将停止服务器
echo ========================================
start http://localhost:8080/index.html
python -m http.server 8080
pause
