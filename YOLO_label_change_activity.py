import os

files = []
sew = []
get_put = []

# Add the path of txt folder
path  = "labels/"
for i in os.listdir(path):
    if i.endswith('.txt'):
        files.append(i)

for item in files:
    # define an empty list
    file_data = []

    with open("labels/"+item, 'r') as myfile:
        print(myfile)
        for line in myfile:
            # remove linebreak which is the last character of the string
            currentLine = line[:-1]
            data = currentLine.split(" ")
            # add item to the list
            file_data.append(data)
    
    # Decrease the first number in any line by one
    for i in file_data:
        if i[0] == '0': 
            temp = 1 
            i[0] = str(int(temp))

        elif i[0] == '1': 
                temp = 0 
                i[0] = str(int(temp))

    # Write back to the file
    f = open("labels_new/"+item, 'w')
    for i in file_data:
        res = ""
        for j in i:
            res += j + " "
        f.write(res)
        f.write("\n")
    f.close()
