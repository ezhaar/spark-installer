#!/usr/bin/env bash

### Settings for Large Machines ###


# number of worker instances to run on each worker (default = 1)
# if this is set make sure to set SPARK_WORKER_CORES otherwise each worker instance will try to use all cores
# export SPARK_WORKER_INSTANCES=2

# Total amount of cores to allow spark applications to use on a worker (default: total - 1)
# export SPARK_WORKER_CORES=4

# Total amount of memory to allow spark applications to use on a worker (default total - 1)
# export SPARK_WORKER_MEMORY=2048m

#########################################


### IMP Directories ###
#SEE SPARK-DEFAULTS.CONF

#export SPARK_CONF_DIR="/usr/local/spark/conf"

# Directory for Spark temporary files. It will be used by Spark Master, Spark Worker, Spark Shell and Spark applications.
#export SPARK_TMP_DIR="/tmp/spark"

# Directory where RDDs will be cached
#export SPARK_RDD_DIR="/var/lib/spark/rdd"

# The directory for storing master.log and worker.log files
#export SPARK_LOG_DIR="/var/log/spark"

# Directory to run applications in, which will include both logs and scratch space (default: /var/lib/spark/work).
#export SPARK_WORKER_DIR="/var/lib/spark/work"

# Temporary storage location (as of Spark 1.0)
#export SPARK_LOCAL_DIRS="$SPARK_RDD_DIR"

#export SPARK_PID_DIR="/var/lib/spark/pids"

##########################################


export SPARK_COMMON_OPTS="$SPARK_COMMON_OPTS -Dspark.kryoserializer.buffer.mb=32 "
LOG4J="-Dlog4j.configuration=file://$SPARK_CONF_DIR/log4j.properties"
export SPARK_MASTER_OPTS=" $LOG4J -Dspark.log.file=/var/log/spark/logs/master.log "
export SPARK_WORKER_OPTS=" $LOG4J -Dspark.log.file=/var/log/spark/logs/worker.log "
export SPARK_EXECUTOR_OPTS=" $LOG4J -Djava.io.tmpdir=/tmp/spark/executor "
export SPARK_REPL_OPTS=" -Djava.io.tmpdir=/spark/repl/\$USER "
export SPARK_APP_OPTS=" -Djava.io.tmpdir=/tmp/spark/app/\$USER "
