```
Github pr
Go to unbxd/analytic-customer-js
Fork
Create a directory or move into directory where you want to clone
Clone(git clone forkedrepourl)
Ex :git clone https://github.com/sangamesh-somashetti-unbxd/analytics-customerjs.git

Move to forked directory
Ex : cd analytics-customerjs

git remote -v
You will see 2 links origin (fetch and push)
	
Add upstream of unbxd/analytics-customer-js
git remote add upstream https://github.com/unbxd/recommendations-proxy.git

Git remote -v (you will see four links 
2 upstream and 2 origin for fetch and push


git fetch upstream
To get all the changes in unbxd repo


git merge upstream/main
(merge change from main repo to forked repo 

git push origin main
(push all changes in unbxd repo to main repo)

Create a new branch with name same as sitename
And move to that branch using command
git checkout -b AldawaeyaEnStage


Check for change in file using git status
Git add all required files(dev-setup config.js
And newly created files config.js and metadata.json)

Git status
(Red to green changes)

Commit changes
Git  commit -m “commit message”

Push changes
Git push origin “branch name”

Go to 
https://github.com/sangamesh-somashetti-unbxd/analytics-customerjs/pull/new/AldawaeyaEnStage. Url and you will see a pop up for creating a new pull request do the same click on It 

And 

git clone https://github.com/tushargupta96/solution-jobs.git<forked repository link>
    cd solution-jobs
    git remote add upstream https://github.com/unbxd/solution-jobs.git
    git fetch upstream
    git merge upstream/main
    git push origin main


Others
Git status
Git stash
//without unbxd main changed
Git add config.js
Git commit —amend  —no-edit
Git push -f origin <branchname>


With 	
Git checkout main
Git branch 
Git fetch upstream
  git merge upstream/main
 git push origin main


Git checkout <branchname>
Git rebase -main
Git push -f origin <branchname>
Git stash pop



Git push origin <branchname>


serengeti_com-u1449554744834
whateverworks_com-u1449555336211
youngexplorers_com-u1449555622595
backinthesaddle_com-u1449556121094
inthcompanyofdogs_com-u1449552526904
magellans_com-u1449552886357



vertical widget - https://github.com/unbxd/recommendations-proxy/blob/master/views/	
horizontal widget - https://github.com/unbxd/recommendations-proxy/blob/master/views/hz-northstyle_com-u1449553627435.html




If we are woking on site that already has previous configuration
Check out to main branch in the repo
Enter command
it fetch upstream pull/{{pr_number}}/head:pr_{{pr_number}}_{{client_dir_name}}
Replace {pr number} with number  in title
Client dir name : site name (not fixed)
New branch will be created 
Checkout to the same branh
Make changes and push for commit
Git push origin main


git commit --amend --no-edit


Correct amend command
git commit --amend --no-edit\








git : saving history of codebase
git : at what time where a person made change to part of the project and when
github(interface) : a website that hosts repositories
repositories : the file that maintain all the changes we made in the current directory

Git commands

git init : initialise a git repository to record change in current project(folder)
git status : shows us all the tracked and untracked changes
git add : add the untracked file to the staging area (all the tracked files )
git commit -m "msg" : saves the version of the project make all changes permanent until you reset the same 
git restore --staged filename.txt : remove the file from staging area and move them to working area
git log : get all the commits(change) made most recent versions will be at first and first commit will be at last
git reset codeofcommit : all the changes after that commits are removed (v1) after this whatever changes were there using git commit are in working tree(unstaged area) we can get the same using git status
git stash : move all the current changes to the working tree and but before that we need to bring them to staging area and then run command git stash and once we need that changes back we can do git stash pop
git stash clear : we do not want that changes that are in unstaged area completly remove them  all the changes. that we made after commit are gone
git remote(to identify we are working with url) add(we are adding url) origin(urlname) url(url of repo webpage) : it connects our local repository to remote repo 
git push(we are pushing changes to remote from local) origin(urlname) main(name of the branch)

Analogy

untracked file : guests who are ready and are not on stage
tracked file : guest that are on stage
commit : taking photo and saving in album

Doubts

if we do git stash clear are all the changes after commit gone



Token-2

```