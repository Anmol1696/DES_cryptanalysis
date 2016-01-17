PC_1 = [[9, 7, 3, 8, 0],
        [2, 6, 5, 1, 4]]

PC_2 = [3, 1, 7, 5, 0, 6, 4, 2]

class RoundKeys:
    """
        consisting of all the functions for round keys for SDES
    """
    def __init__(self, key):
        self.str_key    = key
        self.int_key    = int(key, 2)
        self.key1       = None
        self.key2       = None

    def performPC1(self):
        """
            Perform the first permutation to output C0 and D0
            C0 is the left side of the key and the D0 is the right side
        """
        C0, D0 = ''.join([self.str_key[i] for i in PC_1[0]]), ''.join([self.str_key[i] for i in PC_1[1]])

        return (C0, D0)

    def leftShift(self, C, D, shift):
        """
            Perform left shift on the left and right parts of the key in round
            Here C is the left side of the key and D is the right side of the key

            shift is 1 or 2 depending on how much left shift is needed
        """
        C, D = C[(1*shift):] + '0'*shift, D[(1*shift):] + '0'*shift

        return (C, D)

    def performPC2(self, C, D):
        """
            From the C, D form the final key of 8 bit using the PC2 table
        """
        combination = C + D
        combination = ''.join([combination[i] for i in PC_2])

        return combination

    def populateInit(self):
        """
            Form the keys 1, 2 and fill them in object of class
        """
        C, D = self.performPC1()
        C, D = self.leftShift(C, D, 1)
        self.key1 = self.performPC2(C, D)

        C, D = self.leftShift(C, D, 2)
        self.key2 = self.performPC2(C, D)

if __name__ == "__main__":
    """
        Testing
    """
    key = '1111111111'
    key_obj = RoundKeys(key)
    key_obj.populateInit()

    print "Key1 -> \n", key_obj.key1
    print "Key2 -> \n", key_obj.key2
