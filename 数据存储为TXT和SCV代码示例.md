# 数据保存为TXT

```python
 # 保存为TXT文件
for item in items:
    with open(f"./txt/{table}.txt", "a") as file:
        file.write(json.dumps(item, ensure_ascii=False) + "\n")
```

# 保存为SCV

```python
import csv
  # 保存为CSV文件
         with open(f'./csv/{table}.csv', 'w', newline='') as file:
             fieldnames = ['date', 'monthly_sales', 'share_manufacturers', 'sales_ranking_month', 'maker_ranking',
                           'ranking_compact_cars']
             writer = csv.DictWriter(file, fieldnames=fieldnames)
             # 写入表头
             writer.writeheader()
             # 写入数据
             writer.writerows(items[1:])
```

# 保存为SCV

```python
import pandas as pd
df = pd.DataFrame(items[1:],columns=['date', 'monthly_sales', 'share_manufacturers', 'sales_ranking_month',
                                   'maker_ranking',
                                   'ranking_compact_cars'], dtype=str)
log.info(df)
df.to_csv(f'./csv/{table}.csv')
```


