def most_frequent(string1):
    mydict={}
    for num in string:
       z=string.count(num)
       mydict[num]=str(z)
       list1=list(mydict.items())
       tuple1=tuple(list1)
       tuple1=sorted(mydict.items(),reverse=True,key=lambda x:x[1])
       print("output:\n")
       for x in tuple1:
           print(x[0]+" 0"+x[1])

string=str(input("please enter a string: "))
most_frequent(string)

