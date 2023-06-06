# def centre (width=70):
#    file = open("C:/Users/MSI/Desktop/text.txt","r")
#    rud_file = file.read()

#    for line in rud_file:
#       print (rud_file)

# # ВЫвод содерж файла
# file = open("C:/Users/MSI/Desktop/text.txt","r")
# rud_file = file.read()
# print (rud_file)

# Перезапись из файла в другой файл
file1 = open("C:/Users/MSI/Desktop/text.txt","r")
file2 = open("C:/Users/MSI/Desktop/text1.txt","w+")
# file3 = open("C:/Users/MSI/Desktop/text1.txt","r+")
rud_file = file1.read()
with file2 as text:
    for line in rud_file:
        text.write(line)
    
    
#     # file4 = file3.readlines()
#     #     # for line_num in range(len(file4)):
#     #     #     file4[line_num] = '{:^50}'.format(file4[line_num].strip()) + "\n"

    