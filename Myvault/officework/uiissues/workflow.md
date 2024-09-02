## for stage site 
steps to complete autosuggest css
 
		 go to master branch 
			 git fetch upstream
			 git merge upstream/master 
			 git push origin main
		  create a new branch
			  git checkout -b websitenamestage
			  go to customer folder
			  make changes in required file
			  make change in setting.json
```
```

run these two commmands
	x

run these commands for autosuggesst css updates
grunt bundlecss --custom=autoSuggestcss{file in cocnfig.json of customfile section}
grunt uploadcss --custom=autoSuggestcss
grunt invalidatecss --custom=autoSuggestcss

mkae it js if it is js otheriwse css

grunt uploadjs --custom=stageAutoSuggestjs
grunt invalidatejs --custom=stageAutoSuggestjs


there will be 2 types of file updated
	1st type you have changes(1st type)
	 automatically changed after runnung build commandd

	 git add 1st type
	  git commit -m what changes you have fixed
	  git add 2nd type
	  git commit -m "updated bundle and biuild files"


## for prod site 
   steps to complete autosuggest css
	 for stage 
		 go to master branch 
			 git fetch upstream
			 git merge upstream/master 
			 git push origin main
		  create a new branch
			  git checkout -b websitenamestage
			  go to customer folder
			  make changes in required file
			  make change in setting.json
```
```

run these two commmands

run these commands for autosuggesst css updates
grunt bundlecss --custom=prod-autoSuggestcss
grunt bundlecss --custom=autoSuggestcss




increase the version in build file
there will be 2 types of file updated
	1st type you have changes(1st type)
	 automatically changed after runnung build commandd

	 git add 1st type
	  git commit -m what changes you have fixed
	  git add 2nd type
	  git commit -m "updated bundle and biuild files"

/Users/unbxd/Documents/solsjobcopy/solution-jobs-v2/src/kits/Users/mnt/ebs/kits/ss-unbxd-gcp-kits-com-stage16621684171061/full/ss-unbxd-gcp-kits-com-stage16621684171061_2024_08_19_09_56_45_data_products.json


stage upload id
f22d4b20-61a8-48b1-8072-487921af335f

prod upload id
2190a92d-cc9b-49dc-9a16-aecc82cb8a06



grunt bundlejs --custom=searchjs
grunt uploadjs --custom=searchjs
grunt invalidatejs --custom=searchjs

for 
https://staging.ezcontacts.com/eyeglasses/quickship:true/brand:oakley/page:2/

first change

grunt bundlejs --custom=prod-searchjs
