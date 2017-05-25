#!/usr/bin/env python
# encoding: utf-8

import time
import command
from apscheduler.schedulers.background import BackgroundScheduler

class TaskSchedule:
    '''任务调度'''

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def addJobs(self):
        '''
        year (int|str) – 4-digit year
        month (int|str) – month (1-12)
        day (int|str) – day of the (1-31)
        week (int|str) – ISO week (1-53)
        day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        hour (int|str) – hour (0-23)
        minute (int|str) – minute (0-59)
        second (int|str) – second (0-59)
        start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
        end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
        timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
        '''
        self.scheduler.add_job(command.test, 'cron', day_of_week='0-4', second='*/3')

    def run(self):
        try:
            print '%s schedule start %s' % ('*' * 10, '*' * 10)
            self.addJobs()
            self.scheduler.start()
            while True:
                time.sleep(3)
        except KeyboardInterrupt, SystemExit:
            self.scheduler.shutdown()
            print '%s schedule end %s' % ('*' * 10, '*' * 10)


if __name__ == '__main__':
    ts = TaskSchedule()
    ts.run()
