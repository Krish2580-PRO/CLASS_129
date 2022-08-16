import pandas as pd 

d1 = pd.read_csv("ok.csv")

d1 = d1.dropna()

d1["Radius"] = 0.102763*  d1["Radius"]

d1['Mass']=d1['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

d1['Mass'] = 0.000954588* d1['Mass']

d1.to_csv("converted.csv")


