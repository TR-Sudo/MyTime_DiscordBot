import pandas as pd

time_zone_df = pd.read_csv('timezone-abbreviations.csv')

#checks if time zone provided is valid
def check_time_zone(time_zone):
    return str(time_zone) in time_zone_df['Abbreviation'].unique()
