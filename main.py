from cryptography.fernet import Fernet

#gives user option to enter their log in destination or application
destination = input("Enter the name of your log in application: ")

#raw username and password constants
rawUser = input("Enter your Username: ")
rawPass = input("Enter your password: ")

#encrypts username
def usernameEncryption():
    rawUsername = rawUser
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encUsername = fernet.encrypt(rawUsername.encode())
    decMessage = fernet.decrypt(encUsername).decode()
    print("Your username has been encrypted and stored!")
    f = open("EncryptedPasswords.txt", "ab")
    f.write("Destination".encode('ascii') + ": ".encode('ascii') + destination.encode('ascii') + " , ".encode('ascii')+ encUsername + " , ".encode('ascii') + key + "\n".encode('ascii'))
    f.close()

usernameEncryption()


#encrypts password
def passwordEncryption():
    rawPassword = rawPass
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encPassword = fernet.encrypt(rawPassword.encode())
    decMessage = fernet.decrypt(encPassword).decode()
    print("Your password has been encrypted and stored!")
    f = open("EncryptedPasswords.txt", "ab")
    f.write("Destination".encode('ascii') + ": ".encode('ascii') + destination.encode('ascii') + " , ".encode('ascii')+ encPassword + " , ".encode('ascii') + key + "\n".encode('ascii'))
    f.close()

passwordEncryption()


