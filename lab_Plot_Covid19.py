import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.dates import DateFormatter
import random

options = {
    1: "deaths",
    2: "confirmed",
    3: "recovered"
}
print("Choose option: ")
for opt in options.items():
    print('{} : {}'.format(opt[1], opt[0]))
option = options[int(input())]
print("Wait a bit, Sergei Ivanovich..")

variants = pd.read_csv('https://data.humdata.org/hxlproxy/data/download/time_series_covid19_' + option + '_global_narrow.csv?dest=data_edit&filter01=merge&merge-url01=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D1326629740%26single%3Dtrue%26output%3Dcsv&merge-keys01=%23country%2Bname&merge-tags01=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&filter02=merge&merge-url02=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D398158223%26single%3Dtrue%26output%3Dcsv&merge-keys02=%23adm1%2Bname&merge-tags02=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&merge-replace02=on&merge-overwrite02=on&filter03=explode&explode-header-att03=date&explode-value-att03=value&filter04=rename&rename-oldtag04=%23affected%2Bdate&rename-newtag04=%23date&rename-header04=Date&filter05=rename&rename-oldtag05=%23affected%2Bvalue&rename-newtag05=%23affected%2Binfected%2Bvalue%2Bnum&rename-header05=Value&filter06=clean&clean-date-tags06=%23date&filter07=sort&sort-tags07=%23date&sort-reverse07=on&filter08=sort&sort-tags08=%23country%2Bname%2C%23adm1%2Bname&tagger-match-all=on&tagger-default-tag=%23affected%2Blabel&tagger-01-header=province%2Fstate&tagger-01-tag=%23adm1%2Bname&tagger-02-header=country%2Fregion&tagger-02-tag=%23country%2Bname&tagger-03-header=lat&tagger-03-tag=%23geo%2Blat&tagger-04-header=long&tagger-04-tag=%23geo%2Blon&header-row=1&url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_' + option + '_global.csv', skiprows=[1])
print("Choose country: ")
countries = variants['Country/Region'].unique()
print(" ,".join(countries))
print("Enter country name there: ")
country = [input()]
country_column = country[0]
variants = variants[variants['Province/State'].isnull()]
variants = variants[variants['Country/Region'].isin(country)]
values = variants.pivot (index='Date', columns=['Country/Region'], values='Value')


dates = values.index.tolist()
values2 = values.copy()
for i in range(len(dates)):
    if i == 0:
        values2.loc[dates[i], country_column] = 0
    else:
        values2.loc[dates[i], country_column] = values.loc[dates[i], country_column] - values.loc[
            dates[i - 1], country_column]



def random_color():
     rand = lambda: random.randint(100, 255)
     return '#%02X%02X%02X' % (rand(), rand(), rand())

plt.style.use('ggplot')
plot = values.plot(figsize=(12, 8), linewidth=5, legend=False)
plot.legend(prop={'size': 6})
plot.grid(random_color())
plot.set_xlabel('Date')
plot.set_ylabel('Absolute value of Cases') # абсолютное значение случаев



plot2 = values2.plot(figsize=(12, 5), linewidth=7, legend=True)
plot2.legend(prop={'size': 8})
plot2.grid(random_color())
plot2.set_xlabel('Date')
plot2.set_ylabel('Increase of Cases') # прирост случаев


plt.show()
