copy a file according to enviornment and paste in cronworkflow for cron_workflow folder and change name according to sitekey and env

changes need to be done in workflow template (3 places)
metadata
	labels
		name 
spec 
	workflowspec
		 entrypoint 
spec 
	workflowspec
			workflowtemplateref
					name 
	

![[Screenshot 2024-09-15 at 6.37.23 PM.png]]

||y for workflow template 

diff for same env and same customer
generally 
search for sitekeyvalue of old file and replace it with new sitekey for which you are creating the file with  and replacce api key and secret key in command
along with template names


![[Screenshot 2024-09-15 at 6.45.20 PM.png]]![[Screenshot 2024-09-15 at 6.45.20 PM 1.png]]


