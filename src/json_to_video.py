import numpy as np
import cv2
import os
import json

import sys


def main(video_path, json_path):
    json_data = load_json(json_path)

    all_skeletons = []
    for frame in json_data:
        all_skeletons.append(make_skeleton(frame['people']))

    cap = cv2.VideoCapture(video_path)
    count = -1
    # ret, frame = cap.read()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        count += 1
        draw_skeletons(frame, all_skeletons[count])
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def make_skeleton(people_data):
    skeleton_data = []
    for people in people_data:
        lines = []
        if len(people['pose_keypoints_2d']) == 0:
            return skeleton_data
        for i in range(int(len(people['pose_keypoints_2d']) / 3) - 1):
            p1 = (int(people['pose_keypoints_2d'][i * 3]), int(people['pose_keypoints_2d'][i * 3 + 1]))
            p2 = (int(people['pose_keypoints_2d'][i * 3 + 3]), int(people['pose_keypoints_2d'][i * 3 + 4]))
            lines.append([p1, p2])
        skeleton_data.append(lines)
    return skeleton_data


def draw_skeletons(image, skeletons):
    thickness = 2
    line_type = 8
    pcount = 0
    for person in skeletons:
        annotation_flag = False
        color = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (0, 0, 0)]
        for line in person:
            if not (check_tuple(line[0]) or check_tuple(line[1])):
                cv2.line(image, line[0], line[1], color[pcount % 4], thickness, line_type)
                if not annotation_flag:
                    cv2.putText(image, "Person: {0}".format(pcount), line[0], cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                    annotation_flag = True
            else:
                continue
        pcount += 1


def load_json(path):
    json_data = []
    for file in os.listdir(path):
        with open(os.path.join(path, file), "r") as f:
            json_data.append(json.load((f)))
    return json_data


def check_tuple(tuple):
    # Check if tuple is 0,0
    x1 = tuple[0]
    x2 = tuple[1]
    return x1 == 0 and x2 == 0


if __name__ == "__main__":
    video_path = os.path.abspath("videos\\running\\running\\9zkapadQwHk\\clip_82_85.mp4")
    json_path = os.path.abspath("videos\\running\\running\\9zkapadQwHk\\clip_83_86")
    main(video_path, json_path)
