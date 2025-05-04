import runpod
import subprocess
import os

def handler(event):
    # event["input"]["file"] should be a path or base64 string, depending on your setup
    input_path = event["input"]["file"]
    output_path = "/tmp/output.mp4"

    # Example FFmpeg command (adjust as needed)
    cmd = [
        "ffmpeg", "-i", input_path, "-vf", "scale=1280:720", output_path
    ]
    subprocess.run(cmd, check=True)

    # Return the path to the processed file
    return {"result": output_path}

runpod.serverless.start({"handler": handler})
