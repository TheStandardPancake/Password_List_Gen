#This was written by Boyd Kirkman for educational and professional use only, I take no responsibility for its miss use.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from itertools import permutations, combinations


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

def numsub():
    #replace letters with their common number replacements

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~the main function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    numbers.append(numbers())
    savelist.append((simple(numbers),caps(),numsub()))
    with open("pass.txt","w+") as file:
        for line in savelist:
            file.write(savelist[line])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__=="__main__":
    main()
