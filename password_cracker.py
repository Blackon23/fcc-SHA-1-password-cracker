import hashlib

def crack_sha1_hash(hash, use_salts=False):
  #read the files without changing lines and save it in lists
  passwords = open('top-10000-passwords.txt').read().splitlines()
  open('top-10000-passwords.txt').close()
  salts = open('known-salts.txt').read().splitlines()
  open('known-salts.txt').close()
  
  #for evey password in the list
  for password in passwords:
    #check for the usage of salt
    if use_salts:
      #for every known salt
      for salt in salts:
        #for salt before password
        salted_password = salt + password
        #usage of the sha1 to hash the salted password
        salted_password_hash = hashlib.sha1(salted_password.encode()).hexdigest()
        if salted_password_hash == hash:
          return password
        #for salt after password
        salted_password = password + salt
        #usage of the sha1 to hash the salted password
        salted_password_hash = hashlib.sha1(salted_password.encode()).hexdigest()
        if salted_password_hash == hash:
          return password
    else:
      #usage of the sha1 to hash the password
      password_hash = hashlib.sha1(password.encode()).hexdigest()
      if password_hash == hash:
        return password
  #the password wasn't found
  return "PASSWORD NOT IN DATABASE"
    