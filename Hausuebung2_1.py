#string test

eingabe = input("Enter something:")
      
for i in eingabe:
    try:
        x = int(eingabe)
        print(eingabe, "is not a string")
    except:
        print(eingabe, "is a string") 