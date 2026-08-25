import json
import hashlib
import random
import uuid
from datetime import datetime, timedelta, timezone

# 1. Configuration
DEVICE_ID = "ESP32-001"
GENESIS_HASH = "0000000000000000000000000000000000000000000000000000000000000000"

# 2. Expanded Forensic Event Taxonomy
EVENT_TAXONOMY = [
    # System & Hardware
    {"type": "SYSTEM_BOOT", "level": "INFO", "msg": "Device booted successfully from flash"},
    {"type": "SYSTEM_SHUTDOWN", "level": "WARN", "msg": "Unexpected power loss detected"},
    {"type": "CPU_TEMP_HIGH", "level": "WARN", "msg": "CPU temperature exceeded 75°C threshold"},
    {"type": "MEMORY_WARNING", "level": "WARN", "msg": "Available heap memory dropped below 15%"},
    {"type": "FIRMWARE_UPDATE_START", "level": "INFO", "msg": "Initiated OTA firmware update"},
    {"type": "CONFIG_CHANGE", "level": "WARN", "msg": "System configuration parameters modified"},
    
    # Network & IoT
    {"type": "NETWORK_CONNECT", "level": "INFO", "msg": "Successfully authenticated with Wi-Fi AP"},
    {"type": "NETWORK_DISCONNECT", "level": "WARN", "msg": "Lost connection to Wi-Fi AP"},
    {"type": "MQTT_CONNECT_FAILED", "level": "ERROR", "msg": "TLS handshake failed with Azure IoT Hub"},
    {"type": "SENSOR_READ_ERROR", "level": "ERROR", "msg": "I2C bus communication timeout"},
    
    # Auth & Access
    {"type": "LOGIN_SUCCESS", "level": "INFO", "msg": "User successfully authenticated via local web panel"},
    {"type": "LOGIN_FAILED", "level": "WARN", "msg": "Invalid password provided for admin account"},
    {"type": "SESSION_TIMEOUT", "level": "INFO", "msg": "Idle session automatically terminated"},
    {"type": "LOGOUT", "level": "INFO", "msg": "User manually triggered logout sequence"},
    
    # Security Threats
    {"type": "BRUTE_FORCE_DETECTED", "level": "CRITICAL", "msg": "5+ failed authentication attempts within 60s"},
    {"type": "FILE_READ", "level": "INFO", "msg": "Forensic log archive accessed"},
    {"type": "FILE_MODIFIED", "level": "CRITICAL", "msg": "Unauthorized modification to boot sector"},
    {"type": "FILE_DELETE", "level": "CRITICAL", "msg": "Local volatile log cache forcefully wiped"},
    {"type": "PHYSICAL_TAMPER", "level": "CRITICAL", "msg": "Enclosure open switch triggered"}
]

IP_POOL = [
    "192.168.1.10", "192.168.1.25", "10.0.0.5",  # Internal / Safe
    "185.153.196.11", "45.22.14.88", "194.35.233.10"  # External / Suspicious
]
USER_POOL = ["system", "admin", "guest", "root_unknown"]

def generate_mock_logs(num_logs=50):
    logs = []
    previous_hash = GENESIS_HASH
    
    # Start the timeline 24 hours ago to make the 50 logs look spread out
    current_time = datetime.now(timezone.utc) - timedelta(hours=24)

    for i in range(1, num_logs + 1):
        # Select random attributes for the log
        event = random.choice(EVENT_TAXONOMY)
        src_ip = random.choice(IP_POOL)
        user = random.choice(USER_POOL) if "LOGIN" in event["type"] or "FILE" in event["type"] else "system"
        
        # Advance time by a random interval (from 1 second to 45 minutes)
        current_time += timedelta(seconds=random.randint(1, 2700))
        
        # Build the raw log dictionary
        log_entry = {
            "log_id": str(uuid.uuid4()),
            "device_id": DEVICE_ID,
            "timestamp": current_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event_type": event["type"],
            "level": event["level"],
            "source_ip": src_ip,
            "user": user,
            "message": event["msg"],
            "previous_hash": previous_hash
        }
        
        # Serialize STRICTLY without spaces
        serialized_string = json.dumps(log_entry, separators=(',', ':'))
        
        # Hash the serialized string
        current_hash = hashlib.sha256(serialized_string.encode('utf-8')).hexdigest()
        
        # Append to payload
        log_entry["current_hash"] = current_hash
        
        # Add to list and link the chain
        logs.append(log_entry)
        previous_hash = current_hash

    return logs

if __name__ == "__main__":
    log_count = 50
    print(f"Generating simulated forensic hash chain for {log_count} events...")
    
    simulated_data = generate_mock_logs(log_count)
    
    # Export to JSON
    output_file = "mock_logs.json"
    with open(output_file, "w") as f:
        json.dump(simulated_data, f, indent=2)
        
    print(f"✅ Successfully generated {log_count} mathematically linked logs.")
    print(f"📂 Saved to: {output_file}")
    print(f"🔗 Final Hash in Chain: {simulated_data[-1]['current_hash']}")