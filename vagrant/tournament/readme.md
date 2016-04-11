# Tournament


##1. Description
This collection of files is an application that keeps track of a Swiss tournament. It needs to be run on a machine that can run PostgreSQL and Python.


##2. How to install
You need to fork this directory to your computer install the virtual machine (VM) that Udacity has created for this exercise.

You can do so by following those instructions:
- Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Download and install [Vagrant](https://www.vagrantup.com/downloads.html)
- Fork this directory and clone its content on your computer


##3. How to get started
You will need to do several things to get started:
- navigate to the right directory
- switch on and connect to the vagrant virtual machine
- navigate to the shared /vagrant folder
- create the database by running "tournament.sql" in psql
- run the tests by running "tournament_test.py"

#### Navigate to the right directory
Once you have cloned the directory to your machine, navigate to the vagrant directory using the command line tool:  
`cd yourdirectory/fullstack/vagrant`  

#### Switch on and connect to the Vagrant virtual mchine
From there, turn on the vagrant machine by entering:  
`vagrant up`  
and finally  
`vagrant ssh`  
to connect to it.

#### Navigate to the shared /vagrant folder
Your machine and the VM re two seperate entities. However, they share a common folder to communicate. You can navigate to it by entering:  
`cd /vagrant`  
Once there, you can navigate to the tournament directory:  
`cd tournament`  

#### Create the database by running "tournament.sql" in psql
Enter  
`psql`  
in your terminal.
There, create the database by importing the sql file:  
`\i tournament.sql`  
If all goes well, you will see that psql has created the database along with all the tables and views.

#### Run the tests by running "tournament_test.py"
Enter Ctrl + D to exit psql and enter:  
`python tournament_test.py`  
to launch the test program.


##4. How it all works
What you have done here is effectively creating a virtual computer inside your own. All the code is stored inside the VM which makes it available to your computer via the /vagrant directory. 


##5. About
Made by Jeremie Faye using files and configurations provided by Udacity 