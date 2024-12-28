import hashlib
from pathlib import Path
import requests


class FileCache:
    def __init__(self, cache_dir=None):
        self.cache_dir = Path(cache_dir or Path.home() / ".cache" / "jawikt")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_cached_file(self, url: str) -> Path:
        file_name = hashlib.sha256(url.encode()).hexdigest()
        cached_file = self.cache_dir / file_name
        if cached_file.exists():
            return cached_file
        else:
            return self.download_file(url, cached_file)

    def download_file(self, url: str, file_path: Path) -> Path:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return file_path
