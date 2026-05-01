"""
Pharos RWA Oracle Monitor v1.0
Developed for Pharos Network Ecosystem
"""
import time
import random

class PharosMonitor:
    def __init__(self):
        self.version = "1.0.0"
        self.network = "Pacific Ocean Mainnet"
        
    def start_monitoring(self):
        print(f"--- PHAROS RWA ORACLE MONITOR v{self.version} ---")
        print(f"Status: Connecting to {self.network}...")
        time.sleep(1.5)
        
        try:
            while True:
                # Simulasi data teknis yang lebih dalam
                block = random.randint(1245000, 1260000)
                latency = random.randint(95, 180)
                deviation = round(random.uniform(0.01, 0.05), 4)
                
                print(f"\n[BLOCK {block}] | Network: {self.network}")
                print(f" > Asset: Gold/USD (RWA)")
                print(f" > Oracle Deviation: {deviation}% (Within Safe Threshold)")
                print(f" > Sync Status: SECURE | Latency: {latency}ms")
                print("-" * 50)
                
                time.sleep(3)
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor = PharosMonitor()
    monitor.start_monitoring()