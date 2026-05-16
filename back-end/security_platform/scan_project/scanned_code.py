import hashlib

data = eval(input())

password = hashlib.md5(b"test").hexdigest()