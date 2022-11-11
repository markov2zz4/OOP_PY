class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.rating = rating
        self.surname = surname
        self.name = name

    def __eq__(self, other):
        if(isinstance(other, (int, float))):
            return self.rating == other
        elif(isinstance(other, ChessPlayer)):
            return self.rating == other
        else:
            return "Невозможно выполнить сравнение"
        

    def __gt__(self, other):
        if(isinstance(other, (int, float))):
            return self.rating > other
        elif(isinstance(other, ChessPlayer)):
            return self.rating > other
        else:
            return "Невозможно выполнить сравнение"

    def __lt__(self, other):
        if(isinstance(other, (int, float))):
            return self.rating < other
        elif(isinstance(other, ChessPlayer)):
            return self.rating < other
        else:
            return "Невозможно выполнить сравнение"
        

magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus > ian) # True
print(magnus < ian) # False
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"