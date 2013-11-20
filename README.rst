===============================
Install Spark 0.8.0 with Hadoop
===============================

Requirements
============
1. User running the scripts should be in the sudoers list.
2. Setup hostname and fqdn
3. Make sure to review/update the config files

Usage
=====

1. Copy this repo::

  ``git clone git://github.com/ezhaar/spark-0.8.0``

2. Run the install script::

   ``cd spark-0.8.0;./install``

3. Go grab a coffee.

What Happened?
==============

1. Created a dedicated group and user for hadoop (hduser:hadoop)
2. Installed Java-1.7 and set Java Path
3. Downloaded, installed and configured hadoop-2.0.5-alpha in
   ``/home/hduser/DataAnalaysis/hadoop`` and update PATH.
4. Downloaded, installed and configured Scala-2.9.3.
5. Downloaded, installed and configured Spark-0.8.0 with YARN.

Post Install
============

Hadoop
------

1. Format hadoop's namenode::
   ``hdfs namenode -format``

2. Start HDFS processes::
   ``hadoop-daemon.sh start namenode``
   ``hadoop-daemon.sh start datanode``

3. Start MapReduce Processes::
   ``yarn-daemon.sh start resourcemanager``
   ``yarn-daemon.sh start nodemanager``
   ``mr-jobhistory-daemon.sh start historyserver``

4. Copy a directory to hdfs::
   ``hadoop fs -copyFromLocal dir /dir``

5. Run a wordcount example on some file in dir::
   ``hadoop fs \
   $HADOOP_DIR/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar \
   wordcount /in /out``

6. Check Outpu::
   ``hadoop fs -cat /out/*``

Spark
-----

1. Run the spark-pi example::
   SPARK_JAR=./assembly/target/scala-2.9.3/spark-assembly-0.8.0-incubating-hadoop2.0.5-alpha.jar \
    ./spark-class org.apache.spark.deploy.yarn.Client \
      --jar examples/target/scala-2.9.3/spark-examples-assembly-0.8.0-incubating.jar \
      --class org.apache.spark.examples.SparkPi \
      --args yarn-standalone \
      --num-workers 3 \
      --master-memory 2g \
      --worker-memory 1g \
      --worker-cores 1

2. Check the output::
   ``cat $HADOOP_DIR/logs/userlogs/<application_id>/container*_000001/stdout``

