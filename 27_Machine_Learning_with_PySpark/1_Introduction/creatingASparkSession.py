# Creating a SparkSession
# In this exercise, you'll spin up a local Spark cluster using all available cores. The cluster will be accessible via a SparkSession object.

# The SparkSession class has a builder attribute, which is an instance of the Builder class. The Builder class exposes three important methods that let you:

# specify the location of the master node;
# name the application (optional); and
# retrieve an existing SparkSession or, if there is none, create a new one.
# The SparkSession class has a version attribute which gives the version of Spark.

# Find out more about SparkSession here.

# Once you are finished with the cluster, it's a good idea to shut it down, which will free up its resources, making them available for other processes.

# Note:: You might find it useful to review the slides from the lessons in the Slides panel next to the IPython Shell.

# Instructions
# 100 XP
# Import the SparkSession class from pyspark.sql.
# Create a SparkSession object connected to a local cluster. Use all available cores. Name the application 'test'.
# Use the SparkSession object to retrieve the version of Spark running on the cluster. Note: The version might be different to the one that's used in the presentation (it gets updated from time to time).
# Shut down the cluster.


# Import the PySpark module
from pyspark.sql import SparkSession

# Create SparkSession object
spark = SparkSession.builder \
                    .master('local[*]') \
                    .appName('test') \
                    .getOrCreate()

# What version of Spark?
# (Might be different to what you saw in the presentation!)
print(spark.version)

# Terminate the cluster
spark.stop()
