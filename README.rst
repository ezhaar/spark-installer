===================================
Install Spark 1.0.0 with YARN 2.2.0
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
2. Installed Java-default and set Java Path
3. Downloaded, installed and configured hadoop-2.2.0 in
   ``/home/hduser/DataAnalaysis/hadoop`` and update PATH.
4. Downloaded, installed and configured Scala-2.10.3.
5. Downloaded, installed and configured Spark-1.0.0 with YARN.

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

5. List hadooop examples::

   $ hadoop jar \
   $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.2.0.jar

6. Run Hadoopo pi example::

    hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.2.0.jar pi \
    -Dmapreduce.clientfactory.class.name=org.apache.hadoop.mapred.YarnClientFactory 16 1000

Spark
-----

1. Run the spark-pi example::

    SPARK_JAR=./assembly/target/scala-2.10/spark-assembly-1.0.0-hadoop2.2.0.jar \
    SPARK_YARN_APP_JAR=./examples/target/scala-2.10/spark-examples-assembly-1.0.0.jar \
    ./bin/run-example org.apache.spark.examples.SparkPi yarn-client

