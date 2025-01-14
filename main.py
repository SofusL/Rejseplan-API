from model import *
from view import *
from controller import *
from dotenv import load_dotenv
import os
load_dotenv()
apiKey = os.getenv('API_KEY')


uw = UserView()
um = UserModel(apiKey)
uc = UserController(uw, um)
uw.setController(uc)
uw.run()
