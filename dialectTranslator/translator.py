#Library Imports
import nltk
import pandas as pd
from dialectTranslator import suffixHandler

#Inserting Data in Array
data = pd.read_csv("dataset.csv")
data.columns = ["ctg", "bng", "pos"]

array_of_ctg = list(data.ctg)
array_of_bng = list(data.bng)
array_of_pos = list(data.pos)


#For POS Tagging
def getCtgArray():
    return array_of_ctg

def getPosArray():
    return array_of_pos


#Word Mapping
#For each token of the input word searching with the ctg array of words
#If found the exact words, print the corresponding index of Bng word
#If not found then input is output

#Word Tokenizer
def tokenize_input(word_data):
    # Tokenization Starts
    nltk_tokens = nltk.word_tokenize(word_data)  # Tokenize the sentence
    return nltk_tokens

#Fix negation rule
def fix_negation_rule(tokens):
    for i in range(len(tokens)):
        if i < len(tokens)-1 and (tokens[i].strip() == "ন" or tokens[i].strip() == "নঁ"):
            temp = tokens[i]
            tokens[i] = tokens[i+1]
            tokens[i+1] = temp
    return tokens


#Translate function
def translateWord(word):
    outputWord = ""

    #For word in nltk_tokens:
    status = "Not Found"
    for j in array_of_ctg:
        if word == j:
            index = array_of_ctg.index(j)
            outputWord = str(array_of_bng[index]).strip()
            status = "Found"
            break

    if status == "Not Found":
        outputWord = ""

    return outputWord


#Generate Output Sentence
def generateOutputSentence(inputSentence):
    translation = ""

    tokens = tokenize_input(inputSentence)

    # Fix Negation Rule
    tokens = fix_negation_rule(tokens)

    #Translate each token
    for word in tokens:
        #Try translating word-to-word
        outputWord = translateWord(word)

        if outputWord == "":
            #Handle with suffix stripping
            stemSuffix = suffixHandler.get_stem_suffix(word)
            if len(stemSuffix) <= 0:
                outputWord = word
            else:
                bngStem = translateWord(stemSuffix[0])

                #If bngStem can't be translated either
                if bngStem == "":
                    outputWord = word
                else:
                    bngSuffix = suffixHandler.get_bangla_suffix(bngStem, stemSuffix[1])
                    outputWord = bngStem + bngSuffix

        translation += outputWord + " "

    return translation.strip()