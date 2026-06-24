# tender-shared-contracts

> 🧩 Contratos compartidos de **Keedio Tender Radar**. Modelos Pydantic v2 + JSON-Schema +
> eventos de dominio. Fuente de verdad de los formatos que intercambian los servicios.

Evita que cada servicio invente su propio formato: `tender-api`, `tender-ingestion-service`,
`tender-ai-analysis-service`, `tender-scoring-service` y `tender-telegram-bot` dependen de este
paquete (o de los JSON-Schema exportados).

## Contenido

```
python/tender_contracts/   Paquete Python (modelos Pydantic v2)
  ├── enums.py             Source, TenderStatus, Recommendation, ActionType, DocumentType, EventType…
  ├── tender.py            Tender
  ├── document.py          TenderDocument, DocumentChunk
  ├── score.py             ScoreBreakdown, ScoreFactor, TenderScore
  ├── notification.py      Notification, NotificationItem, NotificationStats
  └── events.py            DomainEvent, make_event
json-schema/               JSON-Schema exportados de los modelos (para consumidores no-Python)
examples/                  Ejemplos válidos (tender, score, notification)
openapi/                   Esqueletos OpenAPI (tender-api, telegram-bot)
scripts/export_schemas.py  Regenera json-schema/ desde los modelos
```

## Uso (Python)

```python
from tender_contracts import Tender, TenderScore, Recommendation, DomainEvent, EventType, make_event

t = Tender(id="...", source="placsp", source_id="PLACSP-2026-000184", title="Plataforma de datos")
ev = make_event(EventType.SCORED, t.id, producer="tender-scoring-service", total=92)
```

Instalación como dependencia (desde otro repo):

```bash
pip install "tender-contracts @ git+https://github.com/keedio-tender-radar/tender-shared-contracts.git"
```

## Eventos de dominio

```
tender.discovered · tender.updated · tender.documents_found · tender.documents_downloaded
tender.documents_extracted · tender.analysis_completed · tender.scored
tender.telegram_notification_sent · tender.user_action_received
```

## Modelo de scoring

`ScoreBreakdown` tiene 9 dimensiones cuyos máximos son los pesos del modelo (suman 100); ver
[`tender-platform-docs/scoring-model.md`](https://github.com/keedio-tender-radar/tender-platform-docs/blob/main/scoring-model.md).

## Desarrollo

```bash
python -m venv .venv && . .venv/Scripts/activate   # Linux/mac: source .venv/bin/activate
pip install -e . pytest ruff jsonschema
python scripts/export_schemas.py     # regenerar JSON-Schema tras tocar modelos
pytest -q                            # 17 tests (modelos + schemas + ejemplos)
ruff check .
```

> Los tests fallan si los JSON-Schema commiteados se desincronizan de los modelos: ejecuta
> `python scripts/export_schemas.py` y commitea el resultado.
