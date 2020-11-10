def ocuur_val(str):
  char = str[0]
  str = str.replace(char, '$')
  str = char + str[1:]

  return str

print(ocuur_val('restart'))