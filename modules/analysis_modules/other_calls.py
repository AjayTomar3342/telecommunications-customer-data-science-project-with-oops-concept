import plotly.express as px


class OtherCalls():
    """Class for analyzing calls which are towards miscellaneous locations like customer care and threeway calls"""
    def __init__(self, other_call_features, general_features):
        """Initializes the parameters for this class"""
        self.other_call_features = other_call_features
        self.general_features = general_features

    def other_calls_statistics(self, dataframe, primary_features, secondary_features):
        """Creates plots for statistics about calls towards non-contemporary locations"""
        primary_features = [self.other_call_features[feature] for feature in primary_features]
        secondary_features = [self.general_features[feature] for feature in secondary_features]

        # Dictionary to customize the title of the plots
        feature_dict = {'da_Mean': 'directory assisted', 'roam_Mean': ' roaming', 'custcare_Mean': 'customer care',
                        'threeway_Mean': 'threeway', 'drop_blk_Mean': 'dropped or blocked',
                        'attempt_Mean': 'attempted calls', 'callfwdv_Mean': ' fowarded', 'callwait_Mean': 'waited',
                        'asl_flag': '(Account spending limit)'}

        # Iterate through primary features submitted by user. Primary feature here being related to other type of calls
        for primary_feature in primary_features:
            # Iterate through secondary features. Secondary features being general features which add layers to analysis
            for secondary_feature in secondary_features:
                # Plot the required graph
                fig = px.histogram(dataframe, x=primary_feature, log_y=True, color=secondary_feature,
                                   title='Histogram displaying percentage of users vs. count of '+
                                         feature_dict[primary_feature] + ' calls with legend: '
                                         + feature_dict[secondary_feature], histnorm='percent')
                fig.update_layout(title_x=0.5, title_font_family="Arial")
                fig.show()


