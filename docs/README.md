### 使用用注意事项：
1. 确保命令行下能够使用ffmpeg：
	window 7 下，将ffmpeg所在文件夹路径添加到环境变量中(ExSubtitle\ffmpeg\bin 下的ffmpeg.exe)
2. 视频文件及文件夹不包含在中文：
3. 确保系统能够访问Google：
	Shadowsock 启动系统代理，使用配置代理端口： 127.0.0.1:1080
4. 确保360等软件不会限制此软件的权限：

#### 问题 一：Windows 系统 文件路径判断及可执行与否判断问题？：
	os.path.isfile(r"C:\ProgramData\ffmpeg-4.0.1-win64-static\bin\ffmpeg.exe")
	True
	os.path.isfile("C:\ProgramData\ffmpeg-4.0.1-win64-static\bin\ffmpeg.exe")
	False

	https://www.douban.com/note/610935909/
		Windows路径的“正统”写法应该是：

		path = os.path.normcase("c:/mydir/mysubdir/")

		os.path.normcase在Windows平台下会自动把正斜杠转换成反斜杠。

	# 修改后判断是否存在文件及可执行与否
	def which(program):
	    def is_exe(file_path):
	        return os.path.isfile(file_path) and os.access(file_path, os.X_OK)

	    fpath, fname = os.path.split(program)
	    if fpath:
	        if is_exe(program):
	            return program
	    else:
	        for path in os.environ["PATH"].split(os.pathsep):
	            path = path.strip('"')
	            exe_file = os.path.join(path, program)
	            if is_exe(exe_file):
	                return exe_file
	            # compatable with backflash of  windows directory
	            exe_file = os.path.join(os.path.normcase(path), (program + '.exe'))
	            if is_exe(exe_file):
	                return exe_file
	    return None

#### 问题 二：Error Permission denied Files Flac
		https://github.com/agermanidis/autosub/issues/31
		https://github.com/agermanidis/autosub/issues/15
		temp = tempfile.NamedTemporaryFile(suffix='.flac')  ---->  temp = tempfile.NamedTemporaryFile(suffix='.flac', delete=False)

#### 问题 三：多进程导致tkinter 会弹出多个窗口问题
    https://blog.csdn.net/qq_34896470/article/details/78782736
    实用multiprocessing之前，添加这行代码：multiprocessing.freeze_support()

#### 问题 四：打包应用：
    pywin32
    pyinstaller
    # 这个命令
    /dist 同一文件夹下文件
    pyinstaller -w -i C:\Users\niuxingjie\Downloads\prog_python_128px_1097222_easyicon.net.ico front.py
    /dist 单个exe文件，失败
    pyinstaller -F -w -i C:\Users\niuxingjie\Downloads\prog_python_128px_1097222_easyicon.net.ico front.py