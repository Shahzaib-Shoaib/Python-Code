import pandas as pd
fpath = "C:\\Users\\means\\Desktop\\Shahzaib University Assignments\\CSSE 305 Lab\\Python-Code\\demo-data.csv"
data = pd.read_csv(fpath)
# print(data.head(), "This will print only starting 5 rows")
# print(data.tail(), "This will print only ending 5 rows")
# print(data.info(),"This will print column names and their data types ")
# print(data.describe(), "This will give you the mathematical insight of data")

# print(data.loc[data['symbol'] == 'AMZN'],"This will print all the rows whose symbol equals to AMZN")
# print(data.loc[(data['symbol'] == 'AMZN') & (data['open'] > 1690)], "More conditions can be added like this")
# print(data.date, "This will only print all the rows of date column")
# print(data[["date", "symbol"]],
#       "This will only print all the rows of desired columns")
# data['change'] = data['close'] - data['open']
# print(data, "This is how you can add another column")
# pivot = data.pivot(index='date', columns='symbol', values='volume')
# symbol          AAPL     AMZN     GOOG
# date
# 2019-03-01  25886167  4974877  1450316
# 2019-03-04  27436203  6167358  1446047
# 2019-03-05  19737419  3681522  1443174
# 2019-03-06  20810384  3996001  1099289
# 2019-03-07  24796374  4957017  1166559
# print(pivot)
df = pd.DataFrame({'Student Names': ['Jenny', 'Singh', 'Charles', 'Richard', 'Veena'],
                   'Category': ['Online', 'Offline', 'Offline', 'Offline', 'Online'],
                   'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
                  'Courses': ['Java', 'Spark', 'PySpark', 'Hadoop', 'C'],
                   'Fee': [15000, 17000, 27000, 29000, 12000],
                   'Discount': [1100, 800, 1000, 1600, 600]})
p_table = pd.pivot_table(df, index=['Gender'])
print(p_table)
