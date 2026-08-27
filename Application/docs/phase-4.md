### Prompt: Phase 4 — Investigator Dashboard

**Context:**
I am building the frontend dashboard for **IoT EvidenceGuard**[cite: 5]. Please read `rules.md` (specifically Rule 1.1: The "Dumb" Frontend, Rule 4.1: Framework Independence, and Rule 4.2: Visual Indicators for Integrity)[cite: 1] and `api_contracts.md`[cite: 2] from the `docs/` folder[cite: 3, 4].

**Current Task — Phase 4 (Vanilla Presentation Dashboard):**
Build the frontend application inside the `frontend/` folder using `index.html`, `style.css`, and `app.js`[cite: 3, 4, 5].

**Instructions & Specifications:**
1. **Architectural Constraints:**
   - Strictly Vanilla HTML5, CSS3, and ES6 JavaScript[cite: 1, 5].
   - Do NOT use React, Vue, Angular, Tailwind, or Bootstrap[cite: 1].
   - NEVER calculate SHA-256 hashes or perform cryptographic checks in the browser[cite: 1]. Rely strictly on the `backend_verification` object returned by the API[cite: 1, 2].

2. **UI Component Layout:**
   - **Header & Sidebar:** System title ("IoT EvidenceGuard"), status indicator, and navigation links[cite: 5].
   - **Metrics Row (4 Summary Cards):** Total Devices, Total Logs Processed, Tamper Alerts Detected, and Chain Integrity Percentage[cite: 2, 5].
   - **Evidence Timeline Table:** Displays Timestamp (UTC), Device ID, Event Type (colored badge), Source IP, User, and Verification Status[cite: 2, 5].
   - **Hash Detail Verification Modal / Panel:** Clicking any log row opens a side drawer or modal displaying `Previous Hash`, `Stored Hash`, `Computed Hash`, and exact match status[cite: 1, 2, 5].

3. **Styling & Visual Alert Logic (CSS):**
   - Modern dark-mode forensic theme using CSS Variables, CSS Grid, and Flexbox[cite: 1, 5].
   - Logs with `verification_status === "VERIFIED"` must display green badge indicators (`#10B981`)[cite: 1, 2].
   - Logs with `verification_status === "TAMPERED"` must display critical red alert styling (`#EF4444`), highlight the table row, and display a warning banner[cite: 1, 2].

4. **API Integration (`app.js`):**
   - Fetch data asynchronously from `http://localhost:3000/api/v1/forensics/summary` and `http://localhost:3000/api/v1/forensics/logs`[cite: 2, 3, 4].
   - Render data dynamically into the DOM without page reloads[cite: 5].
   - Add search/filter controls for Event Type and Verification Status[cite: 2].

Please provide the complete code for `index.html`, `style.css`, and `app.js`[cite: 3, 4, 5].