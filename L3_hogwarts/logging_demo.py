#导入日志模块
import logging
import random
from datetime import datetime

# 设置日志输出格式
fmt = "%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s - %(message)s"
# 根据日志记录时间，动态生成日志文件名
# 如果指定日志存放目录，则前提是必须保证目录已存在，例如：这里的 log 目录
filename = f"./log/log_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
# 注意：由于时分秒一直都在变化，所以每执行一次程序，文件名都不一样，就都会生成一个新文件
# 如果期望一天只生成一个日志文件，则文件名可以只设置年月日，例如：
# filename = f"./log/log_{datetime.now().strftime('%Y%m%d')}.log"

# 配置日志
logging.basicConfig(filename=filename, filemode="a", format=fmt, level=logging.DEBUG)

# # 调用日志器触发日志信息
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

def show():
    logging.info("Show 函数被调用，开始执行")
    print("Show Run ...")
    logging.info("Show 函数执行结束")

def display():
    logging.warning("Display 函数被调用，开始执行")
    print("Display Run ...")
    logging.warning("Display 函数执行结束")

def get_data():
    logging.info("Get_data 函数被调用，开始执行")
    nums = [x for x in range(random.randint(5, 10))]
    # nums = list((x for x in range(random.randint(5, 10))))

    index = random.randint(0, 9)

    # 由于随机数生成结果的不确定，可能会出现下标越界的异常
    try:
        result = nums[index]
    except Exception as err:
        logging.error(err)
        return None
    else:
        return result
    finally:
        logging.info("Get_Data 函数执行结束")

if __name__ == "__main__":
    logging.debug("=========程序开始运行==========")
    funcs = [show, display, get_data]

    for i in range(10):
        func = random.choice(funcs)
        func()
