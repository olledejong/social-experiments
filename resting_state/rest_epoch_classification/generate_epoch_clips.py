"""
This file can be used to extract clips from a experiment recording based on the metadata
of the epoch file that is read. This epoch file namely holds a start and end frame timepoint
for each epoch.
"""
import os
import cv2
import mne
import sys
import numpy as np
import pandas as pd
from settings import paths, cluster_annotations


def generate_clips(subject_epochs, subject_meta, subject_id):
    print(f'Generating clips for subject {subject_id}...')

    # first we need the start and end timepoints of each epoch (in frames)
    epoch_tps_frames = np.array(subject_epochs.metadata["epochs_start_end_frames"])
    split_tps_frames = np.array([start_end.split('-') for start_end in epoch_tps_frames])

    epoch_indexes = np.array(subject_epochs.metadata.index)

    # now we need to load the video
    video_filename = subject_meta['movie_filename'].iloc[0]
    path_to_video_file = os.path.join(paths['recordings_folder'], video_filename)

    # open the video and check if it is actually opened
    cap = cv2.VideoCapture(path_to_video_file)
    if not cap.isOpened():
        sys.exit("Error: Could not open the video file.")

    frame_width, frame_height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps, frame_count = cap.get(cv2.CAP_PROP_FPS), int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i, (start_frame, end_frame) in enumerate(split_tps_frames):
        start_frame, end_frame = int(np.floor(float(start_frame))), int(np.floor(float(end_frame)))

        if start_frame >= frame_count:
            print(f"Error: Start time for clip {i+1} is beyond video length.")
            continue

        if end_frame >= frame_count:
            print(f"Warning: End time for clip {i+1} is beyond video length. Using last frame instead.")
            end_frame = frame_count - 1

        output_file = os.path.join(
            paths['video_analysis_output'], 'clips',
            f"{subject_id}_resting_cluster_epoch_{epoch_indexes[i]}.mp4"
        )
        out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                if cap.get(cv2.CAP_PROP_POS_FRAMES) == end_frame:
                    break
            else:
                break

        out.release()
        print('\r', f"{round((i+1) / len(split_tps_frames) * 100)}% of clips for subject done..", end='')

    cap.release()
    cv2.destroyAllWindows()


def main():
    metadata_df = pd.read_excel(paths["metadata"])

    for i, subject_id in enumerate(metadata_df['mouseId']):

        subject_meta = metadata_df[metadata_df['mouseId'] == int(subject_id)]

        # load this subject's epochs (which include the cluster annotations in the metadata)
        subject_epochs_path = os.path.join(paths['epochs_folder'], f'filtered_epochs_w_clusters_{subject_id}-epo.fif')

        if not os.path.exists(subject_epochs_path):
            print(f"No epoch file with clustering annotation found for subject {subject_id}, proceeding..")
            continue

        subject_epochs = mne.read_epochs(subject_epochs_path)

        all_clips = os.listdir(os.path.join(paths['video_analysis_output'], 'clips'))
        if any(str(subject_id) in file for file in all_clips):
            print(f"Clips have probably already been generated for subject {subject_id}, proceeding..")
            continue

        # get the resting-state cluster epochs
        resting_state_cluster_id = cluster_annotations[int(subject_id)]['rest']
        resting_state_epochs = subject_epochs[subject_epochs.metadata['cluster'] == resting_state_cluster_id]

        # generate the movie clips
        generate_clips(resting_state_epochs, subject_meta, subject_id)

        print(f"Subject {subject_id} complete. Total progress: {round( (i+1) / len(metadata_df['mouseId']) * 100)}%.")
    print("Done, bye.")


if __name__ == '__main__':
    main()
