import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

filename = 'energy_use_per_person.csv'
df = pd.read_csv(filename, header = 0, index_col = 0)
df.drop(columns = '2015', axis = 1, inplace = True)
df = df.reset_index(drop = True).transpose()

df.columns = df.iloc[0]
df = df[1:-1]

# Plotting

plt.plot(range(1960,2014), 'China', data=df)
plt.plot(range(1960,2014), 'Germany', data=df)
plt.plot(range(1960,2014), 'United States', data=df)
plt.plot(range(1960,2014), 'Norway', data=df)
plt.plot(range(1960,2014), 'Senegal', data=df)
plt.title('Energy use per person comparison')
plt.xlabel('t [y]')
plt.ylabel('kWh/person')
plt.axis([1965,2014,0,100000])
plt.legend()
plt.show()
