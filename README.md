# Football Analytics Project

## Introduction

This project focuses on developing a hybrid data collection platform to automate the detection and tracking of football players, referees, and the ball in football match videos. The system is designed to process videos, detect key elements using computer vision models, and generate detailed match analysis outputs, such as player movement, ball possession, and match events. The first phase uses YOLO for object detection and ByteTrack for tracking, providing real-time insights into match dynamics.

This project is aimed at democratizing access to football analytics, especially in African leagues, where resource constraints and manual data collection have limited the use of advanced technologies. The ultimate goal is to bridge the gap between African and European football analytics, providing more data-driven insights for better decision-making in the sport.

## Dataset Preparation and Model Training

To get started with this project, the dataset has been created using **Roboflow** for image annotation and dataset management, and **YOLO** for object detection. The dataset can be accessed and downloaded for training YOLO models. Follow the steps below to download the dataset and use the trained models.

### Step 1: Download the Dataset from Roboflow

We captured the football matches streamed on **Diwan Sports** and uploaded selected video clips to **Roboflow**, where a dataset was created. You can access and download different versions of the YOLO model directly from the [Powerfoot Computer Vision Project](https://universe.roboflow.com/esprit-po5qf/powerfoot) on Roboflow.

To download the dataset and YOLO models for training, refer to the instructions and code provided in the `training/Roboflow_Dataset.ipynb` notebook. Please note that this notebook **only provides instructions for downloading the dataset and models, not for creating a new dataset**.

Visit the [Powerfoot Computer Vision Project](https://universe.roboflow.com/esprit-po5qf/powerfoot) page to download versions of YOLO (YOLOv3, YOLOv5, and YOLOv8) along with the corresponding dataset.

### Step 2: Put Input Videos, Model, and Run

1. **Input Videos**: Download the input football match videos from [Example Tunisain_InputVideo](https://drive.google.com/file/d/1HkajT-JujZwkUuqEkI6U6CuCwx7BfcWS/view?usp=drive_link). Once downloaded, place them in the designated folder (`input_videos/`).
2. **Trained Model**: Download the trained YOLO model from [Example Yolov8_Dataset](https://drive.google.com/file/d/13WSdTF2D-uc_aSkuAIsdG9cetyqPvZaX/view?usp=drive_link) and place it in the appropriate folder (`models/`).
3. **Running the Model**: Execute the script to process the input videos. The system will automatically detect and track players, referees, and the ball. After processing, the output will include annotated videos and an Excel file containing relevant data, such as player movements and ball possession metrics.

### Step 3: Output

- The output will consist of **annotated videos** showing the detected objects (players, referees, and ball) as well as an **Excel file** containing data on player tracking, ball possession, and more.
- You can find the processed output videos in the `output_videos/` folder, or download them from [Example Tunisian_OutputVideo](https://drive.google.com/file/d/1s2TuhMSsJfWNaijPv8VvBsUkiXqQ2lEj/view?usp=drive_link).
- The Excel file with detailed match analysis can be downloaded from [Example ](https://docs.google.com/spreadsheets/d/1fCGVFfCSkONewrB1hoJljajUjM2X1Ue7/edit?usp=drive_link&ouid=112565924282064934387&rtpof=true&sd=true).

## Phase 2: Action Recognition and SuperAnnotate

To continue to the second phase of the project, we will focus on action recognition, identifying key football actions such as passes, shots, and goals.

For this, the next step involves manual annotation of actions using **SuperAnnotate**, a powerful annotation tool that supports both manual and semi-automated annotations. SuperAnnotate allows for efficient labeling of complex sports actions, reducing the time spent on manual annotation. This annotated dataset will serve as the foundation for training action recognition models in the next phase.

Using SuperAnnotate, you can:

1. Annotate actions such as passes, shots, and tackles from the input football videos.
2. Prepare the dataset for training action recognition models in future phases.

This phase will focus on refining the system for more detailed football analysis, enhancing the platform's capabilities for real-time player and match analysis.

# Requirements

To run the Football Analytics Project, ensure you have the following dependencies installed:

## Python Libraries

- **Python**: Version 3.x
- **YOLO**: YOLOv5 or YOLOv8
- **Roboflow API**
- **OpenCV**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **SuperAnnotate**

## Installation

You can install the necessary libraries using pip. Run the following commands:

```bash
pip install pandas matplotlib seaborn supervision
pip install ultralytics
pip install roboflow

