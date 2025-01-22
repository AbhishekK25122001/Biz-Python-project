from Patterns import *
from logger import *

#Decorator function
def validate_func(func):
    def wraper(x):
        logging.info(f"Starting {x} validation.")
        try:
            if func(x)[0]:
                logging.info(f"{x} validation successful.")
                return func(x)[1] 
            else:
                logging.warning("Registration failed for user Invalid format")
        except Exception as e:
            print(e)
    return wraper


#Username validation 
@validate_func
def Val_username(Un):
    try:
        setup_logger(Un)
        if re.match(Pattern_un,Un):
            flag=True
            message="Username validation successfull"
        else:
            raise ValueError("Username should contain number and characters only")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,Un

#validate password
@validate_func
def Val_password(_psw):
    try:
        if re.match(Pattern_psw,_psw):
            flag=True
            message="Password validation successfull"
        else:
            raise ValueError("Password must be of 6-20 digits")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,_psw

#validate name
@validate_func
def Val_name(nm):
    try:
        if re.match(Pattern_name,nm):
            flag=True
            message="Name validation successfull"
        else:
            raise ValueError("Name should start with Capital Letter only and must contain alphabets only")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,nm

#Phone validation
@validate_func
def Val_phone(phone):
    try:
        if re.match(Pattern_phone,phone):
            flag=True
            message="Phone validation successfull"
        else:
            raise ValueError("Phone number must be of 10 digits only")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,phone

#Email validation
@validate_func
def Val_email(email):
    try:
        if re.match(Pattern_email,email):
            flag=True
            message="Email validation successfull"
        else:
            raise ValueError("Email must be in email format only")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,email

#License number
@validate_func
def Val_lic(Lic):
    try:
        if re.match(Pattern_lic,Lic):
            flag=True
            message="License validation successfull"
        else:
            raise ValueError("License number must be of given format")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,Lic

#Aadhaar number
@validate_func
def Val_aadhaar(aadr):
    try:
        if re.match(Pattern_adhr,aadr):
            flag=True
            message="Aadhaar validation successfull"
        else:
            raise ValueError("Aadhaar number must be of 12 Digits")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,aadr

#City
@validate_func
def Val_city(cty):
    try:
        if re.match(Pattern_city,cty):
            flag=True
            message="City validation successfull"
        else:
            raise ValueError("City must be alphabets only")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,cty

#validate pincode
@validate_func
def Val_pincode(pin):
    try:
        if re.match(Pattern_pincode,pin):
            flag=True
            message="PinCode validation successfull"
        else:
            raise ValueError("PinCode must be of 6 digits only")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,pin

#Validate State
@validate_func
def Val_state(st):
    try:
        if re.match(Pattern_state,st):
            flag=True
            message="State validation successfull"
        else:
            raise ValueError("State must be alphabets only")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,st

#Validate Company name
@validate_func
def Val_Cname(cnm):
    try:
        if re.match(Pattern_Company_name,cnm):
            flag=True
            message="Company Name validation successfull"
        else:
            raise ValueError("Company Name must be alphabets only")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,cnm

#Validate model number
@validate_func
def Val_Model(mdl):
    try:
        if re.match(Pattern_mdl,mdl):
            flag=True
            message="Model validation successfull"
        else:
            raise ValueError("Model Name must be Valid")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,mdl

#Validate color
@validate_func
def Val_Color(clr):
    try:
        if re.match(Pattern_Color,clr):
            flag=True
            message="Color validation successfull"
        else:
            raise ValueError("Color must be Valid")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,clr

#Validate Price
@validate_func
def Val_Price(prc):
    try:
        if re.match(Pattern_Price,prc):
            flag=True
            message="Price validation successfull"
        else:
            raise ValueError("Price must be Valid")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,prc

#Validate Fuel
@validate_func
def Val_Fuel(fl):
    try:
        if fl in Patter_Fuel:
            flag=True
            message="Fuel validation successfull"
        else:
            raise ValueError("Fule type must be Valid")
    except Exception as e:
        flag=False
        message=str(e)
    return flag,message,fl

