import ssl
from database import database, users


def get_all_users():
    query = users.select()
    return database.fetch_all(query)


def get_user_by_pseudo(pseudo: str):
    query = users.select().where(users.c.pseudo == pseudo)
    return database.fetch_one(query)


async def create_user(user_in):
    query = users.insert().values(
        pseudo=user_in.pseudo,
        email=user_in.email,
        password=user_in.password,
        last_updated=user_in.last_updated
    )
    try:
        insertion = await database.execute(query)
        return {**user_in.dict(), "id": insertion}
    except Exception as e:
        print(e)
        return {**user_in.dict(), "id": 0}


async def reset_password(pseudo: str, pwd: str, new_pwd: str):
    query = users.update().where((users.c.pseudo == pseudo) & (users.c.password == pwd)).values(password=new_pwd)
    reset_status = await database.execute(query)
    if reset_status == 1:
        return {"message": f"Password for user {pseudo} has been successfully set to {new_pwd}"}
    else:
        return {"message": f" Wrong password given ! Can not modify it !"}


async def delete_user(pseudo: str, pwd: str):
    query = users.delete().where((users.c.pseudo == pseudo) & (users.c.password == pwd))
    # delete also all the data concerning the user in scan table
    delete_status = await database.execute(query)
    if delete_status == 1:
        return {"message": f"User {pseudo} has been successfully deleted"}
    else:
        return {"message": f" Wrong password given ! Can not delete this user !"}


async def send_new_password(email: str):
    query = users.select().where(users.c.email == email)
    response = await database.fetch_all(query)
    if len(response) > 0:
        new_pwd = generate_random_password()
        content = f"""
            Hello dear customer,
            As you have just requested, here is your new password : {new_pwd}.
            Please use it for your next sign in and do not forget to reset it with a new one !
            Best regards.
            Garbage Teams.
            """
        send_email(email, content)
        update_query = users.update().where(users.c.email == email).values(password=new_pwd)
        reset_status = await database.execute(update_query)
        if reset_status == 1:
            return {"message": f"An email has been sent to  {email} and the password has been automatically changed ! "}
    else:
        return {"message": f"There is no user corresponding to this email address !"}


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


def send_email(dst_email: str, content: str):
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
