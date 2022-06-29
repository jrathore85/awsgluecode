from awsglue.context import GlueContext
from awsglue.transforms import *
from pyspark.context import SparkContext
import time

glueContext = GlueContext(SparkContext.getOrCreate())

print('glueContext:', glueContext)
print('this is final code at 7fffffffffffffff June', glueContext)
print('Before sleep')
time.sleep(60) 
print('After sleep')

