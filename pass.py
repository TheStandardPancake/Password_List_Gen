#This was written by Boyd Kirkman for educational and professional use only, I take no responsibility for its miss use.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from itertools import permutations, combinations

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
I take no responsibility for any potentially illegal activity aided by use of this software.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~defining lists and vaiables~~~~~~~~~~~~~~~~~~~~~~~~~~~~
words = ["password"]
numbers = []
savelist = []

#~~~~~~~~~~~~~~~~~~~functions that generate the variants~~~~~~~~~~~~~~~~~~~~~~~~
def numbers():
    #this will create multiple number combinations
    num = []
    for f in range(1,10):
        num.append(["".join(list(str(p))) for p in combinations([0,1,2,3,4,5,6,7,8,9],f)])
    num.append(["".join(list(str(p))) for p in combinations([0,1,2,3,4,5,6,7,8,9])])
    return num

def mixer(in_numbers,in_words):
    #do just the usual mixing and mashing of the words, words with numbers, etc, these can then be transmuted via the others
    listw = []
    listc = []
    listw.append(in_words)
    for f in range(1,(len(in_words)+1)):
        listw.append(["".join(p) for p in permutations(in_words,f)])
    listc.append(listw.append())

def caps(in_words):
    #mix the capital letters throughout
    caps = []
    for f in range(0,len(in_words)):
        caps.append(''.join, itertools.product(*((c.upper(), c.lower()) for c in in_words[f]))
    return caps

def numsub(in_words):
    #replace letters with their common number replacements
    pass

def allcomb(numbers,mixer,caps,numsub):
    #combine all lists created up till now
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~the main function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    print(title)
    print("Input associated words to the target (e.g. name, favourite sport, etc.): \nNOTE: type 'in_done' to escape inputting words and the program will continue")
    collecting = True
    while collecting:
        wordsadd = input(">>> ")
        if wordsadd.lower() == 'in_done'
            collecting = False
        else:
            words.append(wordsadd.lower())
    #memoisation of numbers calculations
    mem_numbers = numbers()
    numbers.append(numbers())
    #memoisation of the other calculations
    mem_mixer = mixer(numbers,words) #STEP 1: Create a list of all possible permutations of the words
    mem_caps = caps(mem_mixer) #STEP 2: Take that list of mixes and find all upper/lower case combos
    mem_numsub = numsub(mem_caps) #STEP 3: create common substitutions of numbers for letters and apply these combos to the list of mixed word case combos
    savelist.append((mem_mixer,mem_caps,mem_numsub,allcomb(mem_numbers,mem_mixer,mem_caps,mem_numsub)))
    with open("pass.txt","w+") as file:
        for line in savelist:
            file.write(savelist[line])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__=="__main__":
    main()
