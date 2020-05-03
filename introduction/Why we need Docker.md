### **Why we need Docker?** 

**Problem 1**

As you can see in the below image that is the most common problem were industries are facing right now.

![img](https://acadgildsite.s3.amazonaws.com/wordpress_images/devops/DockerForBeginner/01_why_we_need_problem_1.jpg)



**Why does it happen?**

It happens because of different computing environments between test & production



## Docker concepts

Docker is a platform for developers and sysadmins*(A **system administrator**, or **sysadmin**, is a person who is responsible for the upkeep, configuration, and reliable operation of computer systems)* to **build, run, and share** applications with containers. The use of containers to deploy applications is called **containerization**. Containers are not new, but their use for easily deploying applications is.

Containerization is increasingly popular because containers are:

- **Flexible**: Even the most complex applications can be containerized.
- **Lightweight**: Containers leverage and share the host kernel, making them much more efficient in terms of system resources than virtual machines.
- **Portable**: You can build locally, deploy to the cloud, and run anywhere.
- **Loosely coupled**: Containers are highly self sufficient and encapsulated, allowing you to replace or upgrade one without disrupting others.
- **Scalable**: You can increase and automatically distribute container replicas across a datacenter.
- **Secure**: Containers apply aggressive constraints and isolations to processes without any configuration required on the part of the user.



**Advantages**

The main advantages of Docker are:

- **Resource Efficiency**: Process level isolation and usage of the container host’s kernel is more efficient when compared to virtualizing an entire hardware server.
- **Portability**: All the dependencies for an application are bundled in the container. This means they can be easily moved between development, test, and production environments.
- **Continuous Deployment and Testing**: The ability to have consistent environments and flexibility with patching has made Docker a great choice for teams that want to move from waterfall to the modern DevOps approach to software delivery.



### Containers and virtual machines

A container runs *natively* on Linux and shares the kernel of the host machine with other containers. It runs a discrete process, taking no more memory than any other executable, making it lightweight.

By contrast, a **virtual machine** (VM) runs a full-blown “guest” operating system with *virtual* access to host resources through a hypervisor. In general, VMs incur a lot of overhead beyond what is being consumed by your application logic.

| ![Container stack example](https://docs.docker.com/images/Container%402x.png) | ![Virtual machine stack example](https://docs.docker.com/images/VM%402x.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |



## Scaling



<img src="https://lh4.googleusercontent.com/UfDsKNXDabNzgEc1gK86hIBfEr8ACb0y9PItiFLwcMo0yF5itzgUYY-cEdu87xMOlY0xqcJstUGJ7H7HGfJrTXwOCqgjgyl-KDKKsd4Q0_INPehP27jgZbTXRBhQ-QDIt3FJIeX_dKg" alt="horizontal-vs-vertical-scaling-vertical-and-horizontal-scaling-explained-diagram.png" style="zoom:50%;" />

**Horizontal scaling means that you scale by adding more machines** into your pool of resources whereas **Vertical scaling means that you scale by adding more power (CPU, RAM) to an existing machine**.



## Example

Imagine that we have 3 different service in our application each man represent services.

- Red man is data analyzing service. It is just 1 MB Python script. It is procession huge data but output is just some statistic.
- Yellow man is data shipper. It just ship data from red man to blue man. It is a Java app.
- Blue man is WebUI. The processed data is show in the WebUI. It is a bootspring app. 



*t=0*

------

![nail (3).png](https://lh4.googleusercontent.com/PVkDPnDEFa41BASFQjBCXTVOLs27KP_ecVnDDcdpR_jhQuPp6hvQuNTP4igw53JiBfWcirk3TVbei7SVOHYSj34Tux_gR_dnQ8OO-dXz4lM37XPXm6Z-yYe44XvmFnnvESEvACcAVVY)![trolley.png](https://lh5.googleusercontent.com/oSuDKpSRwiJ2fm0zcGceHCKYB6K0rHwfX35-3SdbxOuHBoxSZQpI3odCi1GMa9oV557hiz-JGxVrKv2z1-6dS5VLOmWqqc244bwgZCwXgsQU4ZP6Hl3EiTMifr-haW75BBLSPaJfC20)![worker-of-construction-working-with-a-shovel-beside-material-pile.png](https://lh5.googleusercontent.com/K4yIVOEe6h1vM6WkYt-KzKPnKGbj8Wxxc1yNVfRNgtRYWn9JbZM3Ahp85Np8j1EoMWC6gNZbRT1YyjuTu8e6keRovj9hwG3DICu2gkWhryvpCM-RacZaPV3htAAs8lFpKLm0jqBsJn8)

-----



*t=10*

-----

![nail (3).png](https://lh4.googleusercontent.com/PVkDPnDEFa41BASFQjBCXTVOLs27KP_ecVnDDcdpR_jhQuPp6hvQuNTP4igw53JiBfWcirk3TVbei7SVOHYSj34Tux_gR_dnQ8OO-dXz4lM37XPXm6Z-yYe44XvmFnnvESEvACcAVVY)![trolley.png](https://lh5.googleusercontent.com/oSuDKpSRwiJ2fm0zcGceHCKYB6K0rHwfX35-3SdbxOuHBoxSZQpI3odCi1GMa9oV557hiz-JGxVrKv2z1-6dS5VLOmWqqc244bwgZCwXgsQU4ZP6Hl3EiTMifr-haW75BBLSPaJfC20)![dancing-man.png](https://lh6.googleusercontent.com/sPtP7MR4GwRV3aZUVvEUbroVwqiDt0JCaHfji1S31RG-sHQ5Ti6B5KnbcpzxEPCoUSwqt5xUjJqNvr9Lbhge-4j__vcmf3jmQhVAVewZQFRRe0RefI5WdEhNP6EyBtEpyViumDuf9d0)

-----

*t=20*

-----

![nail (3).png](https://lh4.googleusercontent.com/PVkDPnDEFa41BASFQjBCXTVOLs27KP_ecVnDDcdpR_jhQuPp6hvQuNTP4igw53JiBfWcirk3TVbei7SVOHYSj34Tux_gR_dnQ8OO-dXz4lM37XPXm6Z-yYe44XvmFnnvESEvACcAVVY)![dancing-man.png](https://lh6.googleusercontent.com/AAA0_oMqkp_EWzBQKw1sWIUg1fftrkxi3TjsRYhygSUR3rdEQhW7KcJ8tlkwkIjNz3zbrfEFxJSoGT2Lp-Xw4gkdRjRqkZ9T1YaGakoAHkIX65XY6gJ4O9BXXtXknJr7h6iRz06WRko)![dancer-with-music.png](https://lh5.googleusercontent.com/JeRLFkfKxdDzOvsjUOtPs0GX8bk48x5iKkq-qSSLJWOtHogKuhB_g_VJr32D9hkx6_iSH181DbtFsVWJ6Q6ESGz7rgWWsv1T9aPAiwnqy77QgL9sD5_GqC_p5vrRhvi4u7FKTFFRhZE)

----

When customer see the bill, he said that something is wrong.



When you use, containerized app.

![image-20200503195601018](./img/Ekran Resmi 2020-05-03 19.54.53.png)



# Docker Architecture

The Docker architecture uses a client-server model and comprises of the Docker Client, Docker Host, Network and Storage components, and the[ Docker Registry](https://wiki.aquasec.com/display/containers/Docker+Registries+101)/Hub. Let’s look at each of these in some detail.

![](https://wiki.aquasec.com/download/attachments/2854889/Docker_Architecture.png?version=1&modificationDate=1520172700553&api=v2)



## Docker Client

The Docker client enables users to interact with Docker. The Docker client can reside on the same host as the daemon or connect to a daemon on a remote host. A docker client can communicate with more than one daemon. The Docker client provides a command line interface (CLI) that allows you to issue build, run, and stop application commands to a Docker daemon.

**The main purpose of the Docker Client** is to provide a means to direct the pull of images from a registry and to have it run on a Docker host. Common commands issued by a client are:

```
docker build
docker pull
docker run
```

## DockerHost

The Docker host provides a complete environment to execute and run applications. It comprises of the Docker daemon, Images, Containers, Networks, and Storage. As previously mentioned, the daemon is responsible for all container-related actions and receives commands via the CLI or the REST API. It can also communicate with other daemons to manage its services. The Docker daemon pulls and builds container images as requested by the client. Once it pulls a requested image, it builds a working model for the container by utilizing a set of instructions known as a build file. The build file can also include instructions for the daemon to pre-load other components prior to running the container, or instructions to be sent to the local command line once the container is built.



### Images and containers

Fundamentally, a container is nothing but a running process, with some added encapsulation features applied to it in order to keep it isolated from the host and from other containers. One of the most important aspects of container isolation is that each container interacts with its own private filesystem; this filesystem is provided by a Docker **image**. An image includes everything needed to run an application - the code or binary, runtimes, dependencies, and any other filesystem objects required.



### How the Client Talks to the Docker Host

Now let’s visualize how some of the pieces come together:

![blog/docker-client-host-registry.jpg](https://nickjanetakis.com/assets/blog/docker-client-host-registry-fc0858b5191e042ce19437fd6b52ba214d1e429bf646374f633598ebaac1a4ab.jpg)



## How does it works ?

```sh
docker run hello-world
```



![Untitled Diagram](./img/Untitled Diagram.png)



```sh
docker push hello-world registry
```

![docker_push](./img/docker_push.png)





src.

https://dzone.com/articles/all-about-hibernate-manytomany-association

https://wiki.aquasec.com/display/containers/Docker+Registries+101

http://bit.ly/erkanerol-12factor

https://acadgild.com/blog/docker-for-beginner-what-is-architecture-install-commands

https://docs.docker.com/get-started/

https://gokhansengun.com/docker-nedir-nasil-calisir-nerede-kullanilir/