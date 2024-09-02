```
import requests

# List of domains
domains = [
    'wingman-argocd.unbxd.io',
    'feed-anz.unbxd.io',
    'feed-uk.unbxd.io',
    'feed-g-nam.unbxd.io'
    'feed.unbxd.io',
]

# List of sitekeys to replace in the URL
sitekeys = [
 "ss-unbxd-aapac-prod-pak29411712129456",
"ss-unbxd-aapac-prod-bz29411712129281",
 "ss-unbxd-prod-ID-unilever-Bahasa29411703238089",
 "ss-unbxd-prod-ID-unilever13731696257710", 
 "ss-unbxd-prod-th-thailand13731636957583", 
 "ss-unbxd-prod-eng-thailand13731636957760", 
 "prod-ump13731617272191",
 "prod-ph13731629461969"
]

# The base URL
base_url = "https://{domain}/api/{sitekey}/catalog/status"

# Dictionary to store successful sitekeys and domains
successful_urls = {}

for domain in domains:
    for sitekey in sitekeys:
        # Replace placeholders with domain and sitekey
        url = base_url.format(domain=domain, sitekey=sitekey)
        
        try:
            # Send GET request to the URL
            response = requests.get(url)
            
            # Check if the response status is 200 and the content is not empty
            if response.status_code == 200 and response.content:
                successful_urls[sitekey] = domain
                sitekeys.remove(sitekey) 
        except requests.exceptions.RequestException as e:
            print(f"Request to {url} failed: {e}")

# Print the successful sitekeys and domains
print("Successful URLs:")
for sitekey, domain in successful_urls.items():
    print(f"Sitekey: {sitekey}, Domain: {domain}")


```
