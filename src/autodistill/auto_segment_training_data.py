# step 2 of 3: use GroundedSAM to label images from previous step
# code from https://blog.roboflow.com/autodistill/
# code from https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/how-to-auto-train-yolov8-model-with-autodistill.ipynb
# cuda getting started from - https://pytorch.org/get-started/locally/
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# pip install roboflow autodistill autodistill-grounded-sam autodistill-yolov8 autodistill-grounding-dino
# tested with CUDA 12.1 - nvidia-smi

# from autodistill_grounding_dino import GroundingDINO
# from autodistill.detection import CaptionOntology
# from autodistill_grounded_sam import GroundedSAM
# import supervision as sv
import os
import shutil
import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA not available. Please check your CUDA installation.")
    exit()