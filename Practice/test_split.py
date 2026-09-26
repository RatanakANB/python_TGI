a = "python,is:fun"
a = a.split(",")
a = a[0].split(";") + a[1].split(":")
print(a)