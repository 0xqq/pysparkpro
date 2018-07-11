from pyspark.sql import SparkSession
import os,time

spark = SparkSession.builder.appName("pysparkpro").config("spark.some.config.option", "some-value").getOrCreate()

if __name__ == '__main__':
    data = spark.read.csv("file:///Users/leiqiankun/PycharmProjects/lqkcode/tianchi/pyspark_code/fresh_comp_offline/tianchi_fresh_comp_train_item.csv",header=True)
    # print(data.take(3))

    data.createOrReplaceTempView("user")
    # df2.createOrReplaceTempView("item")

    datatem = spark.sql("SELECT * FROM user")
    print(datatem.rdd.take(3))

    # d = data.show()
    # print(d)

    time.sleep(100000)
    spark.stop()