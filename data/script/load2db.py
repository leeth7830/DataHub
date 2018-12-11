# ---------------------------------------------------------------------------------------------------
# spark-submit --packages com.databricks:spark-csv_2.10:1.2.0 load2db.py --prod --overwrite -g 1
# ---------------------------------------------------------------------------------------------------
from pyspark import  SparkContext
from pyspark.sql import HiveContext
import argparse
from sqlalchemy import create_engine
from string import Template
import os
#import yaml

target_schema ='census'
homedir = os.path.expanduser('~')
prod_db    = os.environ.get('SQLALCHEMY_DATABASE_URI')
staging_db = os.environ.get('SQLALCHEMY_DATABASE_URI')
sc = SparkContext('local','pyspark')
sqlContext = HiveContext(sc)
parser = argparse.ArgumentParser(prog='copy to db', description='copies data from S3 to postgres db')
#parser.add_argument('-g','--groupid', help='group_id', default = '1')
parser.add_argument('--prod', help='Run in prod', action='store_true')
parser.add_argument('--overwrite', help='overwrite', action='store_true')
args = parser.parse_args()

#groupid=args.groupid
if args.overwrite is True:
  write_mode='overwrite'
else:
  write_mode='append'

#platform_groupid = " " + str ( groupid ) + " "
# common base path
basepath='../output/government/census/US/'
map = { basepath+"us_census.parquet":"us",
        }

#with open( 'credentials.conf', 'r') as f:
#    credentials = yaml.load(f)
class QueryException(BaseException):
    pass
engine = ""
##commented out user/pass
if args.prod is True:
    name = 
    key = 
else:
    name = 
    key = 

Properties = {'user':name,'password':key, "driver": 'org.postgresql.Driver' }

#print '-----------------------',pwrd

if args.prod is True:
  URL = 'jdbc:postgresql://23.226.138.66:5432/prod'
else:
  URL = 'jdbc:postgresql://23.226.138.66:5432/prod'

for filename in map.keys ():
  tablename = target_schema + '.' + map [ filename ]
  data_object = sqlContext.read.parquet(filename)
  data_object.write.jdbc(url=URL, table = tablename , properties = Properties, mode= write_mode )

print ('Okay')
