def convert_dtype(data):
    data[['Date']] = data[['Date']].astype(str).astype(int)
    data[['Zone Perdue']] = data[['Zone Perdue']].astype(str).astype(float)
    return data
    
    
