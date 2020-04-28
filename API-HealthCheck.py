
import requests
import pandas as pd

ds = pd.read_csv('urlData.csv')

postData = "{\"name\":\"test\",\"salary\":\"123\",\"age\":\"23\"}"

for index,row in ds.iterrows():
    if(row['method'] == 'GET'):
        print(requests.get(url = row['url'], params = {}).status_code)
    elif(row['method'] == 'POST'):
        print(requests.post(url=row['url'],data = postData).status_code)





