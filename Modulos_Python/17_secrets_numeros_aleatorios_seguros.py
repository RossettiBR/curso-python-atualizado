import secrets
import string as s 
from secrets import SystemRandom as sr

print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=15)))

random = secrets.SystemRandom()
