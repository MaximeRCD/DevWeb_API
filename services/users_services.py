import ssl


def generate_random_password():
    # necessary imports
    import secrets
    import string

    # define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    # fix password length
    pwd_length = 12

    # generate password meeting constraints
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            break
    return pwd


def send_email(dst_email: str, content:str):
    import smtplib  # importing the module

    sender_add = 'garbage.projectteam@gmail.com'  # storing the sender's mail id
    receiver_add = dst_email  # storing the receiver's mail id
    password = 'mfafukztberhhtnp'  # storing the password to log in

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls(context=ssl.create_default_context())
    server.login(sender_add, password)
    server.ehlo()
    server.sendmail(sender_add, receiver_add, content.encode('UTF_8'))
    server.quit()
