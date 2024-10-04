

Steps for analytics integration


Has anyone done integration before for same site or similar sit just copy the same and change only when required

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
Sometimes even though necessary add gitqtyfromcb since the qa team will raise the error


Don’t worry about these events for version2
Click firing after add to favourite on sup and crp
Page view after sort by in srp and crp
Issues related to order

The infö that must be I notepad for analytics integration

console link : "https://console-apac.unbxd.io/departments"


stagesite
site key : ss-unbxd-stage-sheel-en41461691580142
api key : 52bfec9904263d9bde507c18cc57c59c
searchapi : http://search.unbxd.io/52bfec9904263d9bde507c18cc57c59c/ss-unbxd-stage-sheel-en41461691580142/search?q=*



Prod site
site key : ss-unbxd-auk-prod-sheel-en41461701864825
api key : d9ac0d99c446cf99be8b3ebf3658ad69
searchapi : http://search.unbxd.io/d9ac0d99c446cf99be8b3ebf3658ad69/ss-unbxd-auk-prod-sheel-en41461701864825/search?q=*

Order page url
Order credentials

Link for analytics documentation : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for analytics prerequisites : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for chatgpt : "https://chatgpt.com/"
Link for claude3 : "https://claude.ai/chats"

Link for bigquery report : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-stage-sheel-en41461691580142?fromDate=2024-06-09&toDate=2024-06-09"
link for bigquery prod site : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-auk-prod-sheel-en41461701864825?fromDate=2024-06-09&toDate=2024-06-09"





prodmetadata.json file
{
  "siteName": "ss-unbxd-auk-prod-sheel-en41461701864825",
  "sdkVersion": "v6.3.1"
}

stagemetadata.json file
{
  "siteName": "ss-unbxd-stage-sheel-en41461691580142",
  "sdkVersion": "v6.3.1"
}

one liner script for stage and prod site
stage site
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-stage-sheel-en41461691580142/ua-staging/ua.js

prod site script
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-auk-prod-sheel-en41461701864825/ua/ua.js

commands to replace sitekey apikey siteurl produrl 

%s/ss-unbxd-stage-sheel-en41461691580142/stgsitk/g
%s/52bfec9904263d9bde507c18cc57c59c/stgapik/g
%s/siteurl/stgsiturl/g



%s/ss-unbxd-auk-prod-sheel-en41461701864825/prodsitk/g
%s/d9ac0d99c446cf99be8b3ebf3658ad69/prodapik/g
%s/siteurl/prodsiturl/g


