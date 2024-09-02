How to create SFTP folder for specific customer? How to access SFTP?
How to perform feed review?
How config.json works and what configuration are stored in config.json
Create AWS credentials with S3 access?
What is AWS S3? How to download or check feed files in S3?
How to setup feed monitoring via S3 config files?
How to pyconversion run in local?
What folders need to be created in the local before run?
How to setup project in vscode or pycharm?
Basic knowledge of Argo on how the workflow orchestrator works. How to create hello world workflow in argo?
How is github actions is setup and What to check in github actions logs, when something fails?
How to raise PR? What are the guidelines that needs to be followed to write the commit message, title etc.
Basic knowledge of feed APIs
there are two apis
one to check status : https://feed.unbxd.io/api/prod-afw817831608714016/catalog/status
one is search api : https://search.unbxd.io/856e58b90f8e2173e411a4e75fb553c0/ss-unbxd-auk-dev-electroplanet53791715855096/search?q=*
in status replace domain and sitekey|
in search api replace api key and sitekey
and make to sure to check for feed upload idd so that it is the omst recent one and it is present in status api alos invalidat cache by adding   a Param cache =‘dghjk’




How to check feed API status?
go to below url
https://feed.unbxd.io/api/prod-afw817831608714016/catalog/status
replace sitekey with the sietkeys you want to check status of and alos make sure to change domain since diffrent region has diffrent you can check for domain in src/monitor/constants.py file in sols-jobs-v2 if it is indexed then previous indexng is correct


How to upload feed using curl?
How to upload schema using curl?



Basic knowledge of Unbxd search API:
unbxd search api look like this : https://search.unbxd.io/856e58b90f8e2173e411a4e75fb553c0/ss-unbxd-auk-dev-electroplanet53791715855096/search?q=
replace respective sitekey and api key to check for customer data
and make sure to add following parameters
variants = false(if there are no variants)
promotion = false(if you want to see feilds that are turned off i console)
you can add filter by appending '&filter=feildname:"feildvaluepattern" 'to url

How to check feedId with search API?
go to search api url and search for keyword "unbxdFeedId" the value of this attribute is a feedid


how to invalidate the search API cache and check the search API?
to invalidate the search api cache addd a param cache = "kjgbhj" and refresh

How to apply filters/sort?
we can apply filters sort through an extension 