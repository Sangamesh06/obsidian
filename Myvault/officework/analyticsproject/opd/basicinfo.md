https://github.com/unbxd/analytics-customerjs/pull/455/files(pr raised for opd analytics integration)


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
site key : ss-unbxd-ganz-dev-opd-nz8091724742488
api key : 27dd8e93d40c61b78eed834d15d4b8b8
searchapi : https://search.unbxd.io/27dd8e93d40c61b78eed834d15d4b8b8/ss-unbxd-aapac-dev-OPD56261719910827/search?q=*
secretkey : bd144743d0abf4f920111576ca59578d


Prod site
site key : sitekeyv2
api key : apikeyv2
searchapi : http://search.unbxd.io/apikeyv2/sitekeyv2/search?q=*

Order page url
Order credentials

Link for analytics documentation : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for analytics prerequisites : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for chatgpt : "https://chatgpt.com/"
Link for claude3 : "https://claude.ai/chats"

Link for bigquery report : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/ss-unbxd-ganz-dev-opd-nz8091724742488?fromDate=2024-06-09&toDate=2024-06-09"
link for bigquery prod site : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/sitekeyv2?fromDate=2024-06-09&toDate=2024-06-09"





prodmetadata.json file
{
  "siteName": "sitekeyv2",
  "sdkVersion": "v6.2.5"
}

stagemetadata.json file
{
  "siteName": "ss-unbxd-ganz-dev-opd-nz8091724742488",
  "sdkVersion": "v6.2.5"
}

one liner script for stage and prod site
stage site
https://libraries.unbxdapi.com/sdk-clients/ss-unbxd-ganz-dev-opd-nz8091724742488/ua-staging/ua.js

prod site script
https://libraries.unbxdapi.com/sdk-clients/sitekeyv2/ua/ua.js

commands to replace sitekey apikey siteurl produrl 

%s/ss-unbxd-ganz-dev-opd-nz8091724742488/stgsitk/g
%s/61549fedbff9ae0e6a870b5bba94808a/stgapik/g
%s/siteurl/stgsiturl/g



%s/sitekeyv2/prodsitk/g
%s/apikeyv2/prodapik/g
%s/siteurl/prodsiturl/g


const element = document.querySelector('.p-minicart-scroll-wrapper .p-product-info');


	/Users/unbxd/Desktop/personal/obsidian/Myvault/officework/analyticsproject/opd/basicinfo.md
