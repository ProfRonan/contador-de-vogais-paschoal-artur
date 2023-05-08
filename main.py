"""This program counts the number of vowels in a string."""
def count_vowels(string:str) -> int:
    vowel = ["a", "e", "i", "o", "u"]
    count = 0
    word = False
    while word == False :
        for i in range(len(string)) :
            if string[i] in vowel :
                count += 1
    return count


#if __name__ == "__main__" :
    #palavra = str(input("Digite uma palavra: "))
    #vowel = ["a", "e", "i", "o", "u"]
    #count = 0
    #for i in range(len(palavra)) :
        #if palavra[i] in vowel :
            #count += 1
    #print(count)
