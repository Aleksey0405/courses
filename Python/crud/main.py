from create_1 import create_user
from read_1 import user_info, all_users_info
#Нужно создать хранилище с мейлами
user_emails = []
users_storage = {}

while True:
    action = input("Please, enter create or read or update or delete: ")

    if action == "create" :
        print('action =', action)

        email = input("Email: ")
        name = input("Name: ")
        password = input("Password: ")
        phone = input("Phone: ")

        create_user(email,
                    name, 
                    password, 
                    phone, 
                    user_emails, 
                    users_storage)
        
        print('user_emails = ', user_emails)
        print('users_storage = ', users_storage)

    elif action == "read_all" :
        print('action =', action)
        all_users_info(users_storage)
    elif action == "read_user" :
        user_e = input("Enter user_email")
        message = user_info(user_e, user_emails, users_storage)
        
        print('action =', action)
        print('User: ', message)

    elif action == "update" :
        print('action =', action)

    elif action == "delete" :
        print('action =', action)
    else:
        print("Please, enter create or read or update or delete: ")
    
