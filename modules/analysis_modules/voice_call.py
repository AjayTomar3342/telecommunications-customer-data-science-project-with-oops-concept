import plotly.express as px


class VoiceCallStats():
    """Class for analyzing dataset about voice calls"""
    def __init__(self, class_specific_features, overall_general_features):
        """Initializes the parameters for this class"""
        self.class_specific_features = class_specific_features
        self.overall_general_features = overall_general_features

    def peak_offpeak_calls(self, dataframe, primary_feature_indexes, secondary_feature_indexes):
        """Creates plots related to peak and off-peak voice calls"""
        primary_features = [self.class_specific_features[feature] for feature in primary_feature_indexes]
        secondary_features = [self.overall_general_features[feature] for feature in secondary_feature_indexes]

        # Dictionary to customize the title of the plots
        inbound_feature_dict = {'mou_peav_Mean': ' mean of unrounded minutes of use during peak hours',
                                'mou_opkv_Mean': ' mean of unrounded minutes of use during off-peak hours',
                                'opk_vce_Mean': 'mean number of calls during off-peak hours',
                                'new_cell': '(New Cell Phone)',
                                'refurb_new': '(Refurbished Phone)'}

        # Iterate through primary features submitted by user. Primary feature here being related to peak/off-peak calls
        for primary_feature in primary_features:
            # Iterate through secondary features. Secondary features being general features which add layers to analysis
            for secondary_feature in secondary_features:
                # Plot the required graph
                fig = px.histogram(dataframe, x=primary_feature, log_y=True, color=secondary_feature,
                                   title='Histogram displaying percentage of users vs.'+
                                         inbound_feature_dict[primary_feature] + ' with legend: '
                                         + inbound_feature_dict[secondary_feature], histnorm='percent')
                fig.update_layout(title_x=0.5, title_font_family="Arial")
                fig.show()

    def inbound_voice_calls(self, dataframe, primary_feature_indexes, secondary_feature_indexes):
        """Creates plots related to inbound voice calls"""
        primary_features = [self.class_specific_features[feature] for feature in primary_feature_indexes]
        secondary_features = [self.overall_general_features[feature] for feature in secondary_feature_indexes]

        # Dictionary to customize the title of the plots
        inbound_feature_dict = {'mou_rvce_Mean': ' mean of unrounded minutes of use during received voice calls',
                                'mouiwylisv_Mean': 'mean of unrounded minutes of use of received'
                                                   ' wireless to wireless calls',
                                'recv_vce_Mean': ' mean number of received voice calls',
                                'new_cell': '(New Cell Phone)',
                                'refurb_new': '(Refurbished Phone)'}
        # Iterate through primary features submitted by user. Primary feature here being related to incoming voice calls
        for primary_feature in primary_features:
            # Iterate through secondary features. Secondary features being general features which add layers to analysis
            for secondary_feature in secondary_features:
                # Plot the required graph
                fig = px.histogram(dataframe, x=primary_feature, log_y=True, color=secondary_feature,
                                   title='Histogram displaying percentage of users vs.' +
                                         inbound_feature_dict[primary_feature] + ' with legend: '
                                         + inbound_feature_dict[secondary_feature], histnorm='percent')
                fig.update_layout(title_x=0.5, title_font_family="Arial")
                fig.show()

    def incomplete_voice_calls(self, dataframe, primary_feature_indexes, secondary_feature_indexes):
        """Creates plots related to incomplete voice calls"""
        primary_features = [self.class_specific_features[feature] for feature in primary_feature_indexes]
        secondary_features = [self.overall_general_features[feature] for feature in secondary_feature_indexes]

        # Dictionary to customize the title of the plots
        inbound_feature_dict = {'drop_vce_Mean': ' dropped',
                                'blck_vce_Mean': ' blocked',
                                'unan_vce_Mean': ' unanswered',
                                'plcd_vce_Mean': ' attempted',
                                'asl_flag': '(Account spending limit)'}
        # Iterate through primary features submitted by user. Primary feature here being related to incoming voice calls
        for primary_feature in primary_features:
            # Iterate through secondary features. Secondary features being general features which add layers to analysis
            for secondary_feature in secondary_features:
                # Plot the required graph
                fig = px.histogram(dataframe, x=primary_feature, log_y=True, color=secondary_feature,
                                   title='Histogram displaying percentage of users vs. Mean number of' +
                                         inbound_feature_dict[primary_feature] + ' voice calls with legend: '
                                         + inbound_feature_dict[secondary_feature], histnorm='percent')
                fig.update_layout(title_x=0.5, title_font_family="Arial")
                fig.show()







