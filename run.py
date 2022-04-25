#!/usr/bin/python3.9
from ast import If
from plocker import User,Credentials
import pyperclip as pyc


def create_user(username,password):
    '''
    Method to create a new user
    '''
    new_user = User(username,password)
    return new_user

def s_user(user):
    '''
    method to save a newly created user
    '''
    user.save_user()
    
def r_user(user):
    '''
    method to create a user
    '''
    user.remove_user()
    
def create_creds(site_name,username,password):
    '''
    method to create a credential
    '''
    new_creds = Credentials(site_name,username,password)
    return new_creds

    
def u_cred(creds):
    '''
    method to update a credential
    '''
    return creds.update_cred()


def remove_cred(cred):
    '''
    method to delete a credential
    '''
    return cred.remove_cred()


def s_creds(creds):
    '''
    method to save a credential
    '''
    creds.save_creds()
    
def search_creds(name):
    '''
    method to search for a credential by name
    '''
    return Credentials.search_cred(name)


def auth(name,password):
    '''
    method to check if a uer already exists in the users list
    '''
    return Credentials.aunthenticate(name,password)


def disp_creds():
    '''
    method to display a list of credentials
    '''
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
        shortcode = input("\t\t\t\t\tEnter the shortcode: ").lower().strip()
        print("\n")
        
        if shortcode == 'ca':
            print("\t\t\t\t\tEnter Your Details")
            print("\t\t\t\t"+"*"*50)
            username = input("\t\t\t\t\tEnter your Username: ").strip()
            print("\n")
            
            while True:
                print("\t\t\t\t\tEnter tp - to type in your password")
                print("\t\t\t\t\tEnter gp - to be generated password")
                
                print("\n")
                pass_choice = input("\t\t\t\t\tChoice:").lower().strip()
                
                if pass_choice == 'tp':
                    password = input("\t\t\t\t\tEnter password: ")
                    break
                elif pass_choice == 'gp':
                    print("\t\t\t\t\tEnter the length of the password")
                    print("\t\t\t\t\tPassword must be between 8 and 12")
                    len=int(input("\t\t\t\t\tLength:"))
                    
                    if len > 12 or len < 8:
                        print("\t\t\t\t\tlength must not be greater than 12 or less than 8")
                        
                    else:
                        password = Credentials.generate_password(len)
                        print(f"\t\t\t\t\tyour password is {password}")
                        break
                        
                else:
                    print("\t\t\t\t\tInvalid Choice.Please use short codes")
                    
            password=password.strip()
            if password == "" or username == "":
                print("/n")
                print("\t\t\t\t\tACCOUNT CREATION FAILED:Username and Password cannot be empty.Please try again")
            else:
                
                s_user(create_user(username,password))
                print("\n")
                print("\t\t\t\t\tAccount created successfully")
                print(f"\t\t\t\t\tUse username:{username} and password:{password} to login ")
                print("\n")
                
        elif shortcode == 'li':
            
            print("\t\t\t\t\tEnter your credentials to login")
            username = input("\t\t\t\t\tUsername:")
            password = input("\t\t\t\t\tPassword:")
            print('\n')
                
            user = auth(username,password)
            print("\t\t\t\t"+"*"*50)
            print("\t\t\t\t"+"*"*50)  
            
            
            if user == username:
                print(f"\t\t\t\t\tHello, {username}.Proceed to select a short code to navigate")
                
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
                    
                    shortcode = input("\t\t\t\t\tShortcode:").lower().strip()
                    print("\n")
                    
                    if shortcode == 'cc':
                        # create a new credential
                        print("\t\t\t\t\tEnter details of the new credentials")
                        site_name = input("\t\t\t\t\tSite Name:").strip()
                        user_name = input("\t\t\t\t\tUser Name:").strip()
                        while True:
                            print("\t\t\t\t\tEnter tp - to type in your password")
                            print("\t\t\t\t\tEnter gp - to be generated password\n")
                
                          
                            pass_choice = input("\t\t\t\t\tChoice:").lower().strip()
                
                            if pass_choice == 'tp':
                                password = input("\t\t\t\t\tEnter password:")
                                break
                            elif pass_choice == 'gp':
                                print("\t\t\t\t\tEnter the length of the password")
                                print("\t\t\t\t\tPassword must be between 8 and 12")
                                len=int(input("\t\t\t\t\tLength:"))
                    
                                if len > 12 or len < 8:
                                    print("\t\t\t\t\tlength must not be greater than 12 or less than 8")
                        
                                else:
                                    password = Credentials.generate_password(len)
                                    print(f"\t\t\t\t\tyour password is {password}")
                                    break
                            else:
                                print("\t\t\t\t\tInvalid Choice.Please use short codes")
                        password=password.strip() 
                        if site_name == "" or user_name == "" or password == "":
                            print("\t\t\t\t\tFAILED TO CREATE AND SAVE CREDENTIALS:Please fill in all details")
                           
                        else:
                            s_creds(create_creds(site_name,user_name,password))
                        
                        
                            
                    elif shortcode == 'fc':
                        print("\t\t\t\t\tEnter the name of the account you want to find")
                        print("\n")
                        account_name = input("\t\t\t\t\tAccount Name:").strip()
                        print("\n")
                        
                        if search_creds(account_name):
                            account = search_creds(account_name)
                            print("\t\t\t\tAccount\t\tUsername\t\tPassword")
                            print("\t\t\t\t\t"+"_"*50)
                            print(f"\t\t\t\t\t{account.site_name}\t\t{account.username}\t\t{account.password}")
                            
                            
                        else:
                            print("\t\t\t\t\tAccount not found")
                                
                    
                    elif shortcode == 'dc':
                        if disp_creds():
                            for cred in disp_creds():
                                
                                print("\t\t\t\t\t"+"_"*50)
                                print(f"\t\t\t\t\t{cred.site_name}\t\t{cred.username}\t\t{cred.password}")
                                print("\n")
                                
                        else:
                            print("\n")
                            print("\t\t\t\t\tThere are no saved credentials available")
                            print("\n")
                            
                    elif shortcode == 'rm':
                        print("\n")
                        print("\t\t\t\t\tEnter the name of the account you wan't to delete")
                        account_name = input("\t\t\t\t\tAccount Name:").strip()
                        print("\n")
                        
                        if search_creds(account_name):
                            account = search_creds(account_name)
                            remove_cred(account)
                            if disp_creds():
                                for cred in disp_creds():
                                    print("\t\t\t\t\tRemaing Accounts......")
                                    print("\t\t\t\t\t"+"_"*50)
                                    print(f"\t\t\t{cred.site_name}\t\t{cred.username}\t\t{cred.password}")
                                
                            else:
                                print("\t\t\t\t\tNo accounts remaining")
                               
                        else:
                            print("\t\t\t\t\tAccount not found")
                            
                            
                    elif shortcode == 'cp':
                        print("\t\t\t\t\tEnter the account you want to update")
                        account_name = input("\t\t\t\t\tAccount Name:").strip()
                        if search_creds(account_name):
                            account = search_creds(account_name)
                            pyc.copy(account.password)
                            print("\t\t\t\t\tPassword copied to clipboard")
                        else:
                            print("\t\t\t\t\taccount not found")
                            
                    elif shortcode == "up":
                        print("\t\t\t\t\tEnter the account you want to update")
                        account_name = input("\t\t\t\t\tAccount Name:").strip()
                        if search_creds(account_name):
                            account = search_creds(account_name)
                            print("\t\t\t\t\tEnter the username to change username.")
                            print("\n")
                            print("\t\t\t\t\tIf you not wish to change the username, type existing username")
                            username = input("\t\t\t\t\tUsername:").strip()
                            print("\n")
                            while True:
                                print("\t\t\t\t\tEnter tp - to type in new password")
                                print("\t\t\t\t\tEnter gp - to be generated new password\n")
                
                                
                                pass_choice = input("\t\t\t\t\tChoice:").lower().strip()
                
                                if pass_choice == 'tp':
                                    password = input("\t\t\t\t\tEnter password:")
                                    break
                                elif pass_choice == 'gp':
                                    print("\t\t\t\t\tEnter the length of the password")
                                    print("\t\t\t\t\tPassword must be between 8 and 12")
                                    len=int(input("\t\t\t\t\tLength:"))
                    
                                    if len > 12 or len < 8:
                                        print("\t\t\t\t\tlength must not be greater than 12 or less than 8")
                        
                                    else:
                                        password = Credentials.generate_password(len)
                                        print(f"\t\t\t\t\tyour password is {password}")
                                        break
                                else:
                                     print("\t\t\t\t\tInvalid Choice.Please use short codes")
                                     
                            if password == "" or username == "":
                                print("\t\t\t\t\tUPDATE FAILED.Please try filling in the values in order to update credential")
                            
                            else:
                                password=password.strip()        
                                account.username = username
                                account.password = password
                                print("\t\t\t\t\tAccount Updated")
                                print("\t\t\t\t\tRemaing Accounts......")
                                print("\t\t\t\t\t"+"_"*50)
                                print(f"\t\t\t\t\t{account.site_name}\t\t{account.username}\t\t{account.password}")
                            
                            
                        else:
                            print("Account not found")
                            
                    elif shortcode == 'ex':
                        print("\n")
                        print("\t\t\t\t"+"*"*50)     
                        print("\t\t\t\t"+"*"*50)
                        print(f"\t\t\t\t\tGoodbye,{username} See you again later")
                        print("\t\t\t\t"+"*"*50)
                        print("\t\t\t\t"+"*"*50)
                        break
                        
                    else:
                        print("\t\t\t\t"+"*"*50)
                        print("\t\t\t\t\tI did not get that, Please use the provided short codes")
                        print("\t\t\t\t"+"*"*50)
            
                        
                        
            else:
                print("\t\t\t\t\tWrong credentials.Please try again")                
                        
                    
                    
        
        
        elif shortcode == 'ex':
            print("\n")
            print("\t\t\t\t"+"*"*50)     
            print("\t\t\t\t"+"*"*50)
            print("\t\t\t\t\tGoodbye, See you again later")
            print("\t\t\t\t"+"*"*50)
            print("\t\t\t\t"+"*"*50)
            
            break
        else:
            print("\t\t\t\t"+"*"*50)
            print("\t\t\t\t\tI did not get that, Please use the provided short codes")
            print("\t\t\t\t"+"*"*50)
            
            
        
        
    
    
    

if __name__ == '__main__':
    main()
    
