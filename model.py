class UserModel:
  def __init__(self):
    pass
  def fetchData(self):
    departure = [
      {
        "name": "5C",
        "direction" : "Husum Torv",
        "scheduled": "10:17",
        "actual" : "10:26",
        "within" : "3 min"
      },
      {
        "name": "250S",
        "direction" : "Gladsaxe",
        "scheduled": "10:17",
        "actual" : "10:26",
        "within" : "5 min"
      },
      {
        "name": "15",
        "direction" : "Hellerup",
        "scheduled": "10:17",
        "actual" : "10:26",
        "within" : "12 min"
      }
    ]
    return departure