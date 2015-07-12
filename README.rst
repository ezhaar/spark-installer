===================================
Install Spark 1.4.0 with hadoop 2.4.0 pandas and jupyter
===================================

Requirements
============
1. User running the scripts should be in the sudoers list.
2. Setup hostname and fqdn
3. Make sure to review/update the config files

Usage
=====

1. Copy this repo::

   $ git clone git://github.com/ezhaar/spark-installer

2. Run the install script::

   $ cd spark-installer;./install

3. Go grab a coffee.

What Happened?
==============

1. Boostraps environment variables
2. Installed Jdk-1.7 and set Java Path
3. Downloaded, installed and configured hadoop-2.4.0 in
   ``/usr/local/hadoop`` and update PATH.
4. Downloaded, installed and configured Scala-2.10.3.
5. Downloaded, installed and configured Spark-1.4.0 standalone

Post Install
============
Make sure to update the slaves file in ``/user/local/hadoop/etc/hadoop/``
Switch to the newly created hduser and cd to home directory::
   
   $ cd; source ~/.bashrc 
   $ fab create_hdfs_dirs

   # if running on single node
   $ fab init_local
   $ /usr/local/spark/sbin/start-all.sh
   $ ./start_notebook.sh

Now you should be able to access the jupyter notebook on ``localhost:9999``

