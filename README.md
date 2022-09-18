# Dockerized Task

## *Docker container for python script to automate task*

### *To build a docker images*
```
docker build --tag execute_task:v1 .
```

### *To execute a task*
```
docker run execute_task:v1 task1.py
```

### *To execute a task with volume*
```
docker run -v D:\docker-tasks-volume:/tmp execute_task:v1 task2.py
```

### Volume in parameter are in the following way:
* host-volume:container-volume

