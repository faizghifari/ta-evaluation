import numpy as np

class WordSimilarityClassifier:

    def __init__(self, word_list):
        self.__class__.__name__ = 'WordSimilarity'
        self.word_list = word_list

    def _convert_input(self, x):
        x = np.asarray(x)
        if x.ndim == 0:
            x = x[None]  # Makes x 1D

        return x


    def predict(self, test):
        result = []
        temp = self._convert_input(test)

        for data in temp:
            data_result = []
            for label in self.word_list:
                if label in data:
                    data_result.append(1)
                else:
                    data_result.append(0)

            result.append(data_result)
        
        return result