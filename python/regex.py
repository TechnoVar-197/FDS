import re

txt = "92054815517"
f="^9.*{9}[0-9]"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("^9{9}[0-9]", txt)

print(x)
