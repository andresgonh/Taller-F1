# Databricks notebook source
# MAGIC %md
# MAGIC **Importación de la librerias necesarias**

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *
import uuid

# COMMAND ----------

# Variables de ubicación de archivos
dl_location = 'abfss://dataengineering@bidatarepositoryg3agonza.dfs.core.windows.net/'
raw_location = dl_location + 'RAW/'

uc_location_aumented = 'medallion_architecture.aumented.'

# Otras variables
date_format = 'dd/MM/yyyy'
