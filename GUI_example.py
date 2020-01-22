from Crypto.Util.number import getPrime, isPrime

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtWidgets import QWidget,QFormLayout,QLineEdit
import sys,functools

#Need to regenerate private keys each time.
#Public don't matter.


#prime bases
public_keyA = getPrime(10)
public_keyB = getPrime(10)

#Secret private keys
private_keyA=199
private_keyB=157

#generate a new rime when called. Ephemeral
def getNewPrime():
    public_keyA = getPrime(10)
    public_keyB = getPrime(10)


def midKey():
    getNewPrime()
    midkey=public_keyA**private_keyA
    midkey=midkey%public_keyB
    return midkey

def fullKey(midkey):
    fk=midkey**private_keyA
    fk=fk%public_keyB
    return fk

def newKey():
    return midKey()

def encryption(msg='hello'):
    enc_msg=""
    key = fullKey(newKey())
    for c in msg:
        #Flip to unicode then obtain int value and add key
        enc_msg +=chr((ord(c)+key))
    print("Encrypted:",enc_msg)
    return enc_msg

def decrypt(enc_msg):
    dec_msg=""
    key = fullKey(newKey())
    for c in enc_msg:
        dec_msg += chr((ord(c)-key))
    return dec_msg

print('Printing partial key:',midKey())
midkey=midKey()
print('Printing fullkey:',fullKey(midkey))
enc=encryption('M')
print('Encryption:',enc)
print('Decrpytion:',decrypt(enc))

elliptical=public_keyA**private_keyA
elliptical=elliptical%public_keyB
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Encryptor')
#window.setGeometry(300,500,300,400)
layout = QFormLayout()
msg_box=QLineEdit()
layout.addRow('Message',msg_box)
enc= QPushButton('Encrypt')
dec=QPushButton('Decrypt')
layout.addWidget(enc)
layout.addWidget(dec)
window.setLayout(layout)
enc.clicked.connect(lambda: encryption(msg_box.text()))

window.move(60,15)
window.show()
sys.exit(app.exec_())