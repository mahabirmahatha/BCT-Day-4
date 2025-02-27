d={1:'ABC',2:'DEF',3:'GHI'}
d2=d.fromkeys(d,"ABC")
print(d2)
print(d.get(2))
print(d.keys())
print(d.values())
d.pop(2)
print(d)
d.popitem()
print(d)

