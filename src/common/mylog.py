import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
print(sys.path)
import logging
from config import parameter




class mylog:
    def __init__(self):
        self.logname = "mylog"

    def setMSG(self, level, msg):
        logger = logging.getLogger()
        # 定义Handler输出到文件和控制台
        fh = logging.FileHandler(parameter.log_path)
        ch = logging.StreamHandler()
        # 定义日志输出格式
        formater = logging.Formatter("%(asctime)s %(levelname)s %(message)s' ")
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        # 添加Handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 添加日志信息，输出INFO级别的信息
        logger.setLevel(logging.INFO)
        if level=='debug':
            logger.debug(msg)
        elif level=='info':
            logger.info(msg)
        elif level=='warning':
            logger.warning(msg)
        elif level=='error':
            logger.error(msg)
        # 移除句柄
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)
    

