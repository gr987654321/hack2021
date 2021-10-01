# How to Collaborate:

1. Fork the repository to your own GitHub account.

2. Clone the repository to your local machine
```
$ git clone "https://www.github.com/{Username}/hack2021.git"
```
where username is your GitHub account username.

3. Create a branch where you can do your local work.
Never work on **master**/**main** branch as we do not allow master commits except by admins.
```
$ git checkout -b branchname
```

4. Do your work and stage your changes.
```
$ git add <filename>
```

5. Commit you changes with a commit message containing your name, file(s) worked upon, changes added.
```
$ git commit -m "Files| Changes"
```

6. Push changes to your forked repository
```
$ git push -u origin branchname
```

