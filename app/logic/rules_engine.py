def evaluate_rules(risk_level, budget_usage):
    if risk_level == "high" and budget_usage > 0.8:
        return "⚠️ Escalate to Program Manager"
    elif risk_level == "medium":
        return "✅ Proceed with caution"
    else:
        return "✅ All systems normal"
