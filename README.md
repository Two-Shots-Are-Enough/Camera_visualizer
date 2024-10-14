### Camera viewer 이용 가이드 ###
![image](https://github.com/user-attachments/assets/cffb3cb2-dcd9-44c8-b20e-1845457754de)

https://github.com/xt4d/CameraViewer 먼저 이 사이트에 들어간 후에 시키는 대대로 가상환경을 만들고 requirements를 다운받아준다.

그 다음 아래에 있는 코드로 app.py를 이용해 Camera의 위치를 위 사진처럼 3D로 나타낼 수 있게 된다.

이를 사용하기 위해서 먼저 각 Camera의 matrix들을 npy 파일로 바꿔줘야 한다. (quick/c2w 파일의 형태를 이용하기 위함)
여기서 MipNeRF360에서 제공되는 pose_bounded.npy 파일을 각 사진 명에 따라 npy 파일로 저장하는 코드가 npy2.py 코드이다. 
이 코드에서 주소만 잘 바꿔서 사용하면 된다. 
