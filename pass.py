#This was written by Boyd Kirkman for educational and professional use only, I take no responsibility for its miss use.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from itertools import permutations, combinations

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Title~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
title = """

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

def simple(in_numbers,in_words):
    #do just the usual mixing and mashing of the words, words with numbers, etc, these can then be transmuted via the others
    listw = []
    listc = []
    listw.append(in_words)
    for f in range(1,(len(in_words)+1)):
        listw.append(["".join(p) for p in combinations(in_words,f)])
    listc.append(listw.append())

def caps():
    #mix the capital letters throughout
    pass

def numsub():
    #replace letters with their common number replacements
    pass

def allcomb(numbers,simple,caps,numsub):
    #combine all lists created up till now
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~the main function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    print(title)
    wordsadd = input("Known information: ")
    words.append(wordsadd)
    #memoisation of numbers calculations
    mem_numbers = numbers()
    numbers.append(numbers())
    #memoisation of the other calculations
    mem_simp = simple(numbers,words)
    mem_caps = caps()
    mem_numsub = numsub()
    savelist.append((mem_simp,mem_caps,mem_numsub,allcomb(mem_numbers,mem_simple,mem_caps,mem_numsub)))
    with open("pass.txt","w+") as file:
        for line in savelist:
            file.write(savelist[line])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__=="__main__":
    main()
