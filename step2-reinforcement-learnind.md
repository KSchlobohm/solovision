# Reinforcement Learning with Human Feedback

Fine-tuning through reinforcement learning is the repeatable second step in the SoloVision project, where we will generate a fine-tuned Yolov8 model. This process involves the following steps:

1. Run Object Detection: Test the YOLOv8 model on a set of unseen images not used for training.
2. Review via WPF App: Use a WPF application to manually examine and confirm or reject object detections.
3. Export Feedback: Export the confirmed results from the WPF app to the YOLO format.
4. Fine-tune Again: Refine the YOLOv8 model using the human-confirmed feedback for better detection accuracy.