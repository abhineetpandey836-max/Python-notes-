# correct email- abhineetpandey836@gmail.com
# password - 12556
email= input("Apna email bata")
if '@' in email:
    password = input("Apna password bhi bata")

    if email == "abhineetpandey836@gmail.com" and password == "12556":
        print("Welcome")
    elif email == "abhineetpandey836@gmail.com" and password != "12556":
        print("Password Incorrect")
        password = input("Password fir se likh")
        # Agar if else ke andar if else se hai to usko "nested if else" bolte hai
        if password == "12556":
            print("Finally correct")
        else:
            print("Still incorrect")
    else:
        print("Incorrect credentials")
else:
    print("Email galat hai sahi likho")
    # Here we finish lecture number 10 :) happy :)don't worry everything will be fine at the end, keep putting the efforts.