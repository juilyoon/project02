# Age in Days
# by Juil
#
# My solution to the problem presented here:
# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4184188665/concepts/1083253730923
#
# Problem:
# Given your birthday and the current date, calculate your age in days. Compensate for leap days. Assume that the birthday and current date are correct dates (and no time travel). Simply put, if you were born 1 Jan 2012 and today's date is 2 jan 2012, you are 1 day old.

#TODO:20 Write simple mechanical solution: Add days

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

def isDatesBefore(d1, d2):
    '''Test if day 2 comes after day 1'''
    if d1['y'] < d2['y']:
        return True
    elif d1['y'] == d2['y']:
        if d1['m'] < d2['m']:
            return True
        elif d1['m'] = d2['m']:
            return d1['d'] <= d2['d']
    return False

def daysBetween(d1, d2):
    #DONE:20 Test for input validity and that d1 < d2
    assert isDatesBefore(d1, d2)
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
        days += getDays(d1) + d2['d']
    # Months in the same year
    elif d1['m'] != d2['m']:
        if isLeap(d1['y']):
            months += daysinLeapMonth[d1['m']:d2['m']-1]
        else:
            months += daysinMonth[d1['m']:d2['m']-1]
        # Calculate left over days
        days += getDays(d1) + d2['d']
    else: # Days in same year and month
        days = d2['d'] - d1['d']

    # Calculate days
    # print y, sum(months), days  # TEST
    return y + sum(months) + days

def getBirthday():
    '''Receive input from user
    Return dict with birthday'''
    # TODO:10 Test for input validity
    birthday = {'y': 1, 'm': 1, 'd': 1}

    print "When is your birthday?"
    birthday['y'] = int(raw_input('Year: '))
    birthday['m'] = int(raw_input('Month: '))
    birthday['d'] = int(raw_input('Day: '))
    return birthday

def main():
    today = getDate()
    print "Today is: {d}-{m}-{y}".format(**today)

    birthday = getBirthday()

    days = daysBetween(birthday, today)

    if today['m']==birthday['m'] and today['d']==birthday['d']:
        print "Happy birthday!"

    print "You are", days, "days old!"

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

if __name__ == '__main__':
    ### #TODO:0 Move test cases to separate function
    print "Unit Tests"
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
    #>>> 30~31       #DONE:0 Days not calculated correctly
    bday = today.copy()
    bday['y'] -= 1
    print bday
    print daysBetween(bday, today), "days old."
    #>>> 365~366     #DONE:10 Days not calculated correctly

    ###
    main()
