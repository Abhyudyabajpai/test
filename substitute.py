import re
text = "last night Mr. Dallo and Mrs. Sana pushed Ms. Chia"

pat = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+',re.I)
result = pat.sub("\g<1> \g<2>", text)
print(result)
