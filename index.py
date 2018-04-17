from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs

def need_join(itemSet1, itemSet2):
    for i in range(len(itemSet1)-2):
        if itemSet1[i] != itemSet2[i]:
            return(False)
    return(True)

print(need_join("dfdf", "dfdf"))
