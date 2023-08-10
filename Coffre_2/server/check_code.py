import pyotp


class TOTP:
    def __init__(self):
        self.secret_key = "U2JI5HQDYPIKYVZHK5BVXTMKM7TIHSU5"
        self.totp = pyotp.TOTP(self.secret_key)

    def verify(self, code):
        return self.totp.verify(code)

