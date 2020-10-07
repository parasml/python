#--------------------------------------------------------------
# Comprehension
#-----------------
lsNumbers = [1, 2, 3, 4, 5, 6]

# Mod of 2 -------------------------
lsEvenNumbers = [i for i in lsNumbers if i%2==0]
print("lsEvenNumbers = ", lsEvenNumbers)

# Square Root -----------------------
lsSqNumbers = [i*i for i in lsNumbers]  #Square root of numbers -------------
print("lsSqNumbers = ", lsSqNumbers)

# Lower ----------------------------
lsNames = ['Apple', 'FRUIT', 'grapes9']
lsNamesLower = [i.lower() for i in lsNames]
print("lsNamesLower = ", lsNamesLower)

# Enumerate ----------------------------
ls = [1, 2, 3, 4, 5, 6]
for idx, val in enumerate(ls):
    print(idx, val)


# Convert list to list of objects -------
lsNew = [{idx:val*2} for idx, val in enumerate(ls)]


# Lambda function ------------------------
x = lambda a:a+10
print(x(5))