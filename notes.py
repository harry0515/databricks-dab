from databricks.connect import DatabricksSession

# you can provide your cluster id in .drabrickscfg file at home directory
spark = DatabricksSession.builder \
    .appName("MyApp") \
    .config("spark.sql.shuffle.partitions", "50") \
    .remote(cluster_id="your-cluster-id") \
    .getOrCreate()


spark.sql("select 1")


