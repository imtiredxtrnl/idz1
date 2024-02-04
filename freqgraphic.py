import matplotlib.pyplot as plt
from nltk import FreqDist
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Загрузка стоп-слов
nltk.download('stopwords')
nltk.download('punkt')

# Пример текста
text = "Ваш текст для анализа точечного графика здесь."

# Предварительная обработка текста: токенизация, удаление стоп-слов и пунктуации
def preprocess_text(text):
    # Приведение к нижнему регистру
    text = text.lower()
    
    # Удаление пунктуации
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Токенизация
    words = word_tokenize(text)
    
    # Удаление стоп-слов
    stop_words = set(stopwords.words('russian'))
    words = [word for word in words if word not in stop_words]
    
    return words

# Обработка текста
words = preprocess_text(text)

# Вычисление частоты встречаемости слов
freq_dist = FreqDist(words)

# Сортировка частот по убыванию
sorted_freq = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)

# Разделение на отдельные списки слов и их частот
words, frequencies = zip(*sorted_freq)

# Построение точечного графика с подписями
plt.figure(figsize=(10, 6))
plt.scatter(range(1, len(words) + 1), frequencies)

# Добавление подписей к точкам
for i, (word, freq) in enumerate(zip(words, frequencies)):
    plt.annotate(word, (i + 1, freq), textcoords="offset points", xytext=(0, 10), ha='center')

plt.title('Точечный график распределения частотности слов (по убыванию)')
plt.xlabel('Ранг слова')
plt.ylabel('Частота встречаемости')
plt.show()