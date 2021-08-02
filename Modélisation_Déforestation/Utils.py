def Remove(Value, v):
    a = 0
    for i in v:
        del Value[i-a]
        a = a +1
    return Value
    
def replace_columns(data):
    Data = data.drop(0)
    columns = ['Date', 'Zone Perdue']
    Data.columns = columns
    return Data
    
    
