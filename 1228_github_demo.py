#!/bin/python3


' to create and connect to website using git bash cli '  #ex1228
-------------------------------------------
1. Create a repository in GitHub. You can do this by clicking the New button on your GitHub profile page, and then filling out the details for your project. Make sure you copy the URL of your repository, which should look like https://github.com/yourusername/your-repo-name.git.

2. Open Git Bash on your computer. You can download Git from here if you don’t have it already.

3. Navigate to the directory where your project files are located. You can use the cd command to change directories. For example, cd C:\Users\yourname\Documents\your-project.

4. Initialize a Git repository in your project directory. You can do this by running the command git init. This will create a hidden .git folder that stores the history of your project.

5. Add a remote location for your GitHub repository. You can do this by running the command git remote add origin <repository URL>, where <repository URL> is the URL you copied in step 1. This will tell Git where to push your changes to.

6. Add your project files to the staging area. You can do this by running the command git add ., which will add all the files in your current directory and its subdirectories. Alternatively, you can specify individual files or patterns to add, such as git add *.txt or git add README.md.

7. Commit your changes to the local repository. You can do this by running the command git commit -m "your message", where "your message" is a brief description of what you have changed. This will create a snapshot of your project at the current state.

8. Push your changes to the remote repository on GitHub. You can do this by running the command git push -u origin main, where main is the name of your default branch. This will upload your project files and history to GitHub, and set up a tracking relationship between your local and remote branches.

