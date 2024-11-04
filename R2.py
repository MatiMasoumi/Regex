import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
url=pd.read_csv('URL.txt',header=None,names=['Kerr','Jolliman','email','address'])
url
def URL_address(text):
    pattern=r'https?://[^\s]+'
    return re.findall(pattern,text)
url['URL']=url['address'].apply(URL_address)
url['URL']