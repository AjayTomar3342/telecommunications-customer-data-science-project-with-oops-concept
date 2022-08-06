
def data_manipulation(dataframe):
    """
        Data Modification
    """
    # Changing values inside 'new_cell' column
    dataframe['new_cell'] = dataframe['new_cell'].replace(['U', 'N', 'Y'], ['Unclear', 'No', 'Yes'])

    # Changing values inside 'refurb_new' column
    dataframe['refurb_new'] = dataframe['refurb_new'].replace(['N', 'R'], ['No', 'Yes'])

    # Changing values inside 'asl_flag' column
    dataframe['asl_flag'] = dataframe['asl_flag'].replace(['N', 'Y'], ['Not Present', 'Present'])

    return dataframe