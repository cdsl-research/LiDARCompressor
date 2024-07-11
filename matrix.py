import numpy as np
import matplotlib.pyplot as plt
import re

def extract_lidar_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    pattern = re.compile(r'theta:\s+([\d\.]+)\s+Dist:\s+([\d\.]+)\s+Q:\s+(\d+)')

    extracted_data = []

    for line in data:
        match = pattern.search(line)
        if match:
            theta = float(match.group(1))
            dist = float(match.group(2))
            q = int(match.group(3))
            extracted_data.append((theta, dist, q))

    return extracted_data

def polar_to_cartesian(data):
    cartesian_coords = []
    for point in data:
        theta_rad = np.deg2rad(point[0])
        x = point[1] * np.cos(theta_rad)
        y = point[1] * np.sin(theta_rad)
        cartesian_coords.append((x, y))
    return cartesian_coords

def data_to_matrix(cartesian_coords, grid_size=10):
    max_x = int(max([abs(x) for x, y in cartesian_coords]))
    max_y = int(max([abs(y) for x, y in cartesian_coords]))
    matrix_size = max(max_x, max_y) * 2 // grid_size + 1

    matrix = np.zeros((matrix_size, matrix_size))

    for x, y in cartesian_coords:
        i = int((x + max_x) // grid_size)
        j = int((y + max_y) // grid_size)
        matrix[i, j] = 1

    return matrix

def plot_matrix(matrix):
    plt.imshow(matrix, cmap="Greys", origin="lower")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("LiDAR Data Plot")
    plt.show()

def get_obstacle_indices(matrix):
    return np.argwhere(matrix == 1)

def save_matrix_to_txt(matrix, file_path):
    np.savetxt(file_path, matrix, fmt='%d')

def save_indices_to_txt(indices, file_path):
    np.savetxt(file_path, indices, fmt='%d')

def save_cartesian_coords_to_txt(cartesian_coords, file_path):
    with open(file_path, 'w') as file:
        for x, y in cartesian_coords:
            file.write(f"{x} {y}\n")

file_path = '/home/masa/teian_matrix/plottest.txt'
output_cartesian_coords_file_path = '/home/masa/teian_matrix/cartesian_coords.txt'

lidar_data = extract_lidar_data(file_path)
cartesian_coords = polar_to_cartesian(lidar_data)
matrix = data_to_matrix(cartesian_coords)

plot_matrix(matrix)
obstacle_indices = get_obstacle_indices(matrix)
print("Obstacle Indices:", obstacle_indices)

output_matrix_file_path = '/home/masa/teian_matrix/matrix/room_matrix.txt'
output_indices_file_path = '/home/masa/teian_matrix/indices/room_indices.txt'
output_rle_file_path = '/home/masa/teian_matrix/rle/room_rle.txt'

save_matrix_to_txt(matrix, output_matrix_file_path)
save_indices_to_txt(obstacle_indices, output_indices_file_path)
save_cartesian_coords_to_txt(cartesian_coords, output_cartesian_coords_file_path)

print(f"Matrix saved to {output_matrix_file_path}")
print(f"Obstacle Indices saved to {output_indices_file_path}")
print(f"Cartesian Coordinates saved to {output_cartesian_coords_file_path}")
