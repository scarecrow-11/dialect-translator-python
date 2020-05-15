#### LOOK FOR DMETAOHONE FUNCTIONS ONLY !!!!
### doublemetaphone_encode(word)
###	measure_similarity_dmetaphone(word, word1)
###	lcs(X, Y)
###	knn_neighbors(word, k)


#IMPORT LIBRARIES
import numpy
import pandas as pd


#Inserting Data in Array
data = pd.read_csv("dataset.csv")
data.columns = ["ctg", "bng", "pos"]

array_of_ctg = list(data.ctg)
array_of_bng = list(data.bng)

#Double Metaphone Algorithm Approach for Phonetic encoding
def doublemetaphone_encode(word):

	# Define Phonetic Encoding Array
	encodes = {"অ": "o", "আ": "a", "া": "a", "ই": "i", "ঈ": "i", "ি": "i", "ী": "i", "উ": "u", "ঊ": "u", "ু": "u",
			   "ূ": "u", "এ": "e", "ে": "e", "ঐ": "oi", "ৈ": "oi", "ও": "o", "ঔ": "ou", "ৌ": "ou", "ক": "k", "খ": "k",
			   "গ": "g", "ঘ": "g", "ঙ": "ng", "ং": "ng", "চ": "c", "ছ": "c", "য": "j", "জ": "j", "ঝ": "j", "ঞ": "n",
			   "ট": "T", "ঠ": "T", "ড": "D", "ঢ": "D", "ঋ": "ri", "র": "r", "ড়": "r", "ঢ়": "r", "ন": "n", "ণ": "n",
			   "ত": "t", "থ": "t", "দ": "d", "ধ": "d", "প": "p", "ফ": "p", "ব": "b", "ভ": "b", "ম": "m", "য়": "y",
			   "ল": "l", "শ": "s", "স": "s", "ষ": "s", "হ": "h", "ঃ": "h", "ৎ": "t", 'ৃ': 'ri'}

	letters_tobe_checked = {'ক', 'য', 'ঞ', 'ব', 'ম', 'হ', 'ঃ'}

	encoded_word = ""
	i, l = 0, len(word)
	while i < l:
		if word[i] not in letters_tobe_checked:
			encoded_word += encodes.get(word[i], "")
		elif word[i] == "ক":
			if word[i:i + 3] == "ক্ষ":
				if i == 0:
					encoded_word += "k"
				else:
					encoded_word += "kk"
				i += 2
			else:
				encoded_word += "k"
		elif word[i] == "য":
			if word[i:i + 2] == 'য়':
				encoded_word += "y"
			elif i != 0 and word[i - 1:i + 1] == '্য':
				if i == 2:
					encoded_word += "e"
				elif i - 3 > -1 and word[i - 3] == '\u09CD':
					pass
				elif word[i - 2] == 'র':
					encoded_word += "j"
				else:
					if encoded_word:
						encoded_word += encoded_word[-1]
			else:
				encoded_word += "j"
		elif word[i] == "ঞ":
			if i != 0 and word[i - 1] == '\u09CD':
				if word[i - 2] == "জ":
					if i == 2 and i + 1 != l and word[i + 1] == "া":
						encoded_word = encoded_word[:-1] + "ge"
						i += 1
					else:
						encoded_word = encoded_word[:-1] + "gg"
				else:
					encoded_word += "n"
			elif i + 1 != l and word[i + 1] in {"া", "আ", "ই", "ি", "ঈ", "ী"}:
				pass
			else:
				encoded_word += "n"

		elif word[i] == "ব":
			if i != 0 and word[i - 1] == '\u09CD':
				if i == 2 or (i - 3 > -1 and word[i - 3] == '\u09CD'):
					pass
				elif word[i - 2] in {'গ', 'ম'} or word[i - 3:i + 1] == 'উদ্ব':
					encoded_word += "b"

				else:
					if encoded_word:
						encoded_word += encoded_word[-1]

			else:
				encoded_word += "b"

		elif word[i] == "ম":
			if i != 0 and word[i - 1] == '\u09CD':
				if i == 2 or (i - 3 > -1 and word[i - 3] == '\u09CD'):
					pass
				elif word[i - 2] in {'ক', 'গ', 'ঙ', 'ট', 'ন', 'ণ', 'ল', 'স', 'শ', 'ষ'}:
					encoded_word += "m"
				#				elif word[i-2] == 'ষ' and (i == l-1 or (i+1 == l-1 and word[i+1] in {"া","আ", "ই","ি","ঈ","ী"} ) ):
				#					pass
				else:
					if encoded_word:
						encoded_word += encoded_word[-1]
			else:
				encoded_word += "m"

		elif word[i] == "হ":
			if word[i + 1:i + 2] == 'ৃ' or word[i + 1:i + 3] == '্র':
				pass
			elif word[i + 1:i + 3] == '্ণ' or word[i + 1:i + 3] == '্ন':
				encoded_word += "n"
			elif word[i + 1:i + 3] == '্ম':
				encoded_word += "m"
			elif word[i + 1:i + 3] == '্য':
				encoded_word += "j"
			elif word[i + 1:i + 3] == '্ল':
				encoded_word += "l"
			else:
				encoded_word += "h"

		elif word[i] == 'ঃ':
			if l < 4 and i == l - 1:
				encoded_word += "h"
			else:
				pass

		if i - 1 > -1 and word[i - 1] == 'ঃ':
			if i - 1 != 0 and i - 1 != l - 1:
				if encoded_word:
					encoded_word += encoded_word[-1]

		i += 1
	return encoded_word.strip()


#LCS Function
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


#Use Double Metaphone Similarity
def measure_similarity_dmetaphone(word, word1):

	lcsLength = 0
	# Check for DMetaphone Approach
	wordDMetaphonePhonetic = doublemetaphone_encode(word)
	word1DMetaphonePhonetic = doublemetaphone_encode(word1)

	# Check Encoded Phonetics Length
	wordPhoneticLength = len(wordDMetaphonePhonetic)
	word1Phoneticlength = len(word1DMetaphonePhonetic)

	# Pick the Bigger one for Max accuracy
	if wordPhoneticLength > word1Phoneticlength:
		lcsLength = lcs(wordDMetaphonePhonetic, word1DMetaphonePhonetic)
	else:
		lcsLength = lcs(word1DMetaphonePhonetic, wordDMetaphonePhonetic)

	return lcsLength		#Larger means Similar for LCS

#USE OF K NEAREST NEIGHBORS
def knn_neighbors(word, k):

	nearest_word_indices = []
	rec_words = []

	for i in range(len(array_of_ctg)):
		compareValue = measure_similarity_dmetaphone(word, array_of_ctg[i])
		nearest_word_indices.append(compareValue)

	#Sort Distance array ascending and return another array containing the indices

	temp = numpy.argsort(nearest_word_indices)
	temp =  temp[::-1]		#Reverse array, Highest LCS Length first

	#Get Max 3 closest words corresponding to the indices
	for i in range(k):
		rec_words.append(array_of_ctg[temp[i]])

	return rec_words


#Suggest Word Function... Starts here
def suggest_word(word):
	return knn_neighbors(word, 3)
