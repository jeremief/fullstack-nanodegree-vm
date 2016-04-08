# Tournament


1. Description
--------------
This collection of files is an application that keeps track of a Swiss tournament. It needs to be run on a machine that can run PostgreSQL and Python.


2. How to install
-----------------
You need to fork this directory to your computer install the virtual machine (VM) that Udacity has created for this exercise.

You can do so by following those instructions:
- Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Download and install [Vagrant](https://www.vagrantup.com/downloads.html)
- Fork this directory and clone its content on your computer


3. How to get started
---------------------
Using the command line tool, change the directory to fullstack/vagrant.
Then run `vagrant up` to launch the virtual machine and finally `vagrant ssh` to connect to it.

Once there, you can navigate to the tournament directory:
`cd tournament`
and run 
`python tournament_test.py` 
to launch the test program.


4. How it all works
-------------------
What you have done here is effectively creating a virtual computer inside your own. All the code is stored inside the VM which makes it available to your computer via the /vagrant directory. 


5. About
--------
Made by Jeremie Faye using files and configurations provided by Udacity 