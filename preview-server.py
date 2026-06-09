from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from shutil import copyfile
from urllib.parse import unquote


SITE_ROOT = Path(__file__).resolve().parent
MODEL_ROOT = Path(r"C:\Users\ELUCY\Downloads\t-shirt\source\T_shirt_gltf")
GRAPHICS_ROOT = Path(r"D:\Grafike")
DESIGN_ROOT = SITE_ROOT / "assets" / "designs"
DESIGN_ASSETS = {
    "be-the.svg": GRAPHICS_ROOT / "Be the .svg",
    "chross.svg": GRAPHICS_ROOT / "Chross.svg",
    "heart.svg": GRAPHICS_ROOT / "Heart.svg",
}
SYNC_WARNINGS = []


def sync_design_assets():
    DESIGN_ROOT.mkdir(parents=True, exist_ok=True)

    for filename, source in DESIGN_ASSETS.items():
        destination = DESIGN_ROOT / filename
        try:
            if source.exists() and (
                not destination.exists()
                or destination.stat().st_size != source.stat().st_size
                or destination.stat().st_mtime < source.stat().st_mtime
            ):
                copyfile(source, destination)
        except OSError as error:
            SYNC_WARNINGS.append(f"{filename}: {error}")


class PreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean_path = unquote(path.split("?", 1)[0].split("#", 1)[0])

        if clean_path.startswith("/model/"):
            relative = clean_path.removeprefix("/model/")
            return str((MODEL_ROOT / relative).resolve())

        if clean_path.startswith("/grafike/"):
            relative = clean_path.removeprefix("/grafike/")
            return str((GRAPHICS_ROOT / relative).resolve())

        if clean_path.startswith("/assets/designs/"):
            relative = clean_path.removeprefix("/assets/designs/")
            local_path = (DESIGN_ROOT / relative).resolve()
            fallback = DESIGN_ASSETS.get(relative)

            if local_path.exists() and local_path.stat().st_size > 2:
                return str(local_path)

            if fallback and fallback.exists():
                return str(fallback.resolve())

            return str(local_path)

        if clean_path == "/":
            clean_path = "/index.html"

        return str((SITE_ROOT / clean_path.lstrip("/")).resolve())

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        super().end_headers()


if __name__ == "__main__":
    sync_design_assets()
    server = ThreadingHTTPServer(("127.0.0.1", 5175), PreviewHandler)
    print("ELUCY preview server: http://127.0.0.1:5175")
    print("Configurator: http://127.0.0.1:5175/konfigurator.html")
    if SYNC_WARNINGS:
        print("Design asset sync warnings:")
        for warning in SYNC_WARNINGS:
            print(f"- {warning}")
    server.serve_forever()
