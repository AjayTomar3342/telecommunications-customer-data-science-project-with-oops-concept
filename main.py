import configparser
import pandas as pd

from modules.data_cleaning.data_cleaning import data_manipulation
from function_calls.analysis_functions import voice_call_analysis, data_call_analysis, other_calls

"""
    Setting up the data sources
"""

# Read config file
config = configparser.ConfigParser()
config.read("config//config_file.ini")

# Ingest data source into a pandas dataframe
telekom_data = pd.read_csv('data/Telecom_customer_churn.csv')

# Function call to change data values as required
telekom_data = data_manipulation(telekom_data)

# Plot analysis results for voice calls
voice_call_analysis(telekom_data)

# Plot analysis results for data calls
data_call_analysis(telekom_data)

# Plot analysis results for calls which are sent to rare locations like customer care and threeway
other_calls(telekom_data)

