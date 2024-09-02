use stage site searchapi for all search queries
stagesite
site key : ss-unbxd-auk-stage-electroplanet53791715855301
api key : d1ca1b96ccf440d772dd7e8725609f9d
searchapi : http://search.unbxd.io/d1ca1b96ccf440d772dd7e8725609f9d/ss-unbxd-auk-stage-electroplanet53791715855301/search?q=*
secret key  : 4d2aa0e8c376175cbe83342251403219

dev-site
site key : ss-unbxd-auk-dev-electroplanet53791715855096
api key : 856e58b90f8e2173e411a4e75fb553c0
searchapi : http://search.unbxd.io/856e58b90f8e2173e411a4e75fb553c0/ss-unbxd-auk-dev-electroplanet53791715855096/search?q=*
secret key  : c98cdfa44b676a1671286c161c0af9e3


Prod site
site key : ss-unbxd-auk-prod-electroplanet53791715855221
api key : f597ec250f749a27ea7c561840095bf4
searchapi : http://search.unbxd.io/f597ec250f749a27ea7c561840095bf4/ss-unbxd-auk-prod-electroplanet53791715855221/search?q=*
secret key  : 93f1fe8f538dbb00e120b5555a7b8f75 

prodmetadata.json file
{
  "siteName": "ss-unbxd-auk-prod-electroplanet53791715855221",
  "sdkVersion": "v6.2.5"
}

stagemetadata.json file
{
  "siteName": "ss-unbxd-auk-stage-electroplanet53791715855301",
  "sdkVersion": "v6.2.5"
}

one liner script for stage and prod site

stagesite
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-auk-stage-electroplanet53791715855301/ua-staging/ua.js

devsite
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-auk-dev-electroplanet53791715855096/ua-staging/ua.js

prod site script
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-auk-prod-electroplanet53791715855221/ua/ua.js

Link for bigquery report : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-auk-dev-electroplanet53791715855096?fromDate=2024-06-09&toDate=2024-06-09"
link for bigquery prod site : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-auk-prod-electroplanet53791715855221?fromDate=2024-06-09&toDate=2024-06-09"

 for as use 
 the stratagy
	 find element on which user clicks
	 fin nearest li element
	 find all elements
	 find the length of selected element li among the total li
	 pass it as data index

and srcquery will only be used in case of popular products filtered where popular products change when we hover over suggestion

ask the customer to make an attribute in parent that includdes all text 
	 
