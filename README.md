# Git Skillz Session Tutorial Repo

## What is git and why do I care?
  - Collaboration
  - Versioning

## How does git help?
  - You get your own copy of all files in a special folder on your computer
    called a git "repository" or "repo" for short
  - Everyone else also gets a the exact same copy of those files in their own repo
  - Each person can work independently on all files in their respective repo
  - Your git repo tracks all changes you make to any files
  - You save your changes with a git "commit" and you can back them up to the
    cloud - or "remote" - with a git "push"
  - Git "fetch" allows you to review all changes made by others before
    accepting - or "merging" - them into your repository
  - Git helps you resolve any collisions where 2 people edited the same file on
    each of their respective computers. It does deep comparisons between versions
    using git "diff"
    the two files and walks you through deciding which one you want
  - Git also allows you to have multiple versions of your entire repo - or "branches" -
    that you can switch back and forth between
  - And lastly, git, if used correctly, will practically never let you lose
    data; you can always recover "lost" changes.

## That's crazy. How does git do all of that!
  - Well we've already started to learn about the model and terminology git uses above!
  - But as a reminder, here's a recap of some terminology:
    - Things:
        - repository - code base stored in a special folder
        - commit     - the set of changes you made to one or more files (analagous to the changes make to a word doc in between saves)
        - branch     - an easy-to-remember label given to a particular commit
        - remote     - a url to someone else's copy of the repository
    - Actions:
        - add        - instruct git to start tracking a new file
        - checkout   - change to a different snapshot (commit/branch) of the repo
        - push       - pushing your changes to a particular remote
        - fetch      - download someone else's changes from a particular remote (but don't accept them into your repo yet)
        - merge      - accept changes into your repo
  - There are more terms that you'll come to know and love, like "rebase" and
    "reset" as you get into more and more advanced git usage


> As an aside, there are all sorts of mental models to use when learning git.
  This tutorial is just one of them. If this one doesn't jive with you, please
  just let me know and I'd be happy to help with any number of other mental models


## A walk through a git example

  - Tell git who you are!

  ```
    git config --global user.name "First Last"
    git config --global user.email "first.last@skyspecs.com"
  ```

  - Get me a repo

  `git clone https://github.com/jbendes/git-skillz.git`


  - Modify some files

  `cd git-skillz; echo "test" > example-file.txt;`


  - See the status of any changes you've made to the repo

  `git status`


  - "Stage" your changes

  `git add example-file.txt`


  - See the status now that you've "staged" your changes

  `git status`


  - Save your changes

  `git commit --all --message "I just made my first git file!"`


  - Push your changes to a remote

  `git push origin master`


  - See which human-readable version of the repo you're in

  `git branch`


  - Make a new branch

  `git branch learn-about-branches`


  - See all branches in your repo

  `git branch -a`


  - Switch to a different commit/branch

  `git checkout learn-about-branches`


  - See all branches in your repo

  `git branch -a`


  - Fetch anybody else's changes

  `git fetch origin`


  - Let's step into the 4th dimension!

  `gitk --all`



### Normal git workflow to preserve a clean tree

        git checkout master
        git branch feature1
        git checkout feature1
        echo "did some work" > example-file2.txt
        git add ./example-file2.txt
        git commit --message "Did work"
        echo "did some more work" > example-file3.txt
        git add ./example-file3.txt
        git commit --message "Did more work"
        git checkout master
        git merge --no-ff feature1 --message "Solved world hunger"
        git branch --delete feature1
        gitk --all
        git push origin master




### Advanced git commands

  - See a unique id - or "hash" - for a branch/commmit

  `git rev-parse learn-about-branches`


  - Move the non-common history of all of my changes on "top" of another branch/commit

  `git rebase master`


  - Move a complex section of history on "top" of another branch/commit

  `git rebase --rebase-merges --onto master <COMMIT BEFORE START> <LAST COMMIT>`


  - Grab a commit and put it on top of your current location in the tree

  `git cherry-pick <COMMIT>`


  - Grab a range of commits and put them on top of your current location in the tree

  `git cherry-pick <COMMIT BEFORE START>..<LAST COMMIT>`


  - Deal with merge conflicts during a rebase

  `git mergetool`


  - Move from your current commit in the tree to a different commit in the tree

  `git reset --hard <COMMIT>`


  - Move from current commit to a different commit and stage all the difference between those commits

  `git reset --soft <COMMIT>`


  - OH NO! I LOST A FILE! Did you commit? If not, your files are lost. If yes, then reflog to the rescue!

  `git reflog`


  - Revert the changes you made in a commit as a new commit

  `git revert <COMMIT>`


  - Time to get tricky

  `git version-number`
