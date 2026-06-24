"""Modelos de documentos del expediente y fragmentos para RAG."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .enums import DocumentType


class TenderDocument(BaseModel):
    """Documento de un expediente (pliego, anexo, modelo)."""

    model_config = ConfigDict(use_enum_values=True)

    id: str
    tender_id: str
    type: DocumentType = Field(default=DocumentType.OTHER)
    filename: str
    url: str | None = Field(default=None, description="URL de descarga en la fuente.")
    storage_key: str | None = Field(default=None, description="Clave en MinIO/S3.")
    content_type: str | None = None
    size_bytes: int | None = Field(default=None, ge=0)
    extracted: bool = Field(default=False, description="¿Texto ya extraído?")
    created_at: datetime | None = None


class DocumentChunk(BaseModel):
    """Fragmento de texto de un documento, base del RAG por expediente (ADR 004)."""

    id: str
    tender_id: str = Field(description="Filtro obligatorio del RAG (ADR 004).")
    document_id: str
    ordinal: int = Field(ge=0, description="Orden del fragmento dentro del documento.")
    content: str
    section: str | None = Field(default=None, description="Sección detectada, si la hay.")
    embedding: list[float] | None = Field(
        default=None, description="Vector de embedding (opcional en el contrato)."
    )
