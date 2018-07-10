from pyspark import SparkConf, SparkContext,SQLContext
from pyspark.sql import HiveContext, SparkSession
import os, time


# 第一种方式
sparkConf = SparkConf().setAppName(value="testspark").setMaster("local[2]")
sc = SparkContext(conf=sparkConf)

spark_v1 = HiveContext(sparkContext=sc)
# 第二种方式
spark_v2 = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
print(spark_v2)
if __name__ == '__main__':
    time.sleep(100000)
    # spark_v1.stop()
    spark_v2.stop()