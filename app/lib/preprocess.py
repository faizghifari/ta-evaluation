import re

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.base import BaseEstimator, ClassifierMixin

class IndoTextCleaner(BaseEstimator):
    
    def __init__(self):
        self.__class__.__name__ = 'IndoTextCleaner'
    
    def fit(self, x, y=None):
        return self
    
    def transform(self, x):
        x = x.lower()
        x = re.sub(r"\'", ' ', x)
        x = re.sub(r'[^\w\s]','', x)
        x = re.sub('\s+', ' ', x)
        x = x.strip(' ')
        return x

class StopWordsEliminator(BaseEstimator):
    
    def __init__(self):
        self.__class__.__name__ = 'StopWordsEliminator'

    def fit(self, x, y=None):
        return self
                          
    def transform(self, x):
        factory = StopWordRemoverFactory()
        stopword = factory.create_stop_word_remover()
        
        x = stopword.remove(x)
        return x