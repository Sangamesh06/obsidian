

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
site key : sitekeyv1
api key : apikeyv1

searchapi : http://search.unbxd.io/a9e2130c468925dda597572094f4c461/ss-unbxd-demo-shoplc-com818081619763026/search?q=*



Prod site
site key : prod-sfshoplc-com818081629357814
api key : cd2c4fd00ceedbc0e711cbbac3e95aff
searchapi : http://search.unbxd.io/cd2c4fd00ceedbc0e711cbbac3e95aff/prod-sfshoplc-com818081629357814/search?q=*

Order page url
Order credentials

Link for analytics documentation : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for analytics prerequisites : "https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration"
Link for chatgpt : "https://chatgpt.com/"
Link for claude3 : "https://claude.ai/chats"

Link for bigquery report : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/sitekeyv1?fromDate=2024-06-09&toDate=2024-06-09"
link for bigquery prod site : "http://aggregator.unbxdapi.com/analytics-aggregator/integration-status/prod-sfshoplc-com818081629357814?fromDate=2024-06-09&toDate=2024-06-09"





prodmetadata.json file
{
  "siteName": "prod-sfshoplc-com818081629357814",
  "sdkVersion": "v6.3.1"
}

stagemetadata.json file
{
  "siteName": "ss-unbxd-demo-shoplc-com818081619763026",
  "sdkVersion": "v6.3.1"
}

one liner script for stage and prod site
stage site
https://libraries.unbxdapi.com/sdk-clients/sitekeyv1/ua-staging/ua.js

prod site script
https://libraries.unbxdapi.com/sdk-clients/prod-sfshoplc-com818081629357814/ua/ua.js

commands to replace sitekey apikey siteurl produrl 

%s/sitekeyv1/stgsitk/g
%s/apikeyv1/stgapik/g
%s/siteurl/stgsiturl/g



%s/prod-sfshoplc-com818081629357814/prodsitk/g
%s/cd2c4fd00ceedbc0e711cbbac3e95aff/prodapik/g
%s/siteurl/prodsiturl/g

https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2416869429/Prerequisites+for+Analytics+v2+Integration

https://unbxdwiki.atlassian.net/wiki/spaces/UU/pages/2412052481/Analytics+V2+Config+Documentation#Pageview

check if there is pid and vid for all products in srp , pdp , category , cart , ccartpopup pages
and ensure it is in dev element rather than just in script or some other element

for autosuggest 
elemwrapper should hold the entire value like suggestion otherwise ask the customer to create an attribute that holds the entire suggestion 
type : check if in suggestion is ther attribute that tells the type of suggestion or products that is (popular product , keyword suggestion)
check if there are popular prodducts filtered that is used for src query
pid : for popular products and popular products filtered there should be pid
srcquery : 
titleasquery : to recieve 



for product impressions
for search result page : search query is required
for 



some of the questions related to analytics integration
1) should product elementwrapper select recommendation products also
		no


autosuggest 
	doubt for src query in autosuggest what if whole title is nt present in one dev
	and element having title does not have class name for the same
	
