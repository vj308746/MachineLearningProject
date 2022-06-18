# MachineLearningProject
This is first machine learning project

creating conda environment
```
conda create -p venv python==3.7 -y

```
pip install -r requirements.txt

to add file in git

```
git add filename
```
to ignore the file/folder from git we can write file name / folder in.gitignore file

to check the git status

```
git status

```

to check all version maintained by git

```
git log
```

to crete version/commit all changes by git

```
git commit -m "message"

```

to sent version or changes to gihub

```
git push origin main
```

to check remote url
```
git remote -v
```
to setup heroku we require below things

heroku emial id - vj308746@gmail.comheroku 
API KEY  - 1448730d-7970-46c3-a05f-027397c688de
application name -  ml-project-regression

BUILD docker image

```
docker build -t <image_name>:<tagname>
```
>note - image name for docker must be in lowercase

to list docker image
```
docker image
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 (imageid)
```

to check the running container in docker
```
docker ps
```
To stop docker container
```
docker stop (container id)
```
