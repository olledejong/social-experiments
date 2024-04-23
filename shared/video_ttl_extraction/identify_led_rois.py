"""
File that holds logic which allows the user to select a ROI on the first frame
of all videos in a selected directory. These ROIs are then saved to a file with
their accompanying video filename.
"""
import os
import cv2
import pandas as pd

from shared.helper_functions import select_folder, select_or_create_folder


def draw_roi(frame, roi):
    """
    Draws a ROI in the given frame.

    :param frame:
    :param roi:
    :return:
    """
    x, y, w, h = roi
    cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)


def select_roi(frame):
    """
    Returns from the frame selected ROI.

    :param frame:
    :return:
    """
    r = cv2.selectROI("Select LED Area", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()
    return r


def select_new_roi(frame, old_roi):
    """
    Function that allows user to select a new ROI for the new video. If enter is pressed
    without a new selection, then the old roi is kept.

    :param frame:
    :param old_roi:
    :return:
    """
    r = cv2.selectROI("Select new LED Area or press enter to keep the pre-selection", frame, fromCenter=False,
                      showCrosshair=True)
    cv2.destroyAllWindows()
    if r == (0, 0, 0, 0):  # if nothing is selected
        return old_roi
    return r


def save_led_rois(video_folder, output_folder):
    """
    Loops through video files in the folder selected through Tkinter and lets the user
    select a ROI. Each video results in an entry into a dataframe, which is eventually
    saved to the filesystem.

    :param video_folder: path to the video folder
    :param output_folder: path to output folder
    :return:
    """
    videos = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi'))]
    roi = None
    data = []

    for video in videos:
        video_path = os.path.join(video_folder, video)
        # read first frame (we only need one for determining ROI)
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()

        if not ret:  # when incapable of reading frame
            print(f"Failed to read video: {video}")
            continue

        if roi is None:  # first video in dir; there's known roi yet
            roi = select_roi(frame)
            draw_roi(frame, roi)
        elif roi is not None:  # if not first selected roi; show previously selected roi
            draw_roi(frame, roi)

        # allow user to select new roi when previous one is not correct
        roi = select_new_roi(frame, roi)

        # save the data
        data.append({'Video': video, 'ROI': roi})
        cap.release()
        cv2.destroyAllWindows()

    df = pd.DataFrame(data)
    df.to_excel(os.path.join(output_folder, 'video_rois.xlsx'), index=False)


if __name__ == "__main__":
    video_folder_path = select_folder("Select folder containing the videos of the experiment you're working on")
    video_analysis_output_path = select_or_create_folder("Create or select a folder to save the LED ROI Excel file to")
    save_led_rois(video_folder_path, video_analysis_output_path)
