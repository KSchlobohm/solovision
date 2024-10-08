# Generalized Fine-tuning

Generalized Fine-tuning is the first step in the SoloVision project, where we prepare the model for reinforcement learning by generating a set of images for training. This process involves the following steps:
1. Image Generation: Use Autodistill to automatically generate a set of images for model training.
2. Object Detection: Apply the Grounded SAM (Segment Anything Model) to identify and isolate objects within the images.
3. YOLO Format Conversion: Convert the detected objects into YOLO format, preparing them for fine-tuning.
4. Fine-tuning: Fine-tune the YOLOv8 model using the generated data to enhance detection performance.

## Image Generation
