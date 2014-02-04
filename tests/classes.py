from PEA_connect import classes

byFullString = classes()
byClassCode = classes(by="ClassCode")

a = byFullString.get("13/FA Selected Topics * (MAT-590-A)#/classes/mat-590-a-cs81877")
b = byClassCode.get("mat-590-a")
assert a == b
