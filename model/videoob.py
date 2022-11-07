import os
import subprocess
from glob import glob


video_path = glob("model/yolov5/tmp/*")[0]
weights = "yolov5s.pt"

# subprocess.run(["env/Scripts/python", "model/yolov5/detect.py", "--source", video_path, "--weights", weights])

name = video_path.split(os.sep)[-1]

results_name = f"model/yolov5/tmp/results.mp4"
#os.replace(f"model/yolov5/runs/detect/exp/{name}", results_name)

os.rmdir("model/yolov5/runs/detect/exp")

