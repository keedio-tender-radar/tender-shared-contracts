"""Modelo de scoring Go/No-Go (ver tender-platform-docs/scoring-model.md)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .enums import FactorKind, Recommendation


class ScoreBreakdown(BaseModel):
    """Sub-scores por dimensión. Los máximos son los pesos del modelo (suman 100)."""

    technical_fit: int = Field(ge=0, le=30, description="Encaje técnico (máx 30).")
    budget_fit: int = Field(ge=0, le=15, description="Presupuesto y margen (máx 15).")
    technical_solvency: int = Field(ge=0, le=15, description="Solvencia técnica (máx 15).")
    economic_solvency: int = Field(ge=0, le=10, description="Solvencia económica (máx 10).")
    deadline: int = Field(ge=0, le=10, description="Plazo disponible (máx 10).")
    partner_need: int = Field(ge=0, le=5, description="Necesidad de partner (máx 5).")
    documental_complexity: int = Field(ge=0, le=5, description="Complejidad documental (máx 5).")
    contractual_risk: int = Field(ge=0, le=5, description="Riesgo contractual (máx 5).")
    incompatibility_risk: int = Field(ge=0, le=5, description="Riesgo incompatibilidad (máx 5).")

    def total(self) -> int:
        return (
            self.technical_fit
            + self.budget_fit
            + self.technical_solvency
            + self.economic_solvency
            + self.deadline
            + self.partner_need
            + self.documental_complexity
            + self.contractual_risk
            + self.incompatibility_risk
        )


class ScoreFactor(BaseModel):
    """Factor explicativo (positivo o negativo) del score, en lenguaje natural."""

    model_config = ConfigDict(use_enum_values=True)

    kind: FactorKind
    message: str


class TenderScore(BaseModel):
    """Resultado del scoring de una licitación."""

    model_config = ConfigDict(use_enum_values=True)

    id: str
    tender_id: str
    total: int = Field(ge=0, le=100)
    breakdown: ScoreBreakdown
    recommendation: Recommendation
    hard_rules: list[str] = Field(
        default_factory=list, description="Reglas duras activadas (overrides)."
    )
    factors: list[ScoreFactor] = Field(default_factory=list)
    model_version: str = Field(default="1.0.0", description="Versión del modelo de scoring.")
    created_at: datetime | None = None
