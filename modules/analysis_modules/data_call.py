import plotly.express as px


class DataCallStats():
    """Class for analyzing dataset about data calls"""
    def __init__(self, class_specific_features, overall_general_features):
        """Initializes the parameters for this class"""
        self.class_specific_features = class_specific_features
        self.overall_general_features = overall_general_features

    def peak_offpeak_minute_calls(self, dataframe, primary_feature_indexes, secondary_feature_indexes):
        """Creates plots related to minutes of use of data calls during peak and off-peak time periods"""
        primary_features = [self.class_specific_features[feature] for feature in primary_feature_indexes]
        secondary_features = [self.overall_general_features[feature] for feature in secondary_feature_indexes]

        # Dictionary to customize the title of the plots
        feature_dict = {'mou_pead_Mean': ' mean of unrounded minutes of data call use during peak hours',
                        'mou_opkv_Mean': ' mean of unrounded minutes of data call use during off-peak hours',
                        'new_cell': '(New Cell Phone)', 'refurb_new': '(Refurbished Phone)'}

        # Iterate through primary features submitted by user. Primary feature here being related to peak/off-peak calls
        for primary_feature in primary_features:
            # Iterate through secondary features. Secondary features being general features which add layers to analysis
            for secondary_feature in secondary_features:
                # Plot the required graph
                fig = px.histogram(dataframe, x=primary_feature, log_y=True, color=secondary_feature,
                                   title='Histogram displaying percentage of users vs.'+
                                         feature_dict[primary_feature] + ' with legend: '
                                         + feature_dict[secondary_feature], histnorm='percent')
                fig.update_layout(title_x=0.5, title_font_family="Arial")
                fig.show()

    def peak_offpeak_count_calls(self, dataframe, primary_feature_indexes, secondary_feature_indexes):
        """Creates plots related to count of data calls during peak and off-peak periods"""
        primary_features = [self.class_specific_features[feature] for feature in primary_feature_indexes]
        secondary_features = [self.overall_general_features[feature] for feature in secondary_feature_indexes]

        # Dictionary to customize the title of the plots
        feature_dict = {'peak_dat_Mean': ' mean of data calls use during peak times',
                        'mou_opkv_Mean': 'mean of data calls use during off-peak', 'new_cell': '(New Cell Phone)',
                        'refurb_new': '(Refurbished Phone)'}
        # Iterate through primary features submitted by user. Primary feature here being related to data calls
        for primary_feature in primary_features:
            # Iterate through secondary features. Secondary features being general features which add layers to analysis
            for secondary_feature in secondary_features:
                # Plot the required graph
                fig = px.histogram(dataframe, x=primary_feature, log_y=True, color=secondary_feature,
                                   title='Histogram displaying percentage of users vs.' +
                                         feature_dict[primary_feature] + ' with legend: '
                                         + feature_dict[secondary_feature], histnorm='percent')
                fig.update_layout(title_x=0.5, title_font_family="Arial")
                fig.show()

    def incomplete_data_calls(self, dataframe, primary_feature_indexes, secondary_feature_indexes):
        """Creates plots related to incomplete data calls"""
        primary_features = [self.class_specific_features[feature] for feature in primary_feature_indexes]
        secondary_features = [self.overall_general_features[feature] for feature in secondary_feature_indexes]

        # Dictionary to customize the title of the plots
        feature_dict = {'drop_dat_Mean': ' dropped', 'blck_dat_Mean': ' blocked', 'unan_dat_Mean': ' unanswered',
                        'plcd_dat_Mean': ' attempted','asl_flag': '(Account spending limit)'}
        # Iterate through primary features submitted by user. Primary feature here being related to data calls
        for primary_feature in primary_features:
            # Iterate through secondary features. Secondary features being general features which add layers to analysis
            for secondary_feature in secondary_features:
                # Plot the required graph
                fig = px.histogram(dataframe, x=primary_feature, log_y=True, color=secondary_feature,
                                   title='Histogram displaying percentage of users vs. Mean number of' +
                                         feature_dict[primary_feature] + ' data calls with legend: '
                                         + feature_dict[secondary_feature], histnorm='percent')
                fig.update_layout(title_x=0.5, title_font_family="Arial")
                fig.show()







