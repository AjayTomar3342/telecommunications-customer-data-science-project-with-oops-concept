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