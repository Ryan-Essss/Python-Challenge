import os
import csv

csvpath = os.path.join ('Resources', 'employee_data.csv')
output_file = os.path.join ('Analysis', 'analysis.csv')

# Set Variables
e_id = []
full_name = []
first_name = []
last_name = []
ymd = []
mdy = []
ssn = []
ssn_obscure = '***-**-' # statically set the value
# ssn_f = []
# ssn_m = []
ssn_e = []
final_ssn = []
state = []
short_state = []
final_list = []


state_ab = {'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',}


# Reads the file
with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header row
    csv_header = next(csvreader)

    for row in csvreader:
        e_id.append(row[0])
        full_name.append(row[1])
        ymd.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
    # print(full_name)
    # print(state)

    for part in full_name:
        first_name.append(part.split(' ')[0])
        last_name.append(part.split(' ')[1])
    # print(first_name)

    for var in ymd:
        y = var.split('-')[0]
        m = var.split('-')[1]
        d = var.split('-')[2]
        mdy.append(f'{m}/{d}/{y}')
    # print(mdy)

    for part in ssn:
        ssn_e = part.split('-')[2]
        formatted_ssn = ssn_obscure + ssn_e
        final_ssn.append(formatted_ssn)
    # print(ssn_f)
    # print(ssn_m)
    # print(ssn_e)
    # print(final_ssn)

    for i in state:
        new_state = state_ab[i]
        short_state.append(new_state)
    # print(short_state)
 
        
    final_list = zip(e_id, first_name, last_name, mdy, final_ssn, short_state)
        # print(final_list)

    # open the output file or whatever this does
    with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)
        writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        writer.writerows(final_list)

    
    






