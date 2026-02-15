# Odoo MCP Backup & Restoration Guide

This repository contains the core infrastructure for the bridge connecting your AI agents to Odoo 19.

## 1. Server Restoration (VPS)
1. Re-install dependencies:
   mkdir -p /opt/mcp-odoo && python3 -m venv /opt/mcp-odoo/venv
   /opt/mcp-odoo/venv/bin/pip install mcp-server-odoo mcp
2. Restore files: Move odoo_mcp_bridge.py and mcp_odoo_config.json to /opt/mcp-odoo/

## 2. Local Restoration
1. Copy mcporter.json to ~/config/mcporter.json
2. Run: mcporter list odoo

## 3. Usage
Ask OpenClaw (Dashboard/Telegram): 'What are my products?'