txt = ["321 + 89", "56 - 413", "329 + 67", "523 - 49", "45 + 525"]
new_txt = []
for i in txt:
    new_txt += i.split(',')

print(new_txt)

soln=[]
#for i in txt:
    #if '+' in i:
      #  a=i.split('+')
     #   soln.append(int(a[0])+int(a[1]))
    #elif '-' in i:
    #    b=i.split('-')
   #     soln.append(int(b[0])-int(b[1])) 
  #  else:
 #       print('Error: Operator must be "+" or "-".')
#
#print(soln)        

first_line=''
for i in txt:
    if '+' in i:
        a=i.split('+')
        first_line += '  '+ a[0] + '    '
    elif '-' in i:
        b=i.split('-')
        first_line += '  ' + b[0] + '    '

print(first_line)        

second_line=''
for i in txt:
    if '+' in i:
        a=i.split('+')
        second_line += '+ ' + a[1] + '    '
    elif '-' in i:
        b=i.split('-')
        second_line += '- ' + b[1] + '    '

print(second_line)   

print('-----    -----    -----    -----    -----')

third_line=''
for i in txt:
    if '+' in i:
        a=i.split('+')
        third_line+= '  ' + str(int(a[0]) + int(a[1])) + '    '
    elif '-' in i:
        b=i.split('-')
        third_line+= '  ' + str(int(b[0]) - int(b[1])) + '    '
    else:
        print('Error: Operator must be "+" or "-".')

print(third_line)        