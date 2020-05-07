# Docker Practice

## Docker Run Options

``--detach , -d`` Run container in background and print container ID

``--interactive , -i``  Keep STDIN open even if not attached

``-it``  Attach container outout to STDOUT and STDINPUT



## Mount Volume

Bind mounts have been around since the early days of Docker. Bind mounts have limited functionality compared to [volumes](https://docs.docker.com/storage/volumes/). When you use a bind mount, a file or directory on the *host machine* is mounted into a container. The file or directory is referenced by its full or relative path on the host machine. By contrast, when you use a volume, a new directory is created within Docker’s storage directory on the host machine, and Docker manages that directory’s contents.

![bind mounts on the Docker host](https://docs.docker.com/storage/images/types-of-mounts-bind.png)

### Differences between `-v` and `--mount` behavior[🔗](https://docs.docker.com/storage/bind-mounts/#differences-between--v-and---mount-behavior)

Because the `-v` and `--volume` flags have been a part of Docker for a long time, their behavior cannot be changed. This means that **there is one behavior that is different between `-v` and `--mount`.**

If you use `-v` or `--volume` to bind-mount a file or directory that does not yet exist on the Docker host, `-v` creates the endpoint for you. **It is always created as a directory.**

If you use `--mount` to bind-mount a file or directory that does not yet exist on the Docker host, Docker does **not** automatically create it for you, but generates an error.

The `--mount` and `-v` examples below produce the same result. You can’t run them both unless you remove the `devtest` container after running the first one.

``--mount``

```sh
$ docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/app \
  nginx:latest
```

``-v``

```sh
$ docker run -d \
  -it \
  --name devtest \
  -v "$(pwd)"/target:/app \
  nginx:latest
```

### What about director permission?

It is depends on how you mount directory to your container, you can mount readonly or writable. 

``readonly``

```sh
$ docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/app,readonly \
  nginx:latest
```

`ro`

```sh
$ docker run -d \
  -it \
  --name devtest \
  -v "$(pwd)"/target:/app:ro \
  nginx:latest
```



### How to mount to Selinux?

https://docs.docker.com/storage/bind-mounts/#configure-the-selinux-label

```sh
$ docker run -d \
  -it \
  --name devtest \
  -v "$(pwd)"/target:/app:z \
  nginx:latest
```



## Attach to Container[🔗](https://docs.docker.com/engine/reference/commandline/attach/)

Attach local standard input, output, and error streams to a running container

```sh
docker attach [OPTIONS] CONTAINER
```

```sh
$ docker run --name test -d -it debian
275c44472aebd77c926d4527885bb09f2f6db21d878c75f0a1c212c03d3bcfab

$ docker attach test

root@f38c87f2a42d:/# exit 13
exit

$ echo $?
13

$ docker ps -a | grep test
275c44472aeb        debian:7            "/bin/bash"         26 secon
```

## Docker Exec

Run a command in a running container

```sh
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```



By default `docker exec` command runs in the same working directory set when container was created.

```sh
$ docker exec -it ubuntu_bash pwd
/
```

You can select working directory for the command to execute into

```sh
$ docker exec -it -w /root ubuntu_bash pwd
/root
```



## Docker Logs[🔗](https://docs.docker.com/engine/reference/commandline/attach/)

Fetch the logs of a container

```sh
docker logs [OPTIONS] CONTAINER
```



**Options**

1. --follow -f
2. --until

```sh
$ docker run --name test -d busybox sh -c "while true; do $(echo date); sleep 1; done"
$ date
Tue 14 Nov 2017 16:40:00 CET
$ docker logs test -f --until=2s
Tue 14 Nov 2017 16:40:00 CET
Tue 14 Nov 2017 16:40:01 CET
Tue 14 Nov 2017 16:40:02 CET
```



## Docker Histor[🔗]

Show the history of an image. You can use it for analyzing an image. How is it assembled etc.

**Case:** A man give me an image. I will run it. How can I trust him?

```sh
docker history [OPTIONS] IMAGE
```



```sh
docker history python:3.7-alpine
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
8922d588eec6        5 months ago        /bin/sh -c #(nop)  CMD ["python3"]              0B                  
<missing>           5 months ago        /bin/sh -c set -ex;   wget -O get-pip.py "$P…   6.25MB              
<missing>           5 months ago        /bin/sh -c #(nop)  ENV PYTHON_GET_PIP_SHA256…   0B                  
<missing>           5 months ago        /bin/sh -c #(nop)  ENV PYTHON_GET_PIP_URL=ht…   0B                  
<missing>           5 months ago        /bin/sh -c #(nop)  ENV PYTHON_PIP_VERSION=19…   0B                  
<missing>           5 months ago        /bin/sh -c cd /usr/local/bin  && ln -s idle3…   32B                 
<missing>           5 months ago        /bin/sh -c set -ex  && apk add --no-cache --…   86.1MB              
<missing>           6 months ago        /bin/sh -c #(nop)  ENV PYTHON_VERSION=3.7.5     0B                  
<missing>           6 months ago        /bin/sh -c #(nop)  ENV GPG_KEY=0D96DF4D4110E…   0B                  
<missing>           6 months ago        /bin/sh -c apk add --no-cache ca-certificates   551kB               
<missing>           6 months ago        /bin/sh -c #(nop)  ENV LANG=C.UTF-8             0B                  
<missing>           6 months ago        /bin/sh -c #(nop)  ENV PATH=/usr/local/bin:/…   0B                  
<missing>           6 months ago        /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B                  
<missing>           6 months ago        /bin/sh -c #(nop) ADD file:fe1f09249227e2da2…   
```





## Expose and Import File ( To | From )  Container

Find out a container’s name or ID using the `docker ps` command:

```
$ docker ps
CONTAINER ID  IMAGE    COMMAND  CREATED      STATUS      PORTS  NAMES
72ca2488b353  my_image          X hours ago  Up X hours         my_container
```

Copy a file from host to container:

```
$ docker cp foo.txt 72ca2488b353:/foo.txt
```

Copy a file from Docker container to host:

```
$ docker cp 72ca2488b353:/foo.txt foo.txt
```



### Commonly Used Docker Command List

- docker images | grep

- docker ps / docker ps -a

- docker exec

- docker run / stop 

- docker log

- docker save [image] > [tar_file]

- docker load [tar_file]

- docker event [container] # real time event

- docker kill



https://docs.docker.com/storage/bind-mounts/

https://docs.docker.com/engine/reference/commandline/attach/

https://docs.docker.com/engine/reference/commandline/logs/

https://www.shellhacks.com/docker-cp-command-copy-file-to-from-container/