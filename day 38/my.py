import os
import re
import sys
from pprint import pprint
import time

proc_dir = "/proc"


def search_all_user(file_path_with_file_name: str) -> list:
    result = []
    if os.path.exists(file_path_with_file_name):
        with open(file_path_with_file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                block = line.split(":")
                uid_user_name = (block[0], block[2])
                result.append(uid_user_name)

    return result


USER_LIST = search_all_user("/etc/passwd")


# output_list = [
#     {
#         "user": "some_user,str",
#         "pid": "some_pid, int",
#         "%CPU": "some_cpu_load,float",
#         "%MEM": "some_mem_load,float",
#         "VSZ": "some_virt_sizw_mem, int",
#         "RSS": "resident_set_size int",
#         "Stat": "idle,sleep,zombie...",
#
#     }
# ]


def pid_search(path_to_file: str) -> str:
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r'^Pid:', line):
                line = line.split(":")
                return line[1].strip()


def proc_name(path_to_file: str) -> str:
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r'^Name:', line):
                line = line.split(":")
                return line[1].strip()


output = []


def user_name(path_to_file: str) -> str:
    global USER_LIST
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r'^Uid:', line):
                for record in USER_LIST:
                    if re.split(r'[:\s]', line)[2] in record:
                        return record[0]


def rss_value(path_to_file: str) -> float:
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            return round(float((int(line.strip().split(" ")[1]) * 4) / 1024), 2)


def vsz_value(path_to_file: str) -> float:
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # переписать формулу, добавить множитель на 4
            return round(float((int(line.strip().split(" ")[0]) * 4) / 1024), 2)


def tty_check(path_to_file: str):
    try:
        return os.readlink(f'{path_to_file}/fd/0')
    except OSError:
        return ""


def check_state(path_to_file: str):
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r'^State:', line):
                line = line.split(":")
                return line[1].strip().split(" ")[0]


def get_start_time(pid):
    with open(f"/proc/{pid}/stat", 'r') as f:
        data = f.readline().split()
        start_time_ticks = float(data[21])
    start_time_seconds = start_time_ticks / os.sysconf(os.sysconf_names['SC_CLK_TCK'])
    boot_time = float(os.popen('cat /proc/stat | grep btime | awk \'{print $2}\'').read())
    process_start_time = boot_time + start_time_seconds
    return time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(process_start_time))


def get_start_procces(path_to_file):
    with open(path_to_file, 'r') as f:
        return f.readline()


for item in os.listdir(proc_dir):
    if item.isdigit():
        pid = item

        status_file = os.path.join(proc_dir, pid)
        if os.path.exists(status_file):
            output.append(
                {
                    "User": user_name(os.path.join(proc_dir, pid, 'status')),
                    "ProcName": proc_name(os.path.join(proc_dir, pid, 'status')),
                    "Pid": pid_search(os.path.join(proc_dir, pid, 'status')),
                    "VSZ": f"{vsz_value(os.path.join(proc_dir, pid, 'statm'))}Mb",
                    "RSS": f"{rss_value(os.path.join(proc_dir, pid, 'statm'))}Mb",
                    "TTY": f"{tty_check(os.path.join(proc_dir, pid))}",
                    "Stat": f"{check_state(os.path.join(proc_dir, pid, 'status'))}",
                    "Start": f"{get_start_time(pid)}",
                    "Command": f"{get_start_procces(os.path.join(proc_dir, pid, 'cmdline'))}"
                }
            )

pprint(output, width=500)
