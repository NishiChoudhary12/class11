# 52) Count all letters, digits, and special symbols from a given string
#     Given: str1 = "P@#yn26at^&i5ve"
#     Expected Outcome:
#     Total counts of chars, digits, and symbols
#     Chars = 8
#     Digits = 3
#     Symbol = 4

a = "P@#yn26at^&i5ve"
alpha=0
num=0
spchar=0
for i in a:
    if i.isalpha():
        alpha=alpha+1
    elif i.isnumeric():
        num=num+1
    else:
        spchar=spchar+1
print(f"char ={alpha}\n num={num} \nspchar= {spchar}")
print(num)
print(spchar)



