from datetime import datetime
from pytz import timezone
tz = timezone('US/Eastern')
fmt = '%Y-%m-%d %H:%M:%S'
y=datetime.now(tz)
print y.strftime(fmt)