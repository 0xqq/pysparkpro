from pyspark.sql import SparkSession


class PysparkPro():
    MYSQL_CONF = ""
    HIVE_CONF = ""
    HBASE_CONF = ""
    KAFKA_CONF = ""
    HADOOP_CONF = ""
    PYSPARKPRO = ""

    def __init__(self):
        super(PysparkPro, self).__init__()
        self.PYSPARKPRO = SparkSession.builder.appName("Pyspark example")\
            .config("spark.some.config.option", "some-value").getOrCreate()