#string test

eingabe = input("Enter something:")
      
for i in eingabe:
    try:
        x = int(eingabe) # testet, ob eingabe ein Intiger ist, wenn ja, dann ist es KEIN String!
        print(eingabe, "is not a string")
    except ValueError:                # Wenn es kein Intiger ist(ValueError), ist es ein String (Exception)
        print(eingabe, "is a string") 

print("done")