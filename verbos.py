import re
pat = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
pattern = re.compile(r"""
    ^([a-zA-Z0-9_.+-]+)
    @
    ([a-zA-Z0-9-]+)
    \.
   ([a-zA-Z0-9-.]+$)
   """, re.VERBOSE)    
match = pattern.search("thomas123@yahoo.com")
print(match.groups())