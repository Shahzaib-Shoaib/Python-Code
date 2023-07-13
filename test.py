import pandas as pd

data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 'France', 'Pakistan', 'Italy', 'Canada', 'Brazil'],
    'Population': [331002651, 1444216107, 126476461, 83783942, 1393409038, 67886011, 65273511, 225199937, 60461826, 37742154, 213993437],
    'Area': [9525067, 9640011, 377975, 357022, 3287263, 242900, 551695, 881912, 301340, 9984670, 8515767],
    'GDP': [21439453, 14342903, 5082465, 4012334, 2954261, 3076270, 2942227, 109200, 1940997, 1778658, 2142999],
    'Continent': ['North America', 'Asia', 'Asia', 'Europe', 'Asia', 'Europe', 'Europe', 'Asia', 'Europe', 'North America', 'South America']
}

df = pd.DataFrame(data)
print("This is raw data \n")
print(df, "\n")
df['Population Density'] = df['Population'] / df['Area']
print("This is the changed data after a new column 'Population Density' is added \n")
print(df, "\n")

p_table = pd.pivot_table(df, index=['Continent'], values=[
                         'Area', "Population", 'GDP'], aggfunc='mean')
print("Data sorted according to the Continents, all values in these columns are mean values  \n")

print(p_table)