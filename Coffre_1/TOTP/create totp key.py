import pyotp

# Générer une nouvelle clé secrète TOTP
secret_key = pyotp.random_base32()
print("Clé secrète TOTP générée :", secret_key)

# Créer un objet TOTP basé sur la clé secrète
totp = pyotp.TOTP(secret_key)

# Générer un code TOTP actuel
current_totp = totp.now()
print("Code TOTP actuel :", current_totp)

# Vous pouvez également afficher un lien QR code pour scanner la clé dans une application mobile
otpauth_url = totp.provisioning_uri("Nom_Utilisateur", issuer_name="Nom_Application")
print("Lien QR code pour l'application mobile :", otpauth_url)
