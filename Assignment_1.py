print("WELCOME TO THE CAESAR AND VIGENERE ENCRYPTION AND DECRYPTION PROGRAM")
while True:
    print("\nMAIN MENU")
    print("Choices in this program are numbers ranging from 1-3")
    print("1. Use Caesar Cipher")
    print("2: Use Vigenere Cipher")
    print("3. Exit")
    choice1 = int(input("Enter your Choice: "))
    
    if choice1 == 1:
        print("\nWhat do you intend to do with Caesar Cipher?")
        print("1. X - Encrypt")
        print("2. Y - Decrypt")
        print("3. Exit")
        choice2 = int(input("Enter your choice: "))
        
        if choice2 == 1:
            message = input("Enter message for encryption: ")
            key = int(input("Enter Encryption Key (any number between 0-25): "))
            print("Ciphertext :", message)
            print("Decrypted Text :", Caesar_encrypt(message, key))
        
        elif choice2 == 2:
            message = input("Enter Message for Decryption: ")
            key = int(input("Enter Decryption Key (any number between 0-25): "))
            print("Decrypted Text :", message)
            print("Ciphertext :", Caesar_decrypt(message, key))
            
        elif choice2 == 3:
            break
            
        else:
            print("Oops! Incorrect Choice.")
            
    elif choice1 == 2:
        print("\nWhat do you intend to do with Vigenere Cipher?")
        print("1. X - Encrypt")
        print("2. Y - Decrypt")
        print("3. Exit")
        choice3 = int(input("Enter your choice: "))
        
        if choice3 == 1:
            message = input("Enter Message for Encryption: ").upper()
            keyword = input("Enter Encryption Keyword: ").upper()
            key = generateKey(message, keyword)
            print("Ciphertext :", message)
            print("Decrypted Text :", Vigenere_encrypt(message, key))
            
        elif choice3 == 2:
            message = input("Enter Message for Decryption: ").upper()
            keyword = input("Enter Decryption Keyword: ").upper()
            key = generateKey(message, keyword)
            print("Decrypted Text :", message)
            print("Ciphertext:", Vigenere_decrypt(message, key))
            
        elif choice3 == 3:
            break
            
        else:
            print("Oops! Incorrect Choice.")
            
    elif choice1 == 3:
        break
    
    else: 
        print("Oops! Incorrect Choice")