import xlrd
from src.common import log
from src.config.parameter import test_data_path 




class excel:
    def __init__(self):
        self.mylog = log.log()

    def open_excel(self, file):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception, e:
            self.mylog.error("error")
    
    def excel_table(self, file, sheetName):
        data = self.open_excel(file)
        table = data.sheet_by_name(sheetName)
        Trows = table.nrows
        Tcolnames = table.row_values(0)
        lister = []
        for rownumber in range(1, Trows):
            row = table.row_values(rownumber)
            if row:
                app={}
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




