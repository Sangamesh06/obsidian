git checkout master && gfu && git merge upstream/master && git push origin master
git checkout {branchname}
git rebase master

git add filename 
git commit --amend --no-edit     
git push  -f origin {branchname}

to clone pr authored by others use the below command
git fetch upstream pull/{{pr_number}}/head:pr_{{pr_number}}_{{client_dir_name}}


github url : https://github.com/unbxd/customer-js/pulls/sangamesh-somashetti-unbxd
can anyone please review and merge this pr
{prlink}

commit messages
fix({customername})  : what changes did you make

chore({customername}) : updating bundle files

