import os
from moviepy.editor import VideoFileClip

# Set the path to the ffmpeg executable
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/local/bin/ffmpeg"

# config
input_ext = '.mov'
output_ext = '.gif'
input_path = os.getcwd() + '/input/'
output_path = os.getcwd() + '/output/'


def convert_video_to_gif(input_file, output_file, start_time=0, end_time=None, fps=10):
    clip = VideoFileClip(input_file)

    if end_time:
        clip = clip.subclip(start_time, end_time)
    clip.write_gif(output_file, fps=fps)

def convert_all_videos(input_path, output_path, input_ext, output_ext, start_time=0, end_time=None, fps=10):
    os.makedirs(output_path, exist_ok=True)

    for filename in os.listdir(input_path):
        if filename.endswith(input_ext):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, os.path.splitext(filename)[0] + output_ext)
            print(f'Converting {input_file} to {output_file}')
            convert_video_to_gif(input_file, output_file, start_time, end_time, fps)


'''
input_file: 입력 비디오 파일의 경로.
output_file: 출력 GIF 파일을 저장할 경로.
start_time: GIF로 변환할 비디오의 시작 시간(초 단위, 기본값 0) 
end_time: GIF로 변환할 비디오의 끝 시간(초 단위, 기본값은 None으로, 비디오의 끝까지 변환)
fps (int, optional): GIF의 프레임 속도(초당 프레임 수, 기본값은 10)
'''
convert_all_videos(input_path, output_path, input_ext, output_ext, start_time=0, end_time=None, fps=10)
