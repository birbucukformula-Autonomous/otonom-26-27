"""Test videolari uzerinde YOLOv11 tespitini calistirir ve ozet istatistik uretir."""

from collections import Counter
from pathlib import Path
import argparse
import cv2
from ultralytics import YOLO

VIDEO_EXTS = {".mp4", ".avi", ".mov", ".mkv"}


def run_on_video(model: YOLO, video_path: Path, output_dir: Path, conf: float, imgsz: int) -> None:
    """Tek bir videoyu isler, kutulu videoyu kaydeder ve kare bazli ozet basar."""
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print(f"[HATA] Video acilamadi: {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out_path = output_dir / f"{video_path.stem}_detected.mp4"
    writer = cv2.VideoWriter(str(out_path), cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    total_frames = 0
    frames_with_detection = 0
    class_hits: Counter[str] = Counter()

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        total_frames += 1

        results = model.predict(frame, conf=conf, imgsz=imgsz, verbose=False)
        result = results[0]
        if len(result.boxes) > 0:
            frames_with_detection += 1
            for cls_tensor in result.boxes.cls:
                class_hits[model.names[int(cls_tensor)]] += 1

        writer.write(result.plot())

    cap.release()
    writer.release()

    ratio = (frames_with_detection / total_frames * 100.0) if total_frames else 0.0
    print(f"\nVideo: {video_path.name}")
    print(f"  Toplam kare       : {total_frames}")
    print(f"  Tespitli kare (%) : {frames_with_detection} ({ratio:.1f}%)")
    print(f"  Sinif dagilimi    : {dict(class_hits)}")
    print(f"  Cikti             : {out_path}")


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="YOLOv11 Video Test Araci")
    parser.add_argument("--weights", type=Path, required=True, help="Egitilmis .pt veya .onnx yolu")
    parser.add_argument(
        "--source",
        type=Path,
        default=project_root / "04_video_test" / "test_videos",
        help="Tek video veya video klasoru",
    )
    parser.add_argument("--conf", type=float, default=0.35, help="Guven esigi")
    parser.add_argument("--imgsz", type=int, default=640, help="Giris cozunurlugu")
    args = parser.parse_args()

    if not args.weights.exists():
        raise FileNotFoundError(f"Model bulunamadi: {args.weights}")

    output_dir = project_root / "04_video_test" / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    videos = [args.source] if args.source.is_file() else sorted(
        p for p in args.source.iterdir() if p.is_file() and p.suffix.lower() in VIDEO_EXTS
    )
    if not videos:
        print(f"[BILGI] Test edilecek video bulunamadi: {args.source}")
        return

    model = YOLO(str(args.weights))
    for video_path in videos:
        run_on_video(model, video_path, output_dir, args.conf, args.imgsz)


if __name__ == "__main__":
    main()
