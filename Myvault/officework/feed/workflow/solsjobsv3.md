before doing feed-review some of the points to keep in mind
1. UniqueId should be mapped to another attribute to make it searchable Ex: productId
2. Newness attribute should be integer and delta of today’s date and product created date
3. Though the customer is not implementing browse, we still need categoryPath/categoryPathId
4. imageUrl and brand should be multivalue
5. Title is coming up differently. Please follow uniformity across all catalogs
6. All price values should be int/float



requirements
csv file (feed file)
site credentials
feature feilds information
schema information : add datatype as long text fro description
transformations : rename the feild to condition to product_condition

==note==
if you are doing it for sirst time please change upload to non_upload so that you willl get file in local and see if it is correct or not


sftp credentials
username
password
path





use as direct tools
fork repo
git@github.com:unbxd/solution-jobs-v3.git
clone repo
git@github.com:sangamesh-somashetti-unbxd/solution-jobs-v3.git


fork repo
git@github.com:unbxd/feed-conversion.git
clone repo

git@github.com:sangamesh-somashetti-unbxd/feed-conversion.git
open feed-conversion
update repo in local(in main branch)
gcm
gfu
gmu
gpom
git checkout -b {branchname}

create virtual enviornment
    python3 -m venv venv
    - source venv/bin/activate 

install dependencies
     pip install -r requirements.txt


configure project interpreter
    Go to PyCharm > Settings on macOS or File > Settings on windows.
    In the left sidebar, navigate to Project: feed-conversion > Python Interpreter
    .(to add local interpreeter)
    chooose existing
![[Screenshot 2024-08-18 at 6.21.54 PM.png]]
    Click the gear icon on the right and select “Add Interpreter”.
    Choose “Virtualenv Environment” and select your project’s virtual environment (venv).
    ![[Screenshot 2024-08-18 at 6.36.23 PM.png]]
Create a run/debug configuration from a template

From the main menu, select Run > Edit Configurations. Alternatively, click dropdown(⌄) in the Run widget and select Edit Configurations from the drop-down
click on + icon
    go to python
	give a name (customername)
	 **Script path/Module name**: Click the list to select `module_name` type as the target to run. Then enter the module name as `src.unbxd.feed.feed`
		 click on dropdown on script and choose module give module name as 
		 src.unbxd.feed.feed
		 ![[Screenshot 2024-08-18 at 6.39.35 PM 1.png]]
![[Screenshot 2024-08-18 at 6.42.29 PM.png]]
		  

**Parameters**: Add the necessary command-line arguments as follows:

Before executing the script, make sure to prepare the `config` file and `custom_transformer` file. Create a `tmp` folder at the root of the `feed-conversion` repository, and then place the config, transformer, and customer feed files in that folder.![[Screenshot 2024-08-18 at 11.45.12 AM.png]]

```
 --local_config_file_path=tmp/config.yml --local_custom_file_path=tmp/custom_transformer.py
```


![[Screenshot 2024-08-18 at 11.34.45 AM.png]]

if we are not using custom transformer 
```
 --local_config_file_path=tmp/config.yml
```
make script parameter as this
but aslo as this has to be unique for custome name it as config_customername.yml and it has to be on tmp folder

- **Working Directory**: Navigate to the feed-conversion directory and set it as working directory.
- same feed-ocnversion insert the same(path of feed-conversion in laptop)
  /Users/unbxd/Desktop/work/feed-conversion
  
  ![[Screenshot 2024-08-18 at 11.40.47 AM.png]]
click on apply and ok


go to file 
```
/Users/unbxd/Desktop/work/feed-conversion/cookiecutter_template/custom_transformer/{{cookiecutter.customer_name.replace('-', '_')}}/config/{{cookiecutter.customer_name.replace('-', '_')}}_{{cookiecutter.env}}.yml
```

and copy the contents of the same and paste it in config_customername file in tmp that is created


parts to edit in the freshly pasted content in config_customername file

keys(site : ) config
	sitekey
	 api key
	 secret key
![[Screenshot 2024-08-18 at 6.56.58 PM.png]]
file path (whicch we need to index it will be in primary parser)
/Users/unbxd/UNBXD_id_ID.csv

![[Screenshot 2024-08-18 at 6.57.26 PM.png]]

region
![[Screenshot 2024-08-18 at 6.58.30 PM.png]]

identify delimiter by seeing files
uniqueId :  (feild that act as unique id in feed file)
participation_size(0 to 2lac)
![[Screenshot 2024-08-18 at 7.07.36 PM.png]]

map feature feild with corresponding feildname in feed file and has to be included only if name is diffrent in feature feild in configuration if the name is same no need to map

schema




default transformer
change config for default transformer



comment this part if you are using only default transformer



```
- package_path: Dummy_Path  
- module_name: {{cookiecutter.site_key.replace('-', '_')}}  
- custom_transformer:  
  - {{cookiecutter.site_key.replace('-', '_')}}:  
      config: 'config'
```

once all this process is completed
site to check status
	https://feed.unbxd.io/api/prod-afw817831608714016/catalog/status
     https://feed.unbxd.io/api/{sitekey}/catalog/status
 


how to schedule job using solsjobsv3

open v3 repo

gcm && gfu && gmu && gpom
git checkout -b branchname
create a virtual env
cd src/feed-conversion
run command in terminal
```
cookiecutter https://github.com/unbxd/feed-conversion.git --directory cookiecutter_template/custom_transformer
```

click on y
customer name : customer name
site key : site key
api key : api key
secret key : secret key
region : region
sftp_username : sftp username
sftp_password  : password
filepath : file path (open filezilla and use credentaials to find file path and copy an dpaste the same here)
env : (stage , dev , prod)
example : files/dev/filename(the path of the file in filezilla)
file url : (if there is no file we are getting from url then make it as NA)
after this a folder is created with customer name

go to 
customer name
	argo
		cronworkflow
			edit schedule as customer has asked us

go to
customer name
	argo
		workflow template
			in templates
				name
					dag
						tasks
							name : sftp_file_fetch
							template :
							 	
for this
						tasks
							name :
							template :
	keep only what is required  sometimes url is not required
	in tasks
		arguments
			artifacts 
	  keep only necessary and remove other that is not required
	  ||y in tasks
			dependencies
and also remove associated steps along with it like
url file fetch

	 
	
	
	
	![[Screenshot 2024-08-18 at 11.42.46 PM.png]]
![[Screenshot 2024-08-18 at 11.46.59 PM.png]]
	as you can see n above example there is no url_file_fetch step ther si sonly sftp_file_fetch


and also remove files in procesing step that is not required
go to
name : processing step
	inputs
		artifacts
		 -name : url_feed_file
		 ![[Screenshot 2024-08-18 at 11.49.47 PM.png]]path : /tmp/feed_file.xml
	as you can see in below example there is no 
	

   compare demo-feed with new one and undertsand the diffrence better
   
   go to file
   src
	   feed-conversion
		   customername
			      config
					   customername_env.yml
   

copy the config file that you have created in feed-conversion and paste it in here

change file path make it same as what is there in processing step of workflow template
not the one from fed-conversion(customername_config.yml)

file in workflow template
![[Screenshot 2024-08-18 at 11.56.37 PM.png]]
file in config

![[Screenshot 2024-08-19 at 12.00.31 AM.png]]

after this we need to raise pr for solsjobsv3

do 
git add .
git commit -m "{customername} : initialisation"
git push origin {branchname}

after raising pr
if we get created new customername_env_full workflow template then it is successful
lint success


after that step 
go to website
https://solutions-argo-workflow.unbxd.io/login?redirect=https://solutions-argo-workflow.unbxd.io/workflow-templates/argo/
and resume the workflow that just got created by raising the pr it has test at end
go to catalog staus url and check if it is indexed
https://{feed-domain}/api/{sitekey}/catalog/status

go to the search api for the same and check if it is coming properly
https://search.unbxd.io/{apikey}/{sitekey}/search?q=*

if all steps are green in argo then the indexing is done successfully



doubts
what if  a field has to be made autosuggest as true






for custom transformer
go to file
``` /Users/unbxd/Desktop/work/feed-conversion/cookiecutter_template/custom_transformer/{{cookiecutter.customer_name.replace('-', '_')}}/src/{{cookiecutter.site_key.replace('-', '_')}}/{{cookiecutter.site_key.replace('-', '_')}}.py
```

copy the content of file 
create a new file in tmp folder named {customername}_transformer.py
_and paste the content in same

and write transformation on each product attribute and make new vlaue as value of product[attribute]
![[Screenshot 2024-08-27 at 4.06.47 PM.png]]

now go to edit configuration


please be sure you are in correct customer feed before you are doing changes




https://github.com/unbxd/solution-jobs-v2/blob/0e9135364c0b31f4aba42180afb98ba2b5dbbefe/src/kits/argo/cron_workflow/ss-unbxd-gcp-kits-com-stage16621684171061_full.yml#L24C10-L25C33



[src/kits/argo/cron_workflow/ss-unbxd-gcp-kits-com-stage16621684171061_full.yml](https://github.com/unbxd/solution-jobs-v2/pull/1562/files#diff-15a1ccbc20867e915ed6ef9a13420e43e15d958d017757b01173fb44e2b47854 "src/kits/argo/cron_workflow/ss-unbxd-gcp-kits-com-stage16621684171061_full.yml")
[src/kits/argo/cron_workflow/ss-unbxd-gcp-opticontacts-stage16621696961246_full.yml](https://github.com/unbxd/solution-jobs-v2/pull/1562/files#diff-5d664e05aacfbc29b0d1e12a827339707de369e67eea2a9a07c5dc3810b3ba9e "src/kits/argo/cron_workflow/ss-unbxd-gcp-opticontacts-stage16621696961246_full.yml")

https://search.unbxd.io/864d1797bfd230ef72d5cfdde5868364/ss-unbxd-gcp-kits-com-stage16621684171061/search?q=*&filter=accept_high_rx:1 OR smart_glasses:1 OR accept_progressive:1 OR accept_light_transition:1&promotion=false&fields=accept*, smart*, features*


https://search.unbxd.io/864d1797bfd230ef72d5cfdde5868364/ss-unbxd-gcp-kits-com-stage16621684171061/search?q=*&filter=accept_high_rx:1 OR smart_glasses:1 OR accept_progressive:1 OR accept_light_transition:1&promotion=false&fields=accept*, smart*, features*



sftp step and url step
- name: feed_sftp_path  
  value: /files/English/Dev/UNBXD_en_US.csv(change file name)
url path

in parameter of processing step we need to cchange this
- name: github_config_relative_path  
  value: config/mapclub_en_prod.yml

contaiener always put new version
container:  
  name: mapclub-en-prod-full  
  image: 012629307706.dkr.ecr.us-east-1.amazonaws.com/feed-conversion:v1.9.4

there 