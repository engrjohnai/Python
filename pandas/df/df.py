import pandas as pd


df = pd.read_csv('/mnt/c/Users/Engr John/OneDrive - Innocorp/Desktop/Code/python/pandas/weather_data.csv')


r1 = df['temperature'].mean() # Get the mean
r2 = df.describe() # Get statistical Information
r3 = df[df.temperature>=32] # Get the days when them temp was greater than or equal to 32
r4 = r4 = df[df.temperature == df.temperature.max()][['day', 'temperature']] # find the row where the temperature is at its maximum,

print(df.index)

print(df.set_index('day')) # Use day as the index instead of numbers

print(df.set_index('day', inplace=True)) # Now the index will change to days

print(df.index)

r5 = df.loc['1/4/2017']
print(r5)

df.reset_index(inplace=True) #Reset index back to original
print(df)



