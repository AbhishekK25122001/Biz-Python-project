from Patterns import *
import logging



Un=input("Enter the username")
logging.basicConfig(level=logging.INFO, filename=f"{Un}_logs.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


#Username
def validate_user_name(f):
    logging.info("Registartion attempt received")
    def helper(*x):
        logging.info("Starting username validation.")
        if re.match(Pattern_un,Un):
            logging.info("Username validated successfully")
            return f(*x)
        else:
            print("Invalid Username! Please enter valid username")
    return helper

#Password
def validate_password(f):
    def helper(*x):
        logging.info("Starting password validation.")
        while True:
            psw=input("Enter Password: ")
            if re.match(Pattern_psw,psw):
                logging.info("Password validation successfull")
                return f(*x)
            else:
                logging.warning("Registration failed for user Password too short")
                print("Incorrect Password! Password must contain [Letters,numbers and special characters and must of  6 to 20 characters ]")
    return helper

#Name
def validate_Name(f):
    def helper(*x):
        logging.info("Starting name validation.")
        while True:
            nm=input("Enter the name: ")
            if re.match(Pattern_name,nm):
                logging.info("Name validation successfull")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid Name format")
                print("Incorrect name! First letter must be capital followed by smaller case letters")
    return helper

#Phone number
def validate_user_phone(f):
    def helper(*x):
        logging.info("Starting phoen_no validation.")
        while True:
            phn=input("Enter the 10 digit number: ")
            if re.match(Pattern_phone,phn):
                logging.info("Phone validation successfull")
                return f(*x) 
            else:
                logging.warning(f"Registration failed for user Invalid phone No. format")
                print("Invalid Phone! Please Enter correct 10 digit phone number")
    return helper

#Email
def validate_email_id(f):
    def helper(*x):
        logging.info("Starting email validation.")
        while True:
            eml=input("Enter the email: ")
            if re.match(Pattern_email,eml):
                logging.info("Email validation successfull")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid email format")
                print("Invalid Email ID! Please Enter valid Email ID!")
    return helper

#License number
def validate_Lic_no(f):
    def helper(*x):
        logging.info("Starting License number validation.")
        while True:
            Licno=input("Enter the License number: ")
            if re.match(Pattern_lic,Licno):
                logging.info("License number validation successfull")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid Lic_ No format")
                print("Invalid License number! License No. should be in format[2-state letter] [2-RTO area no.] [11 digits of LICense no.]")
    return helper

#Adhaar number
def validate_Adhaar_no(f):
    def helper(*x):
        logging.info("Starting adhar validation.")
        while True:
            adr=input("Enter the adhaar number: ")
            if re.match(Pattern_adhr,adr):
                logging.info("Aadhaar number validation successfull")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid Adhar_No format")
                print("Invalid Aadhaar number! Adhaar no. must be correct and contain 12 digits")
    return helper

#City
def validate_city(f):
    def helper(*x):
        logging.info("Starting city name validation.")
        while True:
            cty=input("Enter the city name: ")
            if re.match(Pattern_city,cty):
                logging.info("City name validated successfully")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid City format")
                print("Invalid City name! Enter city Name as alphabets only")
    return helper

#pincode
def validate_pincode(f):
    def helper(*x):
        logging.info("Starting pincode validation.")
        while True:
            pin=input("Enter the pincode: ")
            if re.match(Pattern_pincode,pin):
                logging.info("Pin Code validation successfull")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid pincode format")
                print("Invalid Pin code! Enter 6 digit pincode only")
    return helper

#state
def validate_state(f):
    def helper(*x):
        logging.info("Starting state validation.")
        while True:
            stt=input("Enter the state name: ")
            if re.match(Pattern_state,stt):
                logging.info("State name validated successfully")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid State format")
                print("Invalid State! Enter state name in alphabets only")
    return helper

#Company name
def validate_Company_name(f):
    def helper(*x):
        logging.info("Starting Company validation.")
        while True:
            Cname=input("Enter the Company name: ")
            if re.match(Pattern_Company_name,Cname):
                logging.info("Company name validated successfully")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid Company name format")
                print("Invalid Company Name! Enter valid Company name only")
    return helper

#Model name/number
def validate_model_no(f):
    def helper(*x):
        logging.info("Starting model name validation.")
        while True:
            mdl=input("Enter the model name/number: ")
            if re.match(Pattern_mdl,mdl):
                logging.info("Model name validation successfull")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid model_no format")
                print("Invalid Model name or number! Enter correct model name")
    return helper

#Color
def validate_Color(f):
    def helper(*x):
        logging.info("Starting Colour validation.")
        while True:
            clr=input("Enter the color of the car: ")
            if re.match(Pattern_Color,clr):
                logging.info("Color validation successfull")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid Colour Name format")
                print("Invalid Color! Please enter valid Color only")
    return helper

#Price
def validate_Price(f):
    def helper(*x):
        logging.info("Starting Price validation.")
        while True:
            prc=input("Enter the price of car: ")
            if re.match(Pattern_Price,prc):
                logging.info("Price validated successfully")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid Name format")
                print("Invalid Price! Please enter valid Price only")
    return helper

#Fuel
def validate_Fuel(f):
    def helper(*x):
        logging.info("Starting fuel type validation.")
        while True:
            fl=input("Enter the fuel type: ")
            if fl in Patter_Fuel:
                logging.info("Registration done Successfully.")
                return f(*x)
            else:
                logging.warning(f"Registration failed for user Invalid Fuel type format")
                print("Invalid fuel type! Please enter valid Fuel type only")
    return helper

#validation of user name
@validate_user_name
def check_username():
    pass

#validation of password
@validate_password
def check_password():
    pass

#validation of name
@validate_Name
def check_Name():
    pass

#validation of phone
@validate_user_phone
def check_phone():
    pass

#validation of email
@validate_email_id
def check_email():
    pass

#validation of license numeber
@validate_Lic_no
def check_licno():
    pass

#validation of aadhaar number
@validate_Adhaar_no
def check_Aadhaar():
    pass

#validation of city
@validate_city
def check_city():
    pass

#validation of pincode
@validate_pincode
def check_pin():
    pass

#validation if city
@validate_state
def check_state():
    pass

#validation of company name
@validate_Company_name
def check_Cname():
    pass

#validation of model number
@validate_model_no
def check_model():
    pass

#validation of color
@validate_Color
def check_color():
    pass

#validation of price
@validate_Price
def check_price():
    pass

#validation of fuel
@validate_Fuel
def check_fuel():
    print("Registeration Successfull")