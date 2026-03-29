import subprocess
import os

def run_audit():
    scripts = [
        "scripts/script1.sh", "scripts/script2.sh", 
        "scripts/script3.sh", "scripts/script4.sh", "scripts/script5.sh"
    ]
    
    print("🚀 Initializing Open Source Audit Suite...")
    print("-" * 40)

    for script in scripts:
        if os.path.exists(script):
            print(f"🔄 Executing {script}...")
            # Ensure script is executable
            subprocess.run(["chmod", "+x", script])
            # Execute and capture output
            result = subprocess.run(["bash", script], capture_output=True, text=True)
            print(result.stdout)
        else:
            print(f"⚠️ Warning: {script} not found.")

    print("-" * 40)
    print("✅ Audit Complete. Check 'system_manifesto.txt' for details.")

if __name__ == "__main__":
    run_audit()
