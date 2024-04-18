"""
Settings specific to the analysis of the 3-chamber experiments
"""

resample_freq = 500  # set to desired sampling frequency or to None if you do not wish to down-sample the EEG data

# dictionary holding the subject id that belongs to the batch-cage combinations
subject_id_dict = {
    'batch1_cage1': 78211, 'batch2_cage1': 79593, 'batch5_cage1': 81167, 'batch4_cage1': 80620, 'batch5b_cage1': 81217, 'batch6_cage1': 39489,
    'batch1_cage2': 78233, 'batch2_cage2': 79592, 'batch5_cage2': 81175, 'batch4_cage2': 80625, 'batch5b_cage2': 81218, 'batch6_cage2': 39508,
    'batch1_cage3': 78227, 'batch2_cage3': 79604, 'batch5_cage3': 81207, 'batch4_cage3': 80630,
    'batch1_cage4': 78244, 'batch2_cage4': 79602, 'batch5_cage4': 81193,
}

min_interaction_duration = 1.0  # minimum duration of the interaction between mouse and cup (in seconds)

paths_3c_sociability = {
    "metadata": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_sociability/output/3c_sociability_metadata.xlsx",
    "edf_folder": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_sociability/input/edf_files",
    "behaviour_data_dir": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_sociability/input/behavioural_data",
    "plots_folder": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_sociability/output/plots",
    "recordings_folder": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_sociability/input/videos",
    "video_analysis_output": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_sociability/output/videos",
    "nwb_files_folder": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_sociability/output/nwb"
}

paths_3c_preference = {
    "metadata": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_preference/output/3c_preference_metadata.xlsx",
    "edf_folder": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_preference/input/edf_files",
    "behaviour_data_dir": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_preference/input/behavioural_data",
    "plots_folder": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_preference/output/plots",
    "nwb_files_folder": "/Users/olledejong/Documents/MSc_Biology/ResearchProject2/rp2_data/3C_preference/output/nwb"
}

