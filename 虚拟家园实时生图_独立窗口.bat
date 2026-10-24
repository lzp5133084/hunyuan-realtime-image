@echo off
color 0A
echo 正在启动虚拟家园实时生图（独立窗口版）...
echo 如果这是您第一次运行，请确保已运行"安装依赖.bat"文件。
echo. 
python hunyuan_realtime_image_window.py
if %errorlevel% neq 0 (
    echo. 
    echo 程序启动失败！可能是因为未安装所需的依赖库。
    echo 请先运行"安装依赖.bat"文件来安装必要的库。
    pause
)
pause