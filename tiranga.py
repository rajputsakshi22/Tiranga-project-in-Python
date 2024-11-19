import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

# Create the flag's rectangles
a = patch.Rectangle((0, 1), width=12, height=2, facecolor='green', edgecolor='grey')
b = patch.Rectangle((0, 3), width=12, height=2, facecolor='white', edgecolor='grey')
c = patch.Rectangle((0, 5), width=12, height=2, facecolor='#FF6103', edgecolor='grey')

# Create the plot
fig, ax = plt.subplots()
ax.add_patch(a)
ax.add_patch(b)
ax.add_patch(c)

# Add the Ashoka Chakra
radius = 0.8
center_x, center_y = 6, 4
chakra_color = '#000088ff'

# Draw the Chakra center
ax.plot(center_x, center_y, marker='o', markerfacecolor=chakra_color, markersize=9.5)

# Draw the Chakra circle
chakra = plt.Circle((center_x, center_y), radius, color=chakra_color, fill=False, linewidth=7)
ax.add_artist(chakra)

# Draw the 24 spokes
for i in range(0, 24):
    angle = np.pi * i / 12
    x_outer = center_x + radius * np.cos(angle)
    y_outer = center_y + radius * np.sin(angle)
    x_inner1 = center_x + (radius / 2) * np.cos(angle + np.pi / 48)
    y_inner1 = center_y + (radius / 2) * np.sin(angle + np.pi / 48)
    x_inner2 = center_x + (radius / 2) * np.cos(angle - np.pi / 48)
    y_inner2 = center_y + (radius / 2) * np.sin(angle - np.pi / 48)

    ax.add_patch(
        patch.Polygon([[center_x, center_y], [x_inner1, y_inner1], [x_outer, y_outer], [x_inner2, y_inner2]],
                      fill=True, closed=True, color=chakra_color))

# Set equal aspect ratio and display the plot
ax.set_aspect('equal')
plt.axis('off')  # Optional: Hides the axes for a cleaner look
plt.show()
