import re

def extract_phn(input):
    phn_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phn_regex.search(input)
    if match:
        return match.group()
    return None

print(extract_phn("my number is 235 986-1288"))
print(extract_phn("my number is 760 088-545322"))

def is_valid_phn(input):
    phn = re.compile(r'^\d{3} \d{3}-\d{4}\b$')
    match = phn.search(input)
    if match:
        return True
    return False

print(is_valid_phn("445 352-3399"))
print(is_valid_phn("dsdad 456 322-8876"))
