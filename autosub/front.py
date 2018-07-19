# coding=utf-8
from Tkinter import *
import tkFileDialog
import os
import multiprocessing

from back import start


class Args(object):
    def __init__(self,filename,src_language,dst_language,format):
        self.source_path = filename
        self.src_language = src_language
        self.dst_language = dst_language
        self.format = format
        self.concurrency = None
        self.output = None
        self.api_key = None


class Start(object):
    def __init__(self):
        self.filename = None

    def __call__(self):
        args = Args(self.filename,'en','en','srt')
        start(args)

    def get_file(self):
        self.filename = os.path.normcase(tkFileDialog.askopenfilename())


def main():
    window = Tk(className=" ExSubtitle")

    start = Start()

    # 组件
    label_zero = Label(window, text=u'请确保能够使用ffmpeg！', bg='green', font=('Arial', 12), width=15, height=2)
    label_one = Label(window, text=u'请确保能够刚问Google！', bg='green', font=('Arial', 12), width=15,height=2)
    label_two = Label(window, text=u'请确保文件及文件夹不包含中文！', bg='green', font=('Arial', 12), width=15, height=2)
    file_btn = Button(window,text=u'选择文件',width=45, height=2,command=start.get_file)
    start_btn = Button(window, text=u'点击抽取字幕', width=15, height=2, command=start)

    # 添加组件
    label_zero.pack(fill=X)
    label_one.pack(fill=X)
    label_two.pack(fill=X)
    file_btn.pack(fill=X, pady=10)
    start_btn.pack(fill=X, pady=10)

    # 事件循环
    window.mainloop()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
