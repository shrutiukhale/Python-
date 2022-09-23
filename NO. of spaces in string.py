def check_space(string):
     
    # counter
    count = 0
     
    # loop for search each index
    for i in range(0, len(string)):
         
        # Check each char
        # is blank or not
        if string[i] == " ":
            count += 1
         
    return count
 
# driver node
string =input("string:")
# call the function and display
print("number of spaces ",check_space(string))
# OUTPUT: string:SHRUTIKA RAMDAS MUNDE number of spaces  2