class RailfenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for i in range(num_rails)]
        rail_index = 0
        direction = 1
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails -1:
                direction = -1
                rail_index += direction
            cipher_text = ''.json(''.join(rail) for rail in rails)
            return cipher_text
        
    def rail_fence_decrypt(self, cipher_text, num_rails):
        rail_lenghts = [0] * num_rails
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            rail_lenghts[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails -1:
                direction = -1
                rail_index += direction
            
        rails = []
        start = 0 
        for lenght in rail_lenghts:
            rail.append(cipher_text[start:start + lenght])
            start += lenght
        plain_text = ""
        rail_index = 0 
        direction = 1
        
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index] [0]
            rail[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
                rail_index += direction 
        return cipher_text
                     