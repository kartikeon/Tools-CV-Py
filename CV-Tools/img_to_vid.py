from moviepy.editor import VideoFileClip
from moviepy.editor import ImageSequenceClip
import glob

fps = 20

image_paths = glob.glob('frames/*.jpg')
image_paths.sort()
print(image_paths[:5])
clip = ImageSequenceClip(image_paths, fps=fps)
clip.write_videofile('day_seq1.mp4', fps=fps)
print('DONE')
