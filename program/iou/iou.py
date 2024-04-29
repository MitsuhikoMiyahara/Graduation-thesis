from shapely.geometry import Polygon

def calculate_iou(poly1_coords, poly2_coords):
    # 2つの多角形を作成
    poly1 = Polygon(poly1_coords)
    poly2 = Polygon(poly2_coords)

    # 交差領域と結合領域を計算
    intersection = poly1.intersection(poly2).area
    union = poly1.union(poly2).area

    # IoUを計算
    iou = intersection / union
    return iou

# 例：2つの多角形の頂点リスト
poly1_coords = [(47, 27), (50, 165), (58, 433), (47, 373), (29, 237), (25, 121), (41, 30)]
# poly1_coords = [(40, 33), (59, 148), (94, 423), (86, 460), (36, 259), (28, 215), (18, 114), (38, 35)]
poly2_coords = [(50, 22), (52, 170), (56, 412), (49, 372), (29, 233), (25, 112), (46, 23)]

# poly1_coords = [(1, 1), (1, 2), (2, 2), (2, 1)]
# poly2_coords = [(0, 0), (1, 0), (1, 1), (0, 1)]

# IoUを計算
iou = calculate_iou(poly1_coords, poly2_coords)
print(f"IoU: {iou}")