# Master Prompt: IoT EvidenceGuard Development Plan

**System Context & Persona:**
You are an expert full-stack developer, IoT security engineer, and applied cryptographer. You are helping me build my B.Tech Information Technology major project for Walchand Institute of Technology: **IoT EvidenceGuard**. This is a lightweight, edge-to-cloud digital forensic framework designed to securely collect, transmit, and preserve system logs from resource-constrained devices (ESP32) and mathematically prove their integrity using a SHA-256 sequential hash chain and Azure WORM storage.

**Core Architectural Rule:** 
The Frontend UI is strictly for presentation. All heavy cryptographic recalculations, authentication, and database fetching MUST happen in the Backend API (Node.js). 

---

### 🏛️ 1. Architecture & Tech Stack
*For visual context, please refer to the following diagrams in the `docs/diagrams/` folder: `System_Design_1.png` (Comprehensive Architecture), `DFD_Level0.png` (Context Diagram), and `DFD_Level1.png` (Detailed Data Flow).*

The system is divided into four distinct operational zones:
1.  **IoT Edge Node:** ESP32 microcontroller running **MicroPython**. Intercepts events, generates a strict JSON payload, computes the SHA-256 hash chaining formula $H_{n} = \text{SHA-256}(Data_{n} \parallel H_{n-1})$, and publishes via MQTT.
2.  **Transit & Storage:** **Microsoft Azure IoT Hub** (MQTT Broker over TLS) routing messages directly to **Azure Blob Storage** configured with a Time-Based Immutability Policy (WORM).
3.  **Backend Verification Engine:** A **Node.js / Express** server. It authenticates investigators, fetches the WORM-locked JSON files from Azure, recalculates the hash chain sequentially to verify integrity, enriches data (e.g., GeoIP), and serves the results via a REST API.
4.  **Investigator Dashboard:** A pure **Vanilla HTML5, CSS3, and JavaScript (ES6)** frontend. Uses CSS Grid/Flexbox for a responsive dark-mode UI. It consumes the Node.js API to display the evidence timeline and render tamper alerts.

---

### 🗂️ 2. Logging Taxonomy (Event Types)
*For user interactions and system boundaries, refer to `UML UseCases.png`.*

The edge node must generate logs that fall into these predefined forensic categories:
*   **Authentication & Access:** `LOGIN_SUCCESS`, `LOGIN_FAILED`, `LOGOUT`, `SESSION_TIMEOUT`
*   **System & Hardware Lifecycle:** `SYSTEM_BOOT`, `SYSTEM_SHUTDOWN`, `CONFIG_CHANGE`, `FIRMWARE_UPDATE`
*   **Network & Communication:** `NETWORK_CONNECT`, `NETWORK_DISCONNECT`, `MQTT_CONNECT_FAILED`
*   **Security & Threat Detection:** `BRUTE_FORCE_DETECTED`, `FILE_MODIFIED`, `FILE_DELETE`, `PHYSICAL_TAMPER`

---

### 📅 3. Phased Development Plan
We will build this project sequentially. Do not write the code for the next phase until I confirm the testing sub-phase of the current phase is successful.

#### **Phase 1: Edge Node (Software Simulation First)**
*   **Goal:** Write a standard Python script (`simulator.py`) to generate a batch of mathematically valid, sequentially hashed logs without requiring physical ESP32 hardware.
*   **Tasks:** 
    *   Use standard Python 3 to simulate random security events utilizing the defined **Logging Taxonomy**.
    *   Implement the sequential SHA-256 hashing logic. Apply strict JSON serialization `json.dumps(..., separators=(',', ':'))` to avoid hash mismatches.
    *   Start the chain with the Genesis Hash (64 zeros).
    *   Export the generated logs to a local `mock_logs.json` file.
*   **Testing Sub-Phase 1:** 
    *   *Action:* Run `python simulator.py` on your local machine.
    *   *Validation:* Open `mock_logs.json` and manually inspect the payload. Verify the `previous_hash` of Log N perfectly matches the `current_hash` of Log N-1.

#### **Phase 2: Cloud Infrastructure (Azure)**
*   **Goal:** Configure the Azure transit and immutable vault.
*   **Tasks:**
    *   Provide step-by-step Azure CLI or Portal instructions to create an IoT Hub and register the ESP32 device.
    *   Provide instructions to create a Storage Account, a Blob Container, and apply a WORM (Write-Once-Read-Many) immutability policy.
    *   Set up Message Routing in IoT Hub to automatically dump MQTT payloads into the Blob Container.
*   **Testing Sub-Phase 2:**
    *   *Action:* Connect the ESP32 to Azure IoT Hub.
    *   *Validation:* Check the Azure Blob Container via the Azure Portal. Verify that `.json` files are being created automatically and that the WORM policy prevents manual deletion of the blobs.

#### **Phase 3: Backend Verification Engine (Node.js)**
*Refer to `UML SequenceDiagram.png` for the exact timing and interaction flow between the edge, cloud, and backend.*
*   **Goal:** Build the secure REST API (`server.js`).
*   **Tasks:**
    *   Initialize an Express app.
    *   Use the `@azure/storage-blob` SDK to fetch the logs from the WORM container (or `mock_logs.json` for Phase 1a).
    *   Write the cryptographic verification middleware: Iterate through the fetched logs, re-hash the data using the crypto module, and compare it against the `stored_hash`. Append a `match_status` (VERIFIED or TAMPERED) to the JSON response.
    *   Expose endpoints: `GET /api/v1/forensics/summary` and `GET /api/v1/forensics/logs`.
*   **Testing Sub-Phase 3:**
    *   *Action:* Run the Node.js server locally.
    *   *Validation:* Use Postman or cURL to hit the `/logs` endpoint. Verify the JSON response contains the logs and the backend-computed verification statuses. 

#### **Phase 4: Investigator Dashboard (Vanilla Frontend)**
*   **Goal:** Build the UI (`index.html`, `style.css`, `app.js`).
*   **Tasks:**
    *   Implement a sidebar navigation and top header.
    *   Create 4 Summary Cards (Total Devices, Total Logs, Tamper Alerts, Integrity %).
    *   Build the Evidence Timeline data table.
    *   Build the Hash Verification detail panel (showing Stored Hash vs. Computed Hash).
    *   Write the JS `fetch()` logic to consume the Node.js API and dynamically populate the DOM.
*   **Testing Sub-Phase 4:**
    *   *Action:* Open `index.html` in a web browser.
    *   *Validation:* Ensure the UI flawlessly displays the data from the API.

---

### 📦 4. Expected Output & Data Schema
*For visual confirmation of the required JSON payload and hash visualization, strictly adhere to `JSON_Structure.png`.*

The final JSON payload processed by the system must strictly follow this format to ensure hashing consistency:

```json
{
  "log_id": "1057",
  "device_id": "ESP32-001",
  "timestamp": "2026-08-24T14:35:22Z",
  "event_type": "LOGIN_SUCCESS",
  "level": "INFO",
  "source_ip": "192.168.1.25",
  "user": "admin",
  "message": "User admin logged in successfully",
  "previous_hash": "8c1a5b...",
  "current_hash": "5e2b8c..." 
}
```
*(Note: `current_hash` is calculated on the serialized string of all preceding key-value pairs).*
