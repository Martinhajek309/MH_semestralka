"""Linear point search without a spatial index."""

from __future__ import annotations


Point = tuple[float, float]
BBox = tuple[float, float, float, float]


def point_in_bbox(point: Point, bbox: BBox) -> bool:
    x, y = point
    min_x, min_y, max_x, max_y = bbox
    return min_x <= x <= max_x and min_y <= y <= max_y


def search_points(points: list[Point], bbox: BBox) -> list[Point]:
    return [point for point in points if point_in_bbox(point, bbox)]
