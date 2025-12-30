import json
from pathlib import Path
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

def _static_root_path() -> Path:
    return Path(settings.BASE_DIR) / "static"

@register.simple_tag
def vite_asset(entry: str):
    root = _static_root_path()
    manifest_path = root / "build" / ".vite" / "manifest.json"

    if not manifest_path.exists():
        return mark_safe(f"<!-- Vite manifest not found: {manifest_path} -->")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    chunk = manifest.get(entry)

    if not chunk:
        return mark_safe(f"<!-- Vite entry not found in manifest: {entry} -->")

    tags = []

    for css in chunk.get("css", []):
        tags.append(
            f'<link rel="stylesheet" href="{settings.STATIC_URL}build/{css.lstrip("/")}">'
        )

    tags.append(
        f'<script type="module" src="{settings.STATIC_URL}build/{chunk["file"].lstrip("/")}"></script>'
    )

    return mark_safe("\n".join(tags))
