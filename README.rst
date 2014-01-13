===============================
Install Spark 0.8.1 with YARN 2.2.0
===============================

Requirements
============
1. User running the scripts should be in the sudoers list.
2. Setup hostname and fqdn
3. Make sure to review/update the config files

Usage
=====

1. Copy this repo::

   $ git clone git://github.com/ezhaar/spark-0.8.0

2. Run the install script::

   $ cd spark-0.8.1;./install

3. Go grab a coffee.

What Happened?
==============

1. Created a dedicated group and user for hadoop (hduser:hadoop)
2. Installed Java-1.7 and set Java Path
3. Downloaded, installed and configured hadoop-2.2.0 in
   ``/home/hduser/DataAnalaysis/hadoop`` and update PATH.
4. Downloaded, installed and configured Scala-2.9.3.
5. Downloaded, installed and configured Spark-0.8.1 with YARN.

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

Spark
-----

1. Run the spark-pi example

.. code:: bash
    $ SPARK_JAR=./assembly/target/scala-2.9.3/spark-assembly-0.8.1-incubating-hadoop2.2.0.jar
    SPARK_YARN_APP_JAR=./examples/target/scala-2.9.3/spark-examples-assembly-0.8.1-incubating.jar \
    ./run-example org.apache.spark.examples.SparkPi yarn-client

Common Errors
-------------
if slaves cannot contact master strange things will happen
 - make sure slaves can resolve master
 - make sure firewalls are down and ports are open
