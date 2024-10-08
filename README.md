# SoloVision
SoloVision is an image fine-tuning project that leverages human feedback for reinforcement learning and model refinement. Using a combination of automated tools and personalized user input, SoloVision enhances object detection performance by iteratively fine-tuning models based on real-world feedback.

## Project Scope
SoloVision is a non-production research project, created as part of a personal learning journey. The aim is to explore the concepts of image fine-tuning, reinforcement learning, and human-in-the-loop AI development. This project is for educational purposes only and serves as a platform to experiment with various tools and techniques to deepen understanding in these areas.

Getting Started
To get started with SoloVision, follow the instructions below to set up your development environment and prepare for both the Generalized Fine-tuning and Reinforcement Learning processes.

## Project Overview

### Generalized Fine-tuning
1. Image Generation: Use Autodistill to automatically generate a set of images for model training.
2. Object Detection: Apply the Grounded SAM (Segment Anything Model) to identify and isolate objects within the images.
3. YOLO Format Conversion: Convert the detected objects into YOLO format, preparing them for fine-tuning.
4. Fine-tuning: Fine-tune the YOLOv8 model using the generated data to enhance detection performance.

### Reinforcement Learning with Human Feedback
1. Run Object Detection: Test the YOLOv8 model on a set of unseen images not used for training.
2. Review via WPF App: Use a WPF application to manually examine and confirm or reject object detections.
3. Export Feedback: Export the confirmed results from the WPF app to the YOLO format.
4. Fine-tune Again: Refine the YOLOv8 model using the human-confirmed feedback for better detection accuracy.
   
### Iterative Process
- Repeat Reinforcement Learning with Human Feedback as needed to continuously improve object detection accuracy based on human feedback.
