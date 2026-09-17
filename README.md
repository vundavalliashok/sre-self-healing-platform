# Automated remediation

This directory documents the remediation pattern for the demo:

1. Prometheus detects an SLO-relevant symptom.
2. Alertmanager routes the alert.
3. A remediation controller/job validates the failure.
4. The controller performs a bounded action, such as restarting an unhealthy deployment.
5. The controller verifies recovery.
6. The incident is recorded for RCA.

For safety, remediation should be:
- allow-listed
- idempotent
- rate-limited
- observable
- reversible where possible

The repository deliberately keeps the remediation action separate from the application container.
