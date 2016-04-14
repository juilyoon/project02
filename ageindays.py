# Age in Days
# by Juil
#
# My solution to the problem presented here:
# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4184188665/concepts/1083253730923
#
# Problem:
# Given your birthday and the current date, calculate your age in days. Compensate for leap days. Assume that the birthday and current date are correct dates (and no time travel). Simply put, if you were born 1 Jan 2012 and today's date is 2 jan 2012, you are 1 day old.

import datetime

daysinMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysinLeapMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getDate():
    '''Return the date as a dict'''
    t = datetime.datetime.now()
    today = {'y':1, 'm':1, 'd':1}
    today['y'], today['m'], today['d'] = t.year, t.month, t.day
    return today

def isLeap(year):
    return year % 4 == 0

def getDays(day):
    if isLeap(day['y']):
        return daysinLeapMonth[day['m']-1] - day['d']
    else:
        return daysinMonth[day['m']-1] - day['d']

def daysBetween(d1, d2):
    # Calculate days in full years only >>> number of days
    years, y = range(d1['y'], d2['y']), 0
    months = []
    days = 0
    if len(years)>0:
        y = (len(years) - 1) * 365
        for i in years[1:]:
            if isLeap(i):
                y += 1
        # Calculate days in full months >>> list of months
        if isLeap(d1['y']):
            months += daysinLeapMonth[d1['m']:]
        else:
            months += daysinMonth[d1['m']:]
        if isLeap(d2['y']):
            months += daysinLeapMonth[:d2['m']-1]
        else:
            months += daysinMonth[:d2['m']-1]
        # Calculate left over days
        days += getDays(d1) + daysinMonth[d2['m']]
    # Months in the same year
    elif d1['m'] != d2['m']:
        if isLeap(d1['y']):
            months += daysinLeapMonth[d1['m']:d2['m']-1]
        else:
            months += daysinMonth[d1['m']:d2['m']-1]
        # Calculate left over days
        days += getDays(d1) + daysinMonth[d2['m']]
    else: # Days in same year and month
        days = d2['d'] - d1['d']

    # Calculate days
    return y + sum(months) + days

def getBirthday():
    '''Receive input from user
    Return dict with birthday'''
    birthday = {'y': 1, 'm': 1, 'd': 1}

    print "When is your birthday?"
    birthday['y'] = int(raw_input('Year:'))
    birthday['m'] = int(raw_input('Month:'))
    birthday['d'] = int(raw_input('Day:'))
    print birthday

def main():
    today = getDate()
    print "Today is: {d}-{m}-{y}".format(**today)

    birthday = getBirthday()

    days = daysBetween(birthday, today)
    print "You are", days, "days old!"
if __name__ == '__main__':
    #Test Cases
    today = getDate()
    print "Today", today

    bday = today.copy()
    print bday
    print daysBetween(bday, today), "days old."
    #>>> 0
    bday = today.copy()
    bday['d'] -= 1
    print bday
    print daysBetween(bday, today), "days old."
    #>>> 1
    bday = today.copy()
    bday['m'] -= 1
    print bday
    print daysBetween(bday, today), "days old."
    #>>> 30~31 #FIXME: Days not calculated correctly
    bday = today.copy()
    bday['y'] -= 1
    print bday
    print daysBetween(bday, today), "days old."
    #>>> 365 #FIXME: Days not calculated correctly

    ###
    # main()
