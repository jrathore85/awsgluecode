from awsglue.context import GlueContext
from awsglue.transforms import *
from pyspark.context import SparkContext

glueContext = GlueContext(SparkContext.getOrCreate())

print('glueContext:', glueContext)
print('this is final code at 2 June', glueContext)

