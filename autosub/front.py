# coding=utf-8
from __future__ import print_function
from Tkinter import *
import tkFileDialog
import os
import multiprocessing
from tkinter import ttk
import sys

from autosub.constants import LANGUAGE_CODES
from autosub.back import start


class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''
    def __init__(self,text_area):
        self.text_area = text_area


class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.insert(END,str)


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
    def __init__(self,log_out,lang,form):
        self.filename = None
        self.lang_widget = lang
        self.form_widget = form
        self.log_out = log_out

    def __call__(self):
        args = Args(self.filename, self.lang_widget.get().split(":")[0].strip(), 'en', self.form_widget.get())
        try:
            result = start(args)
            if result == 0:
                print("抽取成功！\n保存至如下路径：")
                print(self.filename.rsplit('.',1)[0] + "." + self.form_widget.get())
        except TypeError:
            pass
        except Exception as e:
            print(u"抽取失败，请检查选项后重新抽取！\n原因如下：")
            print(e)

    def get_file(self):
        self.log_out.delete("1.0", END)
        self.filename = os.path.normcase(tkFileDialog.askopenfilename())
        print("选择文件：",self.filename)


def main():
    window = Tk(className="ExSubtitle")
    window.title("字幕抽取")
    window.geometry("480x480+300+100")
    # window.resizable(0, 0)

    # log
    label_log = LabelFrame(window, text=" 运行日志： ")
    log_area = Text(label_log, width=65, height=5)
    log_out = StdoutRedirector(log_area)
    # log_out = sys.stdout
    sys.stdout = log_out
    sys.stderr = log_out
    label_log.grid(column=0, row=3, padx=10)
    log_area.grid(column=0, row=0)

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

    label_lang.grid(column=0, row=1, padx=10, pady=2)
    language_box.grid(column=1, row=1, padx=10, pady=2)

    label_sub.grid(column=0, row=2, padx=10, pady=2)
    subtitle_format.grid(column=1, row=2, padx=10, pady=2)

    start = Start(log_out=log_area,lang=language_box,form=subtitle_format)

    # 文件
    file_btn = Button(options, text=u'选择文件', width=32, height=1, command=start.get_file)
    file_btn.grid(column=1, row=0, padx=10, pady=2)

    start_btn = Button(window, text=u'抽取', width=8, height=1, command=start)

    start_btn.grid(column=0, row=2, padx=10, pady=10)

    # 事件循环
    window.mainloop()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
