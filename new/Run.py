import sys
sys.path.insert(0,'../banner')
from banner import banner

t = banner
v = t.choices()
print(dir(v))