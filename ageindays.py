# Age in Days
# by Juil
#
# My solution to the problem presented here:
# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4184188665/concepts/1083253730923
#
# Problem:
# Given your birthday and the current date, calculate your age in days. Compensate for leap days. Assume that the birthday and current date are correct dates (and no time travel). Simply put, if you were born 1 Jan 2012 and today's date is 2 jan 2012, you are 1 day old.

#TODO:0 Write simple mechanical solution: Add days

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
    '''From Wikipedia https://en.wikipedia.org/wiki/Leap_year#Algorithm
            if (year is not divisible by 4) then (it is a common year)
            else if (year is not divisible by 100) then (it is a leap year)
            else if (year is not divisible by 400) then (it is a common year)
            else (it is a leap year)'''
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

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
        elif d1['m'] == d2['m']:
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
    total = y + sum(months) + days
    # print y, sum(months), days  # TEST
    # print total
    return total

def getBirthday():
    '''Receive input from user
    Return dict with birthday'''
    # DONE:0 Test for input validity
    birthday = {'y': 1, 'm': 1, 'd': 1}

    print "When is your birthday?"
    year = raw_input('Year: ')
    while not year.isdigit() or not int(year) in range(1, 3000):
        year = raw_input('Please enter a valid year: ')
    month = raw_input('Month: ')
    while not month.isdigit() or not int(month) in range(1, 13):
        month = raw_input('Please enter a valid month: ')
    day = raw_input('Day: ')
    while not day.isdigit() or \
            not int(day) in range(1, daysinLeapMonth[int(month)]+1):
        day = raw_input('Please enter a valid day: ')

    birthday['y'] = int(year)
    birthday['m'] = int(month)
    birthday['d'] = int(day)
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
    '''Copied from [Udacity](https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4184188665/concepts/1082817710923)'''

    # # Assert checks for functions here
    # assert daysBetween({'y':2012, 'm':1, 'd':1},{'y':2012, 'm':1, 'd':2}) == 1

    test_cases = [(({'y':2012, 'm':1, 'd':1},{'y':2012, 'm':2, 'd':28}), 58),
                  (({'y':2012, 'm':1, 'd':1},{'y':2012, 'm':3, 'd':1}), 60),
                  (({'y':2011, 'm':6, 'd':30},{'y':2012, 'm':6, 'd':30}), 366),
                  (({'y':2011, 'm':1, 'd':1},{'y':2012, 'm':8, 'd':8}), 585 ),
                  (({'y':2008, 'm':1, 'd':1},{'y':2012, 'm':8, 'd':8}), 585 + 365*3 + 1 ),
                  (({'y':1900, 'm':1, 'd':1},{'y':1999, 'm':12, 'd':31}), 36523), # Fixed with proper leap year calculation
                  (({'y':2016, 'm':1, 'd':1},{'y':2012, 'm':3, 'd':1}), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetween(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)

if __name__ == '__main__':
    #DONE:10 Move test cases to separate function
    # test()
    main()
