import re
# aaa34 32
pattern=r"^[1-9][0-9][0-9]"

test=input()

if(re.match(pattern,test )):
    print("true")
else:
    print('false')