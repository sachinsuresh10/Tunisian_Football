import pandas as pd
from utils import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator

def main():
    # Read Video (Adjust video path as needed)
    print("Reading video...")
    video_path = 'input_videos/DS1.mp4'
    video_frames, frame_rate = read_video(video_path)
    print(f"Number of video frames read: {len(video_frames)}")
    print(f"Frame rate of the video: {frame_rate}")

    # Initialize Tracker
    print("Initializing tracker...")
    tracker = Tracker('models/dsv8.pt')

    # Get tracks from stub or perform tracking
    print("Getting tracks...")
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=False,  # Ensure to process fresh frames
                                       stub_path='stubs/track_stubs.pkl')
    print(f"Tracks obtained: {tracks.keys()}")
    print(f"Sample track data (first frame): {tracks['BALL'][0] if 'BALL' in tracks else 'No ball track data'}")

    # Get object positions 
    tracker.add_position_to_tracks(tracks)

    # Camera movement estimator
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames,
                                                                                read_from_stub=True,
                                                                                stub_path='stubs/camera_movement_stub.pkl')
    print(f"Number of camera movement frames: {len(camera_movement_per_frame)}")

    if len(camera_movement_per_frame) < len(video_frames):
        print("Warning: Camera movement frames are less than video frames.")

    # Ensure we don't go out of range
    min_length = min(len(video_frames), len(camera_movement_per_frame))

    # Adjust positions with camera movement
    print("Adjusting positions with camera movement...")
    for frame_num in range(len(video_frames)):
        if frame_num >= len(camera_movement_per_frame):
            print(f"Warning: Frame number {frame_num} is out of range for camera movement data.")
            break  # Skip processing if camera movement data is unavailable
        
        camera_movement = camera_movement_per_frame[frame_num]
        for object_type, object_tracks in tracks.items():
            # Check if frame_num is within bounds for the current object_tracks
            if frame_num in object_tracks:
                for track_id, track_info in object_tracks[frame_num].items():
                    position = track_info['position']
                    position_adjusted = (position[0] - camera_movement[0], position[1] - camera_movement[1])
                    tracks[object_type][frame_num][track_id]['position_adjusted'] = position_adjusted

    # Interpolate Ball Positions
    if "BALL" in tracks:
        print("Interpolating ball positions...")
        tracks["BALL"] = tracker.interpolate_ball_positions(tracks["BALL"])
        print(f"Interpolated ball positions (first frame): {tracks['BALL'][0]}")

    # Assign Player Teams
    print("Assigning player teams...")
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], 
                                    tracks['persons'][0])

    for frame_num, player_track in enumerate(tracks['persons']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                  track['bbox'],
                                                  player_id)
            tracks['persons'][frame_num][player_id]['team'] = team 
            tracks['persons'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    # Assign Ball Acquisition
    player_assigner = PlayerBallAssigner()
    team_ball_control = []
    for frame_num, player_track in enumerate(tracks['persons']):
        if 'BALL' in tracks and frame_num < len(tracks['BALL']):
            ball_bbox = tracks['BALL'][frame_num][1]['bbox']
            assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

            if assigned_player != -1:
                tracks['persons'][frame_num][assigned_player]['has_BALL'] = True
                team_ball_control.append(tracks['persons'][frame_num][assigned_player]['team'])
            else:
                # Continue with the previous team if no player is assigned
                if team_ball_control:
                    team_ball_control.append(team_ball_control[-1])
                else:
                    team_ball_control.append(None)
        else:
            # Continue with the previous team if no ball data is available
            if team_ball_control:
                team_ball_control.append(team_ball_control[-1])
            else:
                team_ball_control.append(None)
                
    team_ball_control = np.array(team_ball_control)

    # Gather tracking data for the Excel sheet
    print("Gathering tracking data for Excel sheet...")
    tracking_data = []
    for second in range(0, len(video_frames), int(frame_rate)):
        frame_data = {"Time (s)": second // frame_rate}
        for player_id, player_info in tracks['persons'][second].items():
            # Check for 'position_adjusted'; fall back to original position if not available
            position = player_info.get('position_adjusted', player_info.get('position', None))
            frame_data[f"Player {player_id} Position"] = position
            frame_data[f"Player {player_id} Team"] = player_info['team']
            frame_data[f"Player {player_id} Has Ball"] = player_info.get('has_BALL', False)
        if "BALL" in tracks and second < len(tracks['BALL']):
            frame_data["Ball Position"] = tracks["BALL"][second][1].get('position_adjusted', tracks["BALL"][second][1].get('position', None))
        else:
            frame_data["Ball Position"] = None
        tracking_data.append(frame_data)

    df = pd.DataFrame(tracking_data)
    df.to_excel('output_videos/TrackingData.xlsx', index=False)
    print("Tracking data saved to Excel file.")

    # Draw annotations on video frames
    print("Drawing annotations on video frames...")
    output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)
    print(f"Number of output video frames: {len(output_video_frames)}")

    # Draw Camera movement
    print("Drawing camera movement...")
    # Ensure to draw camera movement only for frames that are within the available data range
    min_length = min(len(video_frames), len(camera_movement_per_frame))
    output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frame[:min_length])

    # Save annotated video (Adjust output path as needed)
    print("Saving annotated video...")
    save_video(output_video_frames, 'output_videos/FinalOutput.avi', frame_rate)
    print("Video saved successfully.")

if __name__ == '__main__':
    main()
