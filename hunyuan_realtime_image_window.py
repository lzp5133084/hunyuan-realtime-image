import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtCore import QUrl, Qt

class HunyuanImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题
        self.setWindowTitle("虚拟家园实时生图")
        
        # 设置窗口大小
        self.resize(1024, 768)
        
        # 创建WebEngineView实例
        self.web_view = QWebEngineView()
        
        # 设置用户代理以提高兼容性
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62")
        
        # 连接信号和槽以监控加载状态
        self.web_view.loadStarted.connect(self.on_load_started)
        self.web_view.loadFinished.connect(self.on_load_finished)
        self.web_view.loadProgress.connect(self.on_load_progress)
        self.web_view.urlChanged.connect(self.on_url_changed)
        self.web_view.page().javaScriptConsoleMessage = self.on_javascript_console_message
        
        # 将WebEngineView设置为主窗口的中心部件
        self.setCentralWidget(self.web_view)
        
        # 加载指定的URL
        self.web_view.load(QUrl("https://hunyuan.tencent.com/realtimeImage?from=/visual"))
        
        # 显示窗口
        self.show()
        
    def on_load_started(self):
        print("开始加载网页...")
        
    def on_load_finished(self, success):
        if success:
            print("网页加载完成！")
        else:
            print("网页加载失败！")
            QMessageBox.warning(self, "加载失败", "无法加载腾讯混元实时生图页面。\n请检查网络连接或稍后再试。")
    
    def on_load_progress(self, progress):
        # 可以在这里添加加载进度条等UI元素
        pass
        
    def on_url_changed(self, url):
        print(f"URL已更改为: {url.toString()}")
        
    def on_javascript_console_message(self, level, message, line_number, source_id):
        # 记录JavaScript控制台消息但不阻止程序运行
        print(f"JS消息({level}): {message} (行号: {line_number})")

def main():
    # 确保中文显示正常
    import os
    os.environ["QT_FONT_DPI"] = "96"
    
    try:
        # 创建应用程序实例
        app = QApplication(sys.argv)
        
        # 设置应用程序样式
        app.setStyle("Fusion")
        
        # 创建主窗口
        window = HunyuanImageWindow()
        
        # 运行应用程序
        sys.exit(app.exec_())
    except Exception as e:
        print(f"程序启动错误: {str(e)}")
        QMessageBox.critical(None, "启动失败", f"程序启动失败！\n错误信息: {str(e)}\n\n可能需要重新安装PyQt5依赖。\n请运行'安装依赖.bat'文件。")

if __name__ == "__main__":
    main()