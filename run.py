#!/usr/bin/python3.9
from plocker import User,Credentials


def create_user(username,password):
    new_user = User(username,password)
    return new_user

def s_user(user):
    user.save_user()
    
def r_user(user):
    user.remove_user()
    
def create_creds(site_name,username,password):
    new_creds = Credentials(site_name,username,password)
    return new_creds

    
def u_cred(creds):
    return creds.update_cred()


def remove_cred(cred):
    return cred.remove_cred()


def s_creds(creds):
    creds.save_creds()
    
def search_creds(name):
    return Credentials.search_cred(name)


def auth(name,password):
    return Credentials.aunthenticate(name,password)


def disp_creds():
    return Credentials.display_creds()



def main():
    print('\n')
    print('\n')
    print("\t-"*50)
    print("\t\t\t\t"+"-"*50)
    print("\n")
    print("\t\t\t\t\t\t\tWelcome")
    print("\n")
    print("\t\t\t\t"+"-"*50)
    print("\t-"*50)
    
    while True:
        '''
         login section 
         CA - create account
         LI - Login
         EX - exit
         
        '''
        print("\n")
        print("\t\t\t\t"+"*"*50)        
        print("\t\t\t\t"+"*"*50)
        print("\n")
        print("\t\t\t\t\tUse These short codes to Navigate:\n\t\t\t\t\tca - to login\n\t\t\t\t\tli - to login\n\t\t\t\t\tex - to exit")
        print("\n")
        print("\t\t\t\t"+"*"*50)
        print("\t\t\t\t"+"*"*50)
        print("\n")
        shortcode = input("\t\t\t\t\tEnter the shortcode:\n").lower().strip()
        
        if shortcode == 'ca':
            print("\t\t\t\t\tEnter Your Details")
            print("\t\t\t\t"+"*"*50)
            username = input("Enter your Username")
            
            while True:
                print("Enter tp - to type in your password")
                print("Enter gp - to be generated password")
                
                password_choice = input("Enter your option:").lower().strip()
                if  password_choice == 'tp':
                    password = input("Enter \n")
                    break
                elif password_choice == 'gp':
                    print("*"*50)
                    print("....generating password")
                    print("enter the length of password between 8 and 12")
                    len =  int(input("length:"))
                    if len >12 and len < 8:
                        print("length must between 8 and 12")
                    
                    password = Credentials.generate_pasword(len)
                    break
                else:
                    print("Invalid choice.please use the short codes provided")
                
            
            
            
                
        
        
        
        if shortcode == 'ex':
            print("\n")
            print("*"*20)        
            print("*"*20)
            print("Goodbye, See you again later")
            print("*"*20)
            print("*"*20)
            
            break
            
            
        
        
    
    
    

if __name__ == '__main__':
    main()
    
