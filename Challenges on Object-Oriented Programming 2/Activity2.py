class flashcard:
    def __init__(self, word , meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
      
      return self.word+ '('+self.meaning+')'
    
flash = []
print("Welcome To The Flashcard Application")

while(True):
   word = input("Enter The Name You Want To Enter The Flashcard: ")

   meaning = input("Enter The Meaning Of The Word: ")

   flash.append(flashcard(word, meaning))
   option = int(input("Enter 0 If You Want To Add Another Card Otherwise Enter 1: "))

   if(option):
      break
   
print("\nYour Flash Cards: ")
for i in flash:
   print(">", i)