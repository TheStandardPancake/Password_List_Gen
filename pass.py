#This was written by Boyd Kirkman for educational and professional use only, I take no responsibility for its miss use.

#~~~~~~~~~~~~~~~~~~~~~~~~defining lists and vaiables~~~~~~~~~~~~~~~~~~~~~~~~~~~~
words = ["password"]
numbers = []
savelist = []

#~~~~~~~~~~~~~~~~~~~functions that generate the variants~~~~~~~~~~~~~~~~~~~~~~~~
def numbers():
    #this will create multiple number combinations

def simple(x):
    #do just the usual mixing and mashing of the words, words with numbers, etc, these can then be transmuted via the others

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
