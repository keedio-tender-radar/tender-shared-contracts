"""Eventos de dominio que circulan entre servicios.

Envoltura genérica `DomainEvent` con un `event_type` (ver `EventType`) y un `payload` libre.
Mantener el formato del sobre estable es lo que evita acoplar los servicios entre sí.
"""

from __future__ import annotations

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field

from .enums import EventType


def _now() -> datetime:
    return datetime.now(UTC)


class DomainEvent(BaseModel):
    """Sobre común de un evento de dominio."""

    model_config = ConfigDict(use_enum_values=True)

    event_type: EventType
    tender_id: str
    occurred_at: datetime = Field(default_factory=_now)
    producer: str | None = Field(default=None, description="Servicio que emite el evento.")
    payload: dict = Field(default_factory=dict, description="Datos específicos del evento.")


def make_event(
    event_type: EventType, tender_id: str, *, producer: str | None = None, **payload: object
) -> DomainEvent:
    """Helper para construir un evento con payload por kwargs."""
    return DomainEvent(
        event_type=event_type, tender_id=tender_id, producer=producer, payload=dict(payload)
    )
