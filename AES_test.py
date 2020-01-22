from Crypto.Cipher import AES
import time 

t0=time.time()
key = 'abcdefghijklmnop'
cipher = AES.new(key)
ciphertext = cipher.encrypt('SomethingCrazyaaSomethingCrazyaa')
print(ciphertext)
t1= time.time()
total = t1-t0
decipher = AES.new(key)
print(decipher.decrypt(ciphertext))


print(total,'seconds')