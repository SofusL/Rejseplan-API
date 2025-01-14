class UserController: 
  def __init__(self, view, model): 
    self.view = view 
    self.model = model 
  def fetchDatas(self):
    Data = self.model.fetchData()
    print(Data)
    return Data