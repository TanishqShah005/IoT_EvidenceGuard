### Prompt: Phase 3 — Backend Verification Engine

**Context:**
I am building the verification engine for **IoT EvidenceGuard**[cite: 5]. Please strictly adhere to `rules.md` (specifically Rule 1.2: Smart Backend, Rule 1.3: Cloud Immutability, Rule 2.2: Deterministic Serialization, and Rule 2.3: Hashing Formula)[cite: 1] and `api_contracts.md`[cite: 2] in my `docs/` folder[cite: 3, 4]. 

*Note for local testing:* Read the existing local `mock_logs.json` file generated in Phase 1a instead of querying Azure Blob Storage directly[cite: 3, 4, 5].

**Current Task — Phase 3 (Backend Verification Engine API):**
Build the complete Node.js / Express backend application inside the `backend/` directory structure[cite: 3, 4, 5].

**Instructions & Specifications:**
1. **Project Setup & Environment:**
   - Initialize the Node.js project structure with `server.js`, routes, controllers, and middleware[cite: 3, 4].
   - Configure `dotenv` to load environment variables as defined in `environment_and_structure.md`[cite: 3, 4].

2. **Cryptographic Hash Chain Verification Middleware/Controller:**
   - Write a core verification function that accepts an array of log entries[cite: 2, 5].
   - Iterate through the logs sequentially from index 0[cite: 2, 5].
   - For each log entry $N$, strip any existing `current_hash` or `backend_verification` fields to reconstruct the raw payload[cite: 1, 2].
   - Strictly serialize the raw payload into a deterministic JSON string without whitespace, matching MicroPython's `json.dumps(data, separators=(',', ':'))` format[cite: 1, 5].
   - Compute the SHA-256 hash using Node.js native `crypto` module[cite: 1, 5].
   - Compare `computed_hash` against `stored_hash` (`current_hash`)[cite: 1, 2].
   - If `computed_hash === stored_hash` AND `previous_hash` of entry $N$ matches `current_hash` of entry $N-1$, mark as `MATCH` / `VERIFIED`[cite: 1, 2].
   - If any hash mismatch or broken chain link is detected, mark as `MISMATCH` / `TAMPERED`[cite: 1, 2].

3. **REST API Endpoints Implementation:**
   - Implement `GET /api/v1/forensics/summary` returning total logs, active devices, tamper alerts, and overall integrity rate[cite: 2, 5].
   - Implement `GET /api/v1/forensics/logs` supporting optional query filters (`device_id`, `event_type`, `status`) and returning enriched log payloads containing the `backend_verification` status object[cite: 2, 5].
   - Adhere 100% to the JSON response schemas specified in `api_contracts.md`[cite: 2].

4. **Security & Guardrails:**
   - Do NOT include any endpoints or routes that support `POST`, `PUT`, `PATCH`, or `DELETE` on log files (enforce Append-Only / WORM rules)[cite: 1].

Please provide the `package.json` dependencies, `server.js`, routes, controllers, and helper modules[cite: 3, 4].