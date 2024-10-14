### Camera viewer 이용 가이드 ###
![image](https://github.com/user-attachments/assets/cffb3cb2-dcd9-44c8-b20e-1845457754de)

https://github.com/xt4d/CameraViewer 먼저 이 사이트에 들어간 후에 시키는 대대로 가상환경을 만들고 requirements를 다운받아준다.

그 다음 아래에 있는 코드로 app.py를 이용해 Camera의 위치를 위 사진처럼 3D로 나타낼 수 있게 된다.

이를 사용하기 위해서 먼저 각 Camera의 matrix들을 npy 파일로 바꿔줘야 한다. (quick/c2w 파일의 형태를 이용하기 위함)
여기서 MipNeRF360에서 제공되는 pose_bounded.npy 파일을 각 사진 명에 따라 npy 파일로 저장하는 코드가 npy2.py 코드이다. 
저장 위치는 inputs/quick/poses
이 코드에서 주소만 잘 바꿔서 사용하면 된다. 
npy는 원하는 idx만 설정해서 뽑을 수 있도록 만든건데, training view랑 test 만 따로 Camera pose 얻고 싶을 때 사용하면 된다.

그리고 training view를 정한 후에 inputs/quick/images에 training view 해당하는 image만 넣으면 코드를 돌릴 때 해당하는 idx의 camera만 빨간색으로 표현된다.

갑자기 오류나서 파일이 안돌아가는데 git clone 한거랑 npy 파일 같은 파일 안에 넣고 돌리시면 됩니다. 자세한건 만나서..
# example 사진 
이런 식으로 폴더 구성하시면 됩니다. 컴퓨터 환경에 따라 주소는 바꿔줘야 함
![image](https://github.com/user-attachments/assets/c0152700-f842-46d7-9ac4-98e7ec9e0108)
여기서 예를 들면 pose는 7개로 training view랑 test view 선정된 것만 뽑은것
이미지에는 training view에 해당하는 사진만 들어가 있음 이렇게 되면 아래와 같은 결과가 나오는 것
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/10b29e5a-cf64-4614-a62c-0e052d796e74/507c0844-a31f-4f18-81bc-2292a8c67f00/image.png)
