class Person:

    def __init__(self, name, listCalls):
        self.years = int(0)
        self.name = name
        self.listCalls = listCalls
        self.averageTime = 0
        self.participant = 0
        self.numberCalls = 0
        self.numberConferences = 0
        self.totaltime = 0
        self.team = "developer"
        self.antiguedad = 0
        self.vacations = 26
        self.publicHolidays = 9
        self.regionalHolidays = 5
        self.location = 'M'  # M or C

    def __init__(self, name, team,time, location):
            self.years = int(0)
            self.name = name
            self.averageTime = 0
            self.participant = 0
            self.numberCalls = 0
            self.numberConferences = 0
            self.totaltime = time
            self.team = team
            self.antiguedad = 0
            self.vacations = 26
            self.publicHolidays = 9
            self.regionalHolidays = 5
            self.location = location


    def __repr__(self):
        return "Name " % self.name

    def __str__(self):
        return "Name is % s " % self.name + " " + self.team + " - " + self.totaltime + " - "+ self.location  ##" number calls: " + str(len(self.listCalls))

    def calculate_stadistics(self, information_list):
        time = 0
        for info in information_list:
            if info.typep == 'Call':
                self.numberCalls = self.numberCalls + 1
            elif info.typep == 'Conference':
                self.numberConferences = self.numberConferences + 1
            time = time + info.duration
            self.participant = int(info.participants) + int(self.participant)
        self.averageTime = round(time / len(information_list), 2)
        self.participant = round(self.participant / len(information_list), 0)
        self.totaltime = time

    def print_stadistics(self):
        print("Name: " + self.name + " Number Calls: " + str(self.numberCalls) + " Number Conferences " + str(
            self.numberConferences))
        print("Average time: " + str(self.averageTime) + " Number Participants: " + str(
            self.participant) + " Total time: " + str(self.totaltime))

    @property
    def return_line(self):
        line = self.name + " ;" + str(self.numberCalls) + " ;" + str(self.numberConferences) + "; " + str(
            self.averageTime) + " ; " + str(self.participant) + " ; " + str(self.totaltime) + "\n"
        return line

    def define_group(self, team, years):
        self.team = team
        self.years = years
