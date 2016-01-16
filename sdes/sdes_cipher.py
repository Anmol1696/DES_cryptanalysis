from round_keys import RoundKeys

IP1     = [1, 5, 2, 0, 3, 7, 4, 6]
inv_IP1 = [3, 0, 2, 4, 6, 1, 7, 5]
E       = [3, 0, 1, 2, 1, 2, 3, 0]
P       = [1, 3, 2, 0]

SBox    = [[[1, 0, 3, 2], 
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 3, 2]],
          [[0, 1, 2, 3],
           [2, 0, 1, 3],
           [3, 0, 1, 0],
           [2, 1, 0, 3]]]

class SDES:
    """
        Class for the main func for SDES
    """
    def __init__(self, text, encrypt):
        """
            Init for the class object
        """
        self.plain_text     = None
        self.cipher_text    = None
        self.encrypt        = encrypt

        if encrypt:
            self.plain_text = text
        else:
            self.cipher_text = text

    def performIP1(self):
        """
            On the text input perform the initial permutation 1
        """
        if self.encrypt:
            text = self.plain_text
        else:
            text = self.cipher_text

        text = ''.join([text[i] for i in IP1])
        L, R = text[:4], text[4:]

        return (L, R)

    def keyFunc(self, side, key):
        """
            The side would be L or R depending on the round

            Takes in the half block and the key and outputs f(R, key)
        """
        #Will house the half-half parts of the result from f
        half_ans = []

        #Expansion Process
        side = ''.join([side[i] for i in E])

        #XOR for expanded side with Key
        side = bin(int(side, 2)^int(key, 2))[2:].zfill(8)  
        #SBox Substitution
        half_sides = [side[:4], side[4:]]

        for i in range(2):
            row_index = half_sides[i][0] + half_sides[i][3]
            col_index = half_sides[i][1:3]
            row_index = int(row_index, 2)
            col_index = int(col_index, 2)

            reduced   = SBox[i][row_index][col_index]
            reduced   = bin(reduced)[2:].zfill(2)
            
            half_ans.append(reduced)

        final_result = ''.join(half_ans)
        final_result = ''.join([final_result[j] for j in P])

        return final_result

    def mainRounds(self, L0, R0, keys):
        """
            Run the main feistel networks and rounds
        """
        for i in range(2):
            L = R0
            R = bin(int(self.keyFunc(R0, keys[i]), 2)^int(L0, 2))[2:].zfill(4)

            L0, R0 = L, R

        result = R + L
        result = ''.join([result[j] for j in inv_IP1])

        if self.encrypt:
            self.cipher_text = result
        else:
            self.plain_text  = result

    def populateInit(self, keys):
        """
            Run all the functions in order
        """
        L0, R0 = self.performIP1()
        self.mainRounds(L0, R0, keys)

def main(text, key, encrypt):
    """
        Calling the fuction and forming the keys
        returns a sdes object
    """
    round_keys = RoundKeys(key)
    round_keys.populateInit()

    keys = [round_keys.key1, round_keys.key2]

    if not encrypt:
        keys.reverse()

    sdes = SDES(text, encrypt)
    sdes.populateInit(keys)

    return sdes

if __name__ == "__main__":
    plain_text = '00011010'
    key        = '0110110101'

    sdes = main(plain_text, key, True)
