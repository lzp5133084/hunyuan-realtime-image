import webbrowser
import subprocess
import sys
import time

# 网站URL
url = "https://hunyuan.tencent.com/realtimeImage?from=/visual"

print("正在打开虚拟家园实时生图...")

# 使用默认浏览器打开URL
webbrowser.open(url)

# 提示信息
print("已尝试打开浏览器。如果浏览器没有自动打开，请手动访问以下URL:")
print(url)
print("\n注意：此程序使用系统默认浏览器打开网页。\n如果需要自定义窗口标题功能，请安装PyQt5库并使用原始版本的程序。")

# 保持程序运行一段时间以便用户看到提示
if sys.platform == 'win32':
    # 在Windows上，等待用户按任意键
    input("按任意键退出...")
else:
    # 在其他系统上，等待3秒
    time.sleep(3)