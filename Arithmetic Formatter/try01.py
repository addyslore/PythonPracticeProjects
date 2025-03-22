txt = ["321 + 89", "56 - 413", "329 + 67", "523 - 49", "45 + 525"]
new_txt = ''
for i in txt:
    new_txt +=' '+ i.replace(' ','')

result = []
result=new_txt
result_1= result.split()     

new_list=[]

for i in result_1:
    if '+' in i:
        a=i.split('+')
        new_list.append(a)
    elif '-' in i:
        b=i.split('-')
        new_list.append(b) 
    else:
        print('Error: Operator must be '+' or '-'.')

new_list_firstline=[]
new_list_secondline=[]

for i in new_list:
    new_list_firstline.append(i[0])
    new_list_secondline.append(i[1])

print(new_list_firstline)
print(new_list_secondline)    

third_line=[]

for i in range(len(new_list_firstline)):
    third_line.append(int(new_list_firstline[i])+int(new_list_secondline[i]))

print(third_line)