 ticket link
https://unbxddev.atlassian.net/browse/CS-6852

Has anyone done integration before for same site or similar sit just copy the same and change only when required : no

Is there any particular approach wen need to follow 
Test for cart removal event no event(cart) should fire 
Test for search event on using sort by and page view should only fire(using fire search misc in search event)
Test if category page and order events are integrated 
Ask for how to do order and can we do It using cod
Whenever doing config do for mobile and also check for mobile also
Just for safety check for pid in feed sometime pid pattern is different
If in big query error is coming it s because of mobile version may be wrong or different selectors
Try to use url selectors along with Dom selectors
check if selector for product click grid are same for grid and list view and browse pages
Sometimes even though not necessary add gitqtyfromcb since the qa team will raise the error

Don’t worry about these events for version2
Click firing after add to favourite on sup and crp
Page view after sort by in srp and crp
Issues related to order

The infö that must be I notepad for analytics integration

console link : "https://console-apac.unbxd.io/departments"


stagesite
site key : ss-unbxd-aus-dev-HealthyplanetCanada802921717490852
api key : 207e83a9df1d940ca3ae9010ffc40b2f
searchapi : http://search.unbxd.io/207e83a9df1d940ca3ae9010ffc40b2f/ss-unbxd-aus-dev-HealthyplanetCanada802921717490852/search?q=*

[http://search.unbxd.io/3dd9846a60b841cedadb80ec181914df/ss-unbxd-aapac-dev-Max-LandMark48741709218573/search?q=*
http://search.unbxd.io/ff6c15ca7695f263efbaae4ec0ac64d7/ss-unbxd-aus-prod-HealthyplanetCanada802921717496646/search?q=*

http://search.unbxd.io/ff6c15ca7695f263efbaae4ec0ac64d7/ss-unbxd-aus-prod-HealthyplanetCanada802921717496646/search?q=*

Prod site
site key : ss-unbxd-aus-prod-HealthyplanetCanada802921717496646
api key : ff6c15ca7695f263efbaae4ec0ac64d7
searchapi : http://search.unbxd.io/ff6c15ca7695f263efbaae4ec0ac64d7/ss-unbxd-aus-prod-HealthyplanetCanada802921717496646/search?q=*

Order page url
Order credentials

Link for analytics documentation : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for analytics prerequisites : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for chatgpt : "https://chatgpt.com/"
Link for claude3 : "https://claude.ai/chats"

Link for bigquery report : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-aus-dev-HealthyplanetCanada802921717490852?fromDate=2024-06-09&toDate=2024-06-09"
link for bigquery prod site : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-aus-prod-HealthyplanetCanada802921717496646?fromDate=2024-06-09&toDate=2024-06-09"

commands to replace sitekey apikey siteurl produrl 
%s/ss-unbxd-aus-dev-HealthyplanetCanada802921717490852/stgsitk/g
%s/207e83a9df1d940ca3ae9010ffc40b2f/stgapik/g
%s/siteurl/stgsiturl/g
secret key for stage : 5be70e482e08fa6aec1250d25cb7f4ce

%s/ss-unbxd-aus-prod-HealthyplanetCanada802921717496646/prodsitk/g
%s/ff6c15ca7695f263efbaae4ec0ac64d7/prodapik/g
%s/siteurl/prodsiturl/g
secretkey for the prod site : 2edf33fcdfe778fbafcbce860e84f7dd


prodmetadata.json file
{
  "siteName": "ss-unbxd-aus-prod-HealthyplanetCanada802921717496646",
  "sdkVersion": "v6.2.5"
}

stagemetadata.json file
{
  "siteName": "ss-unbxd-aus-dev-HealthyplanetCanada802921717490852",
  "sdkVersion": "v6.2.5"
}



usa site
prod site
api key : cce06d4fd02bc41863902c099cee1263
site key : ss-unbxd-aus-Prod-healthyplanetUSA802921717496408

dev Site
site key : ss-unbxd-aus-dev-healthyplanet802921717478591
api key : f564e5c6b98ba9a8ac5584e9b3f7a598
secret key : 8b2c14fda1b99646f2397caa482c04ff


use the devsearch api feed for prod sites also
canada
search api : https://search.unbxd.io/207e83a9df1d940ca3ae9010ffc40b2f/ss-unbxd-aus-dev-HealthyplanetCanada802921717490852/search?q=*
one liner script
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-aus-dev-HealthyplanetCanada802921717490852/ua-staging/ua.js


usa
search api :
https://search.unbxd.io/f564e5c6b98ba9a8ac5584e9b3f7a598/ss-unbxd-aus-dev-healthyplanet802921717478591/search?q=*

one liner script

gcm && gfu && gmu && gpom && git checkout  -b HealthyplanetCanada
grm
gcm && gfu && gmu && gpom && git checkout  -b HealthyplanetUSAProd


swatch image url
swatch product url

