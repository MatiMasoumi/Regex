import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
phone_number=pd.read_csv('User_DATA.txt',header=None,names=['Cacilia','Shattock','email','Genderfluid','number'])
phone_number['number'].str.strip()
def extract_phone_number(text):
    pattern=r'(\+\d{1,3}\s?\(?\d{1,3}\)?[\s-]?\d{3}[\s-]?\d{4}|\d{3}[-]\d{3}[-]\d{4})'
    return re.findall(pattern,text)
phone_number['phone_num']=phone_number['number'].apply(extract_phone_number)
phone_number['phone_num']
