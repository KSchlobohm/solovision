# Generalized Fine-tuning

Generalized Fine-tuning is the first step in the SoloVision project, where we prepare the model for reinforcement learning by generating a set of images for training. This process involves the following steps:
1. Image Generation: Use Autodistill to automatically generate a set of images for model training.
2. Object Detection: Apply the Grounded SAM (Segment Anything Model) to identify and isolate objects within the images.
3. YOLO Format Conversion: Convert the detected objects into YOLO format, preparing them for fine-tuning.
4. Fine-tuning: Fine-tune the YOLOv8 model using the generated data to enhance detection performance.

## Image Generation

> [!NOTE]
> The following steps are designed for the VS Code experience

1. Start a new terminal and run the following to start from the project directory

    ```bash
    VIDEO_SOURCE_FILES=data/video_source_files
    ```

1. Download the sample videos

    ```bash
    wget https://media.roboflow.com/milk.zip -O $VIDEO_SOURCE_FILES/milk.zip
    ```

2. Unzip the downloaded files

    ```bash
    unzip -q $VIDEO_SOURCE_FILES/milk.zip -d $VIDEO_SOURCE_FILES
    ```

3. Use Autodistill to generate images from the videos

    > TODO: Add the command to generate images