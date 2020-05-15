import pandas as pd
from random import *
from dialectTranslator import translator

#Inserting Data in Array
data = pd.read_csv("dataset.csv")
data.columns = ["ctg", "bng", "pos"]

array_of_ctg = list(data.ctg)
array_of_bng = list(data.bng)
array_of_pos = list(data.pos)

testCtg = []
testBng = []


#Inserting Test Sentences
dataSent = pd.read_csv("sent-corpus.csv")
dataSent.columns = ["ctg", "bng"]
testCtgSent = list(dataSent.ctg)
testBngSent = list(dataSent.bng)

#Generate Random indices for Dataset
randomIndices = sample(range(0, 1269), 500)
randomIndices.sort()


#Collect Test samples
for i in randomIndices:
    testCtg.append(array_of_ctg[i])
    testBng.append(array_of_bng[i])


def evaluateWordtoWord():

    errCount = 0
    for i in range(len(testCtg)):
        ctgWord = str(testCtg[i]).strip()
        bngWord = str(translator.generateOutputSentence(ctgWord)).strip()

        ##Check Validity
        if bngWord != str(testBng[i]).strip():
            print(str(ctgWord) + " " + str(bngWord) + " != " + str(testBng[i]))
            errCount += 1
    print("Error Count: " + str(errCount))

def evaluateSentToSent():
    errCount = 0
    for i in range(len(testCtgSent)):
        ctgSent = str(testCtgSent[i]).strip()
        bngSent = str(translator.generateOutputSentence(ctgSent)).strip()

        ##Check Validity
        if bngSent != str(testBngSent[i]).strip():
            print(str(ctgSent) + " ---- " + str(bngSent) + " != " + str(testBngSent[i]))
            errCount += 1
    print("Error Count: " + str(errCount))

evaluateSentToSent()