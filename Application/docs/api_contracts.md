# API Contracts & Schemas: IoT EvidenceGuard

**Version:** 1.0.0
**Base URL:** `http://localhost:3000/api/v1/forensics`
**Authentication:** All endpoints require a valid JWT via the `Authorization` header (`Bearer <token>`).

---

## 1. Get Dashboard Summary
**Endpoint:** `GET /summary`
**Description:** Fetches high-level metrics for the top summary cards on the dashboard.

**Request Headers:**
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Successful Response (200 OK):**
```json
{
  "status": "success",
  "data": {
    "totalDevices": 12,
    "activeDevices": 9,
    "totalLogs": 24851,
    "todayLogs": 1542,
    "tamperAlerts": 7,
    "integrityRate": 99.62
  }
}
```

---

## 2. Get Evidence Timeline (Logs)
**Endpoint:** `GET /logs`
**Description:** Fetches the immutable logs from Azure WORM storage, passes them through the backend cryptographic verification engine, and returns the enriched, verified payloads.

**Request Headers:**
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Query Parameters (Optional Filters):**
* `device_id` (string): Filter by specific ESP32 node.
* `event_type` (string): Filter by taxonomy (e.g., `LOGIN_SUCCESS`).
* `status` (string): `VERIFIED` or `TAMPERED`.

**Successful Response (200 OK):**
```json
{
  "status": "success",
  "count": 1,
  "data": [
    {
      "log_id": "1057",
      "device_id": "ESP32-001",
      "timestamp": "2026-08-24T14:35:22Z",
      "event_type": "LOGIN_SUCCESS",
      "level": "INFO",
      "source_ip": "192.168.1.25",
      "user": "admin",
      "message": "User admin logged in successfully",
      
      "previous_hash": "8c1a5b4e...",
      "stored_hash": "5e2b8c1f...", 
      
      "backend_verification": {
        "computed_hash": "5e2b8c1f...",
        "match_status": "MATCH",
        "verification_status": "VERIFIED" 
      }
    }
  ]
}
```
*(Note: If `stored_hash` != `computed_hash`, `match_status` becomes `"MISMATCH"` and `verification_status` becomes `"TAMPERED"`).*

---

## 3. Threat Alert Generation (Example Tampered Response)
If the Node.js backend detects a fractured hash chain, the `backend_verification` object for that specific log alters its state to trigger the frontend CSS alerts:

**Response Snippet (Tampered Log):**
```json
{
  "log_id": "1058",
  "device_id": "ESP32-001",
  "event_type": "FILE_DELETE",
  "previous_hash": "5e2b8c1f...", 
  "stored_hash": "a3d9f6b1...", 
  
  "backend_verification": {
    "computed_hash": "f4c9a2b7...", 
    "match_status": "MISMATCH",
    "verification_status": "TAMPERED",
    "alert_level": "CRITICAL"
  }
}
```
