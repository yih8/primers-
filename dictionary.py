my_dict={"one":1,"two":2}
a=my_dict["one"]
b=my_dict["two"]
c=my_dict.get("one")
d=my_dict.get("two")
print(a,b,c,d)
my_dict["three"]=3
print(my_dict)
my_dict.pop("one")
print(my_dict)
a=my_dict.items()
b=my_dict.keys()
c=my_dict.values()
d=len(my_dict)
print(a,b,c,d)