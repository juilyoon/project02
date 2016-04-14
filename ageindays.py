# Age in Days
# by Juil
#
# My solution to the problem presented here:
# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4184188665/concepts/1083253730923
#
# Problem:
# Given your birthday and the current date, calculate your age in days. Compensate for leap days. Assume that the birthday and current date are correct dates (and no time travel). Simply put, if you were born 1 Jan 2012 and today's date is 2 jan 2012, you are 1 day old.

import datetime

today = {'y':1, 'm': 1, 'd': 1}
birthday = {'y':1, 'm': 1, 'd': 1}

def main(birthday, today):
    return True

if __name__ == '__main__':
    print "When is your birthday?"
    birthday['y'] = int(raw_input('Year:'))
    birthday['m'] = int(raw_input('Month:'))
    birthday['d'] = int(raw_input('Day:'))
    print birthday

    t = datetime.datetime.now()
    today['y', 'm', 'd'] = t.year, t.month, t.day
    print "Today is: {d}-{m}-{y}".format(**today)
