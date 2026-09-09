setA = {1,2,3,4}
setB = {2,3}
setC = {1,2,3,4}
setD = {1,2,3,4,5}

print("Is setA a superset of setB?", setA >= setB)
print("Is setB a subset of setA?", setB <= setA)

print("Is setA a proper superset of setB?", setA > setB)
print("Is setB a proper subset of setA?", setB < setA)

print("Are setA and setC equal?", setA == setC)

print("Is setB a subset of setD and not equal?", setB <= setD and setB != setD)