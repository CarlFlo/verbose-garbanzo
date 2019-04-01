from datetime import datetime  
from datetime import timedelta 

now = datetime.now() + timedelta(days=(365*70))

print(now)