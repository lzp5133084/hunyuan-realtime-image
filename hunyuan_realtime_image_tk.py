import tkinter as tk
import webview
import sys

def open_hunyuan_window():
    # 创建webview窗口
    window = webview.create_window(
        title="虚拟家园实时生图",
        url="https://hunyuan.tencent.com/realtimeImage?from=/visual",
        width=1024,
        height=768,
        resizable=True
    )
    
    # 启动webview
    webview.start()

if __name__ == "__main__":
    print("正在启动虚拟家园实时生图...")
    try:
        # 尝试直接启动webview
        open_hunyuan_window()
    except Exception as e:
        print(f"启动失败: {e}")
        print("\n请确保已安装webview库。您可以使用以下命令安装:")
        print("pip install pywebview")
        if sys.platform == 'win32':
            input("按任意键退出...")
        else:
            import time
            time.sleep(5)