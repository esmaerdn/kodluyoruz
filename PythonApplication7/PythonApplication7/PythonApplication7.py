import math

# 1. Noktalarý Tanýmlama
points = [(1, 2), (4, 6), (7, 1), (2, 8)]

# 2. Öklid Mesafesi Ýçin Fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 3. Mesafelerin Hesaplanmasý
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# 4. Minimum Mesafenin Bulunmasý
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
