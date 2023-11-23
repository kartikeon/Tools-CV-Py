from moviepy.editor import VideoFileClip
import numpy as np
import os
# from datetime import timedelta

# i.e if video of duration 30 seconds, saves 10 frame per second = 300 frames saved in total
SAVING_FRAMES_PER_SECOND = 10


def main(vid_file):
    # load the video clip
    video_clip = VideoFileClip(vid_file)
    # make a folder by the name of the video file
    vid_name, _ = os.path.splitext(vid_file)
    filename, _ = os.path.splitext(vid_file)
    filename += "-moviepy"
    if not os.path.isdir(filename):
        os.mkdir(filename)

    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
    # if SAVING_FRAMES_PER_SECOND is set to 0, step is 1/fps, else 1/SAVING_FRAMES_PER_SECOND
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
    # iterate over each possible frame

    c = 0

    for current_duration in np.arange(0, video_clip.duration, step):
        # format the file name and save it
        # frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration))
        # c += 1

        frame_filename = os.path.join(filename, f"{vid_name}_{c}.jpg")

        c += 1

        # save the frame with the current duration
        video_clip.save_frame(frame_filename, current_duration)


if __name__ == "__main__":
    # import sys

    #   video_file = sys.argv[1]
    video_file = "traffic-light-vd-71.mp4"
    main(video_file)
