"""Modelo de licitación normalizada."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

from .enums import Source, TenderStatus


class Tender(BaseModel):
    """Licitación tras la ingesta y normalización.

    Es el modelo común que `tender-ingestion-service` produce y `tender-api` persiste.
    """

    model_config = ConfigDict(use_enum_values=True)

    id: str = Field(description="Identificador interno (UUID).")
    source: Source = Field(description="Fuente: placsp | ted | autonomic | other.")
    source_id: str = Field(description="Identificador del expediente en la fuente.")
    title: str
    summary: str | None = Field(default=None, description="Objeto/resumen del anuncio.")
    cpv: list[str] = Field(default_factory=list, description="Códigos CPV.")
    buyer: str | None = Field(default=None, description="Órgano de contratación.")
    budget_amount: float | None = Field(default=None, ge=0, description="Importe (sin IVA).")
    currency: str = Field(default="EUR", min_length=3, max_length=3)
    publication_date: date | None = None
    deadline: datetime | None = Field(default=None, description="Fin de presentación de ofertas.")
    url: str | None = Field(default=None, description="URL del anuncio en la fuente.")
    status: TenderStatus = Field(default=TenderStatus.DISCOVERED)
    created_at: datetime | None = None
    updated_at: datetime | None = None
