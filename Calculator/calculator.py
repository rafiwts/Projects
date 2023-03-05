
class Calculator:
    def __init__(self, number = 0):
        self.number = number
        self.list_of_values = []
        self.dict_of_values = {}
        self.count_calls = 0
        self.sum = 0

    def __add__(self, other_number):
        value = self.number + other_number
        self.sum += value
        self.count_calls += 1
        self.list_of_values.append(value)
        self.dict_of_values[self.count_calls] = value
        return f'The result of this operation is {value}'
    
    def __sub__(self, other_number):
        value = self.number - other_number
        self.sum += value
        self.count_calls += 1
        self.list_of_values.append(value)
        self.dict_of_values[self.count_calls] = value
        return f'The result of this operation is {value}'
    
    def __mul__(self, other_number):
        value = self.number * other_number
        self.sum += value
        self.count_calls += 1
        self.list_of_values.append(value)
        self.dict_of_values[self.count_calls] = value
        return f'The result of this operation is {value}'
    
    def __truediv__(self, other_number):
        value = self.number / other_number
        self.sum += value
        self.count_calls += 1
        self.list_of_values.append(value)
        self.dict_of_values[self.count_calls] = value
        return f'The result of this operation is {value}'

    def average(self):
        return sum(self.list_of_values) / len(self.list_of_values)

