import xlrd 

class ExcelParser(object, excel_name):
    @transaction.commit_on_success        
    def read_excel(self):
        wb = xlrd.open_workbook(excel_name)

        ...
        do your parsing in here.....
        ...