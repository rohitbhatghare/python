def swap_char (str1,str2):
    a = str2[0:2] + str1[-1:]
    b = str1[0:2] + str2[-1:]
    return a + " " + b
print(swap_char("abc","xyz"))