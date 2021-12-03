from hashlib import sha256 # For verifying the accuracy.

# Initial hash values to help seed the output.

# These words were obtained by taking the first thirty-two bits of the fractional parts of the square roots of the first eight prime numbers.
H_constants = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

# These words were obtained by taking the first thirty-two bits of the fractional parts of the cube roots of the first sixty-four prime numbers
K_constants = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

def SHA256(message): 
    # Implementation based on NIST.FIPS.180-4

    # Get the initial values
    K = K_constants
    H = H_constants

    # Pad the message to be multiples of 512 bits
    padded_message = Preprocess(message)    

    # Get the number of cycles needed
    N = len(padded_message) // 512     

    for i in range(1, N+1):        
        W = []

        # Prep only the portion of the message we are working on, in blocks of 512
        start = 512 * (i-1)
        end = 512 * i       
        W = Prep_Message_Schedule(padded_message[start : end], W)
                
        # Set the eight working variables by unpacking            
        a, b, c, d, e, f, g, h = H
        
        for t in range(64):
            # Cycle through the 64 base values, and move and shift and XOR and combine everything                     
            T_one = (h + Sigma_Upper(e, 6, 11, 25) + Choose(e, f, g) + K[t] + W[t] ) % (2 ** 32)
            
            T_two = (Sigma_Upper(a, 2, 13, 22) + Majority(a, b, c)) % (2 ** 32)
            
            h = g
            g = f
            f = e
            e = (d + T_one) % (2 ** 32)
            d = c
            c = b
            b = a
            a = (T_one + T_two) % (2 ** 32)             

        # Compute the ith intermediate hash value 
        H[0] = (a + H[0]) 
        H[1] = (b + H[1]) 
        H[2] = (c + H[2]) 
        H[3] = (d + H[3]) 
        H[4] = (e + H[4]) 
        H[5] = (f + H[5]) 
        H[6] = (g + H[6]) 
        H[7] = (h + H[7])        
    
    # Append the H values to form the final result.
    Final_Message = [format(x % (2 ** 32), '08x') for x in H]
    return ''.join(Final_Message)
                

def Left_Rotate(input, amount, bitSize=32):
    # Shift the input bits left by amount circularly and ensure no padding bits are added, bitwise OR that value with the input shifted to the right by the number of total bits
    # For Example: 11110000, 1 -> 11100001
    # For Example: 10101010, 1 -> 01010101
    # For Example: 11110000, 3 -> 10000111
    return (input << amount%bitSize) & (2**bitSize-1) | ((input & (2**bitSize-1)) >> (bitSize-(amount%bitSize)))

def Right_Rotate(input, amount, bitSize=32):
    # Shift the input bits right by amount circularly and ensure no padding bits are added, bitwise OR that value with the input shifted to the left by the number of total bits
    # For Example: 11110000, 1 -> 01111000
    # For Example: 10101010, 1 -> 01010101
    # For Example: 11110000, 3 -> 00011110
    return ((input & (2**bitSize-1)) >> amount%bitSize) | (input << (bitSize-(amount%bitSize)) & (2**bitSize-1))
 

def Right_Shift(input, amount, bitSize=32):
    # Shift the input bits right by amount and pad the left with 0's
    return (input >> amount) & (2**bitSize - 1)

def Choose(x, y, z):
    # For t values 0 -> 19
    # x input chooses if the output is based on y or z
    # For example: x= 1111, y= 1011, z= 0010 returns 1011
    # For example: x= 0000, y= 1011, z= 0010 returns 0010
    return (x & y) ^ (~x & z)

def Parity(x, y, z):
    # For t values 20 -> 39, 60 -> 79
    # Determines the parity of each bit of the three inputs
    # For Example: x= 1111, y= 1011, z= 0010 returns 0110
    return x ^ y ^ z

def Majority(x, y, z):
    # For t values 40 -> 59
    # Gives the Majority bit value by checking all three inputs - 1 if 2 or 3 bits are 1
    # For Example: x= 1111, y= 1011, z= 0010 returns 1011
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma_Upper(x, first, second, third):
    # XOR of right rotated input to jumble it
    return Right_Rotate(x, amount=first, bitSize=32) ^ Right_Rotate(x, amount=second, bitSize=32) ^ Right_Rotate(x, amount=third, bitSize=32)

def Sigma_Lower(x, first, second, third):
    # XOR of right rotated and right shifted input to jumble it
    return Right_Rotate(x, amount=first, bitSize=32) ^ Right_Rotate(x, amount=second, bitSize=32) ^ Right_Shift(x, amount=third, bitSize=32)


def Get_Bit_Count(message:str):
    # Gets the total number of bits in a string assuming 8 bits per byte, with one byte per letter
    return len(message.encode('ascii')) * 8

def get_binary_list(message:str)-> list:
    # convert the string to ascii bytes
    m_bytes = message.encode('ascii')
    # format the bytes into bits
    return [format(x, '08b') for x in m_bytes]

def Preprocess(message):
    # First pad the message to a length of a multiple of 512 bits
    bit_count = Get_Bit_Count(message)
        
    padding = (447 - bit_count) % 512
        
    bit_message = get_binary_list(message)    
    # Append a 1, then fill the rest with 0's until mod 512 by appending blocks of 8 zeros.          
    bit_message.append('1' + '0' * padding)
    # Finally append the length of the message in binary
    bit_message.append(format(bit_count, '064b'))    
    return ''.join(bit_message)
    
def Prep_Message_Schedule(input, schedule):
    for t in range(80):
        if t <= 15:
            # M_sub-t_exp-i
            # Grab blocks of 32 bits and ensure they are in binary and not string
            # 0->32, 32->64, ... , 448->480, 480->512
            start = 32 * t
            end = 32 * (t + 1)
            sub_block = input[start : end]
            schedule.extend([ int(sub_block, 2) ])
        else:
            # Add a jumbled version of the message onto the message schedule
            sig_1_256 = Sigma_Lower(schedule[t-2], 17, 19, 10)
            sig_0_256 = Sigma_Lower(schedule[t-15], 7, 18, 3)
            chunk = ( sig_1_256 + schedule[t - 7] +  sig_0_256 +  schedule[t-16] ) % (2 ** 32)
            schedule.append(chunk)
    return schedule


def Main():
    #myString = 'abc'
    myString = 'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq'    
    
    print(f'String to encode: {myString}\n\nImplementation:\n')    
    mySHA256 = SHA256(myString)
    print(mySHA256)
    print('\nLibrary Implementation:\n')
    libSHA1 = sha256()
    libSHA1.update(myString.encode("ASCII"))
    print(libSHA1.hexdigest())
    
    if (mySHA256 == libSHA1.hexdigest()):
        print("They match!")
    else:
        print("No match, something went wrong!")


if __name__ == "__main__":
    Main()
