
be in src directory
branchname = {customernameregionenv}
gcm && gfu && gmu && gpom
git checkout {branchname}
grm



git add filename
git commit --amend --no-edit     
git push  -f origin {branchname}


for new integration
be in src directory 

gcm && gfu && gmu && gpom
git checkout -b {branchname}
mkdir {branchname}
cd {branchname}
touch config.js  
touch metadata.json
git add filename
git commit -m "[WIP] added analytics config for {customernameenv}"     
git push  -f origin {branchname}

to clone pr authored by others use the below command
git fetch upstream pull/{{pr_number}}/head:pr_{{pr_number}}_{{client_dir_name}}

github url : https://github.com/unbxd/analytics-customerjs/pulls/sangamesh-somashetti-unbxd
can anyone please review and merge this pr
{prlink}

