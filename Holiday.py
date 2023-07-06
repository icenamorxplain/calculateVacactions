# importing the random module
import random
import datetime
import calendar

PUBLICHOLIDAYJANUARY='06.01'
PUBLICHOLIDAYMARCH='20.03'
PUBLICHOLIDAYEASTER='06.04'
PUBLICHOLIDAYEASTER2='07.04'
PUBLICHOLIDAYMAY='01.05'

REGIONALHOLIDAYMAY='02.05'
REGIONALHOLIDAYMAY2='15.05'

REGIONALHOLIDAYMAYCR='31.05'

REGIONALHOLIDAYJUNCR='05.06'
REGIONALHOLIDAYJUNCR8='08.06'

PUBLICHOLIDAYAUGUST='15.08'

REGIONALHOLIDAYAUGUST='22.08'

PUBLICHOLIDAYOCTOBER='12.10'
PUBLICHOLIDAYNOVEMBER='01.11'

REGIONALHOLIDAYNOVEMBER='09.11'

PUBLICHOLIDAYDECEMBER='06.12'
PUBLICHOLIDAYDECEMBER8='08.12'
PUBLICHOLIDAYDECEMBER25='25.12'

startHolidays='26.06'
endHolidays='30.09'
TOTALHOLIDAYS = 27
percentajeWeeks=0.67

NUMBERWEEKS= 53

class Holiday:

    def __init__(self):
        self.initialDay = 1
        self.initialMonth = 6
        self.lastDay = 1
        self.lasMounth = 6
        self.numberDays=0
        self.restDays = (TOTALHOLIDAYS -self.numberDays)
        self.weeks = [5] * NUMBERWEEKS

    def select_summer_holidays(self):
         m = random.randint(7, 9)
         return m

    def list_day_works(self, year, location):
        day = int(PUBLICHOLIDAYJANUARY.split('.')[0])
        month = int(PUBLICHOLIDAYJANUARY.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYEASTER.split('.')[0])
        month = int(PUBLICHOLIDAYEASTER.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYEASTER2.split('.')[0])
        month = int(PUBLICHOLIDAYEASTER2.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYMAY.split('.')[0])
        month = int(PUBLICHOLIDAYMAY.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYAUGUST.split('.')[0])
        month = int(PUBLICHOLIDAYAUGUST.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYOCTOBER.split('.')[0])
        month = int(PUBLICHOLIDAYOCTOBER.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYNOVEMBER.split('.')[0])
        month = int(PUBLICHOLIDAYNOVEMBER.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYDECEMBER.split('.')[0])
        month = int(PUBLICHOLIDAYDECEMBER.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYDECEMBER8.split('.')[0])
        month = int(PUBLICHOLIDAYDECEMBER8.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1
        day = int(PUBLICHOLIDAYDECEMBER25.split('.')[0])
        month = int(PUBLICHOLIDAYDECEMBER25.split('.')[1])
        dn = datetime.date(year, month, day).isocalendar().week
        self.weeks[dn] = self.weeks[dn] - 1

        ##Madrid
        if (location == 'M'):
            day = int(PUBLICHOLIDAYMARCH.split('.')[0])
            month = int(PUBLICHOLIDAYMARCH.split('.')[1])
            dn = datetime.date(year, month, day).isocalendar().week
            self.weeks[dn] = self.weeks[dn] - 1
            day = int(REGIONALHOLIDAYMAY2.split('.')[0])
            month = int(REGIONALHOLIDAYMAY2.split('.')[1])
            dn = datetime.date(year, month, day).isocalendar().week
            self.weeks[dn] = self.weeks[dn] - 1
            day = int(REGIONALHOLIDAYNOVEMBER.split('.')[0])
            month = int(REGIONALHOLIDAYNOVEMBER.split('.')[1])
            dn = datetime.date(year, month, day).isocalendar().week
            self.weeks[dn] = self.weeks[dn] - 1
        elif (location == 'C'):
        #CIUDAD REAL
            day = int(REGIONALHOLIDAYMAYCR.split('.')[0])
            month = int(REGIONALHOLIDAYMAYCR.split('.')[1])
            dn = datetime.date(year, month, day).isocalendar().week
            self.weeks[dn] = self.weeks[dn] - 1
            day = int(REGIONALHOLIDAYJUNCR.split('.')[0])
            month = int(REGIONALHOLIDAYJUNCR.split('.')[1])
            dn = datetime.date(year, month, day).isocalendar().week
            self.weeks[dn] = self.weeks[dn] - 1
            day = int(REGIONALHOLIDAYJUNCR8.split('.')[0])
            month = int(REGIONALHOLIDAYJUNCR8.split('.')[1])
            dn = datetime.date(year, month, day).isocalendar().week
            self.weeks[dn] = self.weeks[dn] - 1
            day = int(REGIONALHOLIDAYAUGUST.split('.')[0])
            month = int(REGIONALHOLIDAYAUGUST.split('.')[1])
            dn = datetime.date(year, month, day).isocalendar().week
            self.weeks[dn] = self.weeks[dn] - 1
        return self.weeks

    def list_get_holidays(self, year,month, day, duration):
        dn = datetime.date(year, month, day).isocalendar().week
        numberDay = calendar.weekday(year, month, day)
        numberDaysCurrentWeek = 0
        if(numberDay < 5 and duration == 2):
            print("2 weeks between weeks: " + str( numberDay))
            numberDaysCurrentWeek = 5 - numberDay
            self.weeks[dn] = numberDaysCurrentWeek
            self.weeks[dn+1] = 0
            self.weeks[dn+2] = numberDay
            self.restDays = self.restDays - 10
        elif (duration == 2):
            print("2 weeks: " + str( numberDay))
            self.weeks[dn + 1] = 0
            self.weeks[dn + 2] = 0
            self.restDays = self.restDays - 10
        elif(numberDay < 5 and duration == 3):
            print("3 weeks between weeks: " + str( numberDay))
            numberDaysCurrentWeek = 5 - numberDay
            self.weeks[dn] = numberDaysCurrentWeek
            self.weeks[dn + 1] = 0
            self.weeks[dn + 2] = 0
            self.weeks[dn + 3] = numberDay
            self.restDays = self.restDays - 15
        else:
            print("3 weeks: " + str( numberDay))
            self.weeks[dn + 1] = 0
            self.weeks[dn + 2] = 0
            self.weeks[dn + 3] = 0
            self.restDays = self.restDays - 15
        ##print("remain holidays: " + str(self.restDays))
        return self.weeks

    def list_get_chrismast(self, month):
        duration = random.randint (1,2)
        if (month == 12 and duration == 1):
            self.weeks[len(self.weeks)-1] = 0
            self.restDays = self.restDays - 4
        elif (month == 12 and duration == 2):
            self.weeks[len(self.weeks)-1] = 0
            self.weeks[1] = 0
            self.restDays = self.restDays - 8
        elif(month == 13 and duration == 1):
            self.weeks[1] = 0
            self.restDays = self.restDays - 4
        elif(month == 13 and duration == 2):
            self.weeks[1] = 0
            self.weeks[2] = 0
            self.restDays = self.restDays - 9

        ##print("remain holidays: " + str(self.restDays))
        return self.restDays

    def random_selection_weeks(self, year):
        for i in range (int(self.restDays/5 + 1)):
            duration = random.randint (1,6)
            if (duration == 1 and self.restDays  > 2):
                day = int(PUBLICHOLIDAYEASTER.split('.')[0])
                month = int(PUBLICHOLIDAYEASTER.split('.')[1])
                dn = datetime.date(year, month, day).isocalendar().week
                self.weeks[dn] = 0
                self.restDays = self.restDays - 3
            if (duration == 2 and self.restDays  > 2):
                day = int(PUBLICHOLIDAYEASTER.split('.')[0])
                month = int(PUBLICHOLIDAYEASTER.split('.')[1])
                dn = datetime.date(year, month, day).isocalendar().week
                self.weeks[dn] = 0
                self.restDays = self.restDays - 3
            if (duration ==  3 and self.restDays  > 3 ):
                day = int(PUBLICHOLIDAYNOVEMBER.split('.')[0])
                month = int(PUBLICHOLIDAYNOVEMBER.split('.')[1])
                dn = datetime.date(year, month, day).isocalendar().week
                self.weeks[dn] = 0
                self.restDays = self.restDays - 4
            if (duration == 4 and self.restDays  > 2):
                day = int(PUBLICHOLIDAYDECEMBER8.split('.')[0])
                month = int(PUBLICHOLIDAYDECEMBER8.split('.')[1])
                dn = datetime.date(year, month, day).isocalendar().week
                self.weeks[dn] = 0
                self.restDays = self.restDays - 3
            if (duration == 5 and self.restDays  > 2):
                day = int(PUBLICHOLIDAYDECEMBER.split('.')[0])
                month = int(PUBLICHOLIDAYDECEMBER.split('.')[1])
                dn = datetime.date(year, month, day).isocalendar().week
                self.weeks[dn] = 0
                self.restDays = self.restDays - 3
            if (duration == 6 and self.restDays  > 2):
                day = int(REGIONALHOLIDAYJUNCR.split('.')[0])
                month = int(REGIONALHOLIDAYJUNCR.split('.')[1])
                dn = datetime.date(year, month, day).isocalendar().week
                self.weeks[dn] = 0
                self.restDays = self.restDays - 3
            if (duration == 7 and duration > 2):
                day = int(REGIONALHOLIDAYMAY2.split('.')[0])
                month = int(REGIONALHOLIDAYMAY2.split('.')[1])
                dn = datetime.date(year, month, day).isocalendar().week
                self.weeks[dn] = 0
                self.restDays = self.restDays - 3
            ##print("remain holidays: " + str(self.restDays))
        ##print("end random selection: " + str(self.restDays))