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
            username = input("\t\t\t\t\tEnter your Username:\n ")
            
            while True:
                print("\t\t\t\t\tEnter tp - to type in your password")
                print("\t\t\t\t\tEnter gp - to be generated password\n")
                
                print("Enter tp - to type your password\n gp - to get a generated password")
                pass_choice = input("Choice:").lower().strip()
                
                if pass_choice == 'tp':
                    password = input("Enter password\n")
                    break
                elif pass_choice == 'gp':
                    password = Credentials.generate_password(8)
                    break
                else:
                    print("Invalid Choice.Please use short codes")
                    
                    
            create_user(username,password)
                
        elif shortcode == 'li':
            
            print("Enter your credentials to login")
            username = input("Username:")
            password = input("Password")
                
            user = auth(username,password)
            
            if user == username:
                print(f"Hello, {username}.Proceed to select a short code to navigate")
                
                while True:
                    print("\t\t\t\t"+"*"*50)
                    print("\t\t\t\t"+"*"*50)
                    print('\n')
                    print("\t\t\t\t\tcc  - create an a new credential")
                    print("\t\t\t\t\tdc - display credentials")
                    print("\t\t\t\t\tfc - find credential")
                    print("\t\t\t\t\trm - remove credential")
                    print("\t\t\t\t\tup - update credential")
                    print("\t\t\t\t\tcp - copy credential")
                    print("\t\t\t\t\tex - exit app")
                    print('\n')
                    print("\t\t\t\t"+"*"*50)
                    print("\t\t\t\t"+"*"*50)
                    
                    shortcode = input("Shortcode:").lower().strip()
                    
                    if shortcode == 'cc':
                        # create a new credential
                        print("Enter details of the new credentials")
                        site_name = input("Site Name:").strip()
                        user_name = input("User Name:").strip()
                        while True:
                            print("\t\t\t\t\tEnter tp - to type in your password")
                            print("\t\t\t\t\tEnter gp - to be generated password\n")
                
                            print("Enter tp - to type your password\n gp - to get a generated password")
                            pass_choice = input("Choice:").lower().strip()
                
                            if pass_choice == 'tp':
                                password = input("Enter password\n")
                                break
                            elif pass_choice == 'gp':
                                password = Credentials.generate_password(8)
                                break
                            else:
                                print("Invalid Choice.Please use short codes")
                        s_creds(create_creds(site_name,user_name,pass_choice))
                                
                    
                                
                        
                    
                        
                        
                    
                
                    
            
            
                
        
        
        
        if shortcode == 'ex':
            print("\n")
            print("\t\t\t\t"+"*"*50)     
            print("\t\t\t\t"+"*"*50)
            print("\t\t\t\t\tGoodbye, See you again later")
            print("\t\t\t\t"+"*"*50)
            print("\t\t\t\t"+"*"*50)
            
            break
            
            
        
        
    
    
    

if __name__ == '__main__':
    main()
    
