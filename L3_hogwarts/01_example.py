# dir() 是Python内置函数，用于获取指定对象的所有属性和方法的列表
# 格式： dir(obj)
import math
print(dir(math))
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# math模块
# 常用的函数和常量
print(math.pi) # π
print(math.tau) # 2π
print(math.pow(2, 10)) # 2的10次方 1024.0
print(math.sqrt(4)) # 4的平方根 2.0
print(math.ceil(3.14)) # 将数字向上舍入到最接近的整数，比当前参数大的最小整数 4
print(math.floor(3.14)) # 将数字向下舍入到最接近的整数，比当前参数小的最大整数 3
print(math.fabs(-6)) # -6的绝对值 6.0
print(round(3.1415, 3)) # 四舍五入 3.142
print(round(3.1425, 1)) # 四舍五入 3.1

# random模块
import random

fruits = ["苹果", "香蕉", "樱桃"]
random_fruit = random.choice(fruits)
print(random_fruit) # 樱桃

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers) # [5, 3, 1, 4, 2]

# sys模块
import sys

# sys.argv 获取命令行参数列表，包括脚本名称和传递给脚本的其他参数。
# 第一个元素是脚本名称，后续元素是命令行参数
script_name = sys.argv[0]
arguments = sys.argv[1:]

print("脚本名称：", script_name) # 脚本路径
print("命令行参数：", arguments) # [] 空的

# sys.version 获取当前 Python 解释器的版本信息
print("Python 解释器版本：", sys.version)
# 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)]

# sys.version_info 获取当前 Python 解释器的版本信息，以元组形式表示详细的版本号信息
print("Python 解释器版本信息：", sys.version_info)
# sys.version_info(major=3, minor=12, micro=4, releaselevel='final', serial=0)

# sys.platform 获取当前运行的操作系统平台名称
print("当前操作系统平台：", sys.platform) # darwin

# sys.modules 返回已导入的模块信息，返回的是一个字典类型
for module_name, module in sys.modules.items():
    if module_name == "sys":
        print(f"模块名：{module_name}, 模块对象：{module}")
        # 模块名：sys, 模块对象：<module 'sys' (built-in)>
        break

# sys.path 获取模块搜索路径列表，用于指定 Python 解释器搜索模块的路径
print(sys.path)
# ['.../L3_hogwarts', '.../hogwarts_python', '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages', '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']

# sys.getdefaultencoding()：获取编码方式
# 获取系统当前编码
print(sys.getdefaultencoding()) # utf-8

# sys.exit()：运行时退出
print("Python 解释器版本信息：", sys.version_info)
# 运行之后退出，不会运行后面的代码
# sys.exit()
# 后面的代码不会运行
# print(sys.getdefaultencoding())

# os模块
import os

# os.getcwd()：获取当前目录的路径
print("当前目录:", os.getcwd())

# os.chdir()：用于改变当前的工作目录。
# 工作目录是指当前正在执行的脚本所在的目录，通过使用 os.chdir()方法，可以在脚本执行过程中切换到不同的目录。
# 切换到指定目录
# os.chdir("/path/to/directory")
# 切换后的工作目录
# print("切换后的工作目录：", os.getcwd())

# os.path.abspath(path)：获取绝对路径。path 是要获取绝对路径的路径。
absolute_path = os.path.abspath('file1.txt')
print("Absolute Path:", absolute_path)
# .../hogwarts_python/L3_hogwarts/file1.txt

# os.path.basename(path)：返回指定路径的文件名称（不包含父目录路径）
base_name = os.path.basename('file1.txt')
print("Base Name:", base_name) # file1.txt

# os.path.dirname(path)：返回指定路径的父目录路径。
parent_directory = os.path.dirname('file1.txt')
print("父目录为:", parent_directory)

# os.path.split(path)：用于将一个路径拆分为目录部分和文件名部分
path = '/home/user/file.txt'
result = os.path.split(path)
print(result) # ('/home/user', 'file.txt')

# os.path.join(path)：用于连接多个路径部分。它将多个路径片段组合在一起，形成一个新的路径字符串
path1 = '/usr/bin/local'
path2 = 'file.txt'
result = os.path.join(path1, path2)
print(result) # /usr/bin/local/file.txt

# os.path.exists(path) 判断路径是否存在（可以是文件或目录）
path_to_check = 'file1.txt'
if os.path.exists(path_to_check):
    print("路径存在")
else:
    print("路径不存在")

# os.path.isdir(path) 判断是否是目录
# os.path.isfile(path) 判断是否是文件
# os.path.getsize(path) 获取文件大小

# os.listdir()：列出当前目录内容
# os.mkdir()：创建一个新目录
# os.makedirs()：递归创建多级目录
# os.rmdir()：删除目录

# os.rename()：重命名目录
# old_directory_name = '/path/to/old_directory'
# new_directory_name = '/path/to/new_directory'
# os.rename(old_directory_name, new_directory_name)

# os.remove()：删除文件(只能删除文件，不能删除目录)
# file_to_delete = '/path/to/file.txt'
# os.remove(file_to_delete)

# os.name：获取系统名称，在Windows上，os.name 值为 nt。在Linux、macOS，os.name 为 posix
print("Platform Name:", os.name) # Platform Name: posix

# os.chmod(path, mode)：更改文件权限模式。
# path 是要更改权限的文件路径，mode 是权限模式，通常用八进制表示，如 0o755
# # 更改文件权限模式为-rwxr-xr-x
# file_path = '/path/to/file.txt'
# os.chmod(file_path, 0o755)

# os.sep：用于表示操作系统特定的路径分隔符。
# 在Windows操作系统上，路径分隔符是反斜杠 \
# 而在POSIX系统（如Linux、macOS等）上，路径分隔符是正斜杠 /
# 获取路径分隔符
path_separator = os.sep
print("Path Separator:", path_separator) # Path Separator: /

# 正则表达式
import re

# 使用 re.match 进行匹配
pattern = r"\d+"
string = "12345hello world"
match = re.match(pattern, string)
print(match) # <re.Match object; span=(0, 5), match='12345'>
print(match.group()) # 12345
print(match.span()) # (0, 5)
print(match.start()) # 0
print(match.end()) # 5

pattern = r'^\d+'  # 匹配每行开头的数字
string = '123 apple\n456 banana\n789 cherry'

matches = re.findall(pattern, string)
print("单行匹配的结果:", matches) # ['123']

# 使用 re.MULTILINE 标志进行匹配
matches = re.findall(pattern, string, re.MULTILINE)
print("多行匹配的结果:", matches) # ['123', '456', '789']

match_obj = re.match("(\d{3,4})-(\d{4,10})", "010-888999")

if match_obj:
    print(match_obj.group()) # 010-888999
    # 分组:默认是1一个分组，多个分组从左到右依次加1
    print(match_obj.group(1)) # 010
    # 提取第二个分组数据
    print(match_obj.group(2)) # 888999
else:
    print("匹配失败")

# \xxx 引用规则
# 在一个匹配模式中，如果一个规则出现多次，可以将规则进行分组，然后在分组后引用该规则，避免重复书写
match_obj = re.match("<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>", "<html>hh</div>")

if match_obj:
    print(match_obj.group()) # <html>hh</div>
else:
    print("匹配失败")

match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</html>")

if match_obj:
    print(match_obj.group()) # <html>hh</html>
else:
    print("匹配失败")

# (?P<name>) (?P=name) 分组命名与引用
# 在使用分组时，可以给分组进行命名。在匹配规则中，可以通过分组命名引用某个分组中的规则。
match_obj = re.match("<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.baidu.com</h1></html>")

if match_obj:
    print(match_obj.group()) # <html><h1>www.baidu.com</h1></html>
else:
    print("匹配失败")


#导入日志模块
import logging

# 设置日志输出格式
fmt = "%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s - %(message)s"
# 配置日志
logging.basicConfig(filename="myLog.log",filemode="w",format=fmt ,level=logging.NOTSET)
#调用日志器触发日志信息
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
# 2024-08-12 12:08:32,554 - 01_example.py [line:220] - DEBUG - This is a debug message
# 2024-08-12 12:08:32,554 - 01_example.py [line:221] - INFO - This is an info message
# 2024-08-12 12:08:32,554 - 01_example.py [line:222] - WARNING - This is a warning message
# 2024-08-12 12:08:32,554 - 01_example.py [line:223] - ERROR - This is an error message
# 2024-08-12 12:08:32,554 - 01_example.py [line:224] - CRITICAL - This is a critical message
