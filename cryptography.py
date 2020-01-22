
import string

class crypt():
  def __init__(self,text,key):
    self.key =key
    self.input = text 


  def upper_case(self):
    upper = string.ascii_uppercase
    return upper


  def lower_case(self):
    lower = string.ascii_lowercase
    lower = self.reverse(lower)
    return lower


  def special_characters(self):
    x = []
    for i in range(33,48):
      char = chr(i)
      x.append(char)
    for i in range(58,65):
      char = chr(i)
      x.append(char)
    for i in range(91,95):
      char = chr(i)
      x.append(char)
    return x

  # -----------------Encryption Process---------------------
  def reverse(self,s): 
    str = "" 
    for i in s: 
      str = i + str
    return str



  def encryptRailFence(self,text, key): 
    rail = [['\n' for i in range(len(text))] 
                  for j in range(key)]  
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)): 
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 
        rail[row][col] = text[i] 
        col += 1
        if dir_down: 
            row += 1
        else: 
            row -= 1
    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    j = "" . join(result) 
    return j

  def encryption_substitution(self,trans,upper,lower,x):
    sub = list(trans)
    for i in range(len(sub)):
      if (sub[i] == " "):
        sub[i] = "i"
      else:
        if (sub[i].islower()) == True:
          lower_i = lower.index(sub[i])
          sub[i] = x[lower_i]
        else:
          upper_i = upper.index(sub[i])
          sub[i] = x[upper_i] + '`'

    final = "".join(sub)
    return final



  # -----------------Decryption Process---------------------

  def decryption_substitution(self,final,upper, lower, x):
    decryp = list(final)
    count = decryp.count('`')
    y = len(decryp) - count
    for i in range(y - 1):
      if (decryp[i] == 'i'):
        decryp[i] = ' '
      else:
          if (decryp[i + 1] == '`'):
            special_i = x.index(decryp[i])
            decryp[i] = upper[special_i]
            decryp.remove('`')
          else:
            special_i = x.index(decryp[i])
            decryp[i] = lower[special_i]

    if (decryp[-1] == 'i'):
      decryp[-1] = ' '
    else:
      if (decryp[-1] != '`'):
        special_i = x.index(decryp[-1])
        decryp[-1] = lower[special_i]
      else:
        special_i = x.index(decryp[-2])
        decryp[-2] = upper[special_i]
        decryp.remove('`')

    decrypt_sub = "".join(decryp)
    return decrypt_sub


  def decryptRailFence(self,cipher, key): 
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down: 
            row += 1
        else: 
            row -= 1
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
                (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
        if dir_down: 
            row += 1
        else: 
            row -= 1
    decryp_rail = "".join(result)
    return decryp_rail


  def encryption(self):
    b = self.reverse(self.input)
    print("Reverse of the input string: ", b)

    trans = self.encryptRailFence(self.reverse(self.input), self.key)
    print("After Rail Fence Substitution :", trans)

    upper = self.upper_case()
    lower = self.lower_case()
    sc = self.special_characters()
    final = self.encryption_substitution(trans,upper,lower,sc)
    print("After Substitution with Special Characters :", final)

    return final


  def decryption(self):
    desub = self.decryption_substitution(self.encryption(),self.upper_case(), self.lower_case(), self.special_characters())
    print("After decryption substitution:", desub)

    detrans = self.decryptRailFence(desub, self.key)
    print("After Rail Fence Substitution :", detrans)

    final_input = self.reverse(detrans)
    print("Original Input String : ", final_input)
    return final_input
