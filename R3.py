import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
df=pd.read_csv('User_DATA.txt',header=None,names=['Cacilia','Shattock','email','Genderfluid','phone_number'])
df
pattern=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co)'

df['valid_email']=df['email'].apply(lambda x: x if re.findall(pattern,x) else None)
valid_email=df.explode('valid_email').dropna().reset_index(drop=True)
print(valid_email)