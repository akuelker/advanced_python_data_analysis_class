import json
complexNum = complex(23,57)
print(complexNum)
if isinstance(complexNum, complex):
    complexTuple = (complexNum.real, complexNum.imag)
    encoded_complexNum = json.dumps(complexTuple)
else: encoded_complexNum = json.dumps(complexTuple)
print('encoded:', encoded_complexNum)