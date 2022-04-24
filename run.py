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

def s_creds(creds):
    creds.save_creds()
    
def u_cred(creds):
    return creds.update_cred()

    
