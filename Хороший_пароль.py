# Good password 🌶️
def is_password_good(password):
    n_up=0
    n_low=0
    n_digit=0
    for i in password:
        if i.isupper():
            n_up+=1
        elif i.islower():
            n_low+=1
        elif i.isdigit():
            n_digit+=1
    return len(password)>=8 and n_up>=1 and n_low>=1 and n_digit>=1
password=input()
print(is_password_good(password))