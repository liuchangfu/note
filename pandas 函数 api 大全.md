API的整理来自[pandas 函数 api 大全 | pandas 教程 - 盖若 (gairuo.com)](https://gairuo.com/p/pandas-api)网站

## DataFrame

________

### 构造器 Constructor

| api                                            | 介绍                  |
| ---------------------------------------------- | ------------------- |
| DataFrame([data, index, columns, dtype, copy]) | 生成二维、大小可变、可为异构的表格数据 |

### 属性和基础数据 Attributes and underlying data

| api                                         | 介绍                           |
| ------------------------------------------- | ---------------------------- |
| DataFrame.index                             | DataFrame 的索引（行标签）           |
| DataFrame.columns                           | DataFrame的列标签                |
| DataFrame.dtypes                            | 返回DataFrame中的dtype           |
| DataFrame.info([verbose, buf, max_cols, …]) | 打印 DataFrame 的简要摘要           |
| DataFrame.select_dtypes([include, exclude]) | 根据列 dtypes 返回 DataFrame 列的子集 |
| DataFrame.values                            | 返回 DataFrame 的 Numpy 表示形式    |
| DataFrame.axes                              | 返回一个表示 DataFrame 轴的列表        |
| DataFrame.ndim                              | 返回一个表示轴数/数组维数的整数             |
| DataFrame.size                              | 返回表示此对象中元素数量的int             |
| DataFrame.shape                             | 返回一个表示 DataFrame 维数的元组       |
| DataFrame.memory_usage（[index，deep]）        | 返回每列的内存使用情况（以字节为单位）          |
| DataFrame.empty                             | 指示 DataFrame 是否为空            |
| DataFrame.set_flags(*[, copy, …])           | 返回带有更新标志的新对象                 |

### 转换 Conversion

| api                                          | 介绍                                    |
| -------------------------------------------- | ------------------------------------- |
| DataFrame.astype(dtype[, copy, errors])      | 将 pandas 对象转换为指定的 dtype dtype         |
| DataFrame.convert_dtypes([infer_objects, …]) | 使用支持 pd.NA 的 dtypes 将列转换为最佳可能的 dtypes |
| DataFrame.infer_objects()                    | 尝试为对象列推断更好的 dtype                     |
| DataFrame.copy([deep])                       | 复制该对象的索引和数据                           |
| DataFrame.bool()                             | 返回单个元素 Series 或 DataFrame 的布尔值        |

### 索引/迭代 Indexing, iteration

| api                                             | 介绍                                      |
| ----------------------------------------------- | --------------------------------------- |
| DataFrame.head([n])                             | 返回前 n 行                                 |
| DataFrame.at                                    | 访问行/列标签对的单个值                            |
| DataFrame.iat                                   | 通过整数位置访问行/列对的单个值                        |
| DataFrame.loc                                   | 通过标签或布尔数组访问一组行和列                        |
| DataFrame.iloc                                  | 基于位置的纯基于整数位置的索引                         |
| DataFrame.insert(loc, column, value[, …])       | 将列插入到DataFrame中的指定位置                    |
| DataFrame.__iter__()                            | 遍历轴信息                                   |
| DataFrame.items()                               | 遍历（列名，序列）对                              |
| DataFrame.iteritems()                           | 遍历（列名，序列）对                              |
| DataFrame.keys()                                | 获取轴信息                                   |
| DataFrame.iterrows()                            | 将 DataFrame 行作为（索引，系列）对迭代               |
| DataFrame.itertuples([index, name])             | 将 DataFrame 行迭代为 namedtuple             |
| DataFrame.lookup(row_labels, col_labels)        | DataFrame 基于标签的“花式索引”（fancy indexing）功能 |
| DataFrame.pop(item)                             | 删除并返回删除的内容                              |
| DataFrame.tail([n])                             | 返回最后 n 行                                |
| DataFrame.xs(key[, axis, level, drop_level])    | 从 Series/DataFrame 返回横截面。               |
| DataFrame.get(key[, default])                   | 从对象获取给定键的项目                             |
| DataFrame.isin(values)                          | DataFrame 中的每个元素是否包含在值中                 |
| DataFrame.where(cond[, other, inplace, …])      | 替换条件为 False 的值                          |
| DataFrame.mask(cond[, other, inplace, axis, …]) | 替换条件为 True 的值                           |
| DataFrame.query(expr[, inplace])                | 使用布尔表达式字符查询 DataFrame 的列                |

### 计算 (二元运算) Binary operator functions

| api                                              | 介绍                                              |
| ------------------------------------------------ | ----------------------------------------------- |
| DataFrame.add(other[, axis, level, fill_value])  | 加法 Addition（二元运算 radd）dataframe + other，下同      |
| DataFrame.sub(other[, axis, level, fill_value])  | 减法 Subtraction (二元运算 sub)，d - o                 |
| DataFrame.mul(other[, axis, level, fill_value])  | 乘法 Multiplication (二元运算 mul) ，d * o             |
| DataFrame.div(other[, axis, level, fill_value])  | 浮点除 Floating division (二元运算 truediv)，d / o      |
| DataFrame.truediv(other[, axis, level, …])       | 浮点除 Floating division (二元运算 truediv)，d / o      |
| DataFrame.floordiv(other[, axis, level, …])      | 整除 Integer division (二元运算 floordiv)，d // o      |
| DataFrame.mod(other[, axis, level, fill_value])  | 模数 Modulo (二元运算 mod)，d % o                      |
| DataFrame.pow(other[, axis, level, fill_value])  | 指数幂 Exponential power (二元运算 pow) ，`d ** o`      |
| DataFrame.dot(other)                             | 矩阵乘法 matrix multiplication，d @ o（py 3.5+）       |
| DataFrame.radd(other[, axis, level, fill_value]) | 加法 Addition，o + d，与上顺序相反（二元运算 radd）             |
| DataFrame.rsub(other[, axis, level, fill_value]) | (binary operator rsub).                         |
| DataFrame.rmul(other[, axis, level, fill_value]) | (binary operator rmul).                         |
| DataFrame.rdiv(other[, axis, level, fill_value]) | (binary operator rtruediv).                     |
| DataFrame.rtruediv(other[, axis, level, …])      | (binary operator rtruediv).                     |
| DataFrame.rfloordiv(other[, axis, level, …])     | (binary operator rfloordiv).                    |
| DataFrame.rmod(other[, axis, level, fill_value]) | (binary operator rmod).                         |
| DataFrame.rpow(other[, axis, level, fill_value]) | (binary operator rpow).                         |
| DataFrame.lt(other[, axis, level])               | 小于 Less than (二元运算 lt) ，d < o，对应位置的布尔值，下同       |
| DataFrame.gt(other[, axis, level])               | 大于 Greater (二元运算 gt)，d > o                      |
| DataFrame.le(other[, axis, level])               | 小于等于 Less than or equal to，(二元运算 le)，d <= o     |
| DataFrame.ge(other[, axis, level])               | 大于等于 Greater than or equal to， (二元运算 ge)，d >= o |
| DataFrame.ne(other[, axis, level])               | 不等于 Not equal to，(二元运算 ne)，d != o               |
| DataFrame.eq(other[, axis, level])               | 等于 Equal to， (二元运算 eq)，，d == o                  |
| DataFrame.combine(other, func[, fill_value, …])  | 与另一个 DataFrame 按列合并                             |
| DataFrame.combine_first(other)                   | 在其他位置相同的位置更新具有值的空元素                             |

### 函数应用/GroupBy/窗口 Function application, GroupBy & window

| api                                              | 介绍                               |
| ------------------------------------------------ | -------------------------------- |
| DataFrame.apply(func[, axis, raw, …])            | 沿 DataFrame 的轴应用函数               |
| DataFrame.applymap(func)                         | 将一个函数应用于所有元素                     |
| `DataFrame.pipe(func, *args, **kwargs)`          | 应用 `func(self, *args, **kwargs)` |
| DataFrame.agg([func, axis])                      | 使用指定轴上的一项或多项操作进行汇总               |
| DataFrame.aggregate([func, axis])                | DataFrame.agg 的全写                |
| DataFrame.transform(func[, axis])                | 调用 func 产生具有相同结构 DataFrame       |
| DataFrame.groupby([by, axis, level, …])          | 使用映射器或按一列对 DataFrame 进行分组        |
| DataFrame.rolling(window[, min_periods, …])      | 提供滚动窗口计算                         |
| DataFrame.expanding([min_periods, center, axis]) | 提供扩展的转换                          |
| DataFrame.ewm([com, span, halflife, alpha, …])   | 提供指数加权（EW）函数                     |

### 计算/描述性统计 Computations / descriptive stats

| api                                             | 介绍                         |
| ----------------------------------------------- | -------------------------- |
| DataFrame.abs()                                 | 每个元素的绝对数值                  |
| DataFrame.all([axis, bool_only, skipna, level]) | 返回是否所有元素都为 True（可沿着某个轴）    |
| DataFrame.any([axis, bool_only, skipna, level]) | 返回是否有任何元素为 True（可沿着某个轴）    |
| DataFrame.clip([lower, upper, axis, inplace])   | 按给定上下限值进行修剪（超出范围的采用此值）     |
| DataFrame.corr([method, min_periods])           | 计算列的相关性，不包括NA/空值           |
| DataFrame.corrwith(other[, axis, drop, method]) | 计算与其他 DataFrame/Series 相关性 |
| DataFrame.count([axis, level, numeric_only])    | 对每列或每行的非NA单元格进行计数          |
| DataFrame.cov([min_periods, ddof])              | 计算列的成对协方差，不包括NA/null值      |
| DataFrame.cummax([axis, skipna])                | 返回数据帧或序列轴上的累积最大值           |
| DataFrame.cummin([axis, skipna])                | 返回数据帧或序列轴上的累计最小值           |
| DataFrame.cumprod([axis, skipna])               | 返回数据帧或序列轴上的累积乘积            |
| DataFrame.cumsum([axis, skipna])                | 返回数据帧或序列轴上的累积和             |
| DataFrame.describe([percentiles, include, …])   | 生成描述性统计                    |
| DataFrame.diff([periods, axis])                 | 元素的第一离散差分                  |
| DataFrame.eval(expr[, inplace])                 | 计算描述对数据帧列的操作的字符串           |
| DataFrame.kurt([axis, skipna, level, …])        | 返回请求轴上的无偏峰度                |
| DataFrame.kurtosis([axis, skipna, level, …])    | 返回请求轴上的无偏峰度                |
| DataFrame.mad([axis, skipna, level])            | 返回所请求轴的值的平均绝对偏差            |
| DataFrame.max([axis, skipna, level, …])         | 返回请求轴的最大值                  |
| DataFrame.mean([axis, skipna, level, …])        | 返回请求轴的平均值                  |
| DataFrame.median([axis, skipna, level, …])      | 返回所请求轴的值的中位数               |
| DataFrame.min([axis, skipna, level, …])         | 返回请求轴的最小值                  |
| DataFrame.mode([axis, numeric_only, dropna])    | 沿选定轴获取元素的模                 |
| DataFrame.pct_change([periods, fill_method, …]) | 当前元素和前一元素之间的百分比变化          |
| DataFrame.prod([axis, skipna, level, …])        | 返回所请求轴的值的乘积                |
| DataFrame.product([axis, skipna, level, …])     | 返回所请求轴的值的乘积                |
| DataFrame.quantile([q, axis, numeric_only, …])  | 返回请求轴上给定分位数处的值             |
| DataFrame.rank([axis, method, numeric_only, …]) | 沿轴计算数值数据列（1到n）             |
| DataFrame.round([decimals])                     | 将数据帧舍入到可变的小数位数             |
| DataFrame.sem([axis, skipna, level, ddof, …])   | 返回请求轴上平均值的无偏标准误差           |
| DataFrame.skew([axis, skipna, level, …])        | 返回请求轴上的无偏倾斜                |
| DataFrame.sum([axis, skipna, level, …])         | 返回请求轴上的无偏倾斜                |
| DataFrame.std([axis, skipna, level, ddof, …])   | 返回请求轴上的样本标准偏差              |
| DataFrame.var([axis, skipna, level, ddof, …])   | 返回请求轴上的无偏方差                |
| DataFrame.nunique([axis, dropna])               | 计算请求轴上的不同观察值               |
| DataFrame.value_counts([subset, normalize, …])  | 返回数据帧中包含唯一行计数的序列           |

### 重新索引/选择/标签操作 Reindexing / selection / label manipulation

| api                                             | 介绍                             |
| ----------------------------------------------- | ------------------------------ |
| DataFrame.add_prefix(prefix)                    | 标签前缀增加字符串                      |
| DataFrame.add_suffix(suffix)                    | 带字符串后缀的后缀标签                    |
| DataFrame.align(other[, join, axis, level, …])  | 使用指定的连接方法在轴上对齐两个对象             |
| DataFrame.at_time(time[, asof, axis])           | 选择一天中特定时间的值 (如 9:30AM)         |
| DataFrame.between_time(start_time, end_time)    | 选择一天中特定时间之间的值 (如 9:00-9:30 AM) |
| DataFrame.drop([labels, axis, index, …])        | 从行或列中删除指定的标签                   |
| DataFrame.drop_duplicates([subset, keep, …])    | 返回删除重复行的数据帧                    |
| DataFrame.duplicated([subset, keep])            | 返回表示重复行的布尔序列                   |
| DataFrame.equals(other)                         | 返回表示重复行的布尔序列                   |
| DataFrame.filter([items, like, regex, axis])    | 根据指定的索引标签对数据帧行或列进行子集化          |
| DataFrame.first(offset)                         | 基于日期偏移选择时间序列数据的初始时段            |
| DataFrame.head([n])                             | 返回前n行                          |
| DataFrame.idxmax([axis, skipna])                | 返回请求轴上第一次出现的最大值的索引             |
| DataFrame.idxmin([axis, skipna])                | 在请求的轴上第一次出现最小值的返回索引            |
| DataFrame.last(offset)                          | 基于日期偏移选择时间序列数据的最后时段            |
| DataFrame.reindex([labels, index, columns, …])  | 使用可选填充逻辑使序列/数据帧与新索引一致          |
| DataFrame.reindex_like(other[, method, …])      | 与其他对象一样返回具有匹配索引的对象             |
| DataFrame.rename([mapper, index, columns, …])   | 更改轴标签                          |
| DataFrame.rename_axis([mapper, index, …])       | 设置索引或列的轴的名称                    |
| DataFrame.reset_index([level, drop, …])         | 重置索引或其级别                       |
| DataFrame.sample([n, frac, replace, …])         | 从对象轴返回项目的随机样本                  |
| DataFrame.set_axis(labels[, axis, inplace])     | 将所需索引指定给给定轴                    |
| DataFrame.set_index(keys[, drop, append, …])    | 使用现有列设置数据帧索引                   |
| DataFrame.tail([n])                             | 返回最后n行                         |
| DataFrame.take(indices[, axis, is_copy])        | 沿轴返回给定位置索引中的元素                 |
| DataFrame.truncate([before, after, axis, copy]) | 在某个索引值前后截断序列或数据帧               |

### 缺失数据处理 Missing data handling

| api                                               | 介绍                                           |
| ------------------------------------------------- | -------------------------------------------- |
| DataFrame.backfill([axis, inplace, limit, …])     | 同 DataFrame.fillna() 参数 method='bfill'.      |
| DataFrame.bfill([axis, inplace, limit, downcast]) | 同 DataFrame.fillna() 参数 method='bfill'.      |
| DataFrame.dropna([axis, how, thresh, …])          | 删除缺少的值                                       |
| DataFrame.ffill([axis, inplace, limit, downcast]) | 同 DataFrame.fillna() 参数 method='ffill'.      |
| DataFrame.fillna([value, method, axis, …])        | 使用指定的方法填充NA/NaN值                             |
| DataFrame.interpolate([method, axis, limit, …])   | 插值，对于多索引的DataFrame/Series，只支持method='linear' |
| DataFrame.isna()                                  | 检测缺失值                                        |
| DataFrame.isnull()                                | 检测缺失值                                        |
| DataFrame.notna()                                 | 检测现有（非缺失）值                                   |
| DataFrame.notnull()                               | 检测现有（非缺失）值                                   |
| DataFrame.pad([axis, inplace, limit, downcast])   | 同 DataFrame.fillna() 参数 method='ffill'       |
| DataFrame.replace([to_replace, value, …])         | 替换值                                          |

### 整形/分类/换位 Reshaping, sorting, transposing

| api                                             | 介绍                        |
| ----------------------------------------------- | ------------------------- |
| DataFrame.droplevel(level[, axis])              | 返回已删除请求的索引/列级别的数据帧        |
| DataFrame.pivot([index, columns, values])       | 返回由给定索引/列值组织的重塑数据帧        |
| DataFrame.pivot_table([values, index, …])       | 将电子表格样式的数据透视表创建为数据框       |
| DataFrame.reorder_levels(order[, axis])         | 使用输入顺序重新排列索引级别            |
| DataFrame.sort_values(by[, axis, ascending, …]) | 按任一轴上的值排序                 |
| DataFrame.sort_index([axis, level, …])          | 按标签对对象排序（沿轴）              |
| DataFrame.nlargest(n, columns[, keep])          | 返回按列降序排列的前n行              |
| DataFrame.nsmallest(n, columns[, keep])         | 按列升序返回前n行                 |
| DataFrame.swaplevel([i, j, axis])               | 交换特定轴上多索引中的i和j级           |
| DataFrame.stack([level, dropna])                | 将指定的级别从列堆叠到索引             |
| DataFrame.unstack([level, fill_value])          | 将指定的级别从列堆叠到索引             |
| DataFrame.swapaxes(axis1, axis2[, copy])        | 适当地交换轴和交换值轴               |
| DataFrame.melt([id_vars, value_vars, …])        | 将数据帧从宽格式解压为长格式，可以选择保留标识符集 |
| DataFrame.explode(column[, ignore_index])       | 将列表中的每个元素转换为一行，复制索引值      |
| DataFrame.squeeze([axis])                       | 将一维轴对象挤压成标量               |
| DataFrame.to_xarray()                           | 从pandas对象返回xarray对象       |
| DataFrame.T                                     | 转置，同 DataFrame.transpose  |
| DataFrame.transpose(*args[, copy])              | 转置索引和列                    |

### 合并/比较/加入/合并 Combining / comparing / joining / merging

| api                                           | 介绍                          |
| --------------------------------------------- | --------------------------- |
| DataFrame.append(other[, ignore_index, …])    | 将其他行追加到调用者的末尾，返回一个新对象       |
| DataFrame.assign(**kwargs)                    | 为数据帧分配新列                    |
| DataFrame.compare(other[, align_axis, …])     | 与另一个数据帧进行比较并显示差异            |
| DataFrame.join(other[, on, how, lsuffix, …])  | 连接另一个数据帧的列                  |
| DataFrame.merge(right[, how, on, left_on, …]) | 将DataFrame或命名系列对象与数据库样式联接合并 |
| DataFrame.update(other[, join, overwrite, …]) | 使用其他数据帧中的非NA值就地修改           |

### 时间序列相关 Time Series-related

| api                                             | 介绍                               |
| ----------------------------------------------- | -------------------------------- |
| DataFrame.asfreq(freq[, method, how, …])        | 将时间序列转换为指定频率                     |
| DataFrame.asof(where[, subset])                 | 返回where之前的最后一行，不带任何nan           |
| DataFrame.shift([periods, freq, axis, …])       | 用一个可选的时间频率按所需的周期数移动索引            |
| DataFrame.slice_shift([periods, axis])          | 相当于移位而不复制数据                      |
| DataFrame.tshift([periods, freq, axis])         | （已弃用）使用索引的频率（如果可用）移动时间索引         |
| DataFrame.first_valid_index()                   | 返回第一个非NA/null值的索引                |
| DataFrame.last_valid_index()                    | 返回最后一个非NA/null值的索引               |
| DataFrame.resample(rule[, axis, closed, …])     | 重新采样时间序列数据                       |
| DataFrame.to_period([freq, axis, copy])         | 将数据帧从DatetimeIndex转换为PeriodIndex |
| DataFrame.to_timestamp([freq, how, axis, copy]) | 转换为时间戳的DatetimeIndex，在时段开始处      |
| DataFrame.tz_convert(tz[, axis, level, copy])   | 将时间轴转换为目标时区                      |
| DataFrame.tz_localize(tz[, axis, level, …])     | 将序列或数据帧的原始索引本地化为目标时区             |

### 元数据 Metadata

DataFrame.attrs 是用于存储此数据帧的全局元数据的字典。

Warning: 数据帧.attrs被认为是实验性的，可能会毫无征兆地改变。

| api             | 介绍         |
| --------------- | ---------- |
| DataFrame.attrs | 此对象的全局属性字典 |

### 绘图 Plotting

DataFrame.plot 是窗体的特定打印方法的可调用方法和命名空间属性 DataFrame.plot..

| api                                      | 介绍                 |
| ---------------------------------------- | ------------------ |
| DataFrame.plot([x, y, kind, ax, ….])     | 数据帧绘制存取器及方法        |
| DataFrame.plot.area([x, y])              | 绘制堆积面积图            |
| DataFrame.plot.bar([x, y])               | 垂直条形图              |
| DataFrame.plot.barh([x, y])              | 做一个水平条形图           |
| DataFrame.plot.box([by])                 | 绘制数据框列的箱形图         |
| DataFrame.plot.density([bw_method, ind]) | 使用高斯核生成核密度估计图      |
| DataFrame.plot.hexbin(x, y[, C, …])      | 生成六边形箱形图           |
| DataFrame.plot.hist([by, bins])          | 绘制数据帧列的直方图         |
| DataFrame.plot.kde([bw_method, ind])     | 使用高斯核生成核密度估计图      |
| DataFrame.plot.line([x, y])              | 将序列或数据帧绘制为线        |
| DataFrame.plot.pie(**kwargs)             | 生成饼图               |
| DataFrame.plot.scatter(x, y[, s, c])     | 创建具有不同标记点大小和颜色的散点图 |
| DataFrame.boxplot([column, by, ax, …])   | 从DataFrame列生成箱线图   |
| DataFrame.hist([column, by, grid, …])    | 制作数据帧的直方图          |

### 稀疏存取器 Sparse accessor

特定于稀疏数据类型的方法和属性在 DataFrame.sparse。

| api                                       | 介绍                      |
| ----------------------------------------- | ----------------------- |
| DataFrame.sparse.density                  | 非稀疏点与总（密集）数据点的比率        |
| DataFrame.sparse.from_spmatrix(data[, …]) | 从一个scipy稀疏矩阵创建一个新的数据帧   |
| DataFrame.sparse.to_coo()                 | 以稀疏SciPy COO矩阵的形式返回帧的内容 |
| DataFrame.sparse.to_dense()               | 将具有稀疏值的数据帧转换为密集值        |

### 序列化/IO/转换 Serialization / IO / conversion

| api                                             | 介绍                                 |
| ----------------------------------------------- | ---------------------------------- |
| DataFrame.from_dict(data[, orient, dtype, …])   | 从数组的dict构造数据帧                      |
| DataFrame.from_records(data[, index, …])        | 将结构化或记录数组转换为数据帧                    |
| DataFrame.to_parquet(path[, engine, …])         | 将数据帧写入二进制parquet格式                 |
| DataFrame.to_pickle(path[, compression, …])     | Pickle（序列化）对象到文件                   |
| DataFrame.to_csv([path_or_buf, sep, na_rep, …]) | 将对象写入逗号分隔值（csv）文件                  |
| DataFrame.to_hdf(path_or_buf, key[, mode, …])   | 使用HDFStore将包含的数据写入HDF5文件           |
| DataFrame.to_sql(name, con[, schema, …])        | 将数据帧中存储的记录写入SQL数据库                 |
| DataFrame.to_dict([orient, into])               | 将数据帧转换为字典                          |
| DataFrame.to_excel(excel_writer[, …])           | 将对象写入Excel工作表                      |
| DataFrame.to_json([path_or_buf, orient, …])     | 将对象转换为JSON字符串                      |
| DataFrame.to_html([buf, columns, col_space, …]) | 将数据帧呈现为HTML表                       |
| DataFrame.to_feather(path, **kwargs)            | 将数据帧写入二进制羽化格式                      |
| DataFrame.to_latex([buf, columns, …])           | 将对象渲染为LaTeX表格、长表格或嵌套 table/tabular |
| DataFrame.to_stata(path[, convert_dates, …])    | 将DataFrame对象导出为Stata dta格式         |
| DataFrame.to_gbq(destination_table[, …])        | 将数据帧写入google big query表            |
| DataFrame.to_records([index, column_dtypes, …]) | 将数据帧转换为NumPy记录数组                   |
| DataFrame.to_string([buf, columns, …])          | 将数据帧呈现为控制台友好的表格输出                  |
| DataFrame.to_clipboard([excel, sep])            | 将对象复制到系统剪贴板                        |
| DataFrame.to_markdown([buf, mode, index])       | 以便于标记的格式打印数据帧                      |
| DataFrame.style                                 | 返回样式器对象                            |

## Series

-------------

### 构造器 Constructor

| api                                         | 介绍                    |
| ------------------------------------------- | --------------------- |
| Series([data, index, dtype, name, copy, …]) | 生成具有轴标签（可以是时间序列）的一维序列 |

### 属性 Attributes

| api                                | 介绍                                        |
| ---------------------------------- | ----------------------------------------- |
| Series.index                       | 系列的索引（轴标签）                                |
| Series.array                       | 序列的 PandasArray 格式数据                      |
| Series.values                      | 根据 dtype 将 Series 返回为 ndarray 或类似 ndarray |
| Series.dtype                       | 返回基础数据的dtype对象                            |
| Series.shape                       | 返回基础数据形状的元组                               |
| Series.nbytes                      | 返回基础数据中的字节数                               |
| Series.ndim                        | 根据定义，基础数据的维数为1                            |
| Series.size                        | 返回基础数据中的元素数                               |
| Series.T                           | 返回转置，为了兼容，值为自我                            |
| Series.memory_usage([index, deep]) | 返回序列的内存使用情况                               |
| Series.hasnans                     | 返回如果我有任何空值                                |
| Series.empty                       | 指示数据帧是否为空                                 |
| Series.dtypes                      | 返回基础数据的dtype对象                            |
| Series.name                        | 返回序列的名称                                   |
| Series.flags                       | 获取对象关联的属性                                 |
| Series.set_flags(*[, copy, …])     | 返回带有更新标志的新对象                              |

### 转换 Conversion

| api                                       | 介绍                              |
| ----------------------------------------- | ------------------------------- |
| Series.astype(dtype[, copy, errors])      | 将对象强制转换为指定的数据类型                 |
| Series.convert_dtypes([infer_objects, …]) | 使用数据类型将列转换为最佳数据类型，支持 pd.NA.     |
| Series.infer_objects()                    | 尝试为对象列推断更好的数据类型                 |
| Series.copy([deep])                       | 复制此对象的索引和数据                     |
| Series.bool()                             | 返回单个元素序列或数据帧的布尔值                |
| Series.to_numpy([dtype, copy, na_value])  | 返回单个元素序列或数据帧的布尔值                |
| Series.to_period([freq, copy])            | 将序列从DatetimeIndex转换为PeriodIndex |
| Series.to_timestamp([freq, how, copy])    | 转换为时间戳的DatetimeIndex，在时段开始处     |
| Series.to_list()                          | 返回值的列表                          |
| Series.__array__([dtype])                 | 以NumPy数组的形式返回值                  |

### 索引和迭代 Indexing, iteration

| api                                       | 介绍                        |
| ----------------------------------------- | ------------------------- |
| Series.get(key[, default])                | 从给定键的对象获取项（例如：DataFrame列） |
| Series.at                                 | 访问行/列标签对的单个值              |
| Series.iat                                | 按整数位置访问行/列对的单个值           |
| Series.loc                                | 按标签或布尔数组访问一组行和列           |
| Series.iloc                               | 纯整数位置为基础的位置选择索引           |
| Series.__iter__()                         | 返回值的迭代器                   |
| Series.items()                            | 惰性迭代（索引，值）元组              |
| Series.iteritems()                        | 惰性迭代（索引，值）元组              |
| Series.keys()                             | 返回索引的别名                   |
| Series.pop(item)                          | 返回项目并从系列中删除               |
| Series.item()                             | 以python标量形式返回基础数据的第一个元素   |
| Series.xs(key[, axis, level, drop_level]) | 从序列/数据帧返回横截面              |

### 运算符功能 Binary operator functions

| api                                               | 介绍                              |
| ------------------------------------------------- | ------------------------------- |
| Series.add(other[, level, fill_value, axis])      | 返回序列和其他元素的加法（二进制运算符加法）          |
| Series.sub(other[, level, fill_value, axis])      | 返回序列和其他元素的减法（二进制运算符sub）         |
| Series.mul(other[, level, fill_value, axis])      | 按元素返回级数和其它数的乘法（二进制运算符mul）       |
| Series.div(other[, level, fill_value, axis])      | 返回序列和其他元素的浮点除法（二进制运算符truediv）   |
| Series.truediv(other[, level, fill_value, axis])  | 返回序列和其他元素的浮点除法（二进制运算符truediv）   |
| Series.floordiv(other[, level, fill_value, axis]) | 返回序列和其他元素的整数除法（二进制运算符floordiv）  |
| Series.mod(other[, level, fill_value, axis])      | 返回系列和其他元素的模（二进制运算符mod）          |
| Series.pow(other[, level, fill_value, axis])      | 返回序列和其他元素的指数幂（二进制运算符pow）        |
| Series.radd(other[, level, fill_value, axis])     | 返回序列和其他元素的加法（二进制运算符radd）        |
| Series.rsub(other[, level, fill_value, axis])     | 返回序列和其他元素的减法（二进制运算符rsub）        |
| Series.rmul(other[, level, fill_value, axis])     | 按元素返回级数和其它数的乘法（二进制运算符rmul）      |
| Series.rdiv(other[, level, fill_value, axis])     | 返回序列和其他元素的浮点除法（二进制运算符rtruediv）  |
| Series.rtruediv(other[, level, fill_value, axis]) | 返回序列和其他元素的浮点除法（二进制运算符rtruediv）  |
| Series.rfloordiv(other[, level, fill_value, …])   | 返回序列和其他元素的整数除法（二进制运算符rfloordiv） |
| Series.rmod(other[, level, fill_value, axis])     | 返回系列和其他元素的模（二进制运算符rmod）         |
| Series.rpow(other[, level, fill_value, axis])     | 返回序列和其他元素的指数幂（二进制运算符rpow）       |
| Series.combine(other, func[, fill_value])         | 根据func将级数与级数或标量组合               |
| Series.combine_first(other)                       | 组合序列值，首先选择调用序列的值                |
| Series.round([decimals])                          | 将序列中的每个值四舍五入到给定的小数位数            |
| Series.lt(other[, level, fill_value, axis])       | 返回小于系列和其他元素的元素（二进制运算符lt）        |
| Series.gt(other[, level, fill_value, axis])       | 返回大于系列和其他元素的值（二进制运算符gt）         |
| Series.le(other[, level, fill_value, axis])       | 返回小于或等于系列和其他元素的值（二进制运算符le）      |
| Series.ge(other[, level, fill_value, axis])       | 返回大于或等于系列和其他元素的值（二进制运算符ge）      |
| Series.ne(other[, level, fill_value, axis])       | 返回不等于系列和其他元素的整数（二进制运算符ne）       |
| Series.eq(other[, level, fill_value, axis])       | 返回等于系列和其他元素的整数（二进制运算符eq）        |
| Series.product([axis, skipna, level, …])          | 返回所请求轴的值的乘积                     |
| Series.dot(other)                                 | 计算序列和其他列之间的点积                   |

### 函数应用，分组和窗口计算 Function application, GroupBy & window

| api                                            | 介绍                              |
| ---------------------------------------------- | ------------------------------- |
| Series.apply(func[, convert_dtype, args])      | 对序列值调用函数                        |
| Series.agg([func, axis])                       | 在指定轴上使用一个或多个操作进行聚合              |
| Series.aggregate([func, axis])                 | 在指定轴上使用一个或多个操作进行聚合              |
| Series.transform(func[, axis])                 | 调用func生成一个具有转换值的序列              |
| Series.map(arg[, na_action])                   | 根据输入对应关系映射系列值                   |
| Series.groupby([by, axis, level, as_index, …]) | 使用映射器或按一系列列对序列进行分组              |
| Series.rolling(window[, min_periods, …])       | 提供滚动窗口计算                        |
| Series.expanding([min_periods, center, axis])  | 提供扩展转换                          |
| Series.ewm([com, span, halflife, alpha, …])    | 提供指数加权（EW）函数                    |
| Series.pipe(func, *args, **kwargs)             | 支持 func(self, *args, **kwargs). |

### 计算/描述性统计 Computations / descriptive stats

| api                                              | 介绍                            |
| ------------------------------------------------ | ----------------------------- |
| Series.abs()                                     | 返回带有每个元素绝对数值的序列/数据帧           |
| Series.all([axis, bool_only, skipna, level])     | 返回是否所有元素都为真，可能在一个轴上           |
| Series.any([axis, bool_only, skipna, level])     | 返回任何元素是否为真，可能在轴上              |
| Series.autocorr([lag])                           | 计算lag-N自相关                    |
| Series.between(left, right[, inclusive])         | 返回等价于left<=Series<=right的布尔级数 |
| Series.clip([lower, upper, axis, inplace])       | 输入阈值处的微调值                     |
| Series.corr(other[, method, min_periods])        | 计算与其他序列的相关性，不包括缺失值            |
| Series.count([level])                            | 返回序列中非NA/null观测值的数目           |
| Series.cov(other[, min_periods, ddof])           | 计算序列的协方差，不包括缺失值               |
| Series.cummax([axis, skipna])                    | 返回数据帧或序列轴上的累积最大值              |
| Series.cummin([axis, skipna])                    | 返回数据帧或序列轴上的累计最小值              |
| Series.cumprod([axis, skipna])                   | 返回数据帧或序列轴上的累积乘积               |
| Series.cumsum([axis, skipna])                    | 返回数据帧或序列轴上的累积和                |
| Series.describe([percentiles, include, …])       | 生成描述性统计                       |
| Series.diff([periods])                           | 元素的第一离散差分                     |
| Series.factorize([sort, na_sentinel])            | 将对象编码为枚举类型或分类变量               |
| Series.kurt([axis, skipna, level, numeric_only]) | 返回请求轴上的无偏峰度                   |
| Series.mad([axis, skipna, level])                | 返回请求轴值的平均绝对偏差                 |
| Series.max([axis, skipna, level, numeric_only])  | 返回请求轴的最大值                     |
| Series.mean([axis, skipna, level, numeric_only]) | 返回所请求轴的平均值                    |
| Series.median([axis, skipna, level, …])          | 返回所请求轴的中位数                    |
| Series.min([axis, skipna, level, numeric_only])  | 返回请求轴的最小值                     |
| Series.mode([dropna])                            | 返回数据集的模式                      |
| Series.nlargest([n, keep])                       | 返回最大的n个元素                     |
| Series.nsmallest([n, keep])                      | 返回最大的n个元素                     |
| Series.pct_change([periods, fill_method, …])     | 当前元素和上一个元素之间的百分比变化            |
| Series.prod([axis, skipna, level, …])            | 返回所请求轴的值的乘积                   |
| Series.quantile([q, interpolation])              | 返回给定分位数处的值                    |
| Series.rank([axis, method, numeric_only, …])     | 沿轴计算数值数据秩（1到n）                |
| Series.sem([axis, skipna, level, ddof, …])       | 返回请求轴上平均值的无偏标准误差              |
| Series.skew([axis, skipna, level, numeric_only]) | 返回请求轴上的无偏倾斜                   |
| Series.std([axis, skipna, level, ddof, …])       | 返回要求轴上的样本标准偏差                 |
| Series.sum([axis, skipna, level, …])             | 返回所请求轴的值之和                    |
| Series.var([axis, skipna, level, ddof, …])       | 返回请求轴上的无偏方差                   |
| Series.kurtosis([axis, skipna, level, …])        | 返回请求轴上的无偏峰度                   |
| Series.unique()                                  | 返回序列对象的唯一值                    |
| Series.nunique([dropna])                         | 返回对象中唯一元素的数目                  |
| Series.is_unique                                 | 如果对象中的值唯一，则返回布尔值              |
| Series.is_monotonic                              | 如果对象中的值是单调递增的，则返回布尔值          |
| Series.is_monotonic_increasing                   | is_monotonic 的别名              |
| Series.is_monotonic_decreasing                   | 如果对象中的值是单调递减的，则返回布尔值          |
| Series.value_counts([normalize, sort, …])        | 返回包含唯一值计数的序列                  |

### 重新索引/选择/标签操作 Reindexing / selection / label manipulation

| api                                              | 介绍                     |
| ------------------------------------------------ | ---------------------- |
| Series.align(other[, join, axis, level, …])      | 使用指定的连接方法在轴上对齐两个对象     |
| Series.drop([labels, axis, index, columns, …])   | 删除指定索引标签的返回序列          |
| Series.droplevel(level[, axis])                  | 返回已删除请求的索引/列级别的数据帧     |
| Series.drop_duplicates([keep, inplace])          | 删除重复值的返回序列             |
| Series.duplicated([keep])                        | 表示重复的序列值               |
| Series.equals(other)                             | 测试两个对象是否包含相同的元素        |
| Series.first(offset)                             | 基于日期偏移选择时间序列数据的初始时段    |
| Series.head([n])                                 | 返回前n行                  |
| Series.idxmax([axis, skipna])                    | 返回最大值的行标签              |
| Series.idxmin([axis, skipna])                    | 返回最小值的行标签              |
| Series.isin(values)                              | 序列中的元素是否包含在值中          |
| Series.last(offset)                              | 根据日期偏移选择时间序列数据的最后时段    |
| Series.reindex([index])                          | 使用可选填充逻辑使系列符合新索引       |
| Series.reindex_like(other[, method, copy, …])    | 返回索引与其他对象匹配的对象         |
| Series.rename([index, axis, copy, inplace, …])   | 更改系列索引标签或名称            |
| Series.rename_axis([mapper, index, columns, …])  | 设置索引或列的轴的名称            |
| Series.reset_index([level, drop, name, inplace]) | 使用索引重置生成新的数据帧或序列       |
| Series.sample([n, frac, replace, weights, …])    | 从对象轴返回项目的随机样本          |
| Series.set_axis(labels[, axis, inplace])         | 将所需索引指定给给定轴            |
| Series.take(indices[, axis, is_copy])            | 沿轴返回给定位置索引中的元素         |
| Series.tail([n])                                 | 沿轴返回给定位置索引中的元素         |
| Series.truncate([before, after, axis, copy])     | 截断某个索引值前后的序列或数据帧       |
| Series.where(cond[, other, inplace, axis, …])    | 替换条件为 False 的值         |
| Series.mask(cond[, other, inplace, axis, …])     | 替换条件为 True 的值          |
| Series.add_prefix(prefix)                        | 使用字符串前缀为标签添加前缀         |
| Series.add_suffix(suffix)                        | 带有字符串后缀的后缀标签           |
| Series.filter([items, like, regex, axis])        | 根据指定的索引标签对数据帧行或列进行子集设置 |

### 缺失值处理 Missing data handling

| api                                               | 介绍                                      |
| ------------------------------------------------- | --------------------------------------- |
| Series.backfill([axis, inplace, limit, downcast]) | 同 DataFrame.fillna() 使用 method='bfill'  |
| Series.bfill([axis, inplace, limit, downcast])    | 同 DataFrame.fillna() 使用 method='bfill'. |
| Series.dropna([axis, inplace, how])               | 返回已删除缺失值的新序列                            |
| Series.ffill([axis, inplace, limit, downcast])    | 同 DataFrame.fillna() 使用 method='ffill'. |
| Series.fillna([value, method, axis, …])           | 使用指定的方法填充 NA/NaN 值                      |
| Series.interpolate([method, axis, limit, …])      | 插值，多层索引仅支持 method='linear'              |
| Series.isna()                                     | 检测缺失值                                   |
| Series.isnull()                                   | 检测缺失值                                   |
| Series.notna()                                    | 检测现有（非缺失）值                              |
| Series.notnull()                                  | 检测现有（非缺失）值                              |
| Series.pad([axis, inplace, limit, downcast])      | 同 DataFrame.fillna() 使用 method='ffill'. |
| Series.replace([to_replace, value, inplace, …])   | 将指定值替换为给出的值                             |

### 重塑/排序 Reshaping, sorting

| api                                            | 介绍                                   |
| ---------------------------------------------- | ------------------------------------ |
| Series.argsort([axis, kind, order])            | 返回将对序列值进行排序的整数索引                     |
| Series.argmin([axis, skipna])                  | 返回序列中最小值的int位置                       |
| Series.argmax([axis, skipna])                  | 返回序列中最大值的int位置                       |
| Series.reorder_levels(order)                   | 使用输入顺序重新排列索引级别                       |
| Series.sort_values([axis, ascending, …])       | 按值排序                                 |
| Series.sort_index([axis, level, ascending, …]) | 按索引标签对序列进行排序                         |
| Series.swaplevel([i, j, copy])                 | 在多索引中交换级别i和j                         |
| Series.unstack([level, fill_value])            | Unstack，也称为pivot，是一个具有多索引的系列，用于生成数据帧 |
| Series.explode([ignore_index])                 | 将列表中的每个元素转换为一行                       |
| Series.searchsorted(value[, side, sorter])     | 查找应插入元素以保持顺序的索引                      |
| Series.ravel([order])                          | 将展开的基础数据作为 ndarray 返回                |
| Series.repeat(repeats[, axis])                 | 重复系列的元素                              |
| Series.squeeze([axis])                         | 将一维轴对象压缩为标量                          |
| Series.view([dtype])                           | 创建系列的新视图                             |

### 合并/比较/合并/合并 Combining / comparing / joining / merging

| api                                             | 介绍              |
| ----------------------------------------------- | --------------- |
| Series.append(to_append[, ignore_index, …])     | 连接两个或多个系列       |
| Series.compare(other[, align_axis, …])          | 与另一个系列进行比较并显示差异 |
| Series.replace([to_replace, value, inplace, …]) | 将中给出的值替换为值      |
| Series.update(other)                            | 使用传递序列中的值就地修改序列 |

### 时间序列有关 Time Series-related

| api                                             | 介绍                           |
| ----------------------------------------------- | ---------------------------- |
| Series.asfreq(freq[, method, how, …])           | 将时间序列转换为指定的频率                |
| Series.asof(where[, subset])                    | 返回where之前的最后一行，不带任何 NaN      |
| Series.shift([periods, freq, axis, fill_value]) | 按所需周期数和可选时间频率进行移位索引          |
| Series.first_valid_index()                      | 返回第一个非NA/null值的索引            |
| Series.last_valid_index()                       | 返回最后一个非NA/null值的索引           |
| Series.resample(rule[, axis, closed, label, …]) | 对时间序列数据重新采样                  |
| Series.tz_convert(tz[, axis, level, copy])      | 将时间轴转换为目标时区                  |
| Series.tz_localize(tz[, axis, level, copy, …])  | 将序列或数据帧的初始索引本地化为目标时区         |
| Series.at_time(time[, asof, axis])              | 选择一天中特定时间（如上午9:30）的值         |
| Series.between_time(start_time, end_time[, …])  | 选择一天中特定时间（例如上午9:00-9:30）之间的值 |
| Series.tshift([periods, freq, axis])            | （已弃用）使用索引的频率（如果可用）移动时间索引     |
| Series.slice_shift([periods, axis])             | 相当于shift而不复制数据               |

### 存取器 Accessors

Pandas在各种访问器下提供特定于数据类型的方法。这些名称空间是系列中单独的名称空间，仅适用于特定的数据类型。

| Data Type                   | Accessor |
| --------------------------- | -------- |
| Datetime, Timedelta, Period | dt       |
| String                      | str      |
| Categorical                 | cat      |
| Sparse                      | sparse   |

#### 类似日期时间的属性 Datetimelike properties

Series.dt可用于以datetimelike的形式访问序列的值，并返回多个属性。可以像Series.dt.一样访问这些属性。

##### 日期时间属性 Datetime properties

| api                        | 介绍                                                 |
| -------------------------- | -------------------------------------------------- |
| Series.dt.date             | 返回python datetime.date对象的numpy数组（即不含时区信息的时间戳的日期部分） |
| Series.dt.time             | 返回datetime.time的numpy数组                            |
| Series.dt.timetz           | 返回datetime.time的numpy数组，该数组还包含时区信息                 |
| Series.dt.year             | 日期时间的年份                                            |
| Series.dt.month            | 一月=1，十二月=12的月份                                     |
| Series.dt.day              | 日期时间的日期                                            |
| Series.dt.hour             | 日期时间的小时数                                           |
| Series.dt.minute           | 日期时间的分钟数                                           |
| Series.dt.second           | 日期时间的秒数                                            |
| Series.dt.microsecond      | 日期时间的微秒                                            |
| Series.dt.nanosecond       | 日期时间的纳秒数                                           |
| Series.dt.week             | （不推荐）一年中的第几周                                       |
| Series.dt.weekofyear       | （不推荐）一年中的第几周                                       |
| Series.dt.dayofweek        | 星期一=0，星期日=6的一周中的某一天                                |
| Series.dt.weekday          | 星期一=0，星期日=6的一周中的某一天                                |
| Series.dt.dayofyear        | 一年中的第几天                                            |
| Series.dt.quarter          | 日期的四分之一                                            |
| Series.dt.is_month_start   | 指示日期是否为当月的第一天                                      |
| Series.dt.is_month_end     | 指示日期是否为当月的最后一天                                     |
| Series.dt.is_quarter_start | 指示日期是否为季度的第一天                                      |
| Series.dt.is_quarter_end   | 指示日期是否为季度的最后一天                                     |
| Series.dt.is_year_start    | 指明日期是否为一年中的第一天                                     |
| Series.dt.is_year_end      | 指明日期是否为一年中的最后一天                                    |
| Series.dt.is_leap_year     | 如果日期属于闰年，则为布尔指示符                                   |
| Series.dt.daysinmonth      | 当月的天数                                              |
| Series.dt.days_in_month    | 当月的天数                                              |
| Series.dt.tz               | 返回时区（如果有）                                          |
| Series.dt.freq             | 返回此周期数组的频率对象 PeriodArray                           |

##### 日期时间方法 Datetime methods

| api                                    | 介绍                                            |
| -------------------------------------- | --------------------------------------------- |
| Series.dt.to_period(*args, **kwargs)   | 以特定频率强制转换到周期数组/索引 PeriodArray/Index           |
| Series.dt.to_pydatetime()              | 以本机Python datetime对象数组的形式返回数据                 |
| Series.dt.tz_localize(*args, **kwargs) | 将tz naive Datetime数组/索引本地化为tz感知的Datetime数组/索引 |
| Series.dt.tz_convert(*args, **kwargs)  | 将tz感知的日期时间数组/索引从一个时区转换为另一个时区                  |
| Series.dt.normalize(*args, **kwargs)   | 将时间转换为午夜                                      |
| Series.dt.strftime(*args, **kwargs)    | 使用指定的日期格式转换为索引                                |
| Series.dt.round(*args, **kwargs)       | 按指定的频率对数据执行舍入操作                               |
| Series.dt.floor(*args, **kwargs)       | 以指定的频率对数据执行floor操作                            |
| Series.dt.ceil(*args, **kwargs)        | 以指定的频率对数据执行ceil操作                             |
| Series.dt.month_name(*args, **kwargs)  | 返回具有指定区域设置的DateTimeIndex的月份名称                 |
| Series.dt.day_name(*args, **kwargs)    | 返回具有指定区域设置的DateTimeIndex的日期名称                 |

##### 周期属性 Period properties

| API                  | 介绍  |
| -------------------- | --- |
| Series.dt.qyear      |     |
| Series.dt.start_time |     |
| Series.dt.end_time   |     |

##### 时间增量属性 Timedelta properties

| api                    | 介绍                  |
| ---------------------- | ------------------- |
| Series.dt.days         | 每个元素的天数             |
| Series.dt.seconds      | 每个元素的秒数（>=0且小于1天）   |
| Series.dt.microseconds | 每个元素的微秒数（>=0且小于1秒）  |
| Series.dt.nanoseconds  | 每个元素的纳秒数（>=0且小于1微秒） |
| Series.dt.components   | 返回TimeDelta组件的数据帧   |

##### 时间增量方法 Timedelta methods

| api                                      | 介绍                                                          |
| ---------------------------------------- | ----------------------------------------------------------- |
| Series.dt.to_pytimedelta()               | Return an array of native datetime.timedelta objects.       |
| Series.dt.total_seconds(*args, **kwargs) | Return total duration of each element expressed in seconds. |

#### 字符串处理 String handling

Series.str 可用于以字符串形式访问序列的值，并对其应用多种方法。可以像Series.str.<function/property>一样访问这些文件。

| api                                            | 介绍                            |
| ---------------------------------------------- | ----------------------------- |
| Series.str.capitalize()                        | 将序列/索引中的字符串转换为大写              |
| Series.str.casefold()                          | 将序列/索引中的字符串转换为大小写折叠           |
| Series.str.cat([others, sep, na_rep, join])    | 用给定的分隔符连接序列/索引中的字符串           |
| Series.str.center(width[, fillchar])           | 在序列/索引中填充字符串的左侧和右侧            |
| Series.str.contains(pat[, case, flags, na, …]) | 测试模式或正则表达式是否包含在序列或索引的字符串中     |
| Series.str.count(pat[, flags])                 | 统计序列/索引的每个字符串中模式的出现次数         |
| Series.str.decode(encoding[, errors])          | 使用指定的编码对序列/索引中的字符串进行解码        |
| Series.str.encode(encoding[, errors])          | 使用指定的编码对序列/索引中的字符串进行编码        |
| Series.str.endswith(pat[, na])                 | 测试每个字符串元素的结尾是否与模式匹配           |
| Series.str.extract(pat[, flags, expand])       | 将正则表达式pat中的捕获组提取为数据帧中的列       |
| Series.str.extractall(pat[, flags])            | 将正则表达式pat中的捕获组提取为DataFrame中的列 |
| Series.str.find(sub[, start, end])             | 返回序列/索引中每个字符串的最低索引            |
| Series.str.findall(pat[, flags])               | 查找序列/索引中所有出现的模式或正则表达式         |
| Series.str.get(i)                              | 从指定位置的每个组件中提取元素               |
| Series.str.index(sub[, start, end])            | 返回系列/索引中每个字符串中的最低索引           |
| Series.str.join(sep)                           | 包含为序列/索引中的元素并带有传递的分隔符的联接列表    |
| Series.str.len()                               | 计算序列/索引中每个元素的长度               |
| Series.str.ljust(width[, fillchar])            | 在序列/索引中填充字符串的右侧               |
| Series.str.lower()                             | 将序列/索引中的字符串转换为小写              |
| Series.str.lstrip([to_strip])                  | 删除前导字符                        |
| Series.str.match(pat[, case, flags, na])       | 确定每个字符串是否以正则表达式的匹配项开头         |
| Series.str.normalize(form)                     | 返回序列/索引中字符串的Unicode标准格式       |
| Series.str.pad(width[, side, fillchar])        | 填充系列/索引中的字符串，最大宽度为            |
| Series.str.partition([sep, expand])            | 在第一次出现sep时拆分字符串               |
| Series.str.repeat(repeats)                     | 复制序列或索引中的每个字符串                |
| Series.str.replace(pat, repl[, n, case, …])    | 替换序列/索引中出现的每个pattern/regex    |
| Series.str.rfind(sub[, start, end])            | 返回序列/索引中每个字符串的最高索引            |
| Series.str.rindex(sub[, start, end])           | 返回系列/索引中每个字符串的最高索引            |
| Series.str.rjust(width[, fillchar])            | 在序列/索引中填充字符串的左侧               |
| Series.str.rpartition([sep, expand])           | 在最后一次出现sep时拆分字符串              |
| Series.str.rstrip([to_strip])                  | 删除尾随字符                        |
| Series.str.slice([start, stop, step])          | 从序列或索引中的每个元素切片子字符串            |
| Series.str.slice_replace([start, stop, repl])  | 用另一个值替换字符串的位置切片               |
| Series.str.split([pat, n, expand])             | 围绕给定的分隔符/分隔符拆分字符串             |
| Series.str.rsplit([pat, n, expand])            | 围绕给定的分隔符/分隔符拆分字符串             |
| Series.str.startswith(pat[, na])               | 测试每个字符串元素的开头是否与模式匹配           |
| Series.str.strip([to_strip])                   | 删除前导字符和尾随字符                   |
| Series.str.swapcase()                          | 将序列/索引中的字符串大小写转换              |
| Series.str.title()                             | 将序列/索引中的字符串转换为 titlecase      |
| Series.str.translate(table)                    | 通过给定的映射表映射字符串中的所有字符           |
| Series.str.upper()                             | 将序列/索引中的字符串转换为大写              |
| Series.str.wrap(width, **kwargs)               | 以指定的线宽将字符串按系列/索引进行换行          |
| Series.str.zfill(width)                        | 通过在“0”字符前加前缀来填充序列/索引中的字符串     |
| Series.str.isalnum()                           | 检查每个字符串中的所有字符是否都是字母数字         |
| Series.str.isalpha()                           | 检查每个字符串中的所有字符是否按字母顺序排列        |
| Series.str.isdigit()                           | 检查每个字符串中的所有字符是否都是数字           |
| Series.str.isspace()                           | 检查每个字符串中的所有字符是否都是空白           |
| Series.str.islower()                           | 检查每个字符串中的所有字符是否为小写            |
| Series.str.isupper()                           | 检查每个字符串中的所有字符是否都是大写           |
| Series.str.istitle()                           | 检查每个字符串中的所有字符是否都是titlecase    |
| Series.str.isnumeric()                         | 检查每个字符串中的所有字符是否都是数字           |
| Series.str.isdecimal()                         | 检查每个字符串中的所有字符是否为十进制           |
| Series.str.get_dummies([sep])                  | 返回序列的虚拟/指示器变量的数据帧             |

#### 分类存取器 Categorical accessor

在Series.cat访问器下提供了特定于数据类型的分类方法和属性。

| api                                            | 介绍              |
| ---------------------------------------------- | --------------- |
| Series.cat.categories                          | 这一分类的类别         |
| Series.cat.ordered                             | 类别是否具有有序关系      |
| Series.cat.codes                               | 返回一系列代码以及索引     |
| Series.cat.rename_categories(*args, **kwargs)  | 重命名类别           |
| Series.cat.reorder_categories(*args, **kwargs) | 按照新类别中的规定重新排序类别 |
| Series.cat.add_categories(*args, **kwargs)     | 添加新类别           |
| Series.cat.remove_categories(*args, **kwargs)  | 删除指定的类别         |
| Series.cat.remove_unused_categories(*args, …)  | 删除未使用的类别        |
| Series.cat.set_categories(*args, **kwargs)     | 将类别设置为指定的新类别    |
| Series.cat.as_ordered(*args, **kwargs)         | 将分类设置为有序        |
| Series.cat.as_unordered(*args, **kwargs)       | 将分类设置为无序        |

#### 稀疏存取器 Sparse accessor

特定于稀疏数据类型的方法和属性在Series.Sparse访问器下提供。

| api                                      | 介绍                                     |
| ---------------------------------------- | -------------------------------------- |
| Series.sparse.npoints                    | 非填充值点数                                 |
| Series.sparse.density                    | 非填充值点的百分比，以十进制表示                       |
| Series.sparse.fill_value                 | 不存储数据中的填充值元素                           |
| Series.sparse.sp_values                  | 包含 non- fill_value 值                   |
| Series.sparse.from_coo(A[, dense_index]) | 从 scipy.sparse.coo_matrix 矩阵创建具有稀疏值的序列 |
| Series.sparse.to_coo([row_levels, …])    | 从具有多索引的序列创建 scipy.sparse.coo_matrix    |

#### 元数据 Metadata

Series.attrs 是用于存储此系列的全局元数据的字典。

警告：Series.attrs被认为是实验性的，可能会在没有警告的情况下更改。

| api          | 介绍         |
| ------------ | ---------- |
| Series.attrs | 此对象的全局属性字典 |

### 绘图 Plotting

Series.plot 是表单 Series.plot. 的特定绘图方法的可调用方法和命名空间属性。

| api                                        | 介绍                     |
| ------------------------------------------ | ---------------------- |
| Series.plot([kind, ax, figsize, ….])       | 系列绘图存取器及方法             |
| Series.plot.area([x, y])                   | 绘制堆叠面积图                |
| Series.plot.bar([x, y])                    | 垂直条形图                  |
| Series.plot.barh([x, y])                   | 做一个水平条形图               |
| Series.plot.box([by])                      | 制作DataFrame列的方框图       |
| Series.plot.density([bw_method, ind])      | 使用高斯核生成核密度估计图          |
| Series.plot.hist([by, bins])               | 绘制数据帧列的一个直方图           |
| Series.plot.kde([bw_method, ind])          | 使用高斯核生成核密度估计图          |
| Series.plot.line([x, y])                   | 将系列或数据框打印为线            |
| Series.plot.pie(**kwargs)                  | 生成饼图                   |
| Series.hist([by, ax, grid, xlabelsize, …]) | 使用matplotlib绘制输入序列的直方图 |

### 序列化/IO/转换 Serialization / IO / conversion

| api                                             | 介绍                                 |
| ----------------------------------------------- | ---------------------------------- |
| Series.to_pickle(path[, compression, protocol]) | 将对象Pickle（序列化）到文件                  |
| Series.to_csv([path_or_buf, sep, na_rep, …])    | 将对象写入逗号分隔值（csv）文件                  |
| Series.to_dict([into])                          | 将序列转换为{label->value}dict或类似dict的对象 |
| Series.to_excel(excel_writer[, sheet_name, …])  | 将对象写入Excel工作表                      |
| Series.to_frame([name])                         | 将序列转换为数据帧                          |
| Series.to_xarray()                              | 从pandas对象返回一个xarray对象              |
| Series.to_hdf(path_or_buf, key[, mode, …])      | 使用HDFStore将包含的数据写入HDF5文件           |
| Series.to_sql(name, con[, schema, …])           | 将存储在数据帧中的记录写入SQL数据库                |
| Series.to_json([path_or_buf, orient, …])        | 将存储在数据帧中的记录写入SQL数据库                |
| Series.to_string([buf, na_rep, …])              | 呈现序列的字符串表示形式                       |
| Series.to_clipboard([excel, sep])               | 将对象复制到系统剪贴板                        |
| Series.to_latex([buf, columns, col_space, …])   | 将对象渲染为LaTeX表格、长表格或嵌套表格/表格          |
| Series.to_markdown([buf, mode, index])          | 以markdown的格式打印系列                   |

## 分组 GroupBy

-------

GroupBy 对象由 GroupBy 调用返回: pandas.DataFrame.groupby(), pandas.Series.groupby() 等。

### Indexing, iteration

| api                            | 介绍                        |
| ------------------------------ | ------------------------- |
| GroupBy.**iter**()             | Groupby迭代器                |
| GroupBy.groups                 | Dict{组名->组标签}             |
| GroupBy.indices                | Dict{组名->组索引}             |
| GroupBy.get_group(name[, obj]) | 使用提供的名称从组构造数据帧            |
| Grouper(*args, **kwargs)       | Grouper允许用户为对象指定groupby指令 |

### 函数应用 Function application

| api                                           | 介绍                                                         |
| --------------------------------------------- | ---------------------------------------------------------- |
| GroupBy.apply(func, *args, **kwargs)          | 按组应用函数func并将结果组合在一起                                        |
| GroupBy.agg(func, *args, **kwargs)            |                                                            |
| SeriesGroupBy.aggregate([func, engine, …])    | 在指定轴上使用一个或多个操作进行聚合                                         |
| DataFrameGroupBy.aggregate([func, engine, …]) | 在指定轴上使用一个或多个操作进行聚合                                         |
| SeriesGroupBy.transform(func, *args[, …])     | 调用函数，在每个组上生成一个相似的索引序列，并返回一个序列，该序列具有与原始对象相同的索引，其中填充了转换后的值   |
| DataFrameGroupBy.transform(func, *args[, …])  | 调用函数，在每个组上生成一个相似的索引数据帧，并返回一个数据帧，该数据帧的索引与原始对象的索引相同，并填充转换后的值 |
| GroupBy.pipe(func, *args, **kwargs)           | 将带参数的函数func应用于此GroupBy对象并返回函数的结果                           |

### 计算/描述性统计 Computations / descriptive stats

| api                                             | 介绍                               |
| ----------------------------------------------- | -------------------------------- |
| GroupBy.all([skipna])                           | 如果组中的所有值均为True，则返回True，否则返回False |
| GroupBy.any([skipna])                           | 如果组中的任何值为True，则返回True，否则返回False  |
| GroupBy.bfill([limit])                          | 向后填充值                            |
| GroupBy.backfill([limit])                       | 向后填充值                            |
| GroupBy.count()                                 | 计算组的计数，不包括缺少的值                   |
| GroupBy.cumcount([ascending])                   | 将每组中的每个项目编号，从0到该组的长度-1           |
| GroupBy.cummax([axis])                          | 每组的累积最大值                         |
| GroupBy.cummin([axis])                          | 每组的累积最小值                         |
| GroupBy.cumprod([axis])                         | 累积积                              |
| GroupBy.cumsum([axis])                          | 每组的累积总和                          |
| GroupBy.ffill([limit])                          | 向前填充值                            |
| GroupBy.first([numeric_only, min_count])        | 计算第一组值                           |
| GroupBy.head([n])                               | 返回每组的前n行                         |
| GroupBy.last([numeric_only, min_count])         | 计算最后一组值                          |
| GroupBy.max([numeric_only, min_count])          | 计算组值的最大值                         |
| GroupBy.mean([numeric_only])                    | 计算组的平均值，不包括缺失值                   |
| GroupBy.median([numeric_only])                  | 计算组的中值，不包括缺少的值                   |
| GroupBy.min([numeric_only, min_count])          | 计算组值的最小值                         |
| GroupBy.ngroup([ascending])                     | 从0到组数-1对每个组进行编号                  |
| GroupBy.nth(n[, dropna])                        | 如果n是整数，则取每组的第n行；如果n是整数列表，则取行的子集  |
| GroupBy.ohlc()                                  | 计算组的打开、高、低和关闭值，不包括缺少的值           |
| GroupBy.pad([limit])                            | 向前填充值                            |
| GroupBy.prod([numeric_only, min_count])         | 计算组值的prod                        |
| GroupBy.rank([method, ascending, na_option, …]) | 提供每组中的值的排名                       |
| GroupBy.pct_change([periods, fill_method, …])   | 计算每个值相对于组中上一个条目的变化百分比            |
| GroupBy.size()                                  | 计算组大小                            |
| GroupBy.sem([ddof])                             | 计算各组平均值的标准误差，不包括缺失值              |
| GroupBy.std([ddof])                             | 计算各组的标准偏差，不包括缺失值                 |
| GroupBy.sum([numeric_only, min_count])          | 计算组值之和                           |
| GroupBy.var([ddof])                             | 计算组的方差，不包括缺少的值                   |
| GroupBy.tail([n])                               | 返回每组的最后n行                        |

以下方法在SeriesGroupBy和DataFrameGroupBy对象中都可用，但可能略有不同，通常是DataFrameGroupBy版本允许指定axis参数，并且通常是指示是否将应用程序限制为特定数据类型的列的参数。

| api                                              | 介绍                               |
| ------------------------------------------------ | -------------------------------- |
| DataFrameGroupBy.all([skipna])                   | 如果组中的所有值均为True，则返回True，否则返回False |
| DataFrameGroupBy.any([skipna])                   | 如果组中的任何值为True，则返回True，否则返回False  |
| DataFrameGroupBy.backfill([limit])               | 向后填充值                            |
| DataFrameGroupBy.bfill([limit])                  | 向后填充值                            |
| DataFrameGroupBy.corr                            | 计算列的成对相关性，不包括NA/null值            |
| DataFrameGroupBy.count()                         | 计算组的计数，不包括缺少的值                   |
| DataFrameGroupBy.cov                             | 计算列的成对协方差，不包括NA/null值            |
| DataFrameGroupBy.cumcount([ascending])           | 将每组中的每个项目编号，从0到该组的长度-1           |
| DataFrameGroupBy.cummax([axis])                  | 每组的累积最大值                         |
| DataFrameGroupBy.cummin([axis])                  | 每组的累积最小值                         |
| DataFrameGroupBy.cumprod([axis])                 | 每组的累积积                           |
| DataFrameGroupBy.cumsum([axis])                  | 每组的累积总和                          |
| DataFrameGroupBy.describe(**kwargs)              | 生成描述性统计数据                        |
| DataFrameGroupBy.diff                            | 元素的第一离散差分                        |
| DataFrameGroupBy.ffill([limit])                  | 向前填充值                            |
| DataFrameGroupBy.fillna                          | 使用指定的方法填充NA/NaN值                 |
| DataFrameGroupBy.filter(func[, dropna])          | 返回不包含筛选元素的数据帧的副本                 |
| DataFrameGroupBy.hist                            | 制作数据帧的直方图                        |
| DataFrameGroupBy.idxmax                          | 请求轴上最大值第一次出现的返回索引                |
| DataFrameGroupBy.idxmin                          | 请求轴上最小值第一次出现的返回索引                |
| DataFrameGroupBy.mad                             | 返回请求轴值的平均绝对偏差                    |
| DataFrameGroupBy.nunique([dropna])               | 返回每个位置具有唯一元素计数的DataFrame         |
| DataFrameGroupBy.pad([limit])                    | 向前填充值                            |
| DataFrameGroupBy.pct_change([periods, …])        | 计算每个值相对于组中上一个条目的变化百分比            |
| DataFrameGroupBy.plot                            | 类实现，groupby对象的图形属性               |
| DataFrameGroupBy.quantile([q, interpolation])    | 返回给定分位数处的组值，a numpy，百分位数         |
| DataFrameGroupBy.rank([method, ascending, …])    | 提供每组中的值的排名                       |
| DataFrameGroupBy.resample(rule, *args, **kwargs) | 使用TimeGrouper时提供重采样              |
| DataFrameGroupBy.sample([n, frac, replace, …])   | 从每组返回项目的随机样本                     |
| DataFrameGroupBy.shift([periods, freq, …])       | 按观察周期移动每组                        |
| DataFrameGroupBy.size()                          | 计算组大小                            |
| DataFrameGroupBy.skew                            | 返回请求轴上的无偏倾斜                      |
| DataFrameGroupBy.take                            | 沿轴返回给定位置索引中的元素                   |
| DataFrameGroupBy.tshift                          | （已弃用）使用索引的频率（如果可用）移动时间索引         |

以下方法仅适用于SeriesGroupBy对象。

| api                                        | 介绍                     |
| ------------------------------------------ | ---------------------- |
| SeriesGroupBy.hist                         | 使用matplotlib绘制输入序列的直方图 |
| SeriesGroupBy.nlargest                     | 返回最大的n个元素              |
| SeriesGroupBy.nsmallest                    | 返回最小的n个元素              |
| SeriesGroupBy.nunique([dropna])            | 返回组中唯一元素的数目            |
| SeriesGroupBy.unique                       | 返回序列对象的唯一值             |
| SeriesGroupBy.value_counts([normalize, …]) |                        |
| SeriesGroupBy.is_monotonic_increasing      | 如果对象中的值是单调递增的，则返回布尔值   |
| SeriesGroupBy.is_monotonic_decreasing      | 如果对象中的值是单调递减的，则返回布尔值   |

以下方法仅适用于DataFrameGroupBy对象。

| api                                             | 介绍                       |
| ----------------------------------------------- | ------------------------ |
| DataFrameGroupBy.corrwith                       | 计算两两相关性                  |
| DataFrameGroupBy.boxplot([subplots, column, …]) | 从DataFrameGroupBy数据生成方框图 |

## 输入和输出 Input/output

---------

### Pickling

| api                                                   | 介绍                            |
| ----------------------------------------------------- | ----------------------------- |
| pandas.read_pickle(filepath_or_buffer[, compression]) | 从文件中加载pickled的pandas对象（或任何对象） |

### 平面文件 Flat file

| api                                                | 介绍                         |
| -------------------------------------------------- | -------------------------- |
| pandas.read_table(filepath_or_buffer[, sep, …])    | 将常规定界文件读入 DataFrame        |
| pandas.read_csv(filepath_or_buffer[, sep, …])      | 将逗号分隔值（csv）文件读取到 DataFrame |
| pandas.read_fwf(filepath_or_buffer[, colspecs, …]) | 将固定宽度格式的行表读入 DataFrame     |

### 剪贴板 Clipboard

| api                          | 介绍                         |
| ---------------------------- | -------------------------- |
| pandas.read_clipboard([sep]) | 从剪贴板读取文本，然后传递给 read_csv 读取 |

### Excel

| api                                                    | 介绍                            |
| ------------------------------------------------------ | ----------------------------- |
| pandas.read_excel(io[, sheet_name, header, names, …])  | 将Excel文件读取到 DataFrame         |
| pandas.ExcelFile.parse([sheet_name, header, names, …]) | 将指定的工作表解析为 DataFrame          |
| pandas.ExcelWriter(path[, engine])                     | 用于将 DataFrame 对象写入 Excel工作表的类 |

### JSON

| api                                                    | 介绍                      |
| ------------------------------------------------------ | ----------------------- |
| pandas.read_json([path_or_buf, orient, typ, dtype, …]) | 将 JSON 字符串转换为 pandas 对象 |
| pandas.json_normalize(data[, record_path, meta, …])    | 将半结构化 JSON 数据规范化为平面表    |
| pandas.build_table_schema(data[, index, …])            | 根据数据创建表架构               |

### HTML

| api                                              | 介绍                    |
| ------------------------------------------------ | --------------------- |
| pandas.read_html(io[, match, flavor, header, …]) | 将HTML表读入DataFrame对象列表 |

### HDFStore: PyTables (HDF5)

| api                                                   | 介绍                                     |
| ----------------------------------------------------- | -------------------------------------- |
| pandas.read_hdf(path_or_buf[, key, mode, errors, …])  | 从存储中读取信息，读取后将其关闭                       |
| pandas.HDFStore.put(key, value[, format, index, …])   | 在 HDFStore 中存储对象                       |
| pandas.HDFStore.append(key, value[, format, axes, …]) | 追加到文件中的表                               |
| pandas.HDFStore.get(key)                              | Retrieve pandas object stored in file. |
| pandas.HDFStore.select(key[, where, start, stop, …])  | 检索存储在文件中的pandas对象，可以根据条件选择             |
| pandas.HDFStore.info()                                | 打印存储中的详细信息                             |
| pandas.HDFStore.keys([include])                       | 返回与HDFStore中存储的对象相对应的键列表               |
| pandas.HDFStore.groups()                              | 返回所有顶级节点的列表                            |
| pandas.HDFStore.walk([where])                         | 遍历pandas对象的pytables组层次结构               |

### Feather

| api                                               | 介绍            |
| ------------------------------------------------- | ------------- |
| pandas.read_feather(path[, columns, use_threads]) | 从文件路径加载羽毛格式对象 |

### Parquet

| api                                          | 介绍                       |
| -------------------------------------------- | ------------------------ |
| pandas.read_parquet(path[, engine, columns]) | 从文件路径加载 parquet 对象，返回数据帧 |

### ORC

| api                              | 介绍                 |
| -------------------------------- | ------------------ |
| pandas.read_orc(path[, columns]) | 从文件路径加载ORC对象，返回数据帧 |

### SAS

| api                                              | 介绍                            |
| ------------------------------------------------ | ----------------------------- |
| pandas.read_sas(filepath_or_buffer[, format, …]) | 读取存储为XPORT或SAS7BDAT格式文件的SAS文件 |

### SPSS

| api                                                     | 介绍                  |
| ------------------------------------------------------- | ------------------- |
| pandas.read_spss(path[, usecols, convert_categoricals]) | 从文件路径加载SPSS文件，返回数据帧 |

### SQL

| api                                                 | 介绍                         |
| --------------------------------------------------- | -------------------------- |
| pandas.read_sql_table(table_name, con[, schema, …]) | 将SQL数据库表读入DataFrame        |
| pandas.read_sql_query(sql, con[, index_col, …])     | 将SQL查询读取到 DataFrame中       |
| pandas.read_sql(sql, con[, index_col, …])           | 将SQL查询或数据库表读取到 DataFrame 中 |

### Google BigQuery

| api                                                | 介绍                    |
| -------------------------------------------------- | --------------------- |
| pandas.read_gbq(query[, project_id, index_col, …]) | 加载 Google BigQuery 数据 |

### STATA

| api                                        | 介绍                                    |
| ------------------------------------------ | ------------------------------------- |
| pandas.read_stata(filepath_or_buffer[, …]) | 将Stata文件读入数据帧                         |
| pandas.StataReader.data_label              | 返回Stata文件的数据标签                        |
| pandas.StataReader.value_labels()          | 返回一个dict，将每个变量名与dict相关联，将每个值与相应的标签相关联 |
| pandas.StataReader.variable_labels()       | 以dict形式返回变量标签，将每个变量名与相应的标签相关联         |
| pandas.StataWriter.write_file()            |                                       |

## 一般性功能 General functions

--------------------------

使用以下方法的格式是 `pd.xxx()`。

### Data manipulations

| api                                                      | 介绍                                |
| -------------------------------------------------------- | --------------------------------- |
| pandas.melt(frame[, id_vars, value_vars, var_name, …])   | 取消将 DataFrame 从宽格式转为长格式，可以选择保留标识符 |
| pandas.pivot(data[, index, columns, values])             | 返回按给定索引/列值组织的重新整形数据帧              |
| pandas.pivot_table(data[, values, index, columns, …])    | 创建电子表格样式的数据透视表作为数据框               |
| pandas.crosstab(index, columns[, values, rownames, …])   | 计算两个（或更多）因素的简单交叉表                 |
| pandas.cut(x, bins[, right, labels, retbins, …])         | Bin值转换为离散的间隔                      |
| pandas.qcut(x, q[, labels, retbins, precision, …])       | 基于分位数的离散化函数                       |
| pandas.merge(left, right[, how, on, left_on, …])         | 使用数据库样式联接合并数据帧或命名系列对象             |
| pandas.merge_ordered(left, right[, on, left_on, …])      | 使用可选填充/插值执行合并                     |
| pandas.merge_asof(left, right[, on, left_on, …])         | 执行asof合并                          |
| pandas.concat(objs[, axis, join, ignore_index, …])       | 沿特定轴连接对象，沿其他轴连接可选的设置逻辑            |
| pandas.get_dummies(data[, prefix, prefix_sep, …])        | 将分类变量转换为虚拟/指示符变量                  |
| pandas.factorize(values[, sort, na_sentinel, size_hint]) | 将对象编码为枚举类型或分类变量                   |
| pandas.unique(values)                                    | 基于哈希表的唯一性                         |
| pandas.wide_to_long(df, stubnames, i, j[, sep, suffix])  | 宽面板到长格式                           |

### Top-level missing data

| api                 | 介绍             |
| ------------------- | -------------- |
| pandas.isna(obj)    | 检测类似数组的对象缺少的值  |
| pandas.isnull(obj)  | 检测类似数组的对象缺少的值  |
| pandas.notna(obj)   | 检测类似数组的对象的非缺失值 |
| pandas.notnull(obj) | 检测类似数组的对象的非缺失值 |

### Top-level conversions

| api                                        | 介绍         |
| ------------------------------------------ | ---------- |
| pandas.to_numeric(arg[, errors, downcast]) | 将参数转换为数字类型 |

### Top-level dealing with datetimelike

| api                                                    | 介绍                            |
| ------------------------------------------------------ | ----------------------------- |
| pandas.to_datetime(arg[, errors, dayfirst, …])         | 将参数转换为日期时间                    |
| pandas.to_timedelta(arg[, unit, errors])               | 将参数转换为timedelta               |
| pandas.date_range([start, end, periods, freq, tz, …])  | 返回固定频率的DatetimeIndex          |
| pandas.bdate_range([start, end, periods, freq, tz, …]) | 返回固定频率的DatetimeIndex，默认频率为工作日 |
| pandas.period_range([start, end, periods, freq, name]) | 返回一个固定的频率周期索引                 |
| pandas.timedelta_range([start, end, periods, freq, …]) | 返回固定频率TimedeltaIndex，以天作为默认频率 |
| pandas.infer_freq(index[, warn])                       | 根据输入索引推断最可能的频率                |

### 固定频率 Top-level dealing with intervals

| api                                                   | 介绍                  |
| ----------------------------------------------------- | ------------------- |
| pandas.interval_range([start, end, periods, freq, …]) | 返回固定频率IntervalIndex |

### eval 操作 Top-level evaluation

| api                                             | 介绍                        |
| ----------------------------------------------- | ------------------------- |
| pandas.eval(expr[, parser, engine, truediv, …]) | 使用各种后端将Python表达式作为字符串进行求值 |

### 散列操作 Hashing

| api                                                   | 介绍                                 |
| ----------------------------------------------------- | ---------------------------------- |
| pandas.util.hash_array(vals[, encoding, hash_key, …]) | 给定一维数组，返回确定性整数数组                   |
| pandas.util.hash_pandas_object(obj[, index, …])       | 返回Index/Series/DataFrame数据的 hash 值 |

### 测试 Testing

| API | 介绍  |
| --- | --- |
|     |     |
