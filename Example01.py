'''
Created on 2021. 3. 2.

@author: User
'''


class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone number: ", self.phone_number)
        print("E-Mail: ", self.e_mail)
        print("Address: ", self.addr)
        
        
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    print(name, phone_number, e_mail, addr)

if __name__ == '__main__':
    set_contact()