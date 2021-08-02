def CRW(data,Data):
    Array = list(data['Date'])
    dat = Data.loc[Data['Date'].isin(Array)]
    return dat
