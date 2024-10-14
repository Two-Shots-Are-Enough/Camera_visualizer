import numpy as np
import json

# .npy 파일 경로
file_path = 'C:\\Users\\82108\\Yaicon\\360_extra_scenes\\flowers\\poses_bounds.npy'

# numpy 파일 불러오기
data = np.load(file_path)

# 각 변환 행렬을 저장할 리스트
pose_matrices = []
i=9040
for idx, row in enumerate(data):
    # Extract rows and re-arrange the data for the 4x4 matrix
    if i == 9040 or i == 9053 or i == 9068:
        npy_data = [
            [row[0], row[1], row[2], row[3]],
            [row[5], row[6], row[7], row[8]],
            [row[10], row[11], row[12], row[13]],
            [0.0, 0.0, 0.0, 1.0]  # Adding the last row [0, 0, 0, 1]
            ]
        pose_matrices_np = np.array(npy_data)
        output_file_npy = f'C:\\Users\\82108\\Yaicon\\CameraViewer\\inputs\\quick\\test_c2w3\\poses\\_DSC{i}.npy'
        np.save(output_file_npy, pose_matrices_np)
    i+=1

