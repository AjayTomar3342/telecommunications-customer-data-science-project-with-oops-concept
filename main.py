import configparser
import pandas as pd

from modules.voice_call import VoiceCallStats

"""
    Feature Families
"""

# These features will help get specific analytical information about minutes of use voice calls
VOICE_CALL_MINUTE_FEATURES = ['mou_cvce_Mean', 'mou_rvce_Mean', 'mouowylisv_Mean', 'mouiwylisv_Mean',
                              'mou_peav_Mean', 'mou_opkv_Mean']

# These features will help get specific analytical information about count of voice calls
VOICE_CALL_COUNT_FEATURES = ['drop_vce_Mean', 'blck_vce_Mean', 'unan_vce_Mean', 'plcd_vce_Mean', 'recv_vce_Mean',
                              'comp_vce_Mean', 'owylis_vce_Mean','iwylis_vce_Mean', 'peak_vce_Mean', 'opk_vce_Mean']

# These features when coupled with other specific features like VOICE_CALL_FEATURES add more layers to the analysis
# results such as adding area as second level analysis feature for total voice call revenue generated from customers
GENERAL_FEATURES = ['months', 'new_cell', 'crclscod', 'asl_flag', 'prizm_social_one', 'area', 'refurb_new',
                    'hnd_price', 'phones', 'models', 'hnd_webcap', 'truck', 'rv', 'ownrent', 'lor', 'dwlltype',
                    'marital', 'income', 'numbcars', 'dwllsize', 'ethnic', 'creditcd', 'eqpdays']

"""
    Setting up the data sources
"""

# Read config file
config = configparser.ConfigParser()
config.read("config//config_file.ini")

# Ingest data source into a pandas dataframe
telekom_data = pd.read_csv('data/Telecom_customer_churn.csv')

"""
    Data Modification
"""
# Changing values inside 'new_cell' column
telekom_data['new_cell'] = telekom_data['new_cell'].replace(['U','N','Y'],['Unclear', 'No', 'Yes'])

# Changing values inside 'refurb_new' column
telekom_data['refurb_new'] = telekom_data['refurb_new'].replace(['N','R'],['No', 'Yes'])

# Changing values inside 'asl_flag' column
telekom_data['asl_flag'] = telekom_data['asl_flag'].replace(['N','Y'],['Not Present', 'Present'])

"""
    Object Creation for Voice Calls related statistics
"""

# Object to analyse minutes of use for Voice Call data
voice_call_mou_object = VoiceCallStats(VOICE_CALL_MINUTE_FEATURES, GENERAL_FEATURES)

# Object to analyse count of usage for Voice Call data
voice_call_count_object = VoiceCallStats(VOICE_CALL_COUNT_FEATURES, GENERAL_FEATURES)

"""
    Plots creation for 'count of Voice Calls' related statistics 
"""

# # Plot the mean count of use for inbound voice calls
# voice_call_count_object.inbound_voice_calls(telekom_data, [4], [1, 6])

# # Plot the mean count of use during off-peak times
# voice_call_count_object.peak_offpeak_calls(telekom_data, [9], [1, 6])

# # Plot the mean count of failed voice calls (Dropped, Blocked, Unanswered, Attempted)
# voice_call_count_object.incomplete_voice_calls(telekom_data, [0, 1, 2, 3], [3])

"""
    Plots creation for 'minutes of use of Voice Calls' related statistics 
"""

# # Plot the mean moments of use for incoming voice calls
# voice_call_mou_object.inbound_voice_calls(telekom_data, [1, 3], [1, 6])

# # Plot the mean moments of use of voice calls during peak times
# voice_call_mou_object.peak_offpeak_calls(telekom_data, [4], [1, 6])
#
# # Plot the mean moments of use of voice calls during off-peak times
# voice_call_mou_object.peak_offpeak_calls(telekom_data, [5], [1, 6])