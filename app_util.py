import time
import datetime
import os


def gettickcount():
    current_time = time.time()
    return int(round(current_time * 1000))


def now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def is_process_alive(proceess_name):
    cmd = '''
    ps -ef | egrep -i "{}" | grep -v grep | wc -l
    '''.format(proceess_name)
    cmd = cmd.strip()
    result = os.popen(cmd).read()
    return int(result) > 0

def last_log_file(logdir):
    cmd = '''
    ls -rt %s|egrep -i "debug.log\.*"| awk 'END {print}'
    ''' % (logdir)
    cmd = cmd.strip()
    # print(cmd)
    result = os.popen(cmd).read()
    result = result.strip()
    if not result:
        return ""
    return logdir + "/" + result