def is_valid_login(login):
    if (4 <= len(login) <= 16 and login.lower()[0] in "qwertyuiopasdfghjklzxcvbnm"):
        login = login.lower()
        alf = "qwertyuiopasdfghjklzxcvbnm0123456789_"
        for i in login:
            if (i not in alf):
                return False
        return True
    return False