# browser-agent

This repository contains automations implemented around having an AI use a web browser (via the [Browser Use](https://browser-use.com/) library).

## Use Cases

### LASA

The goal is to have the AI navigate to lasa.org, login, and pay the monthly bill. As of 2025-04-27, lasa.org does not have an autopay feature.

Demo of the outputs: [link](https://storage.googleapis.com/kamal-screenshots/385f5f528193614a8b6d7aa1e2acbeb0.html)

Demo video: coming soon (after I receive next month's bill)

#### Instructions:

1. Navigate to lasa.org and setup an account along with a default payment method.
1. `cp .env.lasa.example .env.lasa` and fill out `.env.lasa`.
1. `uv run src/lasa.py`

### PA Vehicle Registration Renewal (PVR)

The goal is to have an AI renew my vehicle registration. This is something that I have to do once per year and only takes ~15 minutes, so the automation is not saving much time. The primary motivation behind building it was to see how far I can get and to learn some new things in the process.

#### Instructions

1. `cp .env.pvr.example .env.pvr` and fill out `.env.pvr`.
1. `uv run src/pa_vehicle_registration.py`
