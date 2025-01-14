import requests
from datetime import datetime, timedelta

class UserModel:
  def __init__(self,key):
    self.accessId = key
    self.stopID = "3601"
    self.basePoint ='https://www.rejseplanen.dk/api/'
    self.endPoint = "departureBoard"

  def request(self):
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d") # Formatér til"YYYY-MM-DD"

    current_time = now.strftime("%H:%M") # Formatér til "HH:MM"

    params = {
      "accessId" : self.accessId,
      "id": self.stopID,
      "date" : current_date,
      "time" : current_time,
      "format": "json",
      "useBus": "0"
    }
    
    url = self.basePoint+self.endPoint
    return requests.get(url,params=params)

  def fetchData(self):
    response = self.request()

    departureList = response.json()['Departure']

    formattedDepatureList = []

    for departure in departureList:
      name = departure.get("name")
      stop = departure.get("stop")
      time = departure.get("time")
      date = departure.get("date")
      rtTime = departure.get("rtTime")
      rtDate = departure.get("rtDate")

    #Hvis bussen ikke er forsinket skal forventet tid være planmæssigtid

      if rtTime == None:
        rtTime = time
        rtDate = date
      
      depTime = datetime.strptime(rtTime, "%H:%M:%S").time()
      depDate = datetime.strptime(rtDate,"%Y-%m-%d").date()
      rtDep = datetime.combine(depDate, depTime)
      now = datetime.now().replace(microsecond=0)

      timeDelta = rtDep-now
      timeDelta = max(timeDelta, timedelta())

      direction = departure.get("direction")

      busStop = {
        "name": name,
        "stop": stop,
        "time": time,
        "rtTime": rtTime,
        "timeDelta": timeDelta,
        "direction": direction
      }

      formattedDepatureList.append(busStop)
    
      
    return(formattedDepatureList)

