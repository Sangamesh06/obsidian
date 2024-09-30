
import requests

# List of domains
domains = [
 'wingman-argocd.unbxd.io',
 'feed.unbxd.io',
 'feed-apac.unbxd.io',
 'feed-anz.unbxd.io',
 'feed-uk.unbxd.io',
 'feed-g-nam.unbxd.io',
 'feed-g-nam.unbxd.io'
]

# List of sitekeys to replace in the URL
sitekeys = ["ss-unbxd-auk-camper-ro-stage38961724976141","ss-unbxd-auk-camper-ro-prod38961724976275"
]

domain_mapping = {
    'ss-dev': 'wingman-argocd.unbxd.io',
    'us-east-1': 'feed.unbxd.io',
    'ap-southeast-1': 'feed-apac.unbxd.io',
    'ap-southeast-2': 'feed-anz.unbxd.io',
    'eu-west-2': 'feed-uk.unbxd.io',
    'us-west-1': 'feed-g-nam.unbxd.io',
    'us-east4rc': 'feed-g-nam.unbxd.io'
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
                print(url)
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


#print(successful_urls)
#print(succurls)



