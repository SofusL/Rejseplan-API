from model import *
from view import *
from controller import *
uw = UserView()
um = UserModel()
uc = UserController(uw, um)
uw.setController(uc)
uw.run()
