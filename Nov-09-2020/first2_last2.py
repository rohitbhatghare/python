def str_fstlst(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(str_fstlst('Rohitbhatghare'))
print(str_fstlst('Ro'))
print(str_fstlst('B'))