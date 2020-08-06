import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

filename_energy = 'energy_use_per_person.csv'
energy = pd.read_csv(filename_energy, header = 0, index_col = 0)
energy.drop(columns = '2015', axis = 1, inplace = True)
energy = energy.reset_index(drop = True).transpose()
energy.columns = energy.iloc[0]
energy = energy[1:-1]

filename_co2 = 'co2_emissions_tonnes_per_person.csv'
co2 = pd.read_csv(filename_co2, header = 0, index_col = 0)
co2 = co2.reset_index().transpose()
co2.columns = co2.iloc[0]
co2 = co2[1:-1]

print(co2.index)
print(energy.index)

# Plotting
for year in range(1960, 2013):
    year = str(year)
    x_values = energy.loc[year,:]
    x_values.dropna(inplace = True)
    y_values = co2.loc[year, :]
    y_values.dropna(inplace = True)

    plt.figure()
    scatter = sns.scatterplot(x_values, y_values, palette = 'deep')
    scatter.set(xlabel='Energy consumption per person [kWh/person]', ylabel='CO_2 emissions per person [t/person]')
    scatter.set_title('Energy consumption vs CO_2 emsissions ' + str(year))

    # Automatic annotation of interesting countries
    y_distance = 1
    countries_of_interest = ['Germany', 'Iceland', 'Qatar', 'Trinidad and Tobago']
    for country in countries_of_interest:
        try:
            scatter.text(x_values[country], y_values[country] - y_distance, country, horizontalalignment='center', size='small', color='black', weight='normal')
        except:
            continue

    plt.savefig('plots/energy_use_per_person_vs_co2/energy_use_per_person_vs_co2_' + year + '.png', dpi = 300)
