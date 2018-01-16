import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
import xlrd
from src.common import mylog
from config.parameter import test_data_path



print(test_data_path)
class excel:
    '''excel处理'''
    def __init__(self):
        self.mylog = mylog.mylog()

    def open_excel(self, file):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            self.mylog.error("error_log2")

    def excel_table(self, file, sheetName):
        data = self.open_excel(file)
        # 通过工作表名称，获取到一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取行数
        Trows = table.nrows
        # 获取 第一行数据
        Tcolnames = table.row_values(0)
        lister = []
        for rownumber in range(1, Trows):
            row = table.row_values(rownumber)
            if row:
                app = {}
                for i in range(len(Tcolnames)):
                    app[Tcolnames[i]] = row[i]
                    lister.append(app)
        return lister

    def get_list(self, sheetname):
        try:
            data_list = self.excel_table(test_data_path, sheetname)
            assert len(data_list)>=0, "excel:" +sheetname 
            return data_list
        except Exception as e:
            self.mylog.error("excel:" +sheetname)
            raise e




