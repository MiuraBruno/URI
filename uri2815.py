stingy = raw_input().split()
translate = ''
for b in stingy:
   if (b[0:2]) == (b[2:4]):
       translate = translate + b[2:] + ' '
   else:
       translate = translate + b + ' '
print(translate[:-1])
