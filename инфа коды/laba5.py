f = open('data_file2.txt','r')
data_file =f.readlines()
f.close()
G1 = int(data_file[0].split(':')[1])
G2 = int(data_file[1].split(':')[1])
S1 = int(data_file[2].split(':')[1])
S2 = int(data_file[3].split(':')[1])
S3 = int(data_file[4].split(':')[1])
S4 = int(data_file[5].split(':')[1])
S5 = int(data_file[6].split(':')[1])
VL1 = int(data_file[7].split(':')[1])
VL2 = int(data_file[8].split(':')[1])
KL1 = int(data_file[9].split(':')[1])
KL2 = int(data_file[10].split(':')[1])
KL3 = int(data_file[11].split(':')[1])
vetv1 = G1&S1&KL1&S4&KL3&S5
vetv2 = G1&S1&VL1&S3&KL2&S4&KL3&S5
vetv3 = G2&S2&VL2&S5
if vetv1 | vetv2 | vetv3:
    result = "Есть электроснабжение"
    if  vetv1 or vetv2:
        i = ' Запитан от первого источника'
    if vetv3:
        i = ' Запитан от второго источника'
    if vetv1 and vetv2 and vetv3:
        i = ' Запитаны от обоих источников'
else:
    result = "Нет электроснабжения"
    i = ' Не запитан'
print(result, i)
h = open('res.txt', 'wb')
res_coded = result.encode('utf-8')
i = i.encode('utf-8')
h.write(res_coded)
h.write(i)
h.close()
