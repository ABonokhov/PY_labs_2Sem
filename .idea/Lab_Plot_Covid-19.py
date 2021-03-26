"""
С сайта https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases
собрать статистику по заболеваемости, выздоровлению и смертям
Скрипт выводит график по выбранной стране(странам) и выбранной категории(заболели, выздоровели, умерли)
страну выбрать на усмотрение, или из списка или с помощью ввода
Также реализовать вывод  не не только абсолютных значений, но и прирост 
Скрипт можно использовать и этот (здесь статистика из другого сайта и в другой форме),
но желательно написать свой
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.dates import DateFormatter
import random

# Section 2 - Loading and Selecting Data
options = {1: "deaths", 2: "confirmed", 3: "recovered"}

print("Choose option: ")
for opt in options.items():
    print('{} - {}'.format(opt[0], opt[1]))

option = options[int(input())]

variants = pd.read_csv(
    "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_" + option + "_global.csv&filename=time_series_covid19_" + option + "_global.csv")
print("Choose country: ")
countries = variants['Country/Region']
print("n/".join(countries))
print("Enter country name there: ")
country = [input()]
country_column = country[0]
variants = variants[variants['Province/State'].isnull()]
variants = variants[variants['Country/Region'].isin(country)]
#values = variants.pivot(index='Date', columns=['Country/Region/State/Province'], values='Value')
print(variants)

color_list = ["orange", "pink", "red", "blue", "pink", "purple", "virgin", 'green', 'brown']
for i in range(country):
    print(random.choice(color_list))
    plt.style.use('fivethirtyeight')

dates = values.index.tolist()
valuesSecond = values.copy()
for i in range(len(dates)):
    if i == 0:
        valuesSecond.loc[dates[i], country_column] = 0
    else:
        valuesSecond.loc[dates[i], country_column] = values.loc[dates[i], country_column] - values.loc[
            dates[i - 1], country_column]
print(variants)

plot = values.plot(figsize=(12, 8), linewidth=5, legend=False)
plot.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('# of Cases')

# Section 8 - Assigning Colour
for country in list(values.keys()):
    plot.text(x='covid.index[-1]', y='covid[country].max()', c='colors[country]', s='country', weight='bold')

plt.show()
