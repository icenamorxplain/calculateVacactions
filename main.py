# This is a sample Python script.
import InformationCall
import Person
import Holiday

# importing the random module
import random
import datetime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Stadistic


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def parse_line(line):
    if len(line) >= 3:
        parse_info = line.split(" ")
        print(parse_info)
        for parse in parse_info:
            parse = parse.replace(",", "")
        if parse_info[7] == 'last':
            parse_info.insert(7, "31")
        return parse_info


def read_file(name, list_person):
    file = open(name)
    try:
        # Usar el fichero
        number = 0
        person = Person.Person("name", [])
        for line in file.readlines():
            if 3 < len(line) < 120:
                person.name = line.strip()
            if len(line) > 37:
                number = number + 1
                separate = parse_line(line)
                # InformationCall.InformationCall("1c2bd166-fefc-4b85-a915-6193eea1b535", "Oct", "7", "2022", "3:00",
                # "PM", "GMT+2", "27", "2" , "00:01:16", "Call")
                example = InformationCall.InformationCall(separate[0], separate[1], separate[2], separate[3],
                                                          separate[4], separate[5], separate[6], separate[7],
                                                          separate[10], separate[12], separate[13])
                example.calculate_time()
                person.listCalls.append(example)
            elif number == 18:
                list_person.append(person)
                number = 0
                person = Person.Person("name", [])
        pass
    finally:
        # Esta sección es siempre ejecutada
        file.close()

def parse_line_holidays(line):
    if len(line) >= 3:
        parse_info = line.split(",")
        return parse_info

def write_file(list_persons, list_holidays):
    file = open("holidays_employees.csv", "w")
    for (f, b) in zip(list_persons, list_holidays):
        print("f:", f, " |  b:", b)
        linecache = f.name + "," + f.team + ","+ f.totaltime + ","+ str(int(f.totaltime)*5)
        weeks = ''
        print(b)
        for w in b.weeks:
                weeks = weeks + "," + str(w)
        linecache =  linecache + weeks + "," + f.location + "\n"
        file.write(linecache)

    file.close()

def read_file_holidays(name, persons):
    file = open(name)
    try:
        number = 0
        for line in file.readlines():
            if len(line) > 17:
                number = number + 1
                separate = parse_line_holidays(line)
                name = separate[0].strip()
                team = separate[1].strip()
                location = separate[3].strip()
                hour = separate[2].strip()
                person = Person.Person(name, team, hour, location)
                persons.append(person)
        pass
    finally:
        # Esta sección es siempre ejecutada
        file.close()
    return persons

# Press the green button in the gutter to run the script.
"""
    # PM GMT+2 27 days ago 2 Participants 00:01:16 Call  Microsoft  TeamsGood
    file = InformationCall.InformationCall("1c2bd166-fefc-4b85-a915-6193eea1b535", "Oct", "7", "2022", "3:00", "PM",
                                           "GMT+2", "27", "2", "00:01:16", "Call")
    file.calculate_time()
"""
YEAR = 2024
if __name__ == '__main__':
    print_hi('Start reading files...')
    # Read files
    list_person = []
    list_holidays = []
    list_person = read_file_holidays('C:\\Users\\isabel\\Desktop\\Planning\\employees.csv', list_person)
    for per in list_person:
        print(per)
        if (random.randint(0,2)==0): ## Only two weeks
            holi = Holiday.Holiday()
            month = holi.select_summer_holidays()
            day = random.randint (1,30)
            holi.list_day_works(YEAR, per.location)
            holi.list_get_holidays(YEAR,month,day, 2)
            chrismast = random.randint (12,13)
            holi.list_get_chrismast(chrismast)
            holi.random_selection_weeks(YEAR)
            list_holidays.append(holi)
            ##print(holi.weeks)
        else: ## 3 weeks
            holi = Holiday.Holiday()
            month = holi.select_summer_holidays()
            day = random.randint(1, 30)
            holi.list_day_works(YEAR, per.location)
            holi.list_get_holidays(YEAR, month, day, 3)
            chrismast = random.randint(12, 13)
            holi.list_get_chrismast(chrismast)
            holi.random_selection_weeks(YEAR)
            list_holidays.append(holi)
            ##print(holi.weeks)
    write_file(list_person, list_holidays)
    """
    stadistic_call = Stadistic.Stadistic(0, "CALL")
    stadistic_conference = Stadistic.Stadistic(0, "CONFERENCE")
    
    read_file('C:\\Users\\isabel\\Desktop\\clienData.txt', list_person)
    read_file('C:\\Users\\isabel\\Desktop\\examples.txt', list_person2)
    read_file('C:\\Users\\isabel\\Desktop\\webandMObile.txt', list_person3)

    f = open('C:\\Users\\isabel\\Desktop\\summary.txt', "w+")
    f.write("Name ; number_Calls ; number_Conferences ; average_time ; participants ; total_time \n")
    conferences = []
    for person in list_person:
        #print(person)
        person.calculate_stadistics(person.listCalls)
        #person.print_stadistics()
        f.write(person.return_line)
        stadistic_call.calculate_call(person.listCalls)
        conferences.append(stadistic_conference.calculate_conference(person.listCalls))
    for person in list_person2:
        #print(person)
        person.calculate_stadistics(person.listCalls)
        #person.print_stadistics()
        f.write(person.return_line)
        stadistic_call.calculate_call(person.listCalls)
        conferences.append(stadistic_conference.calculate_conference(person.listCalls))
    for person in list_person3:
        #print(person)
        person.calculate_stadistics(person.listCalls)
        #person.print_stadistics()
        f.write(person.return_line)
        stadistic_call.calculate_call(person.listCalls)
        conferences.append(stadistic_conference.calculate_conference(person.listCalls))
    f.close()
    print (conferences)"""


