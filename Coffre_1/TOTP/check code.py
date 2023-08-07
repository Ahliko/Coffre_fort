import pyotp


class TOTP:
    def __init__(self, secret_key):
        self.secret_key = "U2JI5HQDYPIKYVZHK5BVXTMKM7TIHSU5"
        self.totp = pyotp.TOTP(secret_key)

    def verify(self, code):
        return self.totp.verify(code)
