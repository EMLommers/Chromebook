# Remove / Replace Bitmaps ChromeOS Python 3 file
# Replace and alter bitmaps

# Chromebook ELM / OAK / HANA / ELM

# Howto:
# flashrom -p host -r firmware.rom
# cbfstool firmware.rom extract -n vbgfx.bin -f vbgfx.bin -m arm64
# (extract vbgfx.bin from firmware file)
# this file in same directory
# python3 ./read_bin_file.py vbgfx.bin


# v0.1
# todo: extract, export, replace, alias, import


import struct
import os
import sys
# Python program to modify the
# content of binary file
 
 
# Function to update the
# content of binary file
def update_binary(command_array):
    #print (command_array)
    command = "plutonium"
    dirfile = ""
    debug = ""
    argnum = command_array.split(',')
    argnum_cnt = len(argnum)-1
    argvalues = 'file_path, command, dirfile, debug'
    #print (argvalues)
    argstr = argvalues.split(',')
    for putvar in range(argnum_cnt):
        argstr[putvar] = argstr[putvar].replace("'","").replace(" ","")
        globals()[argstr[putvar]] = str(argnum[putvar+1].replace("'","").replace(" ","").replace("[","").replace("]",""))
    #   print(argstr[putvar])
    # string variable to store
    # each word after reading
    # from the file
    Flag = 0
    pos = 0
    part = 0
    string = magic= ""
    counter = 0
    file_name = []
    file_size = []
    file_offset = []
    # Open the file in r + b mode which means
    # opening a binary file for reading and
    # writing
    
    # Replace 'your_file_path' with the actual file path
    #file_path = 'your_file_path'

    print ("File   :",file_path)
    try:
        file_path_size = os.path.getsize(file_path)
    #    print(f"File Size in Bytes is {file_size}")
    except FileNotFoundError:
        print("File not found.")
    except OSError:
        print("OS error occurred.")
    
    if file_path_size < 10:
       print ("Invalid archive..")
       exit
    
    file = open(file_path, 'rb+')
 
    while 1:   
 
        # Reading the content of the
        # file character by character
       
        value = file.read(1)
        if not value:
           exit
        cur_pos = file.tell()
        byte_value = struct.unpack('B', value)[0]
        data = byte_value
        #print(f"Byte: {byte_value}")
    
        # checking file magic
        if cur_pos <= 4:
           magic += chr(data)
    
        if cur_pos == 4:
           if magic != "CBAR":    
              print ("This is not a Coreboot Archive..")
              print (magic)
              exit
           else:    
                cbar_file_version =  int.from_bytes(file.read(4), byteorder='little')      
                cbar_file_size =  int.from_bytes(file.read(4), byteorder='little') 
                cbar_file_count  = int.from_bytes(file.read(4), byteorder='little') 
               
                if dirfile == "debug" or debug == "debug":
                   print ("MAGIC : ",magic)
           
                   print ("OFFSET: ",file.tell())
                  
                   print ("VERSION: ",cbar_file_version)
                   print ("SIZE   : ",cbar_file_size) 
                   print ("COUNT  : ",cbar_file_count)
               
           match command:
                  case "list":
                         print ("Action : Show content")
                         print ("")
                         if cbar_file_count > 0:  
                             for count in range(cbar_file_count):
                                name = ""
                                for name_length in range(32):
                                    value =  (struct.unpack('B', file.read(1))[0])
                                    if value == 0:
                                       name  += chr(32) 
                                       continue
                                    else:
                                       name += chr(value)      
                                       continue
                                file_name.append(name) # = name
                                file_offset.append(struct.unpack('i',file.read(4)))
                                file_size.append(struct.unpack('i',file.read(4)))
                                # print ("COUNTNR: ",count)
                                if count == 0:
                                   print ("Archive contents:")
                                   print ("-----------------------")
                                print_len = str(str(count+1) +"   "+ (file_name[count] + "  Offset: " + str(file_offset[count]) + "   Size: " + str(file_size[count])))
                                print_len = print_len.replace("(","")
                                print_len = print_len.replace(")","")
                                print_len = print_len.replace(",","") 
                                print (print_len)
                                
                         if count < 1 or cbar_file_count == 0:
                            print ("Empty archive")
                         break   
                             
                             
                  case "export":
                     exit
                  case "extract":
                     exit
                  case "import":
                     exit
                  case "alias":
                     exit
                  case "build":
                     exit
                  case "replace":
                     exit                  
                  case _:
                     print ("Not a valid choice.")
                     print ("read_bin_file.py chromeos-bin-file action [filedir] [filedir2]")
                     print ()
                     print ("action = list | export | extract | import | alias | build | replace")
                     print ("filedir1 && filedir2 not needed when using 'list'")
                     print ("Still in development... only list working")
                     break
                        
                     
    # Looping till the end of
    # file is reached
    

    file.close()
    exit

         
# Driver code
# Input the word to be found
# and the new word
print ("Edit content of ChromeOS firmware bitmaps")
print ("v0.2 2023 by Ernst M. Lommers")
print() 
names = str(sys.argv)

update_binary(names)
