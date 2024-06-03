import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

# Step 1: Load the 3D Image (Point Cloud)
def load_point_cloud(file_path):'C:/Users/user/Desktop/Alecado Monk'
    pcd = o3d.io.read_point_cloud(file_path)
    return pcd

# Step 2: Process the 3D Data
def extract_features(pcd):
    # Downsample the point cloud for easier processing
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    
    # Convert the point cloud to a NumPy array
    points = np.asarray(downpcd.points)
    
    # Project the points onto the XZ plane (top-down view)
    top_down_view = points[:, [0, 2]]  # Assuming y is the vertical axis
    return top_down_view

# Step 3: Generate the Floor Plan
def generate_floor_plan(top_down_view, output_file):
    plt.figure(figsize=(10, 10))
    
    # Scatter plot of the points
    plt.scatter(top_down_view[:, 0], top_down_view[:, 1], s=0.1, c='black')
    
    # Set plot title and labels
    plt.title("Floor Plan")
    plt.xlabel("X")
    plt.ylabel("Z")
    plt.axis('equal')
    
    # Save the floor plan to an image file
    plt.savefig(output_file)
    
    # Display the floor plan
    plt.show()

# Main function
def main(input_file, output_file):
    # Load the point cloud
    pcd = load_point_cloud(input_file)
    
    # Check if point cloud is empty
    if pcd.is_empty():
        print("The point cloud is empty or invalid.")
        return
    
    # Extract features to create a 2D projection
    top_down_view = extract_features(pcd)
    
    # Generate and save the floor plan
    generate_floor_plan(top_down_view, output_file)

# Example usage
input_file = "path/to/your/point_cloud.ply"  # Update with the actual file path
output_file = "floor_plan.png"
main(input_file, output_file)
