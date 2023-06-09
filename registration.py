import re
import time




def registration(user_name, password):
    
        # checking the password function
    def check_password(p): 
        valid_pass = False
        
        if (len(p)<6 or len(p)>20):
            pass
        elif re.search("[a-z]",p) is None:
            pass
        elif re.search("[0-9]",p) is None:
            pass
        elif re.search("[A-Z]",p) is None:
            pass
        elif re.search("\W",p) is None:
            pass
        elif re.search("\s",p) is not None:
            pass
        else:
            valid_pass = True
        
        return valid_pass

    # telephone number registration and verification
    def registration_telnum():
        fail_count = 0
        while fail_count <=2:
            tel_number = input('Please enter your telephone number in format "+49 *** *** ****": \n ')
            # 
            # original pattern = r"^[+49][0-9]{7}+$"
            
            # modernisated pattern 
            pattern = r"^(\(?\+\(?49\)?[ ()]?([- ()]?\d[- ()]?){10,11})$"

            if re.search(pattern,tel_number) is None:
                fail_count +=1
                tel_number = None
                continue
            else:
                fail_count = 0
                break
        return tel_number
    
    
    reg_success = False
    fail_count = 0
    tel_number =""
    
    # checking user name. if empty - input username
    if user_name == "":
        while fail_count < 3:
            print("Please choose a username") 
            user_name = str(input(":>>>"))  
            if user_name == "":
                fail_count +=1
            else:
                fail_count = 0
                break
    if user_name !="":
        while fail_count <=3:        
        
            pass_message = """Your password should match the following criteria:
    - Should have at least one number.
    - Should have at least one uppercase and one lowercase character.
    - Should have at least one special symbol.
    - Should be between 6 to 20 characters long.
    """
            fail_message = "Please try another password.\n"
            
            if check_password(password):
                reg_success = True
                print('Registration successful! Please remember your data:')
                print(f'\tUsername: {user_name}')
                print(f'\tPassword: {password}')
                fail_count = 0
                break
                
            else: 
                if fail_count > 0: 
                    print(fail_message)
                print(pass_message)
                print("Please choose a password for", user_name)  
                password = str(input(":>>>"))  
                fail_count +=1
    
    if reg_success: 
        tel_number = registration_telnum()
    
    if tel_number is None:
        reg_success = False
    
         
    return user_name, password, tel_number, reg_success

