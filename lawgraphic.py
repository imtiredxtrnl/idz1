import stat
import matplotlib.pyplot as plt
import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Загрузка стоп-слов
nltk.download('stopwords')
nltk.download('punkt')

# Пример текста
text = "Ваш текст для анализа закона Ципфа здесь."

class LawGraphicGenerator:
    
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
        words = LawGraphicGenerator.preprocess_text(text)
        freq_dist = FreqDist(words)
        ranks = list(range(1, len(freq_dist) + 1))
        frequencies = list(freq_dist.values())
        plt.figure(figsize=(10, 6))
        plt.loglog(ranks, frequencies, marker='.')
        plt.title('Закон Ципфа')
        plt.xlabel('Ранг слова')
        plt.ylabel('Частота встречаемости')
        plt.show()
