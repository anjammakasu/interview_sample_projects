import pandas as pd

# Read data from input excel file
# 'Place your .xlsx file path here'
data = pd.read_excel(r'C:\Users\xxxx\General\Input_SpeedandDistance.xlsx')

# Split the duration range to its lower and upper values
data['Duration_lower'] = data['Duration'].map(lambda x:x.split('-')[0])
data['Duration_upper'] = data['Duration'].map(lambda x:x.split('-')[1])

# Extract only the integer value from the lower and upper values
data['Duration_lower_range'] = data.Duration_lower.str.extract(r'^(-?\d+)').astype(int)
data['Duration_upper_range'] = data.Duration_upper.str.extract(r'(\d+)').astype(int)

# Time Taken = Upper range - Lower range in Duration
data['Time'] = data['Duration_upper_range'] - data['Duration_lower_range']

# Distance travelled = Speed * Time taken
data['Distance'] = data['Speed Km/h'] * data['Time']

# Calculation the Total distance travelled and Total Time taken, to calculate Avg Speed
data['Total_Distance'] =data['Distance'].sum()
data['Total_Time_Taken'] = data['Time'].sum()

# Average Speed = Total Distance Travelled / Total time taken
data['Average_Speed'] = data['Total_Distance'] / data['Total_Time_Taken']

data.to_csv('Output_AvgSpeed.csv')
