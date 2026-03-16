import os
import psutil
import datetime
import signal

# --- TARGET SIGNATURES ---
THREAT_SIGNATURES = ["infect.py", "os.urandom", "self_destruct", "pynput"]

def deep_scan_and_destroy():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [*] PHASE 2: DEEP INSPECTION & NEUTRALIZATION...")
    found_threats = 0

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline_list = proc.info.get('cmdline') or []
            cmdline_str = " ".join(cmdline_list)

            # 1. Protection: Don't kill the scanner itself
            if "sanitize.py" in cmdline_str or proc.info['pid'] == os.getpid():
                continue

            # 2. Match the signatures
            if any(sig in cmdline_str for sig in THREAT_SIGNATURES):
                pid = proc.info['pid']
                
                # --- THE REPORT ---
                print("\n" + "="*40)
                print(f"THREAT REPORT - {datetime.datetime.now()}")
                print("="*40)
                print(f"PROCESS NAME: {proc.info['name']}")
                print(f"COMMAND LINE: {cmdline_str}")
                print(f"PROCESS ID:   {pid}")
                print(f"STATUS:       ACTIVE THREAT")
                print("-" * 40)

                # --- THE KILL ---
                print(f"[*] ACTION: TERMINATING PID {pid}...")
                os.kill(pid, signal.SIGKILL) 
                print(f"[+] VERDICT: NEUTRALIZED SUCCESSFULLY.")
                print("="*40 + "\n")
                
                found_threats += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    if found_threats == 0:
        print("[+] ANALYSIS COMPLETE: No active payloads found.")

if __name__ == "__main__":
    print("--- SENTINEL-LINUX: STRIKE MODE ---")
    deep_scan_and_destroy()
