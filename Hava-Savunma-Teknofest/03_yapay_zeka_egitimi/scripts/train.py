"""YOLOv11 egitim scripti (hava savunma kucuk hedef varsayilanlari ile)."""

from pathlib import Path
import argparse
import shutil
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    project_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="YOLOv11 Hava Savunma Egitimi")
    parser.add_argument("--model", default="yolo11s.pt", help="Baslangic modeli (yolo11n.pt / yolo11s.pt)")
    parser.add_argument(
        "--data",
        type=Path,
        default=project_root / "02_veri_toplama" / "configs" / "data.yaml",
        help="data.yaml yolu",
    )
    parser.add_argument("--imgsz", type=int, default=640, help="Giris cozunurlugu (640 veya 960)")
    parser.add_argument("--epochs", type=int, default=80, help="Epoch sayisi")
    parser.add_argument("--batch", type=int, default=16, help="Batch boyutu")
    parser.add_argument("--device", default="0", help="GPU id (0) veya cpu")
    parser.add_argument("--name", default="v1_yolo11s", help="Deney adi")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    project_root = Path(__file__).resolve().parents[2]
    runs_dir = project_root / "03_yapay_zeka_egitimi" / "experiments"
    weights_dir = project_root / "03_yapay_zeka_egitimi" / "weights"
    weights_dir.mkdir(parents=True, exist_ok=True)

    model = YOLO(args.model)
    results = model.train(
        data=str(args.data),
        imgsz=args.imgsz,
        epochs=args.epochs,
        batch=args.batch,
        device=args.device,
        project=str(runs_dir),
        name=args.name,
        flipud=0.0,
        fliplr=0.5,
        mosaic=1.0,
        patience=20,
    )

    best_pt = Path(results.save_dir) / "weights" / "best.pt"
    if best_pt.exists():
        target = weights_dir / f"{args.name}_best.pt"
        shutil.copy2(best_pt, target)
        print(f"En iyi agirlik kopyalandi: {target}")


if __name__ == "__main__":
    main()
