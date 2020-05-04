# Overview of Docker Compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. 

# Installation Docker



# Creating Docker Image

## Example project from GitHub:

```
git clone https://github.com/dockersamples/node-bulletin-board
cd node-bulletin-board/bulletin-board-app
```



## Define a container with Dockerfile[🔗](https://docs.docker.com/get-started/part2/#define-a-container-with-dockerfile)

Take a look at the file called `Dockerfile` in the bulletin board application. Dockerfiles describe how to assemble a private filesystem for a container, and can also contain some metadata describing how to run a container based on this image. The bulletin board app Dockerfile looks like this.

Dockerfile; always start with a `FROM` command, follow it with the steps to build up your private filesystem, and conclude with any metadata specifications. There are many more Dockerfile directives than just the few you see above. For a complete list, see the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/). 

```dockerfile
# Use the official image as a parent image.
# FROM <BASEIMAGE>
# https://hub.docker.com/_/scratch  Empty image
FROM node:current-slim

# Set the working directory.
# 
WORKDIR /usr/src/app

# Copy the file from your host to your current location.
COPY package.json .

# Run the command inside your image filesystem.
RUN npm install

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080

# Run the specified command within the container.
CMD [ "npm", "start" ]

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .
```





## Instruction Explaining

### WORKDIR

```
WORKDIR /path/to/workdir
```

The `WORKDIR` instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` instructions that follow it in the `Dockerfile`. If the `WORKDIR` doesn’t exist, it will be created even if it’s not used in any subsequent `Dockerfile` instruction.

### FROM

```
FROM [--platform=<platform>] <image> [AS <name>]
```

The `FROM` instruction initializes a new build stage and sets the [*Base Image*](https://docs.docker.com/engine/glossary/#base-image) for subsequent instructions. As such, a valid `Dockerfile` must start with a `FROM` instruction. The image can be any valid image – it is especially easy to start by **pulling an image** from the [*Public*](https://docs.docker.com/engine/tutorials/dockerrepos/)

### Copy

COPY has two forms:

```
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

The `COPY` instruction copies new files or directories from `` and adds them to the filesystem of the container at the path ``.

Multiple `` resources may be specified but the paths of files and directories will be interpreted as relative to the source of the context of the build.

### RUN

RUN has 2 forms:

- `RUN ` (*shell* form, the command is run in a shell, which by default is `/bin/sh -c` on Linux or `cmd /S /C` on Windows)
- `RUN ["executable", "param1", "param2"]` (*exec* form)

The `RUN` instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the `Dockerfile`.

### CMD

The `CMD` instruction has three forms:

- `CMD ["executable","param1","param2"]` (*exec* form, this is the preferred form)
- `CMD ["param1","param2"]` (as *default parameters to ENTRYPOINT*)
- `CMD command param1 param2` (*shell* form)

There can only be one `CMD` instruction in a `Dockerfile`. If you list more than one `CMD` then only the last `CMD` will take effect.

**The main purpose of a `CMD` is to provide defaults for an executing container.** These defaults can include an executable, or they can omit the executable, in which case you must specify an `ENTRYPOINT` instruction as well.



>  **Note**
>
> Do not confuse `RUN` with `CMD`. `RUN` actually runs a command and commits the result; `CMD` does not execute anything at build time, but specifies the intended command for the image.





# Layers

Layering `RUN` instructions and generating commits conforms to the core concepts of Docker where commits are cheap and containers can be created from any point in an image’s history, much like source control. Each layer corresponds to certain instructions in your `Dockerfile`.

Docker containers are building blocks for applications. Each container is an image with a readable/writeable layer on top of a bunch of read-only layers.

These layers (also called intermediate images) are generated when the commands in the Dockerfile are executed during the Docker image build.

```sh
Status: Downloaded newer image for node:latest
 ---> 530c750a346e
Step 2 : RUN mkdir -p /usr/src/app
 ---> Running in 5090fde23e44
 ---> 7184cc184ef8
Removing intermediate container 5090fde23e44
Step 3 : WORKDIR /usr/src/app
 ---> Running in 2987746b5fba
 ---> 86c81d89b023
Removing intermediate container 2987746b5fba
Step 4 : COPY package.json /usr/src/app/
 ---> 334d93a151ee
```

## Build Docker Image

Now that you have some source code and a Dockerfile, it’s time to build your first image, and make sure the containers launched from it work as expected.

```sh
$ docker build --tag bulletinboard:1.0 .
$ docker images
```





# Run Docker ............

> Fill in the blank. A) Container B) Image

```sh
docker run --publish 8000:8080 --detach --name bb bulletinboard:1.0
```

There are a couple of common flags here:

- `--publish` asks Docker to forward traffic incoming on the host’s port 8000, to the container’s port 8080. Containers have their own private set of ports, so if you want to reach one from the network, you have to forward traffic to it in this way. Otherwise, firewall rules will prevent all network traffic from reaching your container, as a default security posture.
- `--detach` asks Docker to run this container in the background.
- `--name` specifies a name with which you can refer to your container in subsequent commands, in this case `bb`.





Src.

https://docs.docker.com/get-started/part2/

https://docs.docker.com/engine/reference/builder/#run

https://medium.com/@jessgreb01/digging-into-docker-layers-c22f948ed612

https://dzone.com/articles/docker-layers-explained