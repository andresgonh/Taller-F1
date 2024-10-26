# Databricks notebook source
print("Hola")
print("Hola 222")


# COMMAND ----------




# COMMAND ----------

# MAGIC %md
# MAGIC **Creación de las variables** 

# COMMAND ----------

# Variables de ubicación de archivos
dl_location = 'abfss://dataengineering@bidatarepositoryg3agonza.dfs.core.windows.net/'
raw_location = dl_location + 'RAW/'

uc_location_aumented = 'medallion_architecture.aumented.'

# Otras variables
date_format = 'dd/MM/yyyy'
