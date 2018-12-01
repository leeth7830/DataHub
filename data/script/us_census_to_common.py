# Usage:
# >Basic:
#spark-submit --packages com.databricks:spark-csv_2.10:1.2.0 us_census_to_common.py
#
# >Fancy:
#spark-submit --packages com.databricks:spark-csv_2.10:1.2.0 --conf "spark.yarn.executor.memoryOverhead=1990" --conf "spark.executor.memory=9000m" us_census_to_common.py

from pyspark import  SparkContext
from pyspark.sql import HiveContext
import os

sc = SparkContext()
sqlContext = HiveContext(sc)

us_census_path = "../input/us_census/us0000120101.csv"
us_geo_path = "../input/us_census/usgeo20101.csv"

output_file = "../output/government/census/US/us_census.parquet"

us_census_dataframe = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', comment="N").load(us_geo_path).cache()
us_census_dataframe.registerTempTable("us_census_dataframe")
#us_census_dataframe.write.save(prepocessed_basepath+"underwriting.parquet", mode='overwrite

us_census = sqlContext.sql(""" SELECT
    LOGRECNO as id,
    NAME as name,
    GEOCOMP as geocomp,
    'US' as country,
    REGION as region,
    DIVISION as division,
    STATE as state,
    COUNTY as county,
    COUNTYCC as countycc,
    COUNTYSC as countysc,
    COUSUB as cousub,
    COUSUBCC as cousubcc,
    COUSUBSC as cousubsc,
    PLACE as place,
    PLACECC as placecc,
    AREALAND as area_land,
    AREAWATR as area_water,
    FUNCSTAT as func_stat,
    POP100 as pop_count,
    HU100 as housing_unit,
    INTPTLAT as latitude,
    INTPTLON as longitude,
    STATENS as state_ansi,
    COUNTYNS as county_ansi,
    COUSUBNS as county_sub_ansi,
    PLACENS as place_ansi
    FROM us_census_dataframe
    """)

us_census.registerTempTable("us_census")
us_census.write.save(output_file, mode = 'overwrite')

sqlContext.dropTempTable("us_census_dataframe")
print("Completed")
