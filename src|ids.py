from datetime import datetime

SUSPICIOUS_IPS = []
FAILED_ATTEMPTS = {}

# Load rules
def load_rules():
    try:
        with open("rules.txt", "r") as file:
            for line in file:
                SUSPICIOUS_IPS.append(line.strip())
    except FileNotFoundError:
        print("[!] rules.txt not found")

# Log events
def log_event(message):
    with open("logs.txt", "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

# Detect intrusion
def detect_intrusion(ip, status):
    if ip in SUSPICIOUS_IPS:
        log_event(f"[ALERT] Suspicious IP detected: {ip}")
        return "🚨 ALERT: Known malicious IP"

    if status == "failed":
        FAILED_ATTEMPTS[ip] = FAILED_ATTEMPTS.get(ip, 0) + 1
        
        if FAILED_ATTEMPTS[ip] > 3:
            log_event(f"[ALERT] Brute-force attack from {ip}")
            return "🚨 ALERT: Brute-force attack detected"
    
    log_event(f"[INFO] Normal activity from {ip}")
    return "✅ Normal Activity"

# Simulated monitoring
def start_ids():
    print("🛡️ Intrusion Detection System Started...\n")

    while True:
        ip = input("Enter IP: ")
        status = input("Login status (success/failed): ")

        result = detect_intrusion(ip, status)
        print(result)

if __name__ == "__main__":
    load_rules()
    start_ids()
