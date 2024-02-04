class ResultModel:
    def __init__(self, text ,words, specWords, symbols, symbolsNoSpaces, letters, foreignWords,waterPercentage, marks, stopWords, wordsDistribution, wordsDistributionNoStopWords):
        self.text = text
        self.words = words
        self.specWords = specWords
        self.symbols = symbols
        self.symbolsNoSpaces = symbolsNoSpaces
        self.letters = letters
        self.foreignWords = foreignWords
        self.waterPercenatge = waterPercentage
        self.marks = marks
        self.stopWords = stopWords
        self.wordsDistribution = wordsDistribution
        self.wordsDistributionNoStopWords = wordsDistributionNoStopWords
        
    def print_fields(self):
        print("Words:", self.words)
        print("Specified words amount:", self.specWords)
        print("Symbols:", self.symbols)
        print("Symbols (No Spaces):", self.symbolsNoSpaces)
        print("Letters:", self.letters)
        print("Foreign Words:", self.foreignWords)
        print("Water percentage:", self.waterPercenatge)
        print("Marks:", self.marks)
        print("Stop Words:", self.stopWords)
        print("Words distribution through text with water:")
        for word, count, percentage in self.wordsDistribution:
            print(f"Word: {word}, Count: {count}, Percentage: {percentage:.2f}%")
        print("Words distribution through text without water:")
        for word, count, percentage in self.wordsDistributionNoStopWords:
            print(f"Word: {word}, Count: {count}, Percentage: {percentage:.2f}%")