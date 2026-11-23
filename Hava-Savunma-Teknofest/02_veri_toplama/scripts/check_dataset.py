"""YOLO veri setinde eksik etiket, sinif dagilimi ve split sizintisini kontrol eder."""

from collections import Counter
from pathlib import Path
import argparse
import yaml

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def load_class_names(config_path: Path) -> dict[int, str]:
    """data.yaml dosyasindan sinif ID-isim eslesmesini yukler."""
    with config_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    return {int(k): str(v) for k, v in data["names"].items()}


def inspect_split(split_dir: Path, valid_ids: set[int]) -> dict:
    """Tek bir split (train/val/test) icindeki gorsel ve etiketleri denetler."""
    images_dir = split_dir / "images"
    labels_dir = split_dir / "labels"
    images = [p for p in images_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS]

    class_counts: Counter[int] = Counter()
    missing_labels = []
    invalid_lines = []
    empty_images = 0

    for img_path in images:
        label_path = labels_dir / f"{img_path.stem}.txt"
        if not label_path.exists():
            missing_labels.append(img_path.name)
            continue

        lines = [line.strip() for line in label_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not lines:
            empty_images += 1
            continue

        for line in lines:
            parts = line.split()
            if len(parts) != 5:
                invalid_lines.append(f"{label_path.name}: {line}")
                continue
            cls_id = int(parts[0])
            if cls_id not in valid_ids:
                invalid_lines.append(f"{label_path.name}: gecersiz sinif {cls_id}")
                continue
            class_counts[cls_id] += 1

    return {
        "stems": {p.stem for p in images},
        "image_count": len(images),
        "empty_images": empty_images,
        "missing_labels": missing_labels,
        "invalid_lines": invalid_lines,
        "class_counts": class_counts,
    }


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="YOLO veri seti saglik kontrolu")
    parser.add_argument(
        "--config",
        type=Path,
        default=project_root / "02_veri_toplama" / "configs" / "data.yaml",
        help="data.yaml dosya yolu",
    )
    args = parser.parse_args()

    class_names = load_class_names(args.config)
    dataset_root = (args.config.parent / yaml.safe_load(args.config.read_text(encoding="utf-8"))["path"]).resolve()

    split_reports = {}
    for split in ("train", "val", "test"):
        split_dir = dataset_root / split
        if not split_dir.exists():
            print(f"[UYARI] Eksik klasor: {split_dir}")
            continue
        report = inspect_split(split_dir, set(class_names.keys()))
        split_reports[split] = report

        print(f"\n=== {split.upper()} ===")
        print(f"Gorsel sayisi      : {report['image_count']}")
        print(f"Bos (negatif) kare : {report['empty_images']}")
        print(f"Etiketsiz gorsel   : {len(report['missing_labels'])}")
        print(f"Hatali etiket      : {len(report['invalid_lines'])}")
        for cls_id, name in class_names.items():
            print(f"  - {cls_id} ({name}): {report['class_counts'][cls_id]}")

    if {"train", "val", "test"}.issubset(split_reports.keys()):
        leak_tv = split_reports["train"]["stems"] & split_reports["val"]["stems"]
        leak_tt = split_reports["train"]["stems"] & split_reports["test"]["stems"]
        leak_vt = split_reports["val"]["stems"] & split_reports["test"]["stems"]
        print("\n=== SIZINTI KONTROLU (AYNI DOSYA ADI) ===")
        print(f"train-val cakismasi  : {len(leak_tv)}")
        print(f"train-test cakismasi : {len(leak_tt)}")
        print(f"val-test cakismasi   : {len(leak_vt)}")


if __name__ == "__main__":
    main()
