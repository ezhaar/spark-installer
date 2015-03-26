===================================
Install Spark 1.3.0 with YARN 2.2.0
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

1. Created a dedicated group and user for hadoop (hduser:hadoop)
2. Installed Jdk-1.7 and set Java Path
3. Downloaded, installed and configured hadoop-2.4.0 in
   ``/home/hduser/DataAnalaysis/hadoop`` and update PATH.
4. Downloaded, installed and configured Scala-2.10.3.
5. Downloaded, installed and configured Spark-1.1.3 with YARN.

Post Install
============

Switch to the newly created hduser and cd to home directory::
   
   $ sudo su hduser;cd 

Hadoop
------

0. Update the hostname in ``$HADOOP_DIR/conf/core-site.xml``::
   
   $ sed -i s/XXXX/myHostname/g $HADOOP_CONF_DIR/core-site.xml

1. Format hadoop's namenode::
   
   $ hdfs namenode -format

2. Start HDFS processes::
   
   $ start-dfs.sh

3. Start Yarn Processes::
   
   $ start-yarn.sh

4. Create the initial directories::
   
   $ hdfs dfs -mkdir /user;hdfs dfs -mkdir /user/hduser

