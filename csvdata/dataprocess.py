import pandas as pd

d = {'col1': [1, 2], 'col2': [3, 4]}
temp = pd.DataFrame(data=d)   # dummy dataframe to avoid data type error

def handle_uploaded_file(f):
    global temp
    df = pd.read_csv(f)
    temp = df
    #return temp

def exportCSVdata():

    return temp

def showresult():

    totalrecords = temp.shape[0]
    totalcols = temp.shape[1]
    allcols = list(temp.columns)

    dataset = {'totalrecords':totalrecords, 'totalcols':totalcols, 'allcols':allcols}

    return dataset
