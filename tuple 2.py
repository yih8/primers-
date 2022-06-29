my_tuple = (1,1,1,1,1,"banana","banana","banana","anana",(),(),(),(),(),(),())
a=my_tuple.count("banana")
b=my_tuple.count(1)
c=my_tuple.count(())
d=my_tuple.index("anana")
e=len(my_tuple)

print(a,b,c,d,e)