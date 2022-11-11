# Lucas Wenger
# Coding Theory Program
# SECTION 1 NOT USED IN FINAL PROJECT
# SECTION 2 IS CODE FROM PREVIOUS ASSIGNMENT -- SOME PARTS MAY HAVE BEEN MODIFIED OR IMPROVED
# SECTION 3 IS NEW CODE
# The final function at the end of section 3 is used to compare the Hamming and RS codes using the same message.
# NOTE: Test cases were thought of and tested using Hamming w/o Huffman, for simplicity's sake.
# Test code that highlights Hamming:
    # Use: "Groovy shoes, man!"
    # Hamming block size: 16
    # RS extra characters: 100 (can do any number less, as well -- it's just big to make a point)
    # ERRORS: Every 16 bits, induce an error (i.e., 0, 16, 32, etc.) -- start anywhere in first 8 bits (index 0-7)
    # Comments:
        # This highlights Hamming code because the errors are spread out, which is where Hamming really shines. You can see that the Hamming block size is
        # somewhat robust, at 16 characters/block, but the RS code is really quite robust. You don't really need to input all those errors to see that, even
        # though RS has 100 extra characters, and therefore can correct 50 of them, the 59 errors that this error rate throws at it would still be too much to
        # handle. Meanwhile, the pretty average 16-block Hamming code can handle this. If the blocks were 8 bits instead, it would have room for twice as many
        # errors. additionally, for this sort of spread-out error, Hamming can get the message across with more errors handles and with far more efficiency
        # than RS. One reason for this is that, by nature, RS can never correct half of its characters or more. As the extra characters grow, the proportion
        # of characters that can be corrected converges to 1/2, but never quite gets there. This example disrupts exactly half of the characters (or more if
        # there are an odd number of characters), so no RS code will ever be able to correct this. 
# Test code that highlights Reed-Solomon:
    # Use: "Radical kicks, my dude!"
    # Hamming block size: 16
    # RS extra characters: 4
    # ERRORS: First 16 bits (i.e., 0, 1, 2, 3,...,15) -- or any run of 9 bits
    # Comments:
        # This test highlights RS code because it includes one big burst error. These burst errors are the strength of RS codes. In this case, only a single
        # large burst error was used both to save the fingers of whoever is inputting the errors into this tedious program (Really, the programmer should have
        # made it easier to input errors! This is just a slogfest.) and to demonstrate the potential for RS code to handle a huge number of errors with only 4
        # extra characters added on to the end (that is, 32 extra bits). In a way, this wasn't too bad for the Hamming code either, since the first two blocks
        # picked up all of the errors. If the errors were in smaller bursts throughout the code and the RS code had a few more extra characters, the difference
        # would be more pronounced, since Hamming can only handle a single error in any given block. If the errors were in burst of two or three or four all around,
        # that would not be good for the Hamming code, but since RS can correct characters (that is, 8 bit groups), it would be able to correct far more with less
        # redundancy.
# So, to summarize, Test 1 emphasizes Hamming's strength for dealing with single bit errors spread throughout the code, and Test 2 demonstrates RS's ability to deal
# with massive burst errors with minimal redundancy. They both have their strengths and uses, though since burst errors appear to be a little more common in real
# life, RS may have a little leg up on Hamming. 

import math
import reedsolo as rs

#------------------------------------------------------------------------- SECTION 1 ----------------------------------------------------------------------
'''
def hammingencode(binstring):
    # Make sure string is properly formatted
    try:
        bs = str(binstring)
    except:
        print("ERROR: input must be string")
        return
    if len(binstring) != 11:
        print("ERROR: input string must be 11 bits long")
        return
    for bit in binstring:
        if bit not in ["0","1"]:
            print("ERROR: input string must contain only binary digits")
            return
    # Now we know string is properly formatted
    # Make and fill array
    bs = [int(bit) for bit in bs]
    binsquare = [[0, 0, 0, bs[0]],
                 [0, bs[1], bs[2], bs[3]],
                 [0, bs[4], bs[5], bs[6]],
                 [bs[7], bs[8], bs[9], bs[10]]]
    # Col parity checks
    for parcheck in [1,2]:
        tempsum = 0
        for row in range(4):
            for col in [parcheck,3]:
                tempsum += binsquare[row][col]
        binsquare[0][parcheck] = tempsum % 2
    # Row parity checks
    binsquare[1][0] = sum(binsquare[1]+binsquare[3]) % 2
    binsquare[2][0] = sum(binsquare[2]+binsquare[3]) % 2
    binsquare[0][0] = sum(binsquare[0]+binsquare[1]+binsquare[2]+binsquare[3]) % 2
    # Output new code
    encodedstring = ""
    for row in binsquare:
        for bit in row:
            encodedstring += str(bit)
    return encodedstring


def hammingdecode(binstring):
    # Make sure string is properly formatted
    try:
        bs = str(binstring)
    except:
        print("ERROR: input must be string")
        return
    if len(binstring) != 16:
        print("ERROR: input string must be 16 bits long")
        return
    for bit in binstring:
        if bit not in ["0","1"]:
            print("ERROR: input string must contain only binary digits")
            return
    # Now we know string is properly formatted
    # Create binlist
    binlist = [int(bit) for bit in bs]
    # Check for errors
    enumbinlist = enumerate(binlist)
    totalxor = 0
    for item in enumbinlist:
        if item[1] == 1:
            totalxor = totalxor^item[0]
    if totalxor == 0: # Check for 0 errors
        if sum(binlist) % 2 != 0:
            print("Error detected in index 0")
            return
        print("No errors detected!")
        return
    else:
        if sum(binlist) % 2 == 0:
            print("Two errors detected") # Check for 2 errors
            return
        else:
            print("Error detected in index " + str(totalxor)) # Check for 1 error
            return
'''

#------------------------------------------------------------------------- SECTION 2 ----------------------------------------------------------------------

# SECOND PYTHON ASSIGNMENT
# Contains helper functions, Huffman code class and functions, and complete Hamming code WITH Huffman

# Helper function
def splitlist(lyst, splitlength):
    # Takes a list as an argument and returns the same list, split into sublists of length splitlength
    splitlength = int(splitlength)
    if type(lyst) != list:
        print("ERROR: arg type must be list")
        exit()
    if len(lyst) % splitlength != 0:
        print("ERROR: length of list must be divisible by splitlength")
        exit()
    numlists = int(len(lyst)/splitlength)
    newlyst = [[] for i in range(numlists)]
    counter = 0
    for l in range(numlists):
        newlyst[l] = lyst[counter:splitlength+counter]
        counter += splitlength
    return newlyst


def ispwroftwo(num):
    # If num is a power of two, returns True. Otherwise, returns False.
    onecount = 0
    for bit in str(bin(num)):
        if bit == '1':
            onecount += 1
    if onecount == 1:
        return True
    else:
        return False



def hammingerrorfix(binstring):
    # Make sure string is properly formatted
    try:
        bs = str(binstring)
    except:
        print("ERROR: input must be string")
        return
    for bit in binstring:
        if bit not in ["0","1"]:
            print("ERROR: input string must contain only binary digits")
            return
    # Now we know string is properly formatted
    # Create binlist
    binlist = [int(bit) for bit in bs]
    # Check for errors
    enumbinlist = enumerate(binlist)
    totalxor = 0
    for item in enumbinlist:
        if item[1] == 1:
            totalxor = totalxor^item[0]
    if totalxor == 0: # Check for 0 errors
        if sum(binlist) % 2 != 0:
            binlist[0] = abs(binlist[0]-1)
            return binlist # return list of ints
        return binlist
    else:
        if sum(binlist) % 2 == 0:
            print("Two errors detected in block. Unable to fix.") # Check for 2 errors
            return binlist
        else:
            binlist[totalxor] = abs(binlist[totalxor]-1) # Fix single error
            return binlist # return list of ints


def fullhammingdecode(binstring):
    binlist = hammingerrorfix(binstring) # list of ints, single block
    # Now we just have to remove the parity checks
    binstring = ''
    for digit in range(len(binlist)):
        if not ispwroftwo(digit) and not digit == 0:
            binstring += str(binlist[digit])
    # binstring contains all non-parity bits
    return binstring


#class to help out with Huffman Code function
class HuffmanTree():
    def __init__(self):
        self.tree = {}
        self.code = {}
        '''
        self.tree['Example'] = {
            'parent' : None,
            'children' : [],
            'value' : '0'
            }
        '''
        
    def add_branch(self, name, parent, children, value):
        if name in self.tree:
            print("ERROR: object " + name + " already in tree")
            exit()
        if children == None:
            children = []
        self.tree[name] = {'parent' : parent, 'children' : children, 'value' : value}
        return self
    
    def add_code(self, name, code):
        if name in self.code:
            print("ERROR: object " + name + " already in code")
            exit()
        self.code[name] = code
        return self
    
    def construct_dict(self):
        for branch in self.tree:
            if self.tree[branch]['children'] == []: # if branch has no children (if branch is a char)
                lettercode = ''
                tempname = branch
                while self.tree[tempname]['parent']: # while branch has a parent
                    if self.tree[tempname]['value'] == None:
                        print("ERROR: child of " + tempname + " has no value :(")
                        exit()
                    lettercode = self.tree[tempname]['value'] + lettercode # add value to lettercode
                    tempname = self.tree[tempname]['parent'] # switch to parent)
                self.add_code(branch, lettercode)
        return self.code


# Take a message, return a dictionary containing Huffman codewords
def huffmancode(message):
    # Make sure message is string
    try:
        msg = str(message).lower()
    except:
        print("ERROR: input must be string")
        return
    # Message is good
    # Make dictionary showing letter frequencies
    frequencydict = dict.fromkeys(msg, 0)
    for char in msg:
        frequencydict[char] += 1
    # Make tree (dictionary)
    bintree = HuffmanTree()
    if len(frequencydict) == 1: # If the message is made of only 1 char
           bintree = {message[0]:0}
           return bintree
    while len(frequencydict) > 1: #else
        # Store 2 lowest values in variables as tuples, delete from dictionary
        lowestfreq1 = min(frequencydict.items(), key = lambda x:x[1])
        del frequencydict[lowestfreq1[0]]
        lowestfreq2 = min(frequencydict.items(), key = lambda x:x[1])
        del frequencydict[lowestfreq2[0]]
        workingvals = [lowestfreq1[0], lowestfreq2[0]]
        # add_branch(self, name, parent, children, value)
        for value in workingvals:
            if len(value) == 1: # if value is a char rather than a branch
                bintree.add_branch(value, None, None, None)
            if value == workingvals[0]: # if we are working with lowestfreq 1, value = '1'
                bintree.tree[value]['value'] = '1'
            elif value == workingvals[1]: # same as above, but with lowestfreq 2
                bintree.tree[value]['value'] = '0'
            else: # if our workingval doesn't match either of the above, something is wrong
                print("ERROR: value assignment non working for " + value)
                exit()
        # combine branches
        # add combined branch to freqencydict
        frequencydict[lowestfreq1[0] + lowestfreq2[0]] = lowestfreq1[1] + lowestfreq2[1]
        # add combined branch to bintree
        bintree.add_branch(lowestfreq1[0] + lowestfreq2[0], None, [lowestfreq1[0], lowestfreq2[0]], None)
        # make parent of workingvals
        for value in workingvals:
            bintree.tree[value]['parent'] = lowestfreq1[0] + lowestfreq2[0]
    return bintree.construct_dict()
    

def huffmandecode(bits, huffmandictionary):
    huffmandecoderdict = {value:key for key, value in huffmandictionary.items()}
    outputmsg = ''
    currentcodeword = ''
    for bit in bits:
        currentcodeword += bit
        if currentcodeword in huffmandecoderdict: # If extra 0s match with chars, we'll just have to deal with that
            outputmsg += huffmandecoderdict[currentcodeword]
            currentcodeword = ''
    if '1' not in currentcodeword: # Gets rid of any extra 0s
        currentcodeword = ''
    if currentcodeword != '':
        print("\nERROR: excessive noise caused an error in decoding -- some data missing or incorrect\n")
    print("The translation of this code is: \n" + outputmsg)
    return outputmsg


def completehammingwithhuffman(message):
    # Takes any message, stores as any proper bit Hamming code, asks if you want to
    # flip any bits, corrects code. 
# DECIDE HAMMING TYPE
    # Make sure message is string
    try:
        msg = str(message).lower()
    except:
        print("ERROR: input must be string")
        return
    # Message is good
    # Ask what kind of Hamming code to use
    totalbits = 0
    pwroftwo = False
    while not pwroftwo:
        totalbits = input("How many bits should be in each block of Hamming code? \n")
        # Make sure number entered is an integer
        try:
            totalbits = int(totalbits)
        except:
            print("ERROR: bits must be an integer")
            continue
        # Make sure number entered is at least 4
        if totalbits < 4:
            print("ERROR: bits must be at least 4")
            continue
        # Make sure number entered is a power of two
        if ispwroftwo(totalbits):
            pwroftwo = True
        else:
            print("ERROR: bits must be a power of two")
            continue
    paritybits = math.log(totalbits, 2) + 1
    messagebits = totalbits - paritybits
    # Now we have totalbits = a multiple of two, paritybits, and messagebits
    # We can translate our message into numbers and put it into a matrix
# GET DICT
    huffmandict = huffmancode(msg) # Get huffman dictionary for codewords
    print(huffmandict) # FOR TESTING
    # Now we can encode our message
# ENCODE
    ciphertext = ''
    for char in msg:
        ciphertext += huffmandict[char]
    # Our coded message is contained in ciphertext
    while len(ciphertext) % messagebits != 0:
        ciphertext += '0' # Add zeros to make message fit coding scheme
    cipherlist = splitlist(list(ciphertext), messagebits)
    # cipherlist is now a large list split into sublists; we just have to add parity bits
    newcipherlist = []
    for block in cipherlist:
        block = [int(bit) for bit in block]
        block.insert(0, 0) # insert pos 0 parity check
        for bit in range(totalbits):
            if ispwroftwo(bit): # insert remaining parity bits
                block.insert(bit, 0)
        # Now we have all of our blank parity bits in place; we can label them correctly
        for bit in range(totalbits):
            temppartotal = 0
            if ispwroftwo(bit):
                for i in range(bit,2*bit):
                    temppartotal += sum(block[i::2*bit])
            if temppartotal % 2 == 1:
                block[bit] = 1 # if total is odd, set bit equal to 1, making it even
        if sum(block) % 2 == 1: # set final overall parity bit
            block[0] = 1
        newcipherlist.append(block)
    # We now have each block correctly labeled with parity bits
    # Our encoding is done
    finalcode = ''
    for block in newcipherlist:
        for bit in block:
            finalcode += str(bit)
    #finalcode is set up
# FLIP BITS
    print("Your encoded message is: \n" + finalcode)
    user = ''
    while user != 'n':
        whichbit = ''
        print("\nThere are " + str(len(finalcode)) + " bits.\n")
        while user not in ['y','n']:
            user = input("Would you like to flip a bit? [y/n]\n")
        if user == 'y': # Flip a bit
            while whichbit not in range(len(finalcode)):
                whichbit = input("Which bit index would you like to flip?\n")
                try:
                    whichbit = int(whichbit)
                except:
                    print("Please enter an integer.\n")
            # whichbit = bit index to be flipped
            # flip bit in string
            finalcode = finalcode[:whichbit] + str(abs(int(finalcode[whichbit])-1)) + finalcode[whichbit+1:]
            print("Your new encoded message is: \n" + finalcode)
            user = ''
# DECODE
    print("\nThe program will now attempt to decode the message.\n")
    #Note that the only information carried over is final code, size of Hamming blocks, and Huffman dict
    stringblocks = splitlist(list(finalcode), totalbits)
    for i in range(len(stringblocks)):
        stringblocks[i] = fullhammingdecode(''.join(stringblocks[i]))
    # each item in stringblocks is a string of corrected messagebits characters
    # Now, stringblocks is a list of totally corrected code. We can just join it.
    msgtodecode = ''.join(stringblocks)
    # msgtodecode is a single string, ready to be decoded using the dictionary huffmandict
    return huffmandecode(msgtodecode, huffmandict)
    
    
'''    
# COMMENTS ON RELIABILITY
#Overall, I think this is a very versatile program, especially if you have some idea of how many
#errors you will be encountering. It allows you to set the size of your Hamming blocks to whatever
#power of 2 you want. By doing this, it can greatly increase either its error correcting ability
#or its efficiency. For high levels of noise, you could go with a 16 bit Hamming code, or even an
#8 bit or 4 bit. This means the code can handle without issue, on average, 1 error per (16, 8, or 4)
#bits. I think the biggest issues with this implementation are the inability to correct two errors,
#though that is really just a part of having a Hamming Code. The other big issue is the way it deals
#with putting code into even Hamming blocks. Right now, it just pads the end with zeros. This could
#result in some additional repeated characters at the end of the output. It isn't a major issue, but
#it is an issue. The other problem is if a Hamming block has such dense errors that either don't yield an
#actual codeword. This could mess up the translation of a whole message. Granted, the program may
#tell you that the translation was messed up if it ends on a node with a 1 in the path to it, but the
#output probably would mess up multiple words. And besides, since every combination of 0s and 1s leads to
#a codeword if it goes long enough, there is also a good chance that an encorrected error may just mess
#up a large chunk of code. Since errors could still lead to actual codewords, they may be difficult to
#correct in Huffman Code without some semantic analysis component. You could probably improve the error
#warning system by coming up with an alternative method of making the code fit the Hamming structure.
#Then you could notify the user that there was a transmission error if the code ends on any non-character
#node (rather than a non-character node with a 1 in the path to it).
#But, I would say it is a very versatile implementation of Hamming Code, able to hold up as well as any
#Hamming code can to various amounts of noise, thanks to the adjustable size of the Hamming blocks. It
#can also be as efficient as the user desires, and is already fairly efficient, especially for larger
#chunks of text, since it uses the Huffman Code. The maximum number of errors it can handle perfectly is
#equal to the number of Hamming blocks, with lower-bit blocks being less efficient but more error resistant.
#Of course, if you don't know how many errors are coming, it would be best to use as resistant a code as
#you can afford to. Thanks to the ability to pick how big your blocks are in this code, this is made quite
#easy!
'''

#------------------------------------------------------------------------- SECTION 3 ----------------------------------------------------------------------

# ADDITIONS FOR FINAL PYTHON ASSIGNMENT
# Includes code for RS encoding and decoding, as well as a function to do both Hamming and RS on the same text.
# NOTE: Also includes version of Hamming without Huffman, since it's easier to compare directly to RS and doesn't have the issue with padded zeros at the end.
# (For Hamming w/ Huffman, I didn't find a good way to remove zeros used to pad the end so it would fit Hamming size, so it may produce extra characters)
# Hamming version with Huffman can be used instead if desired. The code is found above.

def completereedsolomon(message):
# CHECK FOR ERRORS
     # Make sure message is string, store in msg
    try:
        msg = str(message)
    except:
        print("ERROR: input must be string")
        return
    # Message is good
# DECIDE ON REDUNDANCY
    # Ask how many characters to add to code
    rscvalisint = False
    while not rscvalisint:
        rscval = input("How many characters of redundancy would you like to add?\n")
        try:
            rscval = int(rscval)
        except:
            print("ERROR: input must be an integer")
            continue
        rscvalisint = True
# ENCODE
    # Create the Codec
    rsc = rs.RSCodec(rscval)
    # Store encoded message
    encodedmsg = rsc.encode(bytes(msg,'utf-8'),rscval)
    # Store binary in list
    binlist = [bin(x).replace("0b","") for x in encodedmsg]
    # Make sure each element has length 8; pad front with zeros
    for i in range(len(binlist)):
        while len(binlist[i]) != 8:
            binlist[i] = '0' + binlist[i]
    # Create final binary string to transmit
    finalcode = ''
    for charbin in binlist:
        finalcode += charbin
# FLIP BITS
    print("Your encoded message is: \n" + finalcode)
    user = ''
    while user != 'n':
        whichbit = ''
        print("\nThere are " + str(len(finalcode)) + " bits.\n")
        while user not in ['y','n']:
            user = input("Would you like to flip a bit? [y/n]\n")
        if user == 'y': # Flip a bit
            while whichbit not in range(len(finalcode)):
                whichbit = input("Which bit index would you like to flip?\n")
                try:
                    whichbit = int(whichbit)
                except:
                    print("Please enter an integer.\n")
            # whichbit = bit index to be flipped
            # flip bit in string
            finalcode = finalcode[:whichbit] + str(abs(int(finalcode[whichbit])-1)) + finalcode[whichbit+1:]
            print("Your new encoded message is: \n" + finalcode)
            user = ''
# DECODE
    print("\nThe program will now attempt to decode the message.\n")
    # Note that the only information carried over is the final code
    # Turn into list and split into sublists of length 8
    finallist = list(finalcode)
    finallist = splitlist(finallist, 8)
    # Combine sublists into strings
    for listnum in range(len(finallist)):
        finallist[listnum] = "".join(finallist[listnum])
    # Turn binary numbers into decimal numbers
    finallist = [int(num,2) for num in finallist]
    # So, now finallist is a list of numbers in decimal
    # Now, we decode with the built in rs function and output the message
    try:
        decodedmsg = rsc.decode(finallist)
    except:
        print("ERROR: too many errors detected to decode")
        return
    # Just message
    jstmsg = [chr(num) for num in decodedmsg[0]]
    # Message + chars
    msgandchar = [chr(num) for num in decodedmsg[1]]
    # Output message
    print("The decoded message is: \n" + "".join(jstmsg))
    print("\n(w/ extra characters: " + "".join(msgandchar) + ")")
    return("".join(jstmsg))


def completehamming(message):
    # Hamming encoding that uses ASCII values instead of Huffman Code
    # DECIDE HAMMING TYPE
    # Make sure message is string
    try:
        msg = str(message)
    except:
        print("ERROR: input must be string")
        return
    # Message is good
    # Ask what kind of Hamming code to use
    totalbits = 0
    pwroftwo = False
    while not pwroftwo:
        totalbits = input("How many bits should be in each block of Hamming code? \n")
        # Make sure number entered is an integer
        try:
            totalbits = int(totalbits)
        except:
            print("ERROR: bits must be an integer")
            continue
        # Make sure number entered is at least 4
        if totalbits < 4:
            print("ERROR: bits must be at least 4")
            continue
        # Make sure number entered is a power of two
        if ispwroftwo(totalbits):
            pwroftwo = True
        else:
            print("ERROR: bits must be a power of two")
            continue
    paritybits = math.log(totalbits, 2) + 1
    messagebits = totalbits - paritybits
    # Now we have totalbits = a multiple of two, paritybits, and messagebits
    # We can translate our message into numbers and put it into a matrix
# ENCODE
    ciphertext = ''
    for char in msg:
        binchar = bin(ord(char)).replace("0b", "")
        while len(binchar) != 8:
            binchar = "0" + binchar
        ciphertext += binchar
    # Our coded message is contained in ciphertext
    while len(ciphertext) % messagebits != 0:
        ciphertext += '0' # Add zeros to make message fit coding scheme
    cipherlist = splitlist(list(ciphertext), messagebits)
    # cipherlist is now a large list split into sublists; we just have to add parity bits
    newcipherlist = []
    for block in cipherlist:
        block = [int(bit) for bit in block]
        block.insert(0, 0) # insert pos 0 parity check
        for bit in range(totalbits):
            if ispwroftwo(bit): # insert remaining parity bits
                block.insert(bit, 0)
        # Now we have all of our blank parity bits in place; we can label them correctly
        for bit in range(totalbits):
            temppartotal = 0
            if ispwroftwo(bit):
                for i in range(bit,2*bit):
                    temppartotal += sum(block[i::2*bit])
            if temppartotal % 2 == 1:
                block[bit] = 1 # if total is odd, set bit equal to 1, making it even
        if sum(block) % 2 == 1: # set final overall parity bit
            block[0] = 1
        newcipherlist.append(block)
    # We now have each block correctly labeled with parity bits
    # Our encoding is done
    finalcode = ''
    for block in newcipherlist:
        for bit in block:
            finalcode += str(bit)
    #finalcode is set up
# FLIP BITS
    print("Your encoded message is: \n" + finalcode)
    user = ''
    while user != 'n':
        whichbit = ''
        print("\nThere are " + str(len(finalcode)) + " bits.\n")
        while user not in ['y','n']:
            user = input("Would you like to flip a bit? [y/n]\n")
        if user == 'y': # Flip a bit
            while whichbit not in range(len(finalcode)):
                whichbit = input("Which bit index would you like to flip?\n")
                try:
                    whichbit = int(whichbit)
                except:
                    print("Please enter an integer.\n")
            # whichbit = bit index to be flipped
            # flip bit in string
            finalcode = finalcode[:whichbit] + str(abs(int(finalcode[whichbit])-1)) + finalcode[whichbit+1:]
            print("Your new encoded message is: \n" + finalcode)
            user = ''
# DECODE
    print("\nThe program will now attempt to decode the message.\n")
    #Note that the only information carried over is final code and size of Hamming blocks
    stringblocks = splitlist(list(finalcode), totalbits)
    for i in range(len(stringblocks)):
        stringblocks[i] = fullhammingdecode(''.join(stringblocks[i]))
    # each item in stringblocks is a string of corrected messagebits characters
    # Now, stringblocks is a list of totally corrected code. We can just join it.
    msgtodecode = ''.join(stringblocks)
    # msgtodecode is a single string
    # Now, we remove exra 0s at the end
    while len(msgtodecode) % 8 != 0:
        msgtodecode = msgtodecode[:-1]
    # Now, we remove any full words made up of 0s, since that is a non-keyboard character
    while msgtodecode[-8] == "00000000":
        msgtodecode = msgtodecode[:-8]
    # NOTE: If the message is completely corrected, this will remove all extra characters. If there is an error in the 0s added at the end that is uncorrected, extra characters
    # could be added, but since there were already errors in that block that went uncorrected, it may be messed up anyway.
    # Put message into list and split message into sublists of length 8
    decodedlist = splitlist(list(msgtodecode),8)
    # Combine sublists into strings
    for listnum in range(len(decodedlist)):
        decodedlist[listnum] = "".join(decodedlist[listnum])
    # Convert to chars
    decodedlist = [chr(int(num,2)) for num in decodedlist]
    print("The decoded message is: \n" + "".join(decodedlist))
    return("".join(decodedlist))
    

def comparecodes(message):
    # Use to compare Hamming and RS with one function -- basically the culmination of the whole program
    print("HAMMING CODE\n")
    user = ''
    while user not in ['1','2']:
        user = input("Would you prefer to use Hamming code:\n" +
                     "1. Without Huffman encoding (using ASCII values), or\n" +
                     "2. With Huffman encoding? [1/2]\n")
    if user == '1':
        hamout = completehamming(message)
        huff = "w/o Huffman"
    elif user == '2':
        hamout = completehammingwithhuffman(message)
        huff = "w/ Huffman"
    print("\nREED-SOLOMON CODE\n")
    rsout = completereedsolomon(message)
    print("\nYour output message from Hamming " + huff + " is: \n" + hamout)
    print("\nYour output message from Reed-Solomon is: \n" + rsout)
    return
    
    
