"""Los JSON-Schema commiteados deben estar sincronizados con los modelos, y los ejemplos
deben validar contra ellos."""

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator
from tender_contracts import Notification, Tender, TenderDocument, TenderScore

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "json-schema"
EXAMPLES = ROOT / "examples"

MODELS = {
    "tender.schema.json": Tender,
    "document.schema.json": TenderDocument,
    "score.schema.json": TenderScore,
    "notification.schema.json": Notification,
}


@pytest.mark.parametrize("filename,model", MODELS.items())
def test_committed_schema_matches_model(filename, model):
    committed = json.loads((SCHEMA_DIR / filename).read_text(encoding="utf-8"))
    assert committed == model.model_json_schema(), (
        f"{filename} desincronizado. Ejecuta: python scripts/export_schemas.py"
    )


@pytest.mark.parametrize("filename", MODELS)
def test_schema_is_valid_jsonschema(filename):
    schema = json.loads((SCHEMA_DIR / filename).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


@pytest.mark.parametrize(
    "example,schema",
    [
        ("tender-example.json", "tender.schema.json"),
        ("score-example.json", "score.schema.json"),
        ("notification-example.json", "notification.schema.json"),
    ],
)
def test_examples_validate_against_schema(example, schema):
    data = json.loads((EXAMPLES / example).read_text(encoding="utf-8"))
    schema_doc = json.loads((SCHEMA_DIR / schema).read_text(encoding="utf-8"))
    Draft202012Validator(schema_doc).validate(data)
