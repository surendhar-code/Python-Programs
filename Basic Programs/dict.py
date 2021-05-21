dict1 = {
   "csk":"dhoni",
    "Mi":"rohit sharma"

}
print(dict1['csk'])
print(dict1.keys())
print(dict1.values())
print(dict1.get("Mi"))
print(dict1.items())
dict1["Rcb"] = "virat"
print(dict1)
dict1['csk'] = "raina"
print(dict1)
dict1.update({"kingpunjab":"Rahul"})
print(dict1)
dict1.pop("Rcb")
print(dict1)