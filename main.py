import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import open3d as o3d

# Step 1: Loading the data points
print("------Processing step 1------")
data = np.load("C:\\3D_reformatter\\3d_shape_points_data.npz")
points = data['points']
print("Loaded point cloud shape:", points.shape)

# Step 2: Deformed shape vizualisation
print("------Processing step 2------")
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Deformed 3D Object")
plt.show()

# Step 3: Detecting Deformations using PCA
print("------Processing step 3------")
pca = PCA(n_components=3)
pca.fit(points)
print("How much the shape is affected in each direction:", pca.explained_variance_ratio_)
print("Axes directions of the deformation:", pca.components_)

# Step 4: Convert points to Open3D format and apply smoothing
print("------Processing step 4------")
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
pcd = pcd.voxel_down_sample(voxel_size=0.02)

# Step 5: Visualize the corrected shape
print("------Processing step 5------")
o3d.visualization.draw_geometries([pcd], window_name="Reconstructed 3D Object")
