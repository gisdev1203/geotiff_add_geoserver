
from shapely.geometry import Polygon

# Define the polygon of Poland's boundary
poland_boundary = Polygon([
    (1866957.758, 538493.775),
    # ... coordinates of the polygon ...
    (69028.486, 356888.045),
    (59634.058, 349894.372),
    (57240.297, 344604.032),
    (52784.572, 336576.068),
    (49450.358, 333825.062),
    (44267.618, 332953.202),
    (39318.885, 329489.647),
    (33410.764, 332072.582),
    (25701.131, 334827.381),
    (22248.713, 338819.5),
    (16158.04, 339450.136),
    (6907.938, 338187.187),
    (0.0, 340000.0),
    # ... more coordinates ...
])

# Define the rectangle coordinates
rectangle = Polygon([
    (x1, y1),  # top-left corner
    (x2, y1),  # top-right corner
    (x2, y2),  # bottom-right corner
    (x1, y2),  # bottom-left corner
    (x1, y1),  # closing the polygon
])

# Check if the rectangle intersects the polygon
has_intersection = poland_boundary.intersects(rectangle)

# Print the result
if has_intersection:
    print("The rectangle intersects the polygon.")
else:
    print("The rectangle does not intersect the polygon.")