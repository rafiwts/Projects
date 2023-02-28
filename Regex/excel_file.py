import openpyxl

excel_file = 'people.xlsx'


def saving_to_excel(dictionary_of_people, excel_file):
    worker_number = 1
    attribute_index = 0
    opened_file = openpyxl.load_workbook(excel_file)
    get_the_sheet = opened_file['People'] # accesing a sheet called "People"
    
    try: # if there is nothing to iterate over, the program will raise an exception "Key error"
        for row_of_cells in get_the_sheet['A2':'M100']: # adding data to given rows
            for cell in row_of_cells:
                get_the_sheet[cell.coordinate] = dictionary_of_people[worker_number].list_of_attributes()[attribute_index] # iterating through the list of a class method called a 'list_of people'
                attribute_index += 1 
            worker_number += 1 # next key for a class object in a dict 
            attribute_index = 0 # when a iteration for a class object is finished, we start from an index 0
    except KeyError:    
        pass 
    
    opened_file.save(excel_file)
