
class InformationCall:

  def __init__(self, uuid, month, dat, year, time, uso, timezone, ago, participants, duration, typep):
    self.uuid = uuid
    self.month = month
    self.dat = dat
    self.year = year
    self.time = time
    self.uso = uso
    self.timezone = timezone
    self.ago = ago
    self.participants = participants
    self.duration = duration
    self.typep = typep

  def calculate_time(self):
    minute = self.duration.split(":")
    totaled = int(minute[0]) * 3600 + int(minute[1]) * 60 + int(minute[2])
    self.duration = totaled
