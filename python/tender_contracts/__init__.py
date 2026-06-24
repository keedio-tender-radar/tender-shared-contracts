"""Contratos compartidos de Keedio Tender Radar.

Modelos Pydantic y enumeraciones comunes a todos los servicios. La fuente de verdad de los
formatos: el resto de repos depende de este paquete (y de los JSON-schema exportados).
"""

from __future__ import annotations

from .document import DocumentChunk, TenderDocument
from .enums import (
    ActionType,
    DocumentType,
    EventType,
    FactorKind,
    NotificationType,
    Recommendation,
    Source,
    TenderStatus,
)
from .events import DomainEvent, make_event
from .notification import Notification, NotificationItem, NotificationStats
from .score import ScoreBreakdown, ScoreFactor, TenderScore
from .tender import Tender

__version__ = "0.1.0"

__all__ = [
    "__version__",
    # enums
    "ActionType",
    "DocumentType",
    "EventType",
    "FactorKind",
    "NotificationType",
    "Recommendation",
    "Source",
    "TenderStatus",
    # models
    "Tender",
    "TenderDocument",
    "DocumentChunk",
    "ScoreBreakdown",
    "ScoreFactor",
    "TenderScore",
    "Notification",
    "NotificationItem",
    "NotificationStats",
    "DomainEvent",
    "make_event",
]
