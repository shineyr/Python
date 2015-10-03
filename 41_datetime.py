__author__ = 'Admin'

import time
from datetime import datetime
# from _datetime import datetime

# 获取当前时间
print(datetime.now())

print(type(datetime.now()))

# 用指定时间创建datetime
dt = datetime(2015,10,3,16,40)
print(dt)

# datetime转换为timestamp
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
print(dt.timestamp())

t = 1443861600.0
print(datetime.fromtimestamp(t))

# 字符串str与datetime互相转换
cday = datetime.strptime('2015-10-3 16:43:10','%Y-%m-%d %H:%M:%S')

print(cday)

# datetime加减
from datetime import timedelta
now = datetime.now();
print(now)

now = now + timedelta(hours = 10)

print(now)

now = now - timedelta(days = 1)
print(now)

# 本地时间转换UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间
from datetime import timezone

tz_utc_8 = timezone(timedelta(hours=8)) #创建时区UTC+8:00
now = datetime.now()

print(now)

now = datetime(2015, 5, 18, 17, 2, 10, 871012)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)

# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
