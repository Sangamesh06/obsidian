

How to perform feed review?
	Feed review is done through the following steps
	Go to srp page of customer site  
	Check  for the following details 
	What details in product card
	Image  
	Title
	brand
	color swatches
	size
	tags
	and we have appropriate data in feed to check for the same
	
	then go to sort by filter
	go through each. filter like
	 newest
	 popular
	 price : High to low
	and check if we can implement through the feed data given
	
	then check in facets
	check for all filters
	like discount
	availability
	check if we can support them through feed given by customer
	 
	after that check for feature feilds mentioned in doc if they are there are         not
	uniqueid
	imageurl
	producturl
	cattegorypath
	these are some of the mandatory feilds we need ot checck for the same
	
	
	after that check in some other areas like breadcrumbs etc


 **How to create SFTP folder for specific customer? How to access SFTP?**
	to access sftp server
	you need to have your ssh public key added to sftp server
	to do the same raise an ops ticket 
	and assign it to either
		nitish
		 aishwaryaditya jha
	example ops ticket
	https://unbxddev.atlassian.net/browse/OPS-3392
	once added we can access the same through ssh
	
     once we have access to sftp server
     follow the  steps in mentioned below doc
     https://unbxdwiki.atlassian.net/wiki/spaces/~5d2ef17352a8370c567f276a/pages/231607             5009/SFTP+account+creation
	and replace <<username>> keyword with name of customer you want to have sftp      account setup
	
	to verify if you have setup account successfully go to filezilla access the       same customer account throughcredentials 
	hostname
	username : 
	password
	port : 22
	if you are able to login then account is setup correctly
	then create stage , dev , prod folder using filezilla by cliking on ..folder      icon you will get option to ceate directory
	create directory
	files/prod
	files/stage
	files/dev 
	etc
	based on customer requirements


**How config.json works and what configuration are stored in config.json**



**Create AWS credentials with S3 access?**

	create an ops ticket with your email id and ask for the aws s3 bucket access       to sre guys 
	(nitesh balaji) along with for which permisiion do you want i.e (io-feed-          report) and name of the permission who has the acess with permiss




How to pyconversion run in local?
to run pyconversion in local 
we need to run command (pip install https://${GITHUB_ACCESS_TOKEN}@github.com/unbxd/pyconversion/archive/refs/tags/${CONVERSION_VERSION}.tar.gz) replacing github access token with your github access token and most recent version can be found in this github repo replace conversion version with most recent verison
https://github.com/unbxd/pyconversion/blob/main/README.md
