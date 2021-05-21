tup = tuple(("suren","sai","ramesh"))
print(tup)

#unpack tuples
tuple1 = (1,2,3,4)
(suren,sai,charann,ram) = tuple1
print(suren)
print(sai)
print(charann)
print(ram)
tuple2 = (1,2,3,4,5,6,7)
(rank1, rank2, *others) = tuple2
print(rank1)
print(rank2)
print(others)

tuple3 = (1,2,3,3,3,4,4,6)
print(tuple3.count(3))