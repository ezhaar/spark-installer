# Configure the necessary Spark environment
import os
os.environ['SPARK_HOME'] = '/usr/local/spark/'
master = os.environ['MASTER']

# And Python path
import sys
sys.path.insert(0, '/usr/local/spark/python')

# Detect the PySpark URL
# choose between local/yarn-clinet

