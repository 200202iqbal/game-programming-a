str = 'X-DSPAM-Confidence:0.8475'
str2 = 'X-DSPAM-Confidence0.8475'

def collect(string):
    frontpost = string.find(":")
    if frontpost == -1:
        return False
    newString = string[frontpost+1:]

    return float(newString)

print(collect(str))
print(collect(str2))