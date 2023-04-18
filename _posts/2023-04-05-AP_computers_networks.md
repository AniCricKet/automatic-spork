---
toc: true
comments: true
layout: post
title: Computers and Networks (Unit 4)
description: Add Definitions from Unit 4 Computer Systems and Networks
categories: []
type: ap
week: 29
---

## Requirements
> Work through College Board Unit 4... blog, add definitions, and pictures.  Be creative, for instance make a story of Computing and Networks that is related to your PBL experiences this year.


### How a Computer Works
> As we have learned, a computer needs aa program to do something smart.  The sequence of a program initiates a series of actions with the computers Central Processing Unit (CPU). This component is essentially a binary machine focussing on program instructions provided.  The CPU retrieives and stores the data it acts upon in Random Access Memory (RAM). Between the CPU, RAM, and Storage Devices a computer can work with many programs and large amounts of data.

List specification of your Computer, or Computers if working as Pair/Trio
- Processor: Apple M1 Chip
- Memory in GB: 8 GB
- Storage in GB: 245 GB
- OS: MacOS Ventura 13.3

Define or describe usage of Computer using Computer Programs. Pictures are preferred over a lot of text.  Use your experience.

- Input devices: Input devices are hardware devices that allow users to interact with a computer by providing input. Examples include keyboards, mice, touchscreens, and microphones. When you use these devices to input information into a computer, the computer processes the data and sends it to the relevant programs for further processing.
- Output devices: Output devices are hardware devices that allow the computer to display or output information to the user. Examples include monitors, printers, and speakers. When a program processes data, it sends the output to the relevant output device for display or playback.
- Program File: A program file is a file that contains executable code that can be run by a computer program. It typically has a file extension such as .exe, .app, or .jar.
- Program Code: Program code is the set of instructions that a computer program uses to perform a specific task. It is written in a programming language such as Python, Java, or C++.
- Processes: In computing, a process is a program or set of instructions that are being executed by a computer. When a program is run, it creates a process that runs independently of other processes on the computer.
- Ports: A port is a connection point on a computer that is used to connect input or output devices. For example, USB ports are used to connect devices such as keyboards and mice to a computer.
- Data File: A data file is a file that contains data or information that is used by a computer program. Examples include text files, image files, and database files.
- Inspect Running Code: When a program is running, it is possible to inspect the code and see how it is executing. This can be useful for debugging or troubleshooting purposes.
- Inspect Variables: Variables are used in programming to store values that can be used by the program. When a program is running, it is possible to inspect the variables and see their current values. This can be useful for debugging or troubleshooting purposes.



### The Internet
> Watch/review College Board Daily Video for 4.1.1

# Essential Knowledge

    - A computing device is a physical artifact that can run a program. Some examples include computers, tablets, servers, routers, and smart sensors.
    - A computing system is a group of computing devices and programs working together for a common purpose.
    - A computer network is a group of interconnected computing devices capable of sending or receiving data.
    - A computer network is a type of computing system. 
    - A path between two computing devices on a computer network (a sender and a receiver) is a sequence of directly connected computing devices that begins at the sender and ends at the receiver.
    - Routing is the process of finding a path from sender to receiver.
    - The bandwidth of a computer network is the maximum amount of data that can be sent in a fixed amount of time.
    - Bandwidth is usually measured in bits per second

- Complete Vocabulary Matching Activity.  Incorporate this into your learnings from year.  To analyze measure path and latency use `traceroute` and `ping` commands from Linux Terminal.  
    - Path: A sequence of directly connected computing devices that begins at the sender and ends at the receiver(A).
    - Route: The process of finding a path from the sender to the receiver(E).
    - Computer System: A group of computing devices and programs working together for a common puropse(B).
    - Computer Device: A physical artifact that can run a program(C).
    - Bandwidth: The maximum amount of data that can be sent in a fixed amount of time(D).
    - Computer Network: A group of interconnected computing devices capable of sending or receiving data(F).

> Watch/review College Board Daily Video 4.1.2

- Complete True of False Questions

- Essential Knowledge
    - The internet is a computer network consisting of interconnected networks that use standardized, open (nonproprierary) communication protocols.
    - Access to the internet depends on the ability to connect a computing device to an internet connected device. 
    - A protocol is an agreed-upon set of rules that specify the behavior of a system.
    - The protocols used in the internet are open, which allows users to easily connect additional computing devices to the internet.
    - Routing on the internet is usually dynamic; it is not specified in advance
    - The scalability of a system is the capacity for the system to change in size and scale to meet new demands.
    - The internet was designed to be scalable
    - Information is passed through the internet as a data stream. Data streams contain chunks of data, which are encapsulated in packets. 
    - Packets contain a chunk of data and metadata used for routing the packet between the origin and the destination on the internet, as well as for data reassembly.
    - Packets may arrive at the destination in order, out of order, or not at all
    - IP, TCP and UDP are common protocols used on the internet.
    - The world wide web is a system of linked pages, programs, and files.
    - HTTP is a protocol used by the world wide web
    - The world wide web uses the internet

- Go over AP videos, vocabulary, and essential knowledge.  Draw a diagram showing the internet and its many levels. A preferred diagram would using your knowledge of frontend, backend, deployment, etc.  Picture would highligh vocabulary by illustration. The below illustration have some ideas

- Often we draw pictures of machines communicating over the Internet with arrows.  However, the real communication goes through protocol layers and the machine and then is trasported of the network.   For College Board and future Computer Knowledge you should become familiar with the following ...

```
     User Machine  <---> Frontend Server <---> Backend Server
    +-----------+         +-----------+         +-----------+
    |  Browser  |         |  GH Page  |         |   Flask   |
    +-----------+    ^    +-----------+    ^    +-----------+
    |    HTTP   |    |    |    HTTP   |    |    |    HTTP   |
    +-----------+    |    +-----------+    |    +-----------+
    |    TCP    |    |    |    TCP    |    |    |    TCP    |   
    +-----------+    |    +-----------+    |    +-----------+
    |     IP    |    V    |     IP    |    V    |     IP    |
    +-----------+         +-----------+         +-----------+
    |  Network  |  <--->  |  Network  |  <--->  |  Network  |
    +-----------+         +-----------+         +-----------+
```

The "http" layer is an application layer protocol in the TCP/IP stack, used for ***communication between web browsers and web servers***. It is the protocol used for transmitting data over the World Wide Web.

The "transport" layer (TCP) is responsible for providing reliable data transfer between applications running on different hosts.  The TCP protocol segments the data into smaller ***chunks called "segments"***. Each segment contains a sequence number that identifies its position in the original stream of data, as well as other control information such as source and destination port numbers, and checksums for error detection.

The "ip" layer is responsible for packetizing data received from the TCP layer of the protocol stack, and then ***encapsulating the data into IP packets***. The IP packets are then sent to the lower layers of the protocol stack for transmission over the network.

The "network" layer is responsible for ***routing data packets between networks*** using the Internet Protocol (IP). This layer handles tasks such as packet addressing and routing, fragmentation and reassembly, and ***network congestion*** control.


### Fault Tolerance
> Watch both Daily videos for 4.2

- Complete the network activity, summarize your understanding of fault tolerance.
- Example #1: This example is fault tolerant because each device has more than one connection.
- Example #2: This example is not fault tolerant because device (F) has only one connection.
- Example #3: This example is not fault tolerant because device (A) has only one connection.
- Question #1: What is not a benefit of a fault-tolerant network? Answer: Data will only take one route from one device to another, no matter the number of routes available.(C)
- Question #2: What would make the given network fault-tolerant? Answer: A connection from A to B.(A)
- Fault tolerance allows data to be transmitted faster and more reliably from one device to another by using multiple different networks.

### Parallel and Distributed Computing
> Review previous lecture on Parallel Computing and watch Daily vidoe 4.3.  Think of ways to make something in you team project to utilize Cores more effectively.  Here are some thoughts to add to your story of Computers and Networks...

- What is naturally Distributed in Frontend/Backend archeticture?  
  
The backend is normally used for the running of different tasks, functions, programs, and even other servers. This allows a program to run its parts and to be usable. The Frontend is normally used just for the user/users to have access to the program. Its job is to display it to the user and do it by having connections with the backend.


- Analyze this command in Docker: ```ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8086"```.   Determine if there is options are options in this command for parallel computing within the server that runs python/gunicorn.  Here is an [article](https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7)


> Last week we discussed parallel computing on local machine.  There are many options.  Here is something to get parallel computing work with a tool called Ray.
- Review this [article](https://www.anyscale.com/blog/writing-your-first-distributed-python-application-with-ray)...  Can you get parallel code on images to work more effectively?  I have not tried Ray.

You can get parallel code on images to work more effectively by using Ray. Ray makes it so an image gets processed through different tasks running parallel across multiple cores. This would make processing the images more time efficient.

- Code example from ChatGPT using squares.  This might be more interesting if nums we generated to be a lot bigger.

```python
import ray

# define a simple function that takes a number and returns its square
def square(x):
    return x * x

# initialize Ray
ray.init()

# create a remote function that squares a list of numbers in parallel
@ray.remote
def square_list(nums):
    return [square(num) for num in nums]

# define a list of numbers to square
nums = [1, 2, 3, 4, 5]

# split the list into two parts
split_idx = len(nums) // 2
part1, part2 = nums[:split_idx], nums[split_idx:]

# call the remote function in parallel on the two parts
part1_result = square_list.remote(part1)
part2_result = square_list.remote(part2)

# get the results and combine them
result = ray.get(part1_result) + ray.get(part2_result)

# print the result
print(result)

```
