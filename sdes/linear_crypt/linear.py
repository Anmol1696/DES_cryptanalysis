import sdes.sdes_cipher as SD

def returnSbox(bin_X, sbox):
    """
        For the given sbox and the value of X return the output of the sbox lookup
    """
    row_index = bin_X[0] + bin_X[3]
    col_index = bin_X[1:3]

    return sbox[int(row_index, 2)][int(col_index, 2)]

def NS(alpha, beta, sbox):
    """
        Returns the number of NS
    """
    ns      = 0
    alpha   = bin(alpha)[2:].zfill(4)
    beta    = bin(beta)[2:].zfill(2)

    for x in xrange(16):
        bin_x = bin(x)[2:].zfill(4)

        X = [int(bin_x[s]) & int(alpha[s]) for s in range(4)]
        S_x = bin(returnSbox(bin_x, sbox))[2:].zfill(2)
        Y = [int(S_x[t]) & int(beta[t]) for t in range(2)]

        X = X[0]^X[1]^X[2]^X[3]
        Y = Y[0]^Y[1]

        if X == Y:
            ns += 1

    return ns

def formNSTable(sbox):
    """
        Forms the table for the NS for all possible values of alpha and beta
        The table does not consider the value 0,0 for NS as answer is 0 only
    """
    ns_table = [[0 for x in range(3)] for x in range(15)]

    for alpha in xrange(1, 16):
        for beta in xrange(1, 4):
            ns_table[alpha-1][beta-1] = NS(alpha, beta, sbox) - 8

    return ns_table

def IO_Table(sbox):
    """
        Forms the Input output table for the sbox
    """
    io_table = [['0' for x in range(2)] for x in range(16)]
    
    for i in xrange(16):
        X = bin(i)[2:].zfill(4)
        Y = bin(returnSbox(X, sbox))[2:].zfill(2)
        io_table[i] = [X, Y]

    return io_table

if __name__ == "__main__":
    print "This is the Table"
    table = formNSTable(SD.SBox[0])
    io_table = IO_Table(SD.SBox[0])

    print 'NS_table------'
    for x in table:
        print x

    print 'IO table------'
    for x in io_table:
        print x
