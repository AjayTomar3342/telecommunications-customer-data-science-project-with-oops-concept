from modules.analysis_modules.voice_call import VoiceCallStats
from modules.analysis_modules.data_call import DataCallStats
from modules.analysis_modules.other_calls import OtherCalls
from modules.feature_families_modules.feature_families import VOICE_CALL_MINUTE_FEATURES, VOICE_CALL_COUNT_FEATURES,\
     DATA_CALL_MINUTE_FEATURES, DATA_CALL_COUNT_FEATURES, OTHER_CALL_FEATURES, GENERAL_FEATURES


def voice_call_analysis(dataframe):
    """
        Object Creation for Voice Calls related statistics
    """

    # Object to analyse count of usage for Voice Call data
    voice_call_count_object = VoiceCallStats(VOICE_CALL_COUNT_FEATURES, GENERAL_FEATURES)

    # Object to analyse minutes of use for Voice Call data
    voice_call_mou_object = VoiceCallStats(VOICE_CALL_MINUTE_FEATURES, GENERAL_FEATURES)


    """
        Plots creation for 'count of Voice Calls' related statistics 
    """

    # # Plot the mean count of use for inbound voice calls
    # voice_call_count_object.inbound_voice_calls(dataframe, [4], [1, 6])
    #
    # # Plot the mean count of use during off-peak times
    # voice_call_count_object.peak_offpeak_calls(dataframe, [9], [1, 6])
    #
    # # Plot the mean count of failed voice calls (Dropped, Blocked, Unanswered, Attempted)
    # voice_call_count_object.incomplete_voice_calls(dataframe, [0, 1, 2, 3], [3])

    """
        Plots creation for 'minutes of use of Voice Calls' related statistics 
    """

    # # Plot the mean moments of use for incoming voice calls
    # voice_call_mou_object.inbound_voice_calls(dataframe, [1, 3], [1, 6])
    #
    # # Plot the mean moments of use of voice calls during peak times
    # voice_call_mou_object.peak_offpeak_calls(dataframe, [4], [1, 6])
    #
    # # Plot the mean moments of use of voice calls during off-peak times
    # voice_call_mou_object.peak_offpeak_calls(dataframe, [5], [1, 6])


def data_call_analysis(dataframe):
    """
        Object Creation for Data Calls related statistics
    """

    # Object to analyse minutes of use for Dataa Call data
    data_call_mou_object = DataCallStats(DATA_CALL_MINUTE_FEATURES, GENERAL_FEATURES)

    # Object to analyse count of usage for Data Call data
    data_call_count_object = DataCallStats(DATA_CALL_COUNT_FEATURES, GENERAL_FEATURES)

    """
         Plots creation for 'minutes of use of Data Calls' related statistics 
     """

    # # Plot the mean moments of use of voice calls during peak times
    # data_call_mou_object.peak_offpeak_minute_calls(dataframe, [1], [1, 6])
    #
    # # Plot the mean moments of use of voice calls during off-peak times
    # data_call_mou_object.peak_offpeak_minute_calls(dataframe, [2], [1, 6])

    """
        Plots creation for 'count of Data Calls' related statistics 
    """

    # # Plot the mean count of failed data calls (Dropped, Blocked, Unanswered, Attempted)
    # data_call_count_object.incomplete_data_calls(dataframe, [0, 1, 2, 3], [3])

    # # Plot the mean count of data calls use during peak and off-peak times
    # data_call_count_object.peak_offpeak_count_calls(dataframe, [5,6], [1, 6])


def other_calls(dataframe):
    """
        Object Creation for statistics about other type of calls
    """

    # Object to analyse statistics about other type of calls than voice or data
    other_calls_object = OtherCalls(OTHER_CALL_FEATURES, GENERAL_FEATURES)

    # Plot the comparison between voice and data calls for unsuccessful  calls
    other_calls_object.other_calls_statistics(dataframe, [0, 1, 2, 3, 4, 5, 6, 7], [3])

