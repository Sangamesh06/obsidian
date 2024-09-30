```
**Getsitekeys.py**

import csv

  

# Open the CSV file

with open('customer_sitekeys.csv', 'r') as file:

    reader = csv.DictReader(file, delimiter='\t')

  

    # Create a list to store the selected rows

    selected_rows = []

  

    # Iterate over each row in the CSV file

    for row in reader:

        # Check if the 'Sitekey' column contains the 'prod' keyword

        # and the 'Version Name' column does not contain 'prod-incremental'

        if 'prod' in row['Sitekey'].lower() and 'prod-incremental' not in row['Name'].lower():

            selected_rows.append(row['CustomerName'] + '\t' + row['Sitekey'] + '\t' + row['Version'] + '\t' + row['Name'])

  

    # Open a new file to write the selected rows

    with open('sitekeys.csv', 'w') as output_file:

        # Write each row on a new line

        for row in selected_rows:

            output_file.write(row + '\n')

  

    print("Selected rows written to sitekeys.csv")

  

  

Absentsitekeys.py

import json

import csv

  

# Read rows from sitekeys.csv file

rows_from_file = []

with open('sitekeys.csv', 'r') as f:

    reader = csv.DictReader(f, delimiter='\t')

    for row in reader:

        rows_from_file.append(row)

  

# Read site keys from sitekeys.json file

with open('src/monitor/sites.json', 'r') as f:

    sitekeys_json = json.load(f)

    sitekeys_from_json = [site['site_key'] for site in sitekeys_json]

    print(sitekeys_from_json)

  

# Find rows that have a site key not present in sitekeys.json

rows_not_in_json = [row for row in rows_from_file if row['Sitekey'] not in sitekeys_from_json]

  

# Write the rows that are not in sitekeys.json to absent_sitekeys.csv

with open('absent_sitekeys.csv', 'w', newline='') as output_file:

    fieldnames = rows_from_file[0].keys()  # Get the fieldnames from the first row

    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row

    for row in rows_not_in_json:

        writer.writerow(row)

  

print("Rows with site keys absent in sitekeys.json written to absent_sitekeys.csv")

  

  

  

  

Get schedule2.py

import os

import csv

import yaml

from cron_descriptor import get_description

  

def cron_to_lookback_period(cron_expression):

    description = get_description(cron_expression)

    interval_parts = description.split()[-1].split('-')

  

    if len(interval_parts) == 2:

        interval_unit = interval_parts[1]

        interval_value = int(interval_parts[0])

    else:

        interval_unit = interval_parts[0]

        interval_value = 1

  

    if interval_unit == 'minutes':

        lookback_period = interval_value

    elif interval_unit == 'hours':

        lookback_period = interval_value * 60

    elif interval_unit == 'days':

        lookback_period = interval_value * 24 * 60

    else:

        return "Unsupported interval unit"

  

    return lookback_period

  

# Path to the directory containing the customer folders

base_dir = "src"

  

# Read the CSV file

csv_data = []

with open("absent_sitekeys.csv", "r") as csv_file:

    reader = csv.DictReader(csv_file)

    csv_data = list(reader)

  

# Create and open the CSV file for writing

with open("output.csv", "w", newline='') as output_file:

    fieldnames = ["CustomerName", "Sitekey", "Name", "Schedule", "LookbackPeriod"]

    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

  

    # Write the header row

    writer.writeheader()

  

    # Loop through each customer in the CSV data

    for customer in csv_data:

        customer_name = customer["CustomerName"]

        sitekey = customer["Sitekey"]

        docker_version = customer["Version"]

        name = customer["Name"]

  

        # Path to the customer folder

        customer_dir = os.path.join(base_dir, customer_name, "argo" , "cron_workflow")

  

        # Check if the customer folder and argo-cron-workflow folder exist

        if os.path.isdir(customer_dir):

            for filename in os.listdir(customer_dir):

                if filename.endswith(".yml"):

                    file_path = os.path.join(customer_dir, filename)

                    with open(file_path, "r") as yml_file:

                        data = yaml.safe_load(yml_file)

  

                    if "template" in name.lower():

                        if data["spec"]["workflowSpec"]["workflowTemplateRef"]["name"] == name:

                            lookback_period = cron_to_lookback_period(data["spec"]["schedule"])

  

                            # Write data to CSV

                            writer.writerow({

                                "CustomerName": customer_name,

                                "Sitekey": sitekey,

                                "Name": name,

                                "Schedule": data["spec"]["schedule"]

                            })

                    else:

                        name2 = name.strip('[]').replace("'", "")

                        if data["metadata"]["name"] == name2:

                            lookback_period = cron_to_lookback_period(data["spec"]["schedule"])

  

                            # Write data to CSV

                            writer.writerow({

                                "CustomerName": customer_name,

                                "Sitekey": sitekey,

                                "Name": name,

                                "Schedule": data["spec"]["schedule"]

  

                            })
```


```
	Feed
Site key : demo-unbxd700181503576558
Api key : fb853e3332f2645fac9d71dc63e09ec1
Secret key : 031d8746b5cd07ca56ca80f54b5b7c0b




Read about download function
Read about featured feilds
Read about default datatypes
Read about sftp src dir dest dir
What is root dir
Read about link datatype(used for urls)
Use any of the customer 

```



![[Screenshot 2024-06-10 at 10.17.09 PM.png]]



```
Errors
 installation  error
Try to resolve like this
Change wifi source and try
Try brew update and then try 
Try pip upgrade and then try back




Read only file error
Add users at start without slash and check again

```

