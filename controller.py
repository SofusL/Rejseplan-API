class UserController: 
  def __init__(self, view, model): 
    self.view = view 
    self.model = model 
  def fetchData(self):
    print(self.model.fetchData())
    return self.model.fetchData()