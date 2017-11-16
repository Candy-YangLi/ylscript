import time
import hashlib
token="gamma20k8h9m6g6b1w2v4z1sjh6v3ocr"
timestamp=str(int(time.time()))
once="1234"
temp_array=[token,timestamp,once]
temp_array.sort()
for temp in temp_array:
    print(temp)
signature=temp_array[0]+temp_array[1]+temp_array[2]
print("signature="+signature)
signaturenew=signature.encode("utf-8")
signaturenewnew=hashlib.sha1(signaturenew).hexdigest()
print(signaturenewnew)