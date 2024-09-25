# Football Analytics Project

## Overview

This project aims to develop a **hybrid data collection platform** for automating the detection and tracking of football players, referees, and the ball in match videos. The platform leverages **computer vision models** such as YOLO and ByteTrack to provide real-time insights into match dynamics, focusing on African football leagues where resource constraints limit the adoption of advanced analytics.

The project is structured in two phases:
1. **Phase 1**: Object Detection and Tracking
2. **Phase 2**: Action Recognition (Completed Annotation)

The goal is to democratize football analytics and bridge the gap between African and European leagues by providing data-driven insights for improved decision-making.

---

## Phase 1: Object Detection and Tracking

In the first phase, we implemented **YOLO** (You Only Look Once) for object detection and **ByteTrack** for tracking key entities such as players, referees, and the ball.

### Features of Phase 1:
- **Object Detection**: Accurate detection of players, referees, and the ball using YOLOv3, YOLOv5, and YOLOv8 models.
- **Object Tracking**: Continuous tracking of objects across frames using ByteTrack, even in cases of occlusion or fast movements.
- **Real-Time Insights**: Provides data on player movements, ball possession, and other metrics.

### How to Use:

#### 1. **Download the Dataset**

The dataset, which has been annotated for football matches, can be accessed via **Roboflow**.

- Go to the [Powerfoot Computer Vision Project on Roboflow](https://universe.roboflow.com/esprit-po5qf/powerfoot) to download different versions of the YOLO model (YOLOv3, YOLOv5, and YOLOv8) along with the corresponding dataset.
- You can choose from different dataset formats compatible with various YOLO versions (e.g., COCO, Pascal VOC, YOLO format).

#### 2. **Prepare the Input Videos**

You will need input football match videos for object detection and tracking. You can use your own videos or download a sample from the provided link.

- Download a sample football match video from [Example Tunisian Input Video](https://drive.google.com/file/d/1HkajT-JujZwkUuqEkI6U6CuCwx7BfcWS/view?usp=drive_link).
- Place the video file in the `input_videos/` directory inside your project folder. If this folder doesn’t exist, create it manually.

#### 3. **Download and Load the Trained YOLO Model**

The project uses pre-trained YOLO models (YOLOv8 is recommended for the best results) for detecting players, referees, and the ball.

- Download the pre-trained YOLOv8 model from [Example YOLOv8 Dataset](https://drive.google.com/file/d/13WSdTF2D-uc_aSkuAIsdG9cetyqPvZaX/view?usp=drive_link).
- Place the downloaded model file (e.g., `.pt` or `.onnx` file) in the `models/` directory. If this folder doesn’t exist, create it manually.

#### 4. **Run the Script**

Execute the script to detect and track objects in the video. The output will consist of annotated videos and an Excel file containing player movements and other metrics.

#### 5. **Output Files**

After running the script, the system will process the video and output:

- **Annotated Videos**: The output video with bounding boxes drawn around detected objects (players, referees, ball) will be saved in the `output_videos/` folder.
- **Excel Data**: The system will generate a detailed **Excel file** containing metrics such as player positions, ball possession, and more. This file will be saved in the `output_data/` folder.

You can download a sample output video from [Example Tunisian Output Video](https://drive.google.com/file/d/1s2TuhMSsJfWNaijPv8VvBsUkiXqQ2lEj/view?usp=drive_link).

The corresponding sample Excel sheet is available [here](https://docs.google.com/spreadsheets/d/1fCGVFfCSkONewrB1hoJljajUjM2X1Ue7/edit?usp=drive_link&ouid=112565924282064934387&rtpof=true&sd=true).

---

## Phase 2: Action Recognition (Completed Annotation)

In the second phase, we focus on **Action Recognition**, aiming to detect and classify key football actions such as passes, shots, and goals.

### Goals for Phase 2:
- **Action Annotation**: We completed the manual and semi-automatic annotation of key football actions using **SuperAnnotate**.
- **Model Training**: The next step is to train advanced models like **I3D** (Inflated 3D ConvNets) and **TCNs** (Temporal Convolutional Networks) to recognize and classify actions in real-time.
- **Enhanced Real-Time Analysis**: Extend the platform's capabilities to not only track players but also recognize specific actions, leading to a deeper understanding of team strategies and player performance.

### Steps Completed:
1. **Action Annotation**: Using SuperAnnotate, we have labeled key actions such as passes, shots, and tackles from the input videos.
2. **Dataset Ready for Model Training**: The dataset is now prepared for training action recognition models in future phases.

### Future Steps:
- **Train Action Recognition Models**: Use the annotated dataset to train models like I3D and TCN for action recognition.
- **Deploy and Test**: Integrate the action recognition models into the platform for real-time match analysis.

---

## Future Directions

1. **Expand the Dataset**: Continue to collect and annotate more football match videos, especially from different African leagues, to improve model robustness.
2. **Advanced Action Recognition**: Incorporate more complex actions like tackles, dribbles, and fouls to provide deeper insights into match tactics.
3. **Real-Time Analytics Dashboard**: Develop a live dashboard to display real-time statistics on player performance, ball possession, and key match events.
4. **Collaboration and Expansion**: Partner with local leagues to expand the use of the platform across African football, adapting it to regional needs and conditions.

---

## Requirements

To run this project, you need the following dependencies:

```bash
pip install pandas matplotlib seaborn supervision
pip install ultralytics
pip install roboflow
 