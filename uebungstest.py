# Belibige User Eingabe programmieren

text = input("Gebe einen Text ein: ")
count = 0
for i in text: 
    if "" in text:
        count1 = count + 1
        print("yes")
    else:
        print("no")
print(count1)
print(text)