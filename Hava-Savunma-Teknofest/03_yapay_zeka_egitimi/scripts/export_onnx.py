"""Egitilen YOLOv11 modelini Jetson Orin NX icin sabit boyutlu ONNX'e aktarir."""

from pathlib import Path
import argparse
from ultralytics import YOLO


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="YOLOv11 ONNX Export")
    parser.add_argument(
        "--weights",
        type=Path,
        default=project_root / "03_yapay_zeka_egitimi" / "weights" / "best.pt",
        help=".pt model dosyasi",
    )
    parser.add_argument("--imgsz", type=int, default=640, help="Sabit giris cozunurlugu")
    parser.add_argument("--opset", type=int, default=17, help="ONNX opset surumu")
    args = parser.parse_args()

    if not args.weights.exists():
        raise FileNotFoundError(f"Agirlik dosyasi bulunamadi: {args.weights}")

    model = YOLO(str(args.weights))
    exported = model.export(format="onnx", imgsz=args.imgsz, opset=args.opset, simplify=True, dynamic=False)
    print(f"ONNX export tamamlandi: {exported}")


if __name__ == "__main__":
    main()
