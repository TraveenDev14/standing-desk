#1
myList = [None,None,None,None,None,None,None,None,None,None]
baseP = 0
topP = -1

def push(item) :
    global topP
    if topP == 9 :
        print("Stack is Full Cannot Push")
    else :
        topP = topP+1
        myList[topP] = item

def pop() :
    global topP
    if topP < baseP :
        print("Stack is Empty Cannot Pop")
    else :
        popItem = myList[topP]
        myList[topP] = None
        topP -= 1
        return popItem

need = None
push(56)
print(myList)
push(34)
print(myList)
pop()
print(myList)
pop()
print(myList)
pop()
print(myList)

#while need != 0 :
 #   need = input("Enter Whether You Want to \"pop\" or \"push\" , Enter \'0\' to exit : ")
  #  if need == "push" :
   #     item = int(input("Enter the value to push : "))
    #    push(item)
     #   print(myList)
    #if need == "pop" :
     #   item = pop()
      #  print(item)
       # print(myList)
