"""Script de pruebas para el servicio de predicción de churn."""

import httpx

BASE_URL = "http://localhost:8000"


def test_health():
    """Verificar health check."""
    r = httpx.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"
    print("✓ Health check OK")


def test_prediccion_alto_riesgo():
    """Cliente de alto riesgo de churn."""
    cliente = {
        "contract": "Month-to-month",
        "tenure": 1,
        "monthly_charges": 85.0,
        "total_charges": 85.0,
        "internet_service": "Fiber optic",
        "online_security": "No",
        "tech_support": "No",
        "payment_method": "Electronic check",
    }
    r = httpx.post(f"{BASE_URL}/predecir", json=cliente)
    assert r.status_code == 200
    resultado = r.json()
    print(f"✓ Alto riesgo: prob={resultado['churn_probability']:.3f}, churn={resultado['churn']}")


def test_prediccion_bajo_riesgo():
    """Cliente de bajo riesgo."""
    cliente = {
        "contract": "Two year",
        "tenure": 48,
        "monthly_charges": 45.0,
        "total_charges": 2160.0,
        "internet_service": "DSL",
        "online_security": "Yes",
        "tech_support": "Yes",
        "payment_method": "Bank transfer (automatic)",
    }
    r = httpx.post(f"{BASE_URL}/predecir", json=cliente)
    assert r.status_code == 200
    resultado = r.json()
    print(f"✓ Bajo riesgo: prob={resultado['churn_probability']:.3f}, churn={resultado['churn']}")


def test_batch():
    """Predicción en batch."""
    clientes = [
        {
            "contract": "Month-to-month",
            "tenure": 2,
            "monthly_charges": 90.0,
            "total_charges": 180.0,
            "internet_service": "Fiber optic",
            "online_security": "No",
            "tech_support": "No",
            "payment_method": "Electronic check",
        },
        {
            "contract": "Two year",
            "tenure": 60,
            "monthly_charges": 30.0,
            "total_charges": 1800.0,
            "internet_service": "DSL",
            "online_security": "Yes",
            "tech_support": "Yes",
            "payment_method": "Credit card",
        },
    ]
    r = httpx.post(f"{BASE_URL}/predecir_batch", json=clientes)
    assert r.status_code == 200
    resultados = r.json()
    assert len(resultados) == 2
    print(f"✓ Batch: {len(resultados)} predicciones realizadas")


if __name__ == "__main__":
    print("Probando servicio de predicción de churn...")
    print(f"URL: {BASE_URL}\n")

    test_health()
    test_prediccion_alto_riesgo()
    test_prediccion_bajo_riesgo()
    test_batch()

    print("\n¡Todos los tests pasaron!")
