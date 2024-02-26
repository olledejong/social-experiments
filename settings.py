"""
This file holds all settings for the project, and can be imported and used in every script/notebook
"""
general = {
    "lab": "Kas_Lab",
    "experimenter": "Vasilis Siozos & Mirthe Ronde",
    "institution": "University of Groningen"
}

paths = {
 "edf_folder": "",
 "coordinate_data_folder": "",
 "nwb_files_folder": "",
 "plots_folder": "",
 "epochs_folder": "",
 "subject_metadata": "",
 "metadata": "",
 "psd_data_folder": "",
 "video_folder": ""
}

filtering = {
    "lcut": 0.5,
    "hcut": 200,
    "art": None,
    "low_val": 0.006,
    "high_val": 0.013,
    "electrode_info": {
        "EEG 2": ["OFC_R", 2.7, -0.75, 2.4, "depth"],
        "EEG 3": ["OFC_L", 2.7, 0.75, 2.4, "depth"],
        "EEG 4": ["CG", 1.3, 0.7, 2, "depth"],
        "EEG 13": ["STR_R", 1.3, -1.5, 3, "depth"],
        "EEG 6": ["S1_L", -0.5, 3, 0, "skull"],
        "EEG 11": ["S1_R", -0.5, -3, 0, "skull"],
        "EEG 12": ["V1_R", -4, -2.5, 0, "skull"],
        "EEG 7": ["EMG_L", 0, 0, 0, "emg"],
        "EEG 10": ["EMG_R", 0, 0, 0, "emg"]
    }
}
