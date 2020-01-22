from Crypto.Util.number import getPrime, isPrime

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtWidgets import QWidget,QFormLayout,QLineEdit
import sys,functools,os, secrets
from cryptography import crypt
import time 
class diffieHellman():
    def __init__(self):
        self.key,self.privKeyA,self.privKeyB=self.getRando()
        self.pubMod=self.getNewPrime()
        self.fk=self.genPubKey(self.key,self.pubMod)
        self.secret=self.generateSecret(self.fk,self.privKeyA)
        self.enc_msg=""

    #generate a new rime when called. Ephemeral?
    def getRando(self):
        self.pubKey = secrets.randbelow(1000)
        self.privKeyA = secrets.randbelow(500)
        self.privKeyB = secrets.randbelow(500)
        return self.pubKey,self.privKeyA,self.privKeyB
        
    def getNewPrime(self):
        self.pubMod = getPrime(10)
        return self.pubMod

    def genPubKey(self,key,mod):
        self.fk=self.key**self.privKeyA
        self.fk=self.fk%self.pubMod
        return self.fk

    def generateSecret(self,pub,priv):
        self.secret=pub**priv
        self.secret=self.secret%self.pubMod
        return self.secret
    
    def genRailKey(self):
        k = self.secret%10
        return k


    def encryption(self,msg):
        self.enc_msg=""
        quotient=0
        val=self.secret%256
        #key = Alice()
        for c in msg:
            #Flip to unicode then obtain int value and add key
            #quotient=(ord(c)+ans)//256
            self.enc_msg +=chr(ord(c)+val)
            newkey=val
            newkey=self.secret+newkey
            val=newkey%256
        #print(self.enc_msg)
        return self.enc_msg

    #ASCII 256 characters
    def decrypt(self,key):
        dec_msg=""
        #self.secret
        val=key%256
        quotient=0
        for c in self.enc_msg:
            #quotient=(ord(c)+ans)//256
            dec_msg += chr(ord(c)-val)
            newkey=val
            newkey=self.secret+newkey 
            val=newkey%256
        #print(dec_msg)
        return dec_msg

def main():
    t0=time.time()
    dh = diffieHellman()
    key,priv,privB=dh.getRando()
    mod=dh.getNewPrime()
    fk=dh.genPubKey(key,mod)
    secret=dh.generateSecret(fk,priv)
    secret2=dh.generateSecret(fk,privB)
    # with open('small.txt', 'r') as fileIn:
    #     text = fileIn.read()
    text = 'testingThIsAlgo'#input("Please enter a string: ")
    key=dh.genRailKey()
    while(key<3):
        print("In loop to remake secret")
        key,priv,privB=dh.getRando()
        fk=dh.genPubKey(key,mod)
        secret = dh.generateSecret(fk,priv)
        key = dh.genRailKey()
        if key >=3:
            break

    print("Key",key)
    cro = crypt(text,key)
    print("Entered input string: ", text)
    #Railfence encrypted
    print("***********Starting encryption process***********")
    final=cro.encryption()
    enc=dh.encryption(final)
    print("Encrypted DH",enc)

    print("***********Starting decryption process***********")

    dec=dh.decrypt(secret2)
    print("Decrypted DH",dec)
    raildec=cro.decryption()
    print("Decrypted Railfence:",raildec)
    t1=time.time()

    total = t1-t0
    print(total,'seconds')
    # print("Public key",key)
    # print("Public modulus",mod)
    # print("Secret",secret)
    # print("Encrypted text:",enc)
    # print("Decrypted:",dec)

if __name__=='__main__':
    main()