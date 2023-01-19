"""
search(s,c) is used to find number of occurrence of a character in the string and the list of index (1-based) for locations of this character
s = list(s) is to convert the input to a list
index is a parameter which finds the corresponding location of a number in the list
count is to find the occurrence number
position is also a parameter indicates the location in the list, but it starts at 1, for one-based
list_1 is a space list which is used to imput [position], location in one-based
return of search(s,c) are time of occurrence and the list for one-based location
"""



def search(s,c):
    s = list(s)
    index = 0
    count = 0
    position = 1
    list_1 = []

    for s[index] in s:
        if s[index] == c:
            list_1 = list_1+[position]
            index = index + 1
            count = count + 1
            position = position + 1
        else:
            index = index + 1
            position = position + 1

    return list_1,count
        

def main():

    s = input("Input text:")
    c = input("Input a character to be searched:")

    list_1,count = search(s,c)
    print("The character",c,"in the text occured",count,"times at",list_1,".")
    
main()
"""
s is the input text; c is the character will be searched"""
    
    
