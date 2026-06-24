"""Enumeraciones del dominio de Keedio Tender Radar."""

from __future__ import annotations

from enum import StrEnum


class Source(StrEnum):
    """Fuente de la licitación."""

    PLACSP = "placsp"
    TED = "ted"
    AUTONOMIC = "autonomic"
    OTHER = "other"


class TenderStatus(StrEnum):
    """Estado en el ciclo de vida de una licitación."""

    DISCOVERED = "discovered"
    SCREENED = "screened"
    ANALYZED = "analyzed"
    SCORED = "scored"
    NOTIFIED = "notified"
    INTERESTED = "interested"
    DISCARDED = "discarded"
    PARTNER = "partner"
    GO = "go"


class Recommendation(StrEnum):
    """Recomendación Go/No-Go."""

    GO = "go"
    REVISAR = "revisar"
    PARTNER = "partner"
    NO_GO = "no_go"


class ActionType(StrEnum):
    """Acción humana recibida (p. ej. desde Telegram)."""

    INTERESTED = "interested"
    DISCARDED = "discarded"
    PARTNER = "partner"
    GENERATE_REPORT = "generate_report"
    COMPLIANCE_MATRIX = "compliance_matrix"
    PRIORITIZE = "prioritize"
    REVIEW_SOLVENCY = "review_solvency"


class DocumentType(StrEnum):
    """Tipo de documento de un expediente."""

    PCAP = "pcap"  # Pliego de Cláusulas Administrativas Particulares
    PPT = "ppt"  # Pliego de Prescripciones Técnicas
    ANEXO = "anexo"
    MODELO = "modelo"
    OTHER = "other"


class NotificationType(StrEnum):
    """Tipo de notificación enviada."""

    DAILY_DIGEST = "daily_digest"
    URGENT_ALERT = "urgent_alert"


class FactorKind(StrEnum):
    """Signo de un factor explicativo del score."""

    POSITIVE = "positive"
    NEGATIVE = "negative"


class EventType(StrEnum):
    """Eventos de dominio que circulan entre servicios."""

    DISCOVERED = "tender.discovered"
    UPDATED = "tender.updated"
    DOCUMENTS_FOUND = "tender.documents_found"
    DOCUMENTS_DOWNLOADED = "tender.documents_downloaded"
    DOCUMENTS_EXTRACTED = "tender.documents_extracted"
    ANALYSIS_COMPLETED = "tender.analysis_completed"
    SCORED = "tender.scored"
    TELEGRAM_NOTIFICATION_SENT = "tender.telegram_notification_sent"
    USER_ACTION_RECEIVED = "tender.user_action_received"
