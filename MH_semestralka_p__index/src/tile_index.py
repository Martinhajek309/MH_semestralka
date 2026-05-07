"""Simple tile-based spatial index for point search."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


Point = tuple[float, float]
BBox = tuple[float, float, float, float]
Tile = tuple[int, int]


@dataclass
class TileIndex:
    tile_size: float
    tiles: dict[Tile, list[Point]]

    @classmethod
    def build(cls, points: list[Point], tile_size: float) -> "TileIndex":
        tiles: dict[Tile, list[Point]] = defaultdict(list)
        index = cls(tile_size=tile_size, tiles=tiles)

        for point in points:
            tiles[index.tile_for_point(point)].append(point)

        return index

    def tile_for_point(self, point: Point) -> Tile:
        x, y = point
        return int(x // self.tile_size), int(y // self.tile_size)

    def tiles_for_bbox(self, bbox: BBox) -> list[Tile]:
        min_x, min_y, max_x, max_y = bbox
        min_tile_x = int(min_x // self.tile_size)
        min_tile_y = int(min_y // self.tile_size)
        max_tile_x = int(max_x // self.tile_size)
        max_tile_y = int(max_y // self.tile_size)

        return [
            (tile_x, tile_y)
            for tile_x in range(min_tile_x, max_tile_x + 1)
            for tile_y in range(min_tile_y, max_tile_y + 1)
        ]

    def search(self, bbox: BBox) -> list[Point]:
        min_x, min_y, max_x, max_y = bbox
        result = []

        for tile in self.tiles_for_bbox(bbox):
            for x, y in self.tiles.get(tile, []):
                if min_x <= x <= max_x and min_y <= y <= max_y:
                    result.append((x, y))

        return result
