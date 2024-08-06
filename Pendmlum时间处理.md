Pendmlim时间处理代码示例

```python
# 时间处理
import pendulum as pdl
from loguru import logger

# 获取当前时间
logger.info(pdl.now().to_date_string() + " " + pdl.now().to_time_string())
# 把当前时间转换为YYYY_MM_DD_HH_mm_ss格式
logger.info(pdl.now().format("YYYY_MM_DD_HH_mm_ss"))
# 获取当前时间戳
logger.info(pdl.now().timestamp())
# 把当前时间戳转换为时间
logger.info(pdl.from_timestamp(int(str(pdl.now().add(hours=8).timestamp()).split('.')[0])))


# timestamp的长度为10位，如果是13位则无法解析
# 使用 Pendulum 从时间戳创建一个 DateTime 对象
dt_obj = pendulum.from_timestamp(timestamp)

# 打印转换后的时间
print(dt_obj)

# 如果需要以特定格式输出时间，可以使用 format 方法
formatted_time = dt_obj.format('%Y-%m-%d %H:%M:%S')
print(formatted_time)

now_ = pendulum.now().add(days=1)
# 当前日期加1天
print(now_.add(days=1))
# 当前日期减1天
print(pendulum.today().subtract(days=1))


# 计算当前日期和时间与指定日期和时间之间的差值
now = pendulum.now()
dt = pendulum.datetime(2021, 10, 1, 12, 30, 45)
diff = now.diff(dt)
print(diff.in_days())

# 计算指定日期和时间与指定日期和时间之间的差值
dt1 = pendulum.datetime(2021, 10, 1, 12, 30, 45)
dt2 = pendulum.datetime(2021, 10, 2, 12, 30, 45)
diff = dt1.diff(dt2)
print(diff.in_hours())

# 计算指定时区的日期和时间与指定时区的日期和时间之间的差值
dt1 = pendulum.datetime(2021, 10, 1, 12, 30, 45, tz='Asia/Shanghai')
dt2 = pendulum.datetime(2021, 10, 2, 12, 30, 45, tz='Asia/Tokyo')
diff = dt1.diff(dt2)
print(diff.in_minutes())
```
