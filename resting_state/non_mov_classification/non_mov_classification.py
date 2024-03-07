"""
This file can be used to extract clips from a experiment recording based on the metadata
of the epoch file that is read. This epoch file namely holds a start and end frame time-point
for each epoch.
"""
import os
import cv2
import pandas as pd
from tkinter import *
from tkinter.simpledialog import askstring

from settings import paths


def label_video(input_video, epoch_n, subject_id):
    cap = cv2.VideoCapture(input_video)  # open the video

    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return

    # make tk window and hide it
    root = Tk()
    root.withdraw()

    user_input = ''
    # loop and show clip as long as the user hasn't provided a behaviour label for it
    while True:
        ret, frame = cap.read()

        # if user input provided, break the loop
        if user_input:
            break
        # show video clip
        elif ret:
            cv2.imshow(f'Subject {subject_id}, epoch {epoch_n}', frame)
            if cv2.waitKey(25) & 0xFF == 27:  # Press Esc to exit
                break
        # set position back to frame 0 for when it possibly needs to be played again
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            user_input = askstring("Input", "Enter behaviour:")

    # lose and destroy windows
    cap.release()
    cv2.destroyAllWindows()
    root.quit()

    return user_input


def get_behaviour(subject_clips, subject_id):
    behaviours = {}

    # loop through all subject's clips
    for clip_filename in subject_clips:
        path_to_clip = os.path.join(paths['video_folder'], 'clips', clip_filename)
        epoch_n = path_to_clip.split("_")[-1].split(".")[0]

        # save this clip's behaviour label
        behaviours[epoch_n] = label_video(path_to_clip, epoch_n, subject_id)

    # return behaviour for all epochs / clips
    return behaviours


def main():

    # load some info about the subject
    metadata_df = pd.read_excel(paths["metadata"])

    # for i, subject_id in enumerate(metadata_df['mouseId']):  # TODO change back
    for i, subject_id in enumerate([39508]):
        subject_meta = metadata_df[metadata_df['mouseId'] == int(subject_id)]

        # get the filenames of this subject's clips
        clips = os.listdir(os.path.join(paths['video_folder'], 'clips'))
        subject_clips = [clip for clip in clips if str(subject_id) in clip]
        print(subject_clips)

        behaviours = get_behaviour(subject_clips, subject_id)
        print(behaviours)


if __name__ == '__main__':
    main()