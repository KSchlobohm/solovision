# Prerequisites
Before starting, ensure you have the following:

- Python 3.8+, PyTorch, YOLOv8, Autodistill, and Grounded SAM installed
- A Windows environment for the WPF application
- Git for cloning the repository and additional dependencies listed in `requirements.txt`

## Installation Steps
1. Clone the Repository
    ```bash
    git clone https://github.com/yourusername/solovision.git
    cd solovision
    ```

2. Create a Virtual Environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install Python Dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Set Up YOLOv8 and Other Models
    - Install YOLOv8:
        ```bash
        pip install ultralytics
        ```
    - Install Autodistill and Grounded SAM as per their documentation.

5. Prepare the WPF Application
    - Navigate to the `WPFApp` directory.
    - Open the solution file in Visual Studio.
    - Build the project to ensure all dependencies are restored.