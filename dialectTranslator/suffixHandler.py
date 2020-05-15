
""" #Checked for Nouns Only
    Algorithm:
        1. Translate 'word'
            2. If 'word' not found in dataset:
                    stemSuffix = get_stem_suffix(word)
                    if len(get_stem_suffix()) <= 0:
                        outputWord = word
                    else:
                        bngStem = translate(stemSuffix[0])
                        bngSuffix = get_bng_suffix(bngStem, stemSuffix[1])
                        output = bngStem + bngSuffix


                        ### Suffix different for Vowels and Consonants
                        ### Checked only for Nouns
                        ### If Stem not translated KEEP the ctg stem as output stem
                        ### Add New Word Automatically in Dataset ???

"""

#Libarary Imports

from dialectTranslator import posHandler


##Necessary as different rules apply based on last character of bngStem based on Vowel and Consonants
vowels = ["অ", "আ", "ই", "ঈ", "উ", "ঊ", "ঋ", "ঌ", "এ", "ঐ", "ও", "ঔ"]
consonants = ["ক", "খ", "গ", "ঘ", "ঙ", "চ", "ছ", "জ", "ঝ", "ঞ", "ট", "ঠ", "ড", "ঢ", "ণ", "ত", "থ", "দ", "ধ", "ন", "প", "ফ", "ব", "ভ", "ম", "য", "র", "ল", "শ", "ষ", "স", "হ", "ড়", "ঢ়", "য়", "ৎ","ং", "ঃ", "‍ঁ"]

diacritic_vowels = ["া", "ি", "ী", "ু", "ূ", "ৃ", "ে", "ৈ", "ো", "ৌ"]
diacritic_consonants = ["‍্", "‍্য", "‍‍‍‍্র", "‍‍র্", "‍্ব", ""]


##Split Word into Stem+Suffix
def get_stem_suffix(word):
    ctg_suffixes = ["ত", "রে", "ে", "র", "গান", "্যা"]
    out = []

    for i in ctg_suffixes:
        if word.endswith(i):
            stem = word.strip(i)
            suffix = i
            out.append(stem)
            out.append(suffix)
            return [stem, suffix]
    return out

##Get Bangla Suffix corresponding to Chittagonian
def get_bangla_suffix(bngStem, suffix):

    suffixes_for_vowels = {"ত": "তে", "রে": "কে", "ে": "য়", "র": "র", "গান": "টি", "্যা": "্যা"}
    suffixes_for_consonants = {"ত": "ে", "রে": "কে", "ে": "ে", "র": "ের", "গান": "টি", "্যা": "ের"}

    #Checked For NOUNS Only

    # posTag = ctgPosTagger(bngStem)
    # if posTag != "বিশেষ্য":
    #     return

    bng_suffix = ""
    if (bngStem[-1] in vowels) or (bngStem[-1] in diacritic_vowels):
        bng_suffix = suffixes_for_vowels.get(suffix)
    elif (bngStem[-1] in consonants) or (bngStem[-1] in diacritic_consonants):
        bng_suffix = suffixes_for_consonants.get(suffix)

    return bng_suffix