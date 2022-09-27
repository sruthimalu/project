import pandas as pd 

df=pd.read_csv('csic_database.csv')

print(df.columns)
print(df['classification'].value_counts())

df=df[['URL','content','classification']]

df=df.dropna()

# print(df.head())
# print(df.columns)

def apply1(x):
    x=x.replace('http://localhost:8080','')
    x=x.replace('HTTP/1.1','')
    # print(x)
    # n/0
    return x

df['URL']=df['URL'].apply(apply1)

# n/0

req=[]

for i in range(len(df)):
    url=df['URL'].iloc[i]
    content=df['content'].iloc[i]
    text=url+'/'+content
    req.append(text)

df['request']=req

df=df[['request','classification']]

print(df.head())
print(df.columns)

df.to_csv('processed.csv',index=False)


