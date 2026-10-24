@echo off

REM 设置文字颜色为绿色
color 0A

REM 显示启动提示信息
cls
echo ===================================================
echo              虚拟家园实时生图 - HTML窗口版
===================================================
echo. 
echo 正在启动腾讯混元实时生图页面...
echo. 
echo 提示: 
echo 1. 此版本使用您的默认浏览器渲染引擎

echo 2. 完全兼容最新版Python (无需安装额外依赖)
echo 3. 按F5可刷新页面
echo. 
echo ===================================================

echo 正在打开页面，请稍候...

REM 使用start命令打开HTML文件
start "虚拟家园实时生图" hunyuan_standalone_window.html

REM 检查上一个命令的退出码
if %errorlevel% neq 0 (
echo. 
echo 启动失败！请手动打开 hunyuan_standalone_window.html 文件
echo 按任意键退出...
pause >nul
) else (
echo 启动成功！程序已在新窗口中打开
echo 3秒后自动退出此窗口...
timeout /t 3 /nobreak >nul
)

REM 恢复默认颜色并退出
color
exit