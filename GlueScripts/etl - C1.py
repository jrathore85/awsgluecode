from awsglue.context import GlueContext
from awsglue.transforms import *
from pyspark.context import SparkContext

glueContext = GlueContext(SparkContext.getOrCreate())

print('glueContext:', glueContext)
print('tested at 30june :', glueContext)

