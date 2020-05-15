#Library Imports
import pandas as pd
import nltk
from dialectTranslator import translator

#Inserting Data in Array
data = pd.read_csv("dataset.csv")
data.columns = ["ctg", "bng", "pos"]

ctg = list(data.ctg)
pos = list(data.pos)


##POS Tagger Chittagonian Word
def getCtgWordPos(word):
    posTag = "Unknown"
    for i in range(len(ctg)):
        if ctg[i] == word:
            if pos[i] != None:
                posTag = pos[i]
                return posTag

    return posTag

##POS Tagger for Chittagonian Sentence
def getCtgSentPos(sent):
    tokens = translator.tokenize_input(sent)
    posTags = ""
    for word in tokens:
        posTags += getCtgWordPos(word) + " "

    return posTags
