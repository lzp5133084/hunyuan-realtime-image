import sys
import os

print("Python版本:", sys.version)
print("Python安装路径:", sys.executable)
print("当前工作目录:", os.getcwd())

# 尝试导入PyQt5模块并显示相关信息
try:
    import PyQt5
    print("PyQt5已安装，版本:", PyQt5.__version__)
    print("PyQt5安装路径:", PyQt5.__file__)
    
    try:
        from PyQt5 import QtCore
        print("QtCore模块加载成功")
        print("Qt版本:", QtCore.QT_VERSION_STR)
    except ImportError as e:
        print("QtCore模块加载失败:", str(e))
        
    try:
        from PyQt5.QtWidgets import QApplication
        print("QtWidgets模块加载成功")
    except ImportError as e:
        print("QtWidgets模块加载失败:", str(e))
        
    try:
        from PyQt5.QtWebEngineWidgets import QWebEngineView
        print("QtWebEngineWidgets模块加载成功")
    except ImportError as e:
        print("QtWebEngineWidgets模块加载失败:", str(e))
        
except ImportError as e:
    print("PyQt5未安装或无法导入:", str(e))

print("\n环境变量PATH的相关部分:")
path = os.environ.get('PATH', '')
qt_paths = [p for p in path.split(';') if 'PyQt5' in p or 'Qt' in p]
if qt_paths:
    for p in qt_paths:
        print(p)
else:
    print("未找到与PyQt5或Qt相关的PATH环境变量")

print("\n诊断完成。如果有DLL加载错误，可能需要重新安装PyQt5或修复环境配置。")