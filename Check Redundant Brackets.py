def findDuplicateparenthesis(string):  
    Stack = []
    count = 0
    for ch in string:                
        if ch == ')':  
            top = Stack.pop()  
            elementsInside = 0
            while top != '(':  
                elementsInside += 1
                top = Stack.pop()
            if elementsInside < 1:  
                return True
        else: 
            Stack.append(ch)  
    return False
if __name__ == "__main__":  
    string = input()
    if findDuplicateparenthesis(string) == True:  
        print("true")  
    else: 
        print("false")
