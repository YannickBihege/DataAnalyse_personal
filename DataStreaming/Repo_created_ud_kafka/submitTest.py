import findspark
findspark.init('/home/yannick/dev/spark-2.4.4-bin-hadoop2.7')

import pyspark
from pyspark import SparkConf
from pyspark.sql import SparkSession


from pyspark import SparkContext



if __name__ == "__main__":
    spark = SparkSession \
    .builder \
    .appName("Explore_Json_File") \
    .getOrCreate()


path = "./police-department-calls-for-service.json"
crime_log = spark.read.json(path,multiLine=True)

crime_log.printSchema()

crime_log.take(10)

spark.stop()
