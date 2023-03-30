# 1. 获取日期 、时间

	import pendulum
	# 获取当前时间 类型为: datetime
	print(f'now:{pendulum.now()}')
	# 返回今天的时间 0时刻
	print(f'today={pendulum.today()}')
	# 昨天日期 0时刻
	print(f'yesterday={pendulum.yesterday()}')
	# 明天日期 0时刻
	print(f'tomorrow={pendulum.tomorrow()}')

# 2.日期、日期时间 转字符串

	import pendulum
	# 转化成日期时间字符串
	print(f'datetime_str={pendulum.now().to_datetime_string()}')
	# 转化成日期字符串
	print(f'date_str={pendulum.now().to_date_string()}')
	# 转换成时间字符串 内部调用的是 format 函数  采用标准的格式串
	print(f'time_str={pendulum.now().to_time_string()}')
	# 转换自定义的数据串
	print(f"datetime_str(s)={pendulum.now().format('YYYY-MM-DD')}")
	# 获取当前时间戳
	logger.info(pdl.now().timestamp())
	# 把当前时间戳转换为时间
	logger.info(pdl.from_timestamp(int(str(pdl.now().add(hours=8).timestamp()).split('.')[0])))

# 3.字串串转 日期 日期时间类型
	import pendulum
	print(f"str_datetime:{pendulum.from_format('2022-02-01', 'YYYY-MM-DD')}")
	# 智能解析
	print(f"str_date:{pendulum.parse('2022-02-01 23:00:00')}")
	# 将时间戳装换成 日期时间类型
	print(f'timestamp = {pendulum.from_timestamp(time.time())}')

# 4.时间进行加减法运算

	import pendulum
	now_ = pendulum.now().add(days=1)
	# 当前日期加1天
	print(now_.add(days=1))
	# 当前日期减1天
	print(pendulum.today().subtract(days=1))

# 5.生成时间序列
	
	subtract(days=3)).range('days')
	for dt in dt_series:
	    print(f'dt={dt.to_date_string()}')

# 6.常用案例-获取月初日期

	# 获取指定日期的月初日期 默认为当前日期的月初
	def get_begin_of_month_base(data_str=None):
	    if not data_str:
	        data_str = get_current_date_str()[0:8]
	    else:
	        data_str = data_str[0:8]
	    return data_str + '01'
	
	def get_begin_of_month(data_str=None):
	    data_str = pendulum.today() if data_str is None else pendulum.parse(data_str)
	    date_str = data_str.replace(day=1).date().__str__()
	    return date_str

# 7.常用案例-获取下个月的月初日期
	
	def get_next_month_begin_date_base(date_str=None):
	    if not date_str:
	        date_str = get_current_date_str()
	    year = int(date_str[0:4])
	    month = int(date_str[5:7])
	    if month != 12:
	        month += 1
	    else:
	        year += 1
	        month = 1
	    result_date = str(year) + '-' + str(month).zfill(2) + '-01'
	    logg.info(f'result_date:{result_date}')
	    return result_date
	
	def get_next_month_begin_date(date_str=None):
	    import pendulum
	    if date_str is None:
	        dt = pendulum.today()
	    else:
	        dt = pendulum.parse(date_str)
	    dt_str = dt.add(months=1).replace(day=1).date().__str__()
	    logg.info(f'dt_str={dt_str}')
	    return dt_str

# 8.常用案例-获取指定日期的月末日期(默认当前日期)


	def get_current_date_str():
	    import pendulum
	    dt_str = pendulum.today().to_date_string()
	    logg.info(f'dt_str={dt_str}')
	    return dt_str
	def get_last_day_of_month(date_str=None):
	    import calendar
	    date_str = get_current_date_str() if date_str is None else date_str
	    year_ = int(date_str[:4])
	    month_ = int(date_str[5:7])
	# monthrange 函数返回两个值 星期 当月的最后一天日期
	    days = calendar.monthrange(year_, month_)[1]
	    return days


# 9.常用案例-日期运算

	def date_add(start_dt, amount, unit='d', to_str=True):
	    dt_ = pendulum.parse(start_dt)
	    assert unit in ('y', 'm', 'w', 'd'), ValueError(f'invalid unit type={unit}'
	                                                    f'only(y,m,w,d)')
	    unit_mapping = {
	        'y': 'years',
	        'm': 'months',
	        'w': 'weeks',
	        'd': 'days'
	    }
	    kv = {
	        unit_mapping[unit]: amount
	    }
	    tmp = dt_.add(**kv)
	    if to_str:
	        dt_str = tmp.to_date_string()
	        logg.info(f'dt_str={dt_str}')
	        return dt_str
	    else:
	        logg.info(f'tmp={tmp}')
	        return tmp


# 10.常用案例-产生日期区间
	
	def generate_data_range(start_date: str, amount, unit='d', ft='YYYY-MM-DD'):
	    assert unit in ('y', 'm', 'w', 'd'), ValueError(f'invalid unit type={unit}'
	                                                    f'only(y,m,w,d)')
	    logg.info(f'start_date={start_date}')
	    logg.info(f'amount={amount}')
	    if amount == 1:
	        logg.info(f'{[start_date]}')
	        return [start_date]
	    else:
	        unit_mapping = {
	            'y': 'years',
	            'm': 'months',
	            'w': 'weeks',
	            'd': 'days'
	        }
	        kv = {
	            unit_mapping[unit]: amount - 1
	        }
	        logg.info(f'unit={unit_mapping[unit]}')
	        end = pendulum.from_format(start_date, ft)
	        start = end.subtract(**kv)
	        dt_series = pendulum.period(start, end).range(unit_mapping[unit])
	        dt = [val.to_date_string() for val in dt_series]
	        logg.info(f'dt={dt}')
	        return dt


# 11.常用案例-产生给定日期(周一~周五)的日期

	def get_week_day(start=None, current=False):
	    if start is None:
	        start = pendulum.today()
	    else:
	        start = pendulum.parse(start)
	    begin = start.start_of('week')
	    end = begin.add(days=6)
	    begin = begin.to_date_string()
	    end = start if current else end.to_date_string()
	    logg.info(f'start_date={begin}, end_date={end}')
	    return begin, end