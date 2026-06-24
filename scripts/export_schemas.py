"""Exporta los JSON-Schema de los modelos a json-schema/.

Uso:  python scripts/export_schemas.py
La CI / el test `test_schemas` comprueba que los ficheros no se desincronicen de los modelos.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "python"))

from tender_contracts import (  # noqa: E402
    Notification,
    Tender,
    TenderDocument,
    TenderScore,
)

# nombre de fichero -> modelo
SCHEMAS = {
    "tender.schema.json": Tender,
    "document.schema.json": TenderDocument,
    "score.schema.json": TenderScore,
    "notification.schema.json": Notification,
}


def schema_json(model) -> str:
    return json.dumps(model.model_json_schema(), indent=2, ensure_ascii=False) + "\n"


def main() -> None:
    out_dir = ROOT / "json-schema"
    out_dir.mkdir(exist_ok=True)
    for filename, model in SCHEMAS.items():
        (out_dir / filename).write_text(schema_json(model), encoding="utf-8")
        print(f"wrote {filename}")


if __name__ == "__main__":
    main()
