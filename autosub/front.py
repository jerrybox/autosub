# coding=utf-8
from Tkinter import *
import tkFileDialog
import os
import multiprocessing
from tkinter import ttk

from constants import LANGUAGE_CODES
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
        self.lang = 'en'
        self.form = 'srt'

    def get_arg(self, lang, form):
        self.lang = lang
        self.form = form
        return self

    def __call__(self):
        args = Args(self.filename, self.lang.get().split(":")[0].strip(), 'en', self.form.get())
        start(args)

    def get_file(self):
        self.filename = os.path.normcase(tkFileDialog.askopenfilename())


def main():
    window = Tk(className="ExSubtitle")
    window.title("字幕抽取")
    window.geometry("490x400+300+100")
    window.resizable(0, 0)
    start = Start()

    # 组件
    labels = LabelFrame(window, text=" 温馨提示： ",width=300,height=50)
    label_zero = Label(labels, text=u'请确保能够使用ffmpeg！', font=('Arial', 12), width=50, height=2)
    label_one = Label(labels, text=u'请确保能够访问Google！', font=('Arial', 12), width=50, height=2)
    label_two = Label(labels, text=u'请确保文件及文件夹不包含中文！', font=('Arial', 12), width=50, height=2)


    # 添加组件
    labels.grid(column=0, row=0, padx=10, pady=10)
    label_zero.grid(column=0, row=0)
    label_one.grid(column=0, row=1)
    label_two.grid(column=0, row=2)



    # 配置相关
    options = LabelFrame(window, text=" 配置选项： ",width=300,height=50)

    # 文件
    file_btn = Button(options,text=u'选择文件',width=32, height=1, command=start.get_file)

    # 语言
    label_lang = Label(options, text=u'语言：', font=('Arial', 10),width= 5, height=2)
    lang_name = StringVar()
    language_box = ttk.Combobox(options, width=50, height=10,textvariable=lang_name)
    language_box['values'] = [k+u" : "+v for k,v in sorted(LANGUAGE_CODES.items())]
    language_box.current(14)

    # 字幕格式
    label_sub = Label(options, text=u'格式：', font=('Arial', 10), width= 5, height=2)
    subtitle_name = StringVar()
    subtitle_format = ttk.Combobox(options, width=50, height=4,textvariable=subtitle_name)
    subtitle_format['values'] = ['srt', 'vtt', 'json', 'raw']
    subtitle_format.current(0)

    options.grid(column=0, row=1, padx=10, pady=10)
    file_btn.grid(column=1, row=0, padx=10, pady=2)

    label_lang.grid(column=0, row=1, padx=10, pady=2)
    language_box.grid(column=1, row=1, padx=10, pady=2)

    label_sub.grid(column=0, row=2, padx=10, pady=2)
    subtitle_format.grid(column=1, row=2, padx=10, pady=2)

    start_btn = Button(window, text=u'抽取', width=8, height=1, command=start.get_arg(language_box,subtitle_format))

    start_btn.grid(column=0, row=2, padx=10, pady=10)

    # 事件循环
    window.mainloop()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
