"""
Interactive Vulnerability Chaining Simulator
Demonstrates how low-severity flaws combine to create critical breaches.
"""

import time
import sys

def simulate_typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def main():
    print("=" * 60)
    simulate_typing("[!] INITIALIZING VULNERABILITY CHAINING SIMULATOR...")
    print("=" * 60)
    print("Target: 192.168.1.100 (Simulated Corp Server)\n")
    
    print("During your Phase 2 scanning, you found four isolated vulnerabilities:")
    print("  [A] File Upload Form (No extension filtering)")
    print("  [B] Server Version Banner Leak (Apache 2.4.41)")
    print("  [C] Open Directory Listing (/backups/)")
    print("  [D] Hardcoded Credentials in Config (admin:password123)\n")
    
    simulate_typing("[?] Your goal: Achieve Remote Code Execution (RCE).")
    simulate_typing("[?] What is the correct logical order to exploit these? (e.g., B,C,D,A)")
    
    attempts = 0
    while attempts < 3:
        user_input = input("\nEnter your sequence (4 letters): ").strip().upper().replace(",", "")
        
        if len(user_input) != 4:
            print("[-] Please enter exactly 4 letters.")
            continue
            
        if user_input == "BCDA":
            simulate_typing("\n[+] Executing Exploit Chain...")
            time.sleep(1)
            print("    -> Step 1 (B): Version leak confirms server OS.")
            time.sleep(1)
            print("    -> Step 2 (C): Open directory allows you to find hidden files.")
            time.sleep(1)
            print("    -> Step 3 (D): You download the config file and extract admin credentials.")
            time.sleep(1)
            print("    -> Step 4 (A): You log in as admin and upload a Python reverse shell.")
            time.sleep(1)
            print("\n[$$$] SUCCESS! Root access achieved via vulnerability chaining.")
            break
        elif user_input[0] == "A":
            print("[-] FAILED: You tried to upload a file, but you don't have admin credentials yet.")
        elif user_input[0] == "D":
            print("[-] FAILED: You can't see the config file until you find the open directory.")
        else:
            print("[-] FAILED: The sequence broke. The server logged your suspicious activity and blocked your IP.")
            
        attempts += 1
        
    if attempts == 3:
        print("\n[!] Blue Team detected your attacks. Simulation Terminated.")

if __name__ == "__main__":
    main()