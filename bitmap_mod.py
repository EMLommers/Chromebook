# Remove / Replace Bitmaps ChromeOS
# Chromebook ELM / OAK / HANA / ELM

# Howto:
# flashrom -p host -r firmware.rom
# cbfstool firmware.rom extract -n vbgfx.bin -f vbgfx.bin -m arm64
# (extract vbgfx.bin from firmware file)
# this file in same directory
# python3 ./bitmap_mod.py
# cbfstool firmware.rom remove -n vbgfx.bin
# cbfstool firmware.rom add -n vbgfx.bin -f vbgfx.bin -m arm64
# flashrom -p host -w firmware.rom

# V0.20
# Should work on locale_xx.bin and font.bin as well (not yet tested)


import struct
# Python program to modify the
# content of binary file
 
 
# Function to update the
# content of binary file
def update_binary(word, new):
    # string variable to store
    # each word after reading
    # from the file
    string = b""
 
    # Flag variable to check
    # if the record is found or
    # not
    Flag = 0
    pos = 0
    part = 0
    string = ""
    counter = 0
    # Open the file in r + b mode which means
    # opening a binary file for reading and
    # writing
    file = open('vbgfx.bin', 'rb+')
 
    while 1:   
 
        # Reading the content of the
        # file character by character
            value = file.read(1)
            if not value:
                 break

            byte_value = struct.unpack('B', value)[0]
            #print(f"Byte: {byte_value}")
            
            data = byte_value 

            # Looping till the end of
            # file is reached
   
 
           
 
            # checking the word read with
            # the word entered by user
            #print(string)
            if string == word:
	         # Moving the file pointer
	         # at the end of the previously
	         # read recor
                 print("Found..")
                 file.seek(pos+54)

                 # Updating the content of the file
                 for x in range(128*2):
                        file.write(b"\0")
	            
                 Flag = 1
                 pos = file.tell()
                 counter = counter+1
                 string = ""
                 continue
	    
            else:
                 # storing the position of
                 # current file pointer i.e. at
                 # the end of previously read record
                 pos = file.tell()
         
    
                 string += chr(data)
                 string = string[-2:]
                 continue
 
    file.close()

    if Flag:
        print("Record successfully updated")
        print(f"Found: {counter}")
    else:
        print("Record not found")
         
         
# Driver code
# Input the word to be found
# and the new word
word = "BM"
 
update_binary(word, new)