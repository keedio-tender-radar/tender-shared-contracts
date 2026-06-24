import json
from pathlib import Path

import pytest
from tender_contracts import (
    DomainEvent,
    EventType,
    Notification,
    Recommendation,
    ScoreBreakdown,
    Tender,
    TenderScore,
    make_event,
)

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"


def _load(name: str) -> dict:
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))


def test_tender_example_parses_and_roundtrips():
    t = Tender.model_validate(_load("tender-example.json"))
    assert t.source == "placsp"
    assert "72300000" in t.cpv
    # round-trip
    again = Tender.model_validate(json.loads(t.model_dump_json()))
    assert again == t


def test_score_example_total_matches_breakdown():
    s = TenderScore.model_validate(_load("score-example.json"))
    assert s.total == s.breakdown.total() == 92
    assert s.recommendation == "go"


def test_notification_example_parses():
    n = Notification.model_validate(_load("notification-example.json"))
    assert n.type == "daily_digest"
    assert n.stats.analyzed == 184
    assert len(n.items) == 3
    assert n.items[0].recommendation == Recommendation.GO.value


def test_score_total_can_reach_100():
    full = ScoreBreakdown(
        technical_fit=30,
        budget_fit=15,
        technical_solvency=15,
        economic_solvency=10,
        deadline=10,
        partner_need=5,
        documental_complexity=5,
        contractual_risk=5,
        incompatibility_risk=5,
    )
    assert full.total() == 100


def test_score_breakdown_rejects_over_weight():
    with pytest.raises(ValueError):
        ScoreBreakdown(
            technical_fit=31,  # excede el peso máximo (30)
            budget_fit=0,
            technical_solvency=0,
            economic_solvency=0,
            deadline=0,
            partner_need=0,
            documental_complexity=0,
            contractual_risk=0,
            incompatibility_risk=0,
        )


def test_make_event_envelope():
    ev = make_event(
        EventType.SCORED, "tender-1", producer="tender-scoring-service", total=92
    )
    assert isinstance(ev, DomainEvent)
    assert ev.event_type == EventType.SCORED.value
    assert ev.tender_id == "tender-1"
    assert ev.payload["total"] == 92
    assert ev.occurred_at is not None
