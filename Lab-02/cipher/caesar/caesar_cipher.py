from cipher.caesar import ALPHABET

class CaesarCipher: 
    def __init__(self):
          self.alphabet = ALPHABET 

    def encrypt_text(self,  plaintext, key): #hutech key =5 
        len_alphabet = len(self.alphabet)
        plaintext = plaintext.upper()
        encrypt_text = []
        for i in plaintext:
            letter_index = self.alphabet.index(i) #7
            output_index = (letter_index + key) % len_alphabet #12
            output_letter = self.alphabet[output_index]
            encrypt_text.append(output_letter)
        return "".join(encrypt_text)     
            
    def decrypt_text(self, cipher, key): #hutech key =5 
        len_alphabet = len(self.alphabet)
        cipher = cipher.upper()
        decrypt_text = []
        for i in cipher:
            letter_index = self.alphabet.index(i) 
            output_index = (letter_index - key) % len_alphabet 
            output_letter = self.alphabet[output_index]
            decrypt_text.append(output_letter)
        return "".join(decrypt_text)