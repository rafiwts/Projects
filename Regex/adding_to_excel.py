
import openpyxl

def saving_to_excel():
    excel_file_path = 'C:/Users/rafiw/Workspace/people.xlsx'
    excel_file = openpyxl.load_workbook(excel_file_path)
    ss_sheet = excel_file['People']
    for row_of_cells in ss_sheet['A2':'N2']:
        for cell in row_of_cells:
            ss_sheet[cell.coordinate] = 'Rows'
    excel_file.save(excel_file_path)
