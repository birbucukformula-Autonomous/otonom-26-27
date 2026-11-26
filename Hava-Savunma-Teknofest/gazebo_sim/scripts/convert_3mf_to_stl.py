"""3MF .model dosyalarini Gazebo uyumlu binary STL (metre olceginde) dosyalarina cevirir."""

from pathlib import Path
import argparse
import math
import struct
import xml.etree.ElementTree as ET

MODEL_NS = {"m": "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}

MODEL_MAP = {
    "object_18.model": "fuze",
    "object_19.model": "helikopter",
    "object_20.model": "f16",
    "object_21.model": "drone",
}


def compute_normal(v0: tuple[float, float, float], v1: tuple[float, float, float], v2: tuple[float, float, float]) -> tuple[float, float, float]:
    """Ucgen yuzeyin birim normal vektorunu hesaplar."""
    ux, uy, uz = v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2]
    vx, vy, vz = v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2]
    nx = uy * vz - uz * vy
    ny = uz * vx - ux * vz
    nz = ux * vy - uy * vx
    length = math.sqrt(nx * nx + ny * ny + nz * nz)
    if length == 0.0:
        return (0.0, 0.0, 0.0)
    return (nx / length, ny / length, nz / length)


def convert_model_to_stl(src_path: Path, dst_path: Path, scale: float = 0.001) -> int:
    """Tek bir 3MF .model XML dosyasini binary STL olarak yazar ve ucgen sayisini doner."""
    root = ET.parse(src_path).getroot()
    vertices = [
        (float(v.attrib["x"]) * scale, float(v.attrib["y"]) * scale, float(v.attrib["z"]) * scale)
        for v in root.findall(".//m:vertex", MODEL_NS)
    ]
    triangles = root.findall(".//m:triangle", MODEL_NS)

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    header = f"TEKNOFEST {dst_path.stem} (meters)".encode("ascii", errors="ignore").ljust(80, b"\x00")[:80]

    with dst_path.open("wb") as handle:
        handle.write(header)
        handle.write(struct.pack("<I", len(triangles)))
        for tri in triangles:
            v0 = vertices[int(tri.attrib["v1"])]
            v1 = vertices[int(tri.attrib["v2"])]
            v2 = vertices[int(tri.attrib["v3"])]
            normal = compute_normal(v0, v1, v2)
            handle.write(struct.pack("<12fH", *normal, *v0, *v1, *v2, 0))

    return len(triangles)


def main() -> None:
    sim_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="3MF .model -> Gazebo binary STL donusturucu")
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("/home/zuzu/Downloads/Modeller/3D/Objects"),
        help="3MF object_*.model dosyalarinin bulundugu klasor",
    )
    parser.add_argument("--scale", type=float, default=0.001, help="Olcek carpani (mm -> m icin 0.001)")
    args = parser.parse_args()

    if not args.source.exists():
        raise FileNotFoundError(f"Kaynak klasor bulunamadi: {args.source}")

    for filename, model_name in MODEL_MAP.items():
        src = args.source / filename
        if not src.exists():
            print(f"[ATLANDI] Bulunamadi: {src}")
            continue
        dst = sim_root / "models" / model_name / "meshes" / f"{model_name}.stl"
        tri_count = convert_model_to_stl(src, dst, scale=args.scale)
        size_mb = dst.stat().st_size / (1024 * 1024)
        print(f"[OK] {filename} -> {dst} ({tri_count} ucgen, {size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
