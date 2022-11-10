import pandas as pd
from datetime import datetime

file = open("last_logged.txt", "r")

last_logged = pd.to_datetime(file.read(), format='%d-%b-%y %I:%M:%S %p')
def sort_alarms(site):
    df = pd.read_csv(f'test_data/{site}.csv')
        
    df['time'] = pd.to_datetime(df['time'], format='%d-%b-%y %I:%M:%S %p')

    df.sort_values(by=['alarmState', 'time'], ascending = [True, False], ignore_index = True, inplace = True)

    df = df[df['alarmState'] == 'active']

    for row in df.itertuples():
        if row[3] < last_logged:
            df = df[df.index[0]:df.index[row[0]]]
            break
        else:
            continue

    return df

##alarm_list = []
##for site in ['site1', 'site2', 'site3', 'site4', 'site5']:
##    alarm_list.append(sort_alarms(site))
##
##alarms_to_log = pd.concat(alarm_list, ignore_index = True)
##print(alarms_to_log)


alarms_to_log = pd.DataFrame()
for site in ['site1', 'site2', 'site3', 'site4', 'site5']:
    alarms_to_log = alarms_to_log.append(sort_alarms(site), ignore_index = True)

print(alarms_to_log)
alarms_to_log.to_csv('alarms_to_log.csv', index = False)

file = open("last_logged.txt", 'w')
new_last_logged = (datetime.now()).strftime('%d-%b-%y %I:%M:%S %p')
file.write(new_last_logged)
file.close()

