# Repository Structure & Environment Setup: IoT EvidenceGuard

This document outlines the strict directory structure and required environment variables for the project. The AI assistant must adhere to this structure when generating or modifying files.

---

## 1. Directory Structure

The repository must be divided into three distinct operational domains, plus a documentation folder containing all markdown files and reference diagrams.

```text
IoT_EvidenceGuard/
│
├── edge_node/                  # ESP32 MicroPython Codebase & Simulation
│   ├── simulator.py            # Log generator for Phase 1a
│   ├── boot.py                 # Network setup and NTP time sync
│   ├── main.py                 # Event simulation, hashing, and MQTT publishing
│   ├── umqttsimple.py          # Lightweight MQTT library for MicroPython
│   └── config.json             # Edge configuration (Wi-Fi, MQTT details)
│
├── backend/                    # Node.js Verification Engine & API
│   ├── src/
│   │   ├── server.js           # Express app initialization
│   │   ├── routes/             # API route definitions (e.g., forensics.js)
│   │   ├── controllers/        # Logic to fetch from Azure & verify hashes
│   │   └── middleware/         # JWT authentication & error handling
│   ├── package.json            # Node dependencies
│   └── .env                    # Secret environment variables (DO NOT COMMIT)
│
├── frontend/                   # Investigator Dashboard (Pure UI)
│   ├── index.html              # Dashboard layout (CSS Grid)
│   ├── style.css               # Theming, UI components, and tamper alerts
│   ├── app.js                  # DOM manipulation and API consumption
│   └── assets/                 # Icons and placeholder images
│
└── docs/                       # Project Documentation
    ├── plan.md
    ├── rules.md
    ├── api_contracts.md
    ├── environment_and_structure.md
    └── diagrams/               # Architecture and Design References
        ├── DFD_Level0.png
        ├── DFD_Level1.png
        ├── JSON_Structure.png
        ├── System_Design_1.png
        ├── UML SequenceDiagram.png
        └── UML UseCases.png
```

---

## 2. Environment Variables & Configuration

To ensure security and modularity, hardcoded secrets are strictly forbidden. Use the following configuration standards for each tier.

### A. Edge Node Configuration (`edge_node/config.json`)
Since MicroPython does not use traditional `.env` files natively in the same way Node.js does, the ESP32 will read a `config.json` file upon boot. 

**Required Keys:**
```json
{
  "WIFI_SSID": "your_wifi_name",
  "WIFI_PASSWORD": "your_wifi_password",
  "MQTT_BROKER": "your_azure_iot_hub_url_or_local_broker",
  "MQTT_PORT": 8883,
  "MQTT_CLIENT_ID": "ESP32-001",
  "MQTT_TOPIC": "devices/ESP32-001/messages/events/",
  "DEVICE_ID": "ESP32-001"
}
```

### B. Backend API Secrets (`backend/.env`)
The Node.js server requires these secrets to run securely. The AI assistant should utilize `dotenv` to load these in `server.js`.

**Required Variables:**
```env
# Server Configuration
PORT=3000
NODE_ENV=development

# Security
JWT_SECRET=super_secure_random_string_for_investigator_auth

# Azure WORM Storage Integration
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=...
AZURE_CONTAINER_NAME=forensic-logs-worm
```

### C. Frontend Configuration (`frontend/app.js`)
Since this is a vanilla JavaScript frontend, configuration variables will be defined at the top of the main `app.js` file.

**Required Constants:**
```javascript
// Point this to the local or deployed Node.js backend
const API_BASE_URL = "http://localhost:3000/api/v1";
```
