# step 2 of 3: use GroundedSAM to label images from previous step
# code from https://blog.roboflow.com/autodistill/
# code from https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/how-to-auto-train-yolov8-model-with-autodistill.ipynb
# cuda getting started from - https://pytorch.org/get-started/locally/
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# pip install scikit-learn roboflow autodistill autodistill-grounded-sam autodistill-yolov8 autodistill-grounding-dino
# tested with CUDA 12.1 - nvidia-smi

from autodistill_grounding_dino import GroundingDINO
from autodistill.detection import CaptionOntology
from autodistill_grounded_sam import GroundedSAM
import supervision as sv
import os
import shutil
import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA not available. Please check your CUDA installation.")
    exit()


IMAGE_DIR_PATH = "./data/input_from_video"
YOLO_DATASET_DIR_PATH = "./data/yolo_dataset"

ontology = CaptionOntology({
    "milk bottle": "bottle",
    "blue cap": "cap"
})

base_model = GroundingDINO(ontology=ontology)

if os.path.exists(YOLO_DATASET_DIR_PATH):
    shutil.rmtree(YOLO_DATASET_DIR_PATH)

# Automatically label images in the input folder using the base model and save the labeled dataset to the output folder.
# This step is crucial as it converts raw images into a labeled dataset that can be used for training the YOLO model.
# The base model uses the provided ontology to generate accurate labels, making this process efficient and reducing manual labeling effort.
dataset = base_model.label(
    input_folder=IMAGE_DIR_PATH,
    extension=".png",
    output_folder=YOLO_DATASET_DIR_PATH)


ANNOTATIONS_DIRECTORY_PATH = f"{YOLO_DATASET_DIR_PATH}/train/labels"
IMAGES_DIRECTORY_PATH = f"{YOLO_DATASET_DIR_PATH}/train/images"
DATA_YAML_PATH = f"{YOLO_DATASET_DIR_PATH}/data.yaml"

# Convert the labeled YOLO dataset into a DetectionDataset object.
# This step is crucial for preparing the dataset in a structured format that is compatible with YOLO training.
# It ensures that the images and their corresponding annotations are correctly organized.
# By automating the conversion process, it reduces manual effort and potential errors in dataset preparation.
# Ensures that the dataset adheres to the expected format, which is important for the training process to run smoothly.
dataset = sv.DetectionDataset.from_yolo(
    images_directory_path=IMAGES_DIRECTORY_PATH,
    annotations_directory_path=ANNOTATIONS_DIRECTORY_PATH,
    data_yaml_path=DATA_YAML_PATH)