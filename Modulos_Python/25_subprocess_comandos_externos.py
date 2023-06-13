import subprocess
import sys

print(sys.platform)

cmd = ['ping', '127.0.0.1', '-c', '4']
enconding = 'utf_8'
system = sys.platform

if system == 'win32':
    cmd = ['ping', '127.0.0.1']
    enconding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=enconding,
)

print()
print(proc.stdout)