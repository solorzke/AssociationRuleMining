from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs

#check if two (k-1)-itemsets need to be joined into a k-itemset
def need_join(itemSet1, itemSet2):
    for i in range(len(itemSet1)-2):
        #check if all items except the last ones are identical
        if itemSet1[i] != itemSet2[i]:
            return(False)
    return(True)

def join(itemSet1, itemSet2):
    itemSet3 = itemSet1
    itemSet3 = itemSet3 + itemSet2
    return(itemSet3)

print(need_join("dfdf", "dfdf"))
