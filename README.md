# Newspaper Analysis Project

The objective of this project is to build an internal reporting tool to answer 3 questions in relation to the visits and popularity of the newspaper site.

The three questions are:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

`results.txt` has been included which shows the format in which the output looks like on successfully running the python script.

## Setting up

### Using a Virtual Machine (VM)

We are using the below to install and manage the VM:

1. VirtualBox
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com (https://www.vagrantup.com/downloads.html). Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

2. VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
Get

Finally, get the Vagrantfile from: https://github.com/udacity/fullstack-nanodegree-vm and run the below on your command line,

```
$ vagrant up
$ vagrant ssh
```

### Using your machine

You need:
1. Python 3 
2. PostgreSQL
3. psycopg2

## How to run the project?

The project works by connecting to a PostgreSQL database called `news`. You can downlad the data (link below), and follow the steps below to run the python script.

1. Download the data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. You will need to unzip this file once downloaded. The file inside is called `newsdata.sql`. Put this file in your working directory if using your desktop or, on your `vagrant` directory, which is shared with your virtual machine if using a VM
3. From your virtual machine, to load the data `cd` into `vagrant` directory and use the command `psql -d news -f newsdata.sql`. Similar steps for on your machine except you will not have a vagrant file and you will need to `cd` into your relevant directory
4. Run the script by using `python logs-analysis.py` and see the output

## Methodolgy

The `main` function runs all the individual methods and prints them out.
This codes are also in line with `pep257` and `pycodestyle`guides.