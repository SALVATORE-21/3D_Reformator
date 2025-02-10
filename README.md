3D Shape Reconstruction from Point Cloud Data

📌 Project Overview  
This project focuses on analyzing and reconstructing a machine component that has undergone deformations due to extended usage. 
A sensor captured the deformed component’s surface as a collection of 3D points, stored in `"XXXX.npz"`. The goal is to:  
- Determine the original shape of the component.  
- Identify and analyze the deformations present.  
- Reconstruct the original shape by correcting the deformations.

📂 Dataset  
- File: `XXXXX.npz`  
- Format: NumPy `.npz` storing 3D point cloud data  
- Structure: Each point is represented in (x, y, z) coordinates  

🛠 Libraries Used  
- NumPy – Loading `.npz` files and numerical computations  
- Matplotlib – Plotting and visualizing 3D data  
- mpl_toolkits.mplot3d – Helper for 3D plotting  
- scikit-learn (PCA) – Identifying major deformation axes  
- Open3D – Handling and processing 3D point clouds  

## 📊 Expected Outcomes  
- Clear visualization of deformed vs. reconstructed shape.  
- Identification of major deformation axes and their impact.  
- A near-original shape reconstructed from the deformed data.  
