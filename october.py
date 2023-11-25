from english_words import get_english_words_set


words = get_english_words_set(['web2'], lower=True)

vowels= ["a","e","i","o","u"]

def vowel_order (word,vowels):
    i=-1
    for v in vowels:
        try:
            i=i+1
            while (word[i]!=v) :
                if (word[i] in vowels):
                    return(False)
                i=i+1
        except IndexError:
            return(False)
    return(True)

def get_words(vowels):
    res=[]
    for word in words:
        if (vowel_order(word,vowels)):
            res.append(word)
    return(res)

print( [ word for word in get_words(["u", "o", "i", "e", "a"]) if len(word)>=12] )
                         
                         




