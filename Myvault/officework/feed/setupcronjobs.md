create one file in croon workflow
create one file in  workflow template
replace env wherever necessary(dev , prod , stage in both file)(keyword)
if there i workflow in previous cron
  delete the same
 in new cron
	 resume the same
	template is always created with test
	once you raise the pr it will happen



before submitting please keep in mind
add docker file in pr
add sitekeys to sftp_config.json
change the pyconversion version in dockerfile(in 14 line) to 0.2.34
updated line
```
RUN pip install https://${GITHUB_TOKEN}@github.com/unbxd/pyconversion/archive/refs/tags/0.2.34.tar.gz --no-cache-dir --compile
```

and always before merging ensure that jobs are running properly (submit in argo-solutions) and see through that it is complete
checking feed indexing status is completed

