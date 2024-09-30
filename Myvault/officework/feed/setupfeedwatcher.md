https://unbxdwiki.atlassian.net/wiki/spaces/~5d2ef17352a8370c567f276a/pages/2315649072/Argo+Feed+Watcher+Setup

```
"camper": {
        "cron_workflows": {
            "camper-ro-prod-full": {
                "sitekey": "ss-unbxd-auk-camper-ro-prod38961724976275",
                "path": "/romanian/prod/timestamp.json"
            },
            "camper-ro-stage-full": {
                "sitekey": "ss-unbxd-auk-camper-ro-stage38961724976141",
                "path": "/romanian/stage/timestamp.json"
            }
        }
    }
```
/files/romanian/stage(upper path)
sftp details

```
"shopperstop": {
    "cron_workflows": {
        "shopperstop-dev": {
            "sitekey": "ss-unbxd-aapac-shoppersstop-dev50901709028198",
            "path": "/dev/full/timestamp.json"
        }
    }
}

```



for prod site

```
"shopperstop": {
    "cron_workflows": {
        "shopperstop-prod": {
            "sitekey": "ss-unbxd-aapac-shoppersstop-prod50901711607748",
            "path": "/prod/full/timestamp.json"
        }
    }
}
```

hello
```
camper
$!c@m#$&=512r

```

sftp://camper@sftp.unbxdapi.com/files/romanian/stage/timestamp.json
sftp://shopperstop@sftp.unbxdapi.com/files/dev/full/timestamp.json
sftp://shopperstop@sftp.unbxdapi.com/files/prod/full/timestamp.json


workflow
1) login to sftp
```
ssh -o PubkeyAcceptedKeyTypes=ssh-rsa dev@sftp.unbxdapi.com
```

2) get customers foldername 
```
ls -al /uploads
```

 use the customer present in here to construct json object

3) go to directory where paths.json is present
```
cd /home/dev/argosentinel/
```

4) Update the `paths.json` file in the folder as per step 5.
```
 vim paths.json
```
if you get a swap file choose e(edit anyway)


CUSTOMERFOLDERNAME` is the folder name from step 2

`ARGOWORKFLOWNAME` is the name of the argo workflow(go to url https://solutions-argo-workflow.unbxd.io/cron-workflows/argo/ to find the same)

`SITEKEY` is the sitekey for which the feedwatcher you want to setup

`TIMESTAMP_FILE_PATH` is the relative filepath for the timestamp file. It is relative to the `/files` folder of the customer
 open filezilla through sftp credentials 
	go to directory where timestamp.json file is present
	 copy url of timestamp.json file 	
     remove part until you remove files from url
	     before : sftp://shopperstop@sftp.unbxdapi.com/files/dev/full/timestamp.json
	     after : /dev/full/timestamp.json
	     sftp://shopperstop@sftp.unbxdapi.com/files/prod/full/timestamp.json
	     
5) After updating the `paths.json` file, run the following command to restart the sentinel service:
```
    sudo service argo-file-watcher restart
```
       password is 
```
       dev@unbxd123
```

In order for us to check if what we have done is correct 
open filezilla
use sftp credentials of customer to see customer files
go to directory where  timestamp.json file is present
download the same to local file 
upload the same file to sftp remote. where sftp file was present
choose override in popup
go to status api for current site
check if there is new entry with indexing status(it takes time)
if there is one then the setup is successful



another method to check if it is successful
login to sftp through command line
go to directory
```
cd /home/dev/argosentinel/.backup/argofeedwatcher
```

do 
```
ls
```

do
```
tail watcher_new.log
```

if you see a new entry at lost with new argo workflow that is same as the one that you want to be triggered 
then it is successful



```
https://feed-apac.unbxd.io/api/ss-unbxd-aapac-dev-mapclub-en56931721299790/catalog/status
```