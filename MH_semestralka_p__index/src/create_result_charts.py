"""Create benchmark charts for CSV tables in the results directory."""

from __future__ import annotations

import csv
import math
import re
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "charts"

REQUIRED_COLUMNS = {"method", "total_seconds"}
SPLIT_COLUMN = "query_window_size_m"
GROUP_COLUMNS = ["area_name", "dataset_size", "query_count", "radius_m", "polygon_count"]

METHOD_LABELS = {
    "linear_search": "linear search",
    "tile_index": "tile index",
    "rtree_index": "R-tree / STRtree",
    "linear_search_radius": "linear search",
    "tile_index_radius": "tile index",
    "rtree_index_radius": "R-tree / STRtree",
    "linear_search_polygon": "linear search",
    "tile_index_polygon": "tile index",
    "rtree_index_polygon": "R-tree / STRtree",
}

METHOD_COLORS = {
    "linear search": "#b84a4a",
    "tile index": "#23875c",
    "R-tree / STRtree": "#2c64aa",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    sample = path.read_text(encoding="utf-8-sig")[:2048]
    delimiter = ";" if sample.count(";") > sample.count(",") else ","
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def slug(value: object) -> str:
    text = str(value).strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_") or "all"


def numeric_sort_key(value: str) -> tuple[int, float | str]:
    try:
        return (0, float(value))
    except ValueError:
        return (1, value)


def method_label(method: str) -> str:
    return METHOD_LABELS.get(method, method)


def row_group_key(row: dict[str, str], has_split: bool) -> tuple[tuple[str, str], ...]:
    columns = [column for column in GROUP_COLUMNS if column in row and row[column]]
    if has_split:
        columns = [column for column in columns if column != SPLIT_COLUMN]
    return tuple((column, row[column]) for column in columns)


def title_from_group(csv_path: Path, group_key: tuple[tuple[str, str], ...]) -> str:
    if not group_key:
        return csv_path.stem
    details = ", ".join(f"{column}={value}" for column, value in group_key)
    return f"{csv_path.stem}: {details}"


def plot_grouped_by_method(
    rows: list[dict[str, str]],
    title: str,
    output_path: Path,
    split_column: str | None = None,
) -> None:
    split_values = [""]
    if split_column:
        split_values = sorted({row[split_column] for row in rows}, key=numeric_sort_key)

    methods = []
    for row in rows:
        label = method_label(row["method"])
        if label not in methods:
            methods.append(label)

    cols = min(3, len(split_values))
    rows_count = math.ceil(len(split_values) / cols)
    width = max(7.2, cols * 4.0)
    height = max(4.2, rows_count * 3.3)
    fig, axes = plt.subplots(rows_count, cols, figsize=(width, height), dpi=180, squeeze=False)

    for index, split_value in enumerate(split_values):
        ax = axes[index // cols][index % cols]
        plot_rows = rows
        if split_column:
            plot_rows = [row for row in rows if row[split_column] == split_value]

        totals: dict[str, list[float]] = defaultdict(list)
        for row in plot_rows:
            totals[method_label(row["method"])].append(float(row["total_seconds"]))

        labels = [method for method in methods if totals[method]]
        values = [sum(totals[method]) / len(totals[method]) for method in labels]
        colors = [METHOD_COLORS.get(label, "#6b7280") for label in labels]

        ax.bar(labels, values, color=colors)
        ax.set_ylabel("total_seconds [s]")
        ax.grid(axis="y", alpha=0.22)
        ax.tick_params(axis="x", labelrotation=18)
        if split_column:
            ax.set_title(f"{split_column} = {split_value} m", fontsize=10)

    for empty_index in range(len(split_values), rows_count * cols):
        axes[empty_index // cols][empty_index % cols].axis("off")

    fig.suptitle(title, fontsize=13)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def create_charts_for_csv(csv_path: Path) -> list[Path]:
    rows = read_csv(csv_path)
    if not rows:
        return []

    columns = set(rows[0].keys())
    if not REQUIRED_COLUMNS.issubset(columns):
        missing = ", ".join(sorted(REQUIRED_COLUMNS - columns))
        print(f"Skipping {csv_path.name}: missing {missing}")
        return []

    has_split = SPLIT_COLUMN in columns
    grouped: dict[tuple[tuple[str, str], ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row_group_key(row, has_split)].append(row)

    output_paths = []
    for group_key, group_rows in grouped.items():
        suffix = "_".join(f"{slug(column)}_{slug(value)}" for column, value in group_key)
        output_name = f"{csv_path.stem}"
        if suffix:
            output_name = f"{output_name}_{suffix}"
        output_path = OUTPUT / f"{output_name}.png"
        title = title_from_group(csv_path, group_key)
        split_column = SPLIT_COLUMN if has_split else None
        plot_grouped_by_method(group_rows, title, output_path, split_column)
        output_paths.append(output_path)

    return output_paths


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)

    created = []
    for csv_path in sorted(RESULTS.glob("*.csv")):
        created.extend(create_charts_for_csv(csv_path))

    print(f"Created {len(created)} chart(s) in {OUTPUT}")
    for path in created:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
