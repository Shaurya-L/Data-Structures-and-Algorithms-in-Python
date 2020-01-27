def uniqueChars(string):
    s = ""
    for ele in string:
        if(ele not in s):
            s=s+ele
    return s        
string = input()
print(uniqueChars(string))
