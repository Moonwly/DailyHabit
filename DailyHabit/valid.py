import re


class Valid:
    @classmethod
    def valid_email(cls, email):
        if re.match(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z_.]{0,20}', email):
            return True
        return False

    @classmethod
    def valid_username(cls, username):
        if len(username) >= 6:
            return True
        return False

    @classmethod
    def valid_password(cls, password):
        if len(password) >= 6:
            return True
        return False

