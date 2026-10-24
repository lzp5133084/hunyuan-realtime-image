@echo off
color 0A
echo 正在安装运行虚拟家园实时生图（简易窗口版）所需的依赖库...
echo 这可能需要几分钟时间，请耐心等待...
python -m pip install --upgrade pip
echo. 
echo 正在安装pywebview...
python -m pip install pywebview
echo. 
echo 依赖库安装完成！
echo. 
echo 现在您可以运行"虚拟家园实时生图_简易窗口.bat"来启动程序。
pause