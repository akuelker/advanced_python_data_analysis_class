import json
complexNum = complex(2, 3)
#print (complexNum)
#encoded_complexNum = json.dumps(complexNum)

if isinstance(complexNum, complex):
    complexTuple =  ('complex', complexNum.real, complexNum.imag)
encoded_complexNum = json.dumps(complexTuple)

print(encoded_complexNum)
