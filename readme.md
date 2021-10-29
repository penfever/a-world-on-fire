# Big Data: Group Project

Here's some important information related to our group project. If you have questions or comments, let me know on Slack.

## Dev Environment

The current plan is for us to work locally on identical Docker images (we can discuss this during the meeting) using branches. Then we can submit PRs to the repo when we are ready to share our changes with the group.

### Docker Image

For now, we can use the all-spark-notebook. I may have to switch us over to a custom image at some point, however, in order to enable PyTorch and Dask.

https://github.com/jupyter/docker-stacks/tree/master/all-spark-notebook

## Repo

Here you will find some simple instructions related to repo use.

### Basics

* pull the repo to some clean directory on your local drive before starting to edit the project
* all data files should be hosted elsewhere in the cloud and downloaded via ipynb cells either using APIs, wget, gdown, etc. Please do not create PRs which include data
* please use gitignore to avoid adding unwanted files to your PRs (hidden files, local requirements, etc)

### Structure

Please do not create PRs that change the repo structure without checking with me first.

bd_proj_main.ipynb will be our working code-base. Please create PRs for all your changes to main. Please do not copy or rename bd_proj_main.ipynb.

docs is for any documentation related to the project (such as proposal or presentation docs)

### Pull

Please remember to pull the most recent version of all files before editing any files in this repo.

### Branching and PRs

We will be using a standard [branch and merge](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow for all changes to the repo. All your changes should be made in a new branch and then submitted as a PR when you're ready to share.