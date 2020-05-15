
"""
Handle Hyphenated Words that are tokenized as a single word
"""


#LIBRARY Imports
import tkinter as tk
from googletrans import *

from dialectTranslator import translator

from dialectTranslator import suggestWord

from dialectTranslator import posHandler


win = tk.Tk()
win.title("Translator")

win.geometry("600x400")

frame_suggestion = tk.Frame(win, width= "590", height = "210")
frame_suggestion.place(relx = 0.012, rely = 0.46)

#Suggestion button list
suggestion_buttons = []
suggestion_labels = []

#Translator Function call from Word Mapping Script
def translate():
    output.delete("0.0",tk.END)
    inputSentence = str(entry.get("0.0", tk.END)).strip()

    #If Empty Input
    if len(inputSentence) <= 0:
        tk.messagebox.showinfo("Alert!", "Empty Input!!")
        return

    #Detect Language
    gTranslator = Translator()
    detectedLang = gTranslator.detect(inputSentence)
    if str(detectedLang.lang).strip() != "bn":
        tk.messagebox.showinfo("Alert!", "Type in Bangla Characters!!")
        return

    #Translate from Chittagonian to Standard Bangla
    translation = str(translator.generateOutputSentence(inputSentence)).strip()
    show_output(translation)
    print(translation)          ##For Debugging on Console Window

#Show output
def show_output(word):
    output.insert(tk.END, word)


## Suggestion Function
def suggest():
    inputSentence = str(entry.get("0.0", tk.END)).strip()

    #Empty Input
    if len(inputSentence) <= 0:
        tk.messagebox.showinfo("Alert!", "Empty Input!!")
        return

    # Detect Language
    gTranslator = Translator()
    detectedLang = gTranslator.detect(inputSentence)
    if str(detectedLang.lang).strip() != "bn":
        tk.messagebox.showinfo("Alert!", "Type in Bangla Characters!!")
        return

    tokens = translator.tokenize_input(inputSentence)

    #Suggestion for each token 2D array
    suggestions = []
    for i in tokens:
        suggestions.append(suggestWord.suggest_word(i))

    display_suggestion(tokens, suggestions)
    print(suggestions)


#display suggestion on GUI
def display_suggestion(tokens, suggestions):

    relyVal = 0.05
    for i in range(len(tokens)):
        temp = create_suggestion_row(tokens[i].strip(), suggestions[i], relyVal, i)
        suggestion_buttons.append(temp)
        relyVal += 0.15




##Create Suggestion Row
def create_suggestion_row(word, suggestionsIn, relyVal, tokenIndex):
    labelRow = tk.Label(frame_suggestion, text = word + " --->> ")
    labelRow.config(font=('Helvetica', 10))
    labelRow.place(relx = 0.012, rely = relyVal)
    suggestion_labels.append(labelRow)

    btnRelxInc = 0
    temp = []
    for i in range(len(suggestionsIn)):
        temp.append(tk.Button(frame_suggestion, text=suggestionsIn[i], command=None, bg="#b6cecf", width=18))
        temp[i].config(font=('Helvetica', 9))
        temp[i].place(relx=0.3+btnRelxInc, rely=relyVal)
        btnRelxInc += 0.235

    ###ISSUE HANDLED: Only the last button in a row used to work
    temp[0]['command'] = lambda : replace_word(temp[0]['text'], tokenIndex)
    temp[1]['command'] = lambda : replace_word(temp[1]['text'], tokenIndex)
    temp[2]['command'] = lambda : replace_word(temp[2]['text'], tokenIndex)

    return temp




#Replace Input with Suggested Word
def replace_word(newInput, tokenIndex):

    word = str(entry.get("0.0", tk.END)).strip()
    tokens = translator.tokenize_input(word)

    tokens[tokenIndex] = newInput.strip()

    #Generate New input text
    newInput = ""
    for i in range(len(tokens)):
        if i >= len(tokens):
            newInput += tokens[i]
        else:
            newInput += tokens[i] + " "

    ##Setting Text in Input box
    entry.delete("0.0", tk.END)
    entry.insert(tk.END, newInput.strip())


##Find POS of input sentence
def getPOS():
    output.delete("0.0", tk.END)
    inputSentence = str(entry.get("0.0", tk.END)).strip()

    # If Empty Input
    if len(inputSentence) <= 0:
        tk.messagebox.showinfo("Alert!", "Empty Input!!")
        return

    # Detect Language
    gTranslator = Translator()
    detectedLang = gTranslator.detect(inputSentence)
    if str(detectedLang.lang).strip() != "bn":
        tk.messagebox.showinfo("Alert!", "Type in Bangla Characters!!")
        return

    ##Get POS of each token in INPUT Sentence
    posOutput = str(posHandler.getCtgSentPos(inputSentence)).strip()
    show_output(posOutput)
    print(posOutput)  ##For Debugging on Console Window



##Function RESET
def reset() :
    entry.delete("0.0",tk.END)
    output.delete("0.0",tk.END)

    #Destroy buttons
    for i in suggestion_buttons:
        for j in i:
            j.destroy()
    for j in suggestion_labels:
        j.destroy()


##-------------------
##DESIGN SENCTION
##creating the widgets
label = tk.Label(win,text = "Chittagonian")
label.config(font=('Helvetica', 10, 'bold'))
label.place(relx = 0.012, rely = 0.01)

entry = tk.Text(win)
entry.place(relx = 0.012, rely = 0.09, relwidth = 0.4, relheight = 0.17)

button = tk.Button(win,text = "Translate",command = translate, bg = "#829FD9", width = 8)
button.config(font=('Helvetica', 10))
button.place(relx  = 0.26, rely = 0.28)
button2 = tk.Button(win,text = "Reset",command = reset, bg = "#829FD9", width = 7)
button2.config(font=('Helvetica', 10))
button2.place(relx = 0.41, rely = 0.28)
button3 = tk.Button(win,text = "Check Input",command = suggest, bg = "#829FD9", width = 10)
button3.config(font=('Helvetica', 10))
button3.place(relx = 0.55, rely = 0.28)
button4 = tk.Button(win,text = "Get POS",command = getPOS, bg = "#829FD9", width = 10)
button4.config(font=('Helvetica', 10))
button4.place(relx = 0.73, rely = 0.28)


label1 = tk.Label(win,text = "Standard Bangla")
label1.config(font=('Helvetica', 10, 'bold'))
label1.place(relx = 0.4, rely = 0.01)
output = tk.Text(win)
output.place(relx = 0.5, rely = 0.09, relwidth = 0.4, relheight = 0.17)

#Suggestion Label
label2 = tk.Label(win, text = "Suggested Words:")
label2.config(font=('Helvetica', 10, 'bold'))
label2.place(relx = 0.012, rely = 0.4)

if __name__ == '__main__':
    win.mainloop()