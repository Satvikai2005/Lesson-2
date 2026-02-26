class Flashcard:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def __str__(self):
        return f"Question: {self.question}\n Answer: {self.answer}"

flash = []
while True:
    q = input("Enter a question: ")
    ans = input("Enter the answer: ")
    o = Flashcard(q, ans)
    flash.append(o)
    ag = int(input("Press 1 to play again and 0 t exit: "))
    if ag == 0:
        break
    elif ag == 1:
        continue
    else:
        print("Enter a valid choice next time.")

for i in flash:
    print(i)
