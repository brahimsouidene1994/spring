class User:
  def __init__(self, name, age, numTel):
    self.name_user = name
    self.ageUser = age
    self.numTel_User = numTel 

  def myfunc(self):
    print("Hello my name is " + self.name_user + ' '+ self.ageUser + ' '+  self.numTel_User)