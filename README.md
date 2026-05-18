# Alamut

**Alamut is a self-hosted backup and monitoring tool for small homelabs, built from scratch as a Python learning project.**

> This is a work in progress. Alamut is an AI-assisted learning project.
> There is no finished solution here — just real code, written step by step, on real infrastructure.

---

## What it will do

- Incremental backups with snapshots (Time Machine style)
- Only changed files are copied — no duplicates, no wasted space
- Backs up: Nextcloud, AppDaemon scripts, Home Assistant config, MariaDB
- Backup target: external drive mounted via SMB/NFS
- Log output for every backup run
- Later: Web UI, status monitoring, Proxmox API integration

---

## Target infrastructure

| Machine | Role |
|---------|------|
| i5-6600K, 16GB, Proxmox | Home Assistant OS (AdGuard, MariaDB), AppDaemon LXC |
| Raspberry Pi 4, 4GB, Ubuntu | Nextcloud (Docker) |
| External USB drive (planned) | Backup target, mounted at router |

---

## Roadmap

| Phase | What | Status |
|-------|------|--------|
| 1 | CLI, copy files, log output | In progress |
| 2 | Config from file, keep last N backups | Planned |
| 3 | MariaDB dump, HA backup, Nextcloud specific | Planned |
| 4 | Web UI | Planned |
| 5 | Monitoring, status overview | Planned |
| 1.0 | Stable, documented, deployable | Goal: 2027/2028 |

---

## About this project

Alamut is named after the mountain fortress — a single point that keeps everything safe.

This project is built by someone learning Python from zero, using real infrastructure as the classroom.
No tutorials, no toy examples — every line of code runs on actual hardware and solves actual problems.

AI (Claude by Anthropic) is used as a tutor and architecture partner, not as a code generator.
The goal is to understand every line that goes into production.

---

## Status

Early development. Nothing works yet. Come back later.
