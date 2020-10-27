#This was written by Boyd Kirkman for educational and professional use only, I take no responsibility for its miss use.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from itertools import permutations, combinations, product
from more_itertools import collapse

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Title~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
title = """
 ________  _______   ________  ________  _____ ______   _______       _______      ___    ___ _______
|\\   __  \\|\  ___ \\ |\\   __  \\|\\   ___ \\|\\   _ \\  _   \\|\\  ___ \\     |\\  ___ \\    |\\  \\  /  /|\\  ___ \\
\\ \\  \\|\\  \\ \\   __/|\\ \\  \\|\\  \\ \\  \\_|\\ \\ \\  \\\\\\__\\ \\  \\ \\   __/|    \\ \\   __/|   \\ \\  \\/  / | \\   __/|
 \\ \\   _  _\\ \\  \\_|/_\\ \\   __  \\ \\  \\ \\\\ \\ \\  \\\\|__| \\  \\ \\  \\_|/__   \\ \\  \\_|/__  \\ \\    / / \\ \\  \\_|/__
  \\ \\  \\\\  \\\\ \\  \\_|\\ \\ \\  \\ \\  \\ \\  \\_\\\\ \\ \\  \\    \\ \\  \\ \\  \\_|\\ \\ __\\ \\  \\_|\\ \\  /     \\/   \\ \\  \\_|\\ \\
   \\ \\__\\\\ _\\\\ \\_______\\ \\__\\ \\__\\ \\_______\\ \\__\\    \\ \\__\\ \\_______\\\\__\\ \\_______\\/  /\\   \\    \\ \\_______\\
    \\|__|\\|__|\\|_______|\\|__|\\|__|\\|_______|\\|__|     \\|__|\\|_______\\|__|\\|_______/__/ /\\ __\\    \\|_______|
                                                                                  |__|/ \\|__|

        #      #
      #     #      #
   # #   ##  ###   #   #
       #    #    ##   #  ##
  #  ##   ##   ###   #
    /\\# ###/\\  #  _/*\\  #
   /*@*\\__/**\\/\\/*&@*|   #
   \*% ________ *%$#!*\\
    | |        | \\**^%*|
    |\\| ~~~~~~~L___\\*!@/
     \\| ~~~~~~~~~~~ |/
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      .-------------.
        README.exe

PASSWORD CRACKER v1.0.0
WARNING: This will likely create a very large list.
DISCLAIMER: I take no responsibility for any potentially illegal activity aided by use of this software.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~defining lists and vaiables~~~~~~~~~~~~~~~~~~~~~~~~~~~~
words = ["password"]
numberlist = []
savelist = []

#~~~~~~~~~~~~~~~~~~~functions that generate the variants~~~~~~~~~~~~~~~~~~~~~~~~
def numbers():
    #this will create multiple number combinations
    num = []
    for f in range(1,11):
        for p in combinations([0,1,2,3,4,5,6,7,8,9],f):
            num.append("".join(["".join(str(q)) for q in p]))
    return num

def mixer(in_words):
    #do just the usual mixing and mashing of the words, words with numbers, etc, these can then be transmuted via the others
    listw = []
    listc = []
    for f in range(1,(len(in_words)+1)):
        print("mixing words:",f,"/",len(in_words))
        listw.append(["".join(p) for p in permutations(in_words,f)])
    listc.append(listw)
    return list(collapse(listc))

def caps(in_words):
    #mix the capital letters throughout
    caps = []
    for f in range(0,len(in_words)):
        print("mixing in caps:",f,"/",len(in_words))
        caps.append(list(map(''.join, product(*zip(in_words[f].upper(), in_words[f].lower())))))
    return list(collapse(caps))

def numsub(in_words):
    #replace letters with their common number replacements -------> I think I'll leave this out for now else the word list will get way to long
    return 0

def allcomb(in_numbers,in_words,numsub):
    #combine all lists created up till now
    comb = []
    comb.append(in_words)
    for i in range(0,len(in_words)):
        for f in range(0,len(in_numbers)):
            comb.append(in_words[i]+in_numbers[f])
            comb.append(in_numbers[f]+in_words[i])
    comb.append(in_numbers)
    print(f"wow thats a long file: {len(comb)} guesses in total")
    return list(collapse(comb))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~the main function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    print(title)
    print("Input associated words to the target (e.g. name, favourite sport, etc.): \nNOTE: type 'in_done' to escape inputting words and the program will continue")
    collecting = True
    while collecting:
        wordsadd = input(">>> ")
        if wordsadd.lower() == 'in_done':
            collecting = False
        else:
            words.append(wordsadd.lower())
    #memoisation of numbers calculations
    mem_numbers = numbers()
    numberlist.append(numbers())
    #memoisation of the other calculations
    mem_mixer = mixer(words) #STEP 1: Create a list of all possible permutations of the words

    #currently out of the program  due to memory errors:
    mem_caps = 0#caps(mem_mixer) #STEP 2: Take that list of mixes and find all upper/lower case combos
    mem_numsub = numsub(mem_caps) #STEP 3: create common substitutions of numbers for letters and apply these combos to the list of mixed word case combos
    savelist.append(allcomb(mem_numbers,mem_mixer,mem_numsub))
    with open("pass.txt","w+") as file:
        for line in savelist[0]:
            file.write(line+"\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__=="__main__":
    main()
