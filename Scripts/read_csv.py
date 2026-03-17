import mediapipe as mp
import cv2
import os
import glob

input_folder = "Signs/Proccessing_Batch_Signs"
output_folder = "Data/Wrist_Cords"
os.makedirs(output_folder, exist_ok=True)

def get_cord():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        smooth_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    video_files = glob.glob(os.path.join(input_folder, "*.mp4"))
    if not video_files:
        print("No MP4 files found.")
        return

    wrist_l = 16  # Coord no# in mp documentation
    wrist_r = 15
    visibility_threshold = 0.02
    sample_interval = 0.01  # seconds

    header = "frame_idx,l_x,l_y,r_x,r_y\n"

    for video_path in video_files:
        base = os.path.splitext(os.path.basename(video_path))[0]
        csv_path = os.path.join(output_folder, f"wrist_cord_{base}.csv")

        with open(csv_path, "w") as file:
            file.write(header)
            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                print(f"Error opening {video_path}")
                continue

            fps = cap.get(cv2.CAP_PROP_FPS)
            step = max(1, int(sample_interval * fps))
            frame_idx = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = pose.process(rgb)

                if frame_idx % step == 0 and results.pose_landmarks:
                    lm = results.pose_landmarks.landmark

                    l_xy = (
                        [lm[wrist_l].x, lm[wrist_l].y]
                        if lm[wrist_l].visibility > visibility_threshold
                        else None
                    )
                    r_xy = (
                        [lm[wrist_r].x, lm[wrist_r].y]
                        if lm[wrist_r].visibility > visibility_threshold
                        else None
                    )

                    if l_xy is not None and r_xy is not None:
                        file.write(",".join(map(str, [frame_idx] + l_xy + r_xy)) + "\n")

                frame_idx += 1
                cv2.imshow("MediaPipe Pose Tracking", frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break

            cap.release()

    cv2.destroyAllWindows()