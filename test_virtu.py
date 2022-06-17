import os
import subprocess
source="test_1"
dest="test_2"

cmd_1=(f"ls {source} > {source}_file.txt")
os.system(cmd_1)
cmd_2=(f"ls {dest} > {dest}_file.txt")
os.system(cmd_2)

cmd_3=subprocess.run(['comm','-23',(f'{source}_file.txt'),(f'{dest}_file.txt')],stdout=subprocess.PIPE)
dir=cmd_3.stdout.decode('utf-8')
cmd_4=['cp', '-r', f'/Users/vikramsingh/vikrams_projects/learn_python/exercises/{source}/2.1.0', f'/Users/vikramsingh/vikrams_projects/learn_python/exercises/{dest}/']
subprocess.run(cmd_4, stdout=subprocess.PIPE)

