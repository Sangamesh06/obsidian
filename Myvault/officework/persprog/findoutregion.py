import requests

# List of domains
domains = [
    'feed-apac.unbxd.io',
    'wingman-argocd.unbxd.io',
    'feed-anz.unbxd.io',
    'feed-uk.unbxd.io',
    'feed-g-nam.unbxd.io'
    'feed.unbxd.io',
]

# List of sitekeys to replace in the URL
sitekeys = [
"ss-unbxd-aapac-prod-Homecentre-LandMark48741709218990",
"ss-unbxd-aapac-prod-Max-LandMark48741709218622",
"ss-unbxd-aapac-prod-lifestyle-LandMark48741706891693"
]

domain_mapping = {
    'ss-dev': 'wingman-argocd.unbxd.io',
    'us-east-1': 'feed.unbxd.io',
    'ap-southeast-1': 'feed-apac.unbxd.io',
    'ap-southeast-2': 'feed-anz.unbxd.io',
    'eu-west-2': 'feed-uk.unbxd.io',
    'us-west-1': 'feed-g-nam.unbxd.io',
}

# The base URL
base_url = "https://{domain}/api/{sitekey}/catalog/status"

# Dictionary to store successful sitekeys and domains
successful_urls = {}
succurls= []
for domain in domains:
    for sitekey in sitekeys:
        # Replace placeholders with domain and sitekey
        url = base_url.format(domain=domain, sitekey=sitekey)
        
        try:
            # Send GET request to the URL
            response = requests.get(url)
            
            # Check if the response status is 200 and the content is not empty
            if response.status_code == 200 and response.content:
                response = requests.get(url)
                json_data = response.json()
                array_length = len(json_data)
                print(f"The JSON array contains {array_length} objects.")
                if(array_length >= 1):
                    successful_urls[sitekey] = domain
                    succurls.append(url)
                    sitekeys.remove(sitekey)
        except requests.exceptions.RequestException as e:
            print(f"Request to {url} failed: {e}")
print(successful_urls)
for sitekey, domain in successful_urls.items():
    # Reverse lookup to find the key for the current domain in the mapping
    for key, mapped_domain in domain_mapping.items():
        if domain == mapped_domain:
            successful_urls[sitekey] = key
            break

# print(successful_urls)
print(succurls)

import json

# Sample dictionary with site keys and regions
sitekey_region_mapping = successful_urls

# Predefined values
lookback_period_minutes = 1470
additional_email_ids = [
"Suchith.HS@landmarkgroup.in",
"AnilKumar.Gajula@landmarkgroup.in",
"Anurag.Kaliya@landmarkgroup.in",
"Savitha.Shivananda@landmarkgroup.in"
]

# List to hold the generated JSON objects
json_objects = []

# Loop through the dictionary to create JSON objects
for site_key, region in sitekey_region_mapping.items():
    json_object = {
        "site_key": site_key,
        "lookback_period_minutes": lookback_period_minutes,
        "region": region
    }

    # Include the additional email ids if they are not empty
    if additional_email_ids:
        json_object["additional_email_id"] = additional_email_ids

    # Add the JSON object to the list
    json_objects.append(json_object)

# Print the JSON objects
for obj in json_objects:
    print(json.dumps(obj, indent=2))

# Print the successful sitekeys and domains
# print("Successful URLs:")
# for sitekey, domain in successful_urls.items():
#     print(f" {sitekey}, {domain}")

