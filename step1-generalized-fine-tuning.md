# Generalized Fine-tuning

Generalized Fine-tuning is the first step in the SoloVision project, where we will generate a fine-tuned Yolov8 model. This process involves the following steps:

1. Image Generation: Use Autodistill to automatically generate a set of images for model training.
2. Object Detection: Apply the Grounded SAM (Segment Anything Model) to identify and isolate objects within the images.
3. YOLO Format Conversion: Convert the detected objects into YOLO format, preparing them for fine-tuning.
4. Fine-tuning: Fine-tune the YOLOv8 model using the generated data to enhance detection performance.

## Image Generation
Before we can fine-tune the YOLOv8 model, we need to generate a set of images for training. We will use Autodistill to automatically generate images from sample videos.

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

3. Create a Virtual Environment at the root of the project

    ```bash
    python -m venv .venv
    ```

4. Activate the environment

    ```bash
    source ./.venv/bin/activate
    ```


5. Install the required packages

    ```bash
    pip install -r requirements.txt
    ```

6. Use Autodistill to generate images from the videos

    ```bash
    python src/autodistill/video_to_images.py
    ```

7. Use the Grounded SAM to detect objects in the images

    ```bash
    python src/autodistill/auto_segment_training_data.py
    ```

8. Use the dataset we just generated to fine-tune the YOLOv8 model

    ```bash
    python src/autodistill/finetune_yolo.py
    ```