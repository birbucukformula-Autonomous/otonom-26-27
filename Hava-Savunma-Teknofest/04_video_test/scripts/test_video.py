"""Test videolari uzerinde YOLOv11 tespitini calistirir ve ozet istatistik uretir."""

from collections import Counter
from pathlib import Path
import argparse
import cv2
import numpy as np
from ultralytics import YOLO

VIDEO_EXTS = {".mp4", ".avi", ".mov", ".mkv"}


def classify_balloon_color(frame: np.ndarray, xyxy: tuple[int, int, int, int]) -> str:
    """Balon kutusunun merkez bolgesinden HSV ile kirmizi/mavi renk ayrımı yapar."""
    x1, y1, x2, y2 = xyxy
    dx, dy = max(1, (x2 - x1) // 4), max(1, (y2 - y1) // 4)
    roi = frame[max(0, y1 + dy):max(1, y2 - dy), max(0, x1 + dx):max(1, x2 - dx)]
    if roi.size == 0:
        return "belirsiz"

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    red_low = cv2.inRange(hsv, (0, 70, 50), (10, 255, 255))
    red_high = cv2.inRange(hsv, (170, 70, 50), (180, 255, 255))
    red_ratio = np.count_nonzero(red_low | red_high) / (roi.shape[0] * roi.shape[1])
    blue_ratio = np.count_nonzero(cv2.inRange(hsv, (95, 70, 50), (135, 255, 255))) / (roi.shape[0] * roi.shape[1])

    if max(red_ratio, blue_ratio) < 0.15:
        return "belirsiz"
    return "DUSMAN(kirmizi)" if red_ratio >= blue_ratio else "DOST(mavi)"


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
        annotated = result.plot()
        if len(result.boxes) > 0:
            frames_with_detection += 1
            for box in result.boxes:
                cls_name = model.names[int(box.cls[0])]
                if cls_name == "balon":
                    x1, y1, x2, y2 = (int(v) for v in box.xyxy[0].tolist())
                    iff_tag = classify_balloon_color(frame, (x1, y1, x2, y2))
                    class_hits[f"balon:{iff_tag}"] += 1
                    cv2.putText(annotated, iff_tag, (x1, min(height - 5, y2 + 18)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
                else:
                    class_hits[cls_name] += 1

        writer.write(annotated)

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
