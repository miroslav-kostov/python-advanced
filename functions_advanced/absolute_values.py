def get_data():
    result = input()
    return result

def transform_to_list(data):
    result = data.split()
    return result

def transform_str_to_float(data):
    result = [float(x) for x in data]
    return result

def make_value_abs(data):
    result = [abs(x) for x in data]
    return result

data = get_data()
data = transform_to_list(data)
data = transform_str_to_float(data)
data = make_value_abs(data)
print(data)