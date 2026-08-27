### Prompt: Phase 2 — Cloud Infrastructure Setup

**Context:**
I am building the cloud transit and storage vault for my B.Tech project, **IoT EvidenceGuard**[cite: 5]. Please refer to my project documentation in the `docs/` folder, specifically `environment_and_structure.md`[cite: 3, 4], `plan.md`[cite: 5], and the architecture diagram `System_Design_1_2.png`[cite: 4, 5].

**Current Task — Phase 2 (Cloud Infrastructure Setup):**
I need a complete setup guide including Azure CLI commands and Azure Portal steps to provision the cloud infrastructure[cite: 5].

**Instructions & Specifications:**
1. **Azure IoT Hub Provisioning:**
   - Provide Azure CLI commands to create a standard tier Azure IoT Hub[cite: 5].
   - Provide commands to register an edge device with the ID `ESP32-001`[cite: 2, 4, 5].
   - Retrieve and display the primary connection string for device authentication[cite: 3, 4].

2. **Azure Storage & WORM Container:**
   - Provide Azure CLI commands to create a General Purpose v2 Storage Account[cite: 5].
   - Create a Blob Storage container named `forensic-logs-worm`[cite: 3, 4, 5].
   - Provide step-by-step instructions to configure a **Time-Based Immutability Policy (WORM)** on `forensic-logs-worm` so that uploaded log payloads cannot be edited, overwritten, or deleted by any user or administrator[cite: 1, 3, 5].

3. **Message Routing Configuration:**
   - Provide step-by-step portal or CLI instructions to create a custom endpoint in Azure IoT Hub pointing to the `forensic-logs-worm` blob container[cite: 5].
   - Configure a message route that automatically forwards all incoming MQTT telemetry from `ESP32-001` directly to the Blob Container in JSON file format[cite: 4, 5].

4. **Environment Mapping:**
   - Show how the resulting `AZURE_STORAGE_CONNECTION_STRING` and `AZURE_CONTAINER_NAME` map into the backend `.env` file[cite: 3, 4].

Please provide the exact Azure CLI commands followed by clear, numbered Azure Portal execution steps[cite: 5].