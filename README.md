# Camera Viewer Guide


This guide explains how to set up and use the [Camera Viewer](https://github.com/xt4d/CameraViewer) to visualize camera positions in 3D.
<img src="https://github.com/user-attachments/assets/cffb3cb2-dcd9-44c8-b20e-1845457754de" alt="Example Viewer Image" style="width:60%; height:auto;">


### 1. **Setup**

Run the following commands in your terminal to set up the environment and install dependencies:

```bash
# Clone the repository
git clone https://github.com/xt4d/CameraViewer.git
cd CameraViewer

# Create a virtual environment and activate it
python -m venv env
source env/bin/activate  # For macOS/Linux
# On Windows: .\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### 2. **Running the Viewer**

After setting up, you can launch the viewer using:

```bash
python app.py
```
---

### 3. **Preparing Camera Poses (`npy` Files)**

1. **Convert Camera Matrices to `.npy`**  
   To use the viewer, camera poses must be converted into `.npy` files compatible with the `quick/c2w` format. Use the `npy2.py` script for this.

   ```bash
   # Run the conversion script (adjust paths as needed)
   python npy2.py
   ```

   - The script uses the `pose_bounded.npy` file provided by MipNeRF360.  
   - It saves `.npy` files named after each image into the directory `inputs/quick/poses`.  
   - You can filter poses by index to generate training or test views selectively.

---

### 4. **Set Up Input Data for Viewer**

1. **Training and Test Views**  
   - Place camera poses for training and test views into `inputs/quick/poses`.  
   - Add training view images into `inputs/quick/images`.  

2. **Visualization**  
   - When running the viewer, only the cameras corresponding to training images will be highlighted in **red**.

3. Example folder structure:  
   ```
   inputs/
    └── quick/
        ├── images/
        │   ├── _DSC9203.JPG
        │   ├── _DSC9205.JPG
        │   └── _DSC9208.JPG
        ├── poses/
            ├── _DSC9094.npy
            ├── _DSC9144.npy
            ├── _DSC9198.npy
            ├── _DSC9203.npy
            ├── _DSC9205.npy
            ├── _DSC9208.npy
            └── _DSC9211.npy

   ```
---

### Troubleshooting

If the script fails, ensure:
- `npy` files are placed in the same directory as the cloned repository.
- Adjust paths in `npy2.py` as needed.
