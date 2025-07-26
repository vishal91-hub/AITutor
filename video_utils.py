import subprocess
import uuid
import os

def merge_audio_with_avatar(audio_path, avatar_path, output_path):
    command = [
        "ffmpeg", "-y",
        "-i", avatar_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        output_path
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output_path