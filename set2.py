s1={1,2,7,4,9,6}
s2={2,9,7}
print("Intersection of s1 and s2=",s1.intersection(s2))
print("Union of s1 and s2=",s1.union(s2))
print("Is s2 subset of s1?",s2.issubset(s1))
print("Is s1 superset of s2?",s1.issuperset(s2))
s1.pop()
print("After using pop function on s1:",s1)
s1.clear()
print("After clearing s1:",s1)