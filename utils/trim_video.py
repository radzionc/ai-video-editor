from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

def trim_video(input_path, output_path, segments):
  """
  Trims a video to include only the specified segments.

  Parameters:
  - video_path: str, path to the input mp4 video file.
  - segments: list of tuples, each tuple contains two values (start, end) specifying the
    segment in seconds.

  Returns:
  - A new mp4 video that includes only the parts specified in segments.
  """
  with VideoFileClip(input_path) as video:
    print(video.fps)
    if video.fps is None:
      video.fps = 30
    clips = [video.subclip(start, end) for start, end in segments]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path)