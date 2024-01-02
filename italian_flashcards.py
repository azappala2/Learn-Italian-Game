from tkinter import *
from random import randint

root = Tk()
root.title('Italian Language Flashcards')
root.geometry("700x300")



#verb flashcard function
def verbs():
    pass

#phrase flashcard function
def phrases():
    pass    


#create menu
main_menu = Menu(root)
root.config(menu=main_menu)

#create menu items
verbs_menu = Menu(main_menu)
main_menu.add_cascade(label="Options", menu=verbs_menu)
verbs_menu.add_command(label="Verbs", command = verbs)
verbs_menu.add_command(label="Phrases", command = phrases)



#keep track of score
score = 0

def italianClick():
    italian = True
    myLabel = Label(root, text="You will see the Italian word")
    myLabel.pack()

def englishClick():
    myLabel = Label(root, text="You will see the English word")
    myLabel.pack()

def nextWord():
    global random_word 
    global hinter
    global hint_count  
    
    #clear screen
    my_entry.delete(0, END)
    answer_label.config(text="")
    hint_label.config(text="")
    hinter = ""
    hint_count = 0

    #pick new random word
    random_word = randint(0, len(words)-1)
    italian_word.config(text=words[random_word][0])
    

def checkAnswer():
    if my_entry.get().lower() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
        global score
        global hint_count
        if hint_count == 0:
            score += 1
            Score.config(text = f" Score: {score}")
    else:
        answer_label.config(text="Incorrect!")

#Keep track of hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter
    if hint_count < len(words[random_word][1]):
        hinter += words[random_word][1][hint_count]
        if hint_count == 0:
            hint_label.config(text=f"The first letter is {words[random_word][1][0]}")
        else:
            hint_label.config(text=f"The first {hint_count+1} letters are {hinter}")
        hint_count += 1
    
words = [
    (("avere"), ("to have")),
    (("essere"), ("to be")),
    (("andare"), ("to go")),
    (("fare"), ("to do")),
    (("dire"), ("to say")),
    (("partire"), ("to leave")),
    (("stare"), ("to stay")),
    (("dare"), ("to give")),
    (("vedere"), ("to see")),
    (("sapere"), ("to know")),
    (("volere"), ("to want")),
    (("scrivere"), ("to write")),
    (("capire"), ("to understand"))
]



italian_word = Label(root, text="", fg = "white", font=("Helvetica", 48))
italian_word.pack(pady=10)
#if italian == False:
   # english_word = Label(root, text=words[randint(0, len(words)-1)][1])
  #  english_word.pack()

answer_label = Label(root, text="")
answer_label.pack()

my_entry = Entry(root)
my_entry.pack(pady=10)

hint_label = Label(root, text="")
hint_label.pack()

button_frame = Frame(root)
button_frame.pack(pady=10)

#italianButton = Button(root, text="See Italian Word", command=italianClick)
#italianButton.pack()

#englishButton = Button(root, text="See English Word", command=englishClick)
#englishButton.pack()

answer_button = Button(button_frame, text="Check Answer", command=checkAnswer)
answer_button.grid(row=6, column=0, pady=10, padx=10)

hint_button = Button(button_frame, text="Hint", command = hint)
hint_button.grid(row=6, column=1, pady=10, padx=10 )

next_button = Button(button_frame, text="Next Word", command=nextWord)
next_button.grid(row=6, column=2, pady=10, padx=10)

Score = Label(button_frame, text=f"Score: {score}")
Score.grid(row=7, column=1, pady=10, padx=10)
nextWord()

root.mainloop()