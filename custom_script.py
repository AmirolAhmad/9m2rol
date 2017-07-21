#! /usr/bin/python
import subprocess
import sys
from time import gmtime, strftime
import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc):

    print('='*30)
    print('iStats Performance')
    print('='*30)
    print(subprocess.run(["istats"]))
    print('='*30)

    # log the above status
    f = open('outfile.txt', 'a')
    f.write(strftime("%d-%m-%Y %H:%M:%S : ", gmtime()))
    f.write('iStat Complete\n')
    f.close()
    s.enter(30, 1, do_something, (sc,))

s.enter(30, 1, do_something, (s,))
s.run()
