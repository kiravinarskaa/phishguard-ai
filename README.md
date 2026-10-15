# PhishGuard AI

PhishGuard AI is a multi-agent phishing prevention system designed to analyze suspicious emails and identify social engineering indicators.

The project is being developed as a university AI-agent project.

## Current Status

The project is planned as a system of five AI agents.

Currently implemented:

- Agent 1 — Email Triage & Social Engineering Analysis

Planned agents:

- Agent 2 — URL & Domain Investigation
- Agent 3 — Sender Verification
- Agent 4 — Risk & Prevention
- Agent 5 — Incident Response

---

## Agent 1 — Email Triage & Social Engineering Analysis

Agent 1 analyzes the content of an email and looks for common phishing and social engineering indicators.

It currently detects:

- urgency;
- threats;
- credential requests;
- financial requests;
- sensitive data requests;
- possible impersonation;
- social engineering techniques.

It also produces a preliminary risk level:

- low;
- medium;
- high.

The agent does not perform detailed URL or domain reputation analysis.

That functionality is intended for Agent 2.

---

## How It Works

The current workflow is:

User ->  Gradio Web Interface -> Email Triage Agent -> Cloud LLM -> Structured JSON Analysis