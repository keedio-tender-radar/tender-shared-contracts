"""Modelo de notificación (radar diario / alerta urgente) hacia Telegram."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .enums import NotificationType, Recommendation


class NotificationItem(BaseModel):
    """Una licitación dentro de una notificación."""

    model_config = ConfigDict(use_enum_values=True)

    tender_id: str
    title: str
    score: int = Field(ge=0, le=100)
    recommendation: Recommendation
    budget_amount: float | None = Field(default=None, ge=0)
    currency: str = Field(default="EUR", min_length=3, max_length=3)
    deadline: datetime | None = None
    url: str | None = None


class NotificationStats(BaseModel):
    """Cifras agregadas del radar diario."""

    analyzed: int = Field(ge=0)
    relevant: int = Field(ge=0)
    prioritized: int = Field(ge=0)
    discarded: int = Field(ge=0)


class Notification(BaseModel):
    """Notificación enviada a un canal (Telegram en el MVP)."""

    model_config = ConfigDict(use_enum_values=True)

    id: str
    type: NotificationType
    channel: str = Field(default="telegram")
    stats: NotificationStats | None = Field(
        default=None, description="Presente en el radar diario."
    )
    items: list[NotificationItem] = Field(default_factory=list)
    sent_at: datetime | None = None
