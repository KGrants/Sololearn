import re
u = input()
if len(u) == 8 and u.startswith(('1','8','9')):
    print("Valid")
else:
    print("Invalid")
