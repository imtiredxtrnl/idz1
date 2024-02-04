import stat
import matplotlib.pyplot as plt
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import string


class GenerateGitsoGraphics:
    
    @staticmethod
    def preprocess_text(text):
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = word_tokenize(text)
        stop_words = set(stopwords.words('russian'))
        words = [word for word in words if word not in stop_words]
        return words

    @staticmethod 
    def generate_image(text):
        words = GenerateGitsoGraphics.preprocess_text(text)
        freq_dist = FreqDist(words)
        plt.figure(figsize=(10, 6))
        freq_dist.plot(20, cumulative=False) 
        plt.title('Гистограмма частоты встречаемости слов')
        plt.xlabel('Слова')
        plt.ylabel('Частота встречаемости')
        plt.show()
