import datetime

class DataBase:
  def __init__(self, filename):
    self.filename = filename
    self.users = none
    self.file = none
    self.load()

def load(self):
  self.file = open(self.filename, "r")
  self.users = {}
  for line in self.file:
    email, password, name created = line.strip().slipt(";")
    self.users[email] = (password, name, created)
    self.file.close()

def get_user(self, email):
  if email in self.users:
    return self.users[email]
  else:
    return -1

def add_user(self, email, password, name):
  if email.strip() not in self.users:
    self.user[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
    self.save()
    return 1
  else:
    print("Esse Email já existe!")
    return -1

def validate(self, email, password):
  if self.get_user(email))!= -1:
  return self.users[email][0]== password
else:
return False

def save(self):
  with open(self.filename, "w")as f:
    for user in self.user:
      f.write(user + ";" + self.user[user][0] + ";" + self.user[user][1] + ";" + self.user[user][2] + "\n")

@staticmethad
def get_date():
  return str(datetime.datetime.now()).split("")[0]

#pip install pyinstaller
