# xs_scripts
python scripts to launch on xslocobot

Start of the ME_Project

How to think of git
 
||  Local Directory                                  |   Stage                                             |  Local Repo       |  Remote Repo
||  (File you reside in   --git add <file name>-->   |   --git commit -m "enter message"-->                |  (on your pc)     |  On GitHub.com
||   currently)                                      |   <-- git checkout <file name> --                   |  -- git push -->  |  All our branches live here
||                                                   |   <-- git checkout --track origin/<Branch name> --  |  <-- git pull --  |  (rent free) 

To get started clone the git repo following this guide
https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
 
you may need to authenticate using this guide 
https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git



**STARTING WORK?** 

Generally it is BEST PRACTICE to ensure your local repo is updated 
at the start of every working session
1. git status
Check to see if there are any differences between your local repo 
and the master ( this is one way between your repo and the master )
If there are unsaved changes do the following 
        a. cry
        b. contact me
        c. git push 
        
2. git pull 
This will update your local repo to pull everything from the remote repo
Doing this will ensure you're working on the latest changes
You're set to start working! 



**MAKING BRANCHES**

Try to make branches from our remote repo at GitHub.com
then pull them to your local by doing the following
1. git pull 
This will get all the branches from main 

2. git checkout --track origin/your-branch-name
Then you will have your branch on your pc 

git status will tell you what branch you're on

**SWITCHING BRANCHES**

1. git checkout <branchname>



**PUSHING YOUR CODE** 

in your terminal cd to the directory of your local repo
1. git status
check for changes marked in red text

2. git add <file name> 
Ex. git add My_script.py 

2. git status
check to see if you've successfullyl added your code
marked in green text

3. git commit -m "Write a relevant message here" 
Ex. git commit -m "Renee updated My_script.py added 1 function" 

4. (optional) git status 
check that your commit went through 
you should see no highlighted text 

5. git push
You're done! 
code is now on remote repo! 
