import os
import random
import datetime
import string
import time

# --- CONFIGURAÇÃO DO UNIVERSO ---
# Altere estes valores para moldar a sua realidade
BASE_DIR = "Agent-Hub-VFS-Generated"
NUM_CORP_FILES = 2500
NUM_LORE_FILES = 500
NUM_MISC_FILES = 1000
TOTAL_FILES = NUM_CORP_FILES + NUM_LORE_FILES + NUM_MISC_FILES

# --- ELEMENTOS NARRATIVOS ---
CORPORATIONS = ["ZetaTech", "RivalCorp", "OmniGen", "Aetherion"]
PROJECTS = ["Alpine", "Odyssey", "Helios", "Nyx"]
KEY_PERSONNEL = ["Dr. Aris", "Kaelen", "Unit 734", "The Archivist"]
CONCEPTS = ["Phantoms", "Echoes", "The Signal", "The Glitch"]

# --- GERADORES DE CONTEÚDO ---

def generate_random_text(length=100):
    """Gera texto aleatório para preencher ficheiros."""
    chars = string.ascii_letters + string.digits + " \n\t."
    return ''.join(random.choice(chars) for _ in range(length))

def generate_timestamp():
    """Cria um timestamp no formato de log."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def generate_log_entry():
    """Gera uma linha de log de sistema variada."""
    log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"]
    services = ["auth.service", "kernel.sys", "network.manager", "cron.job", "api.v3"]
    messages = [
        "User authentication successful", "Failed login attempt", "System memory approaching limit",
        "Connection timed out", f"Executing scheduled task {random.randint(1000, 9999)}",
        f"Data packet received from {random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        f"NULL pointer exception at memory address 0x{random.randint(0, 0xFFFFFFFF):08X}",
        "Firewall rule #4815 blocked an incoming connection."
    ]
    return f"{generate_timestamp()} [{{random.choice(log_levels)}}] ({{random.choice(services)}}): {{random.choice(messages)}}\n"

def generate_email():
    """Gera um e-mail corporativo fictício."""
    sender_corp = random.choice(CORPORATIONS)
    recipient_corp = random.choice(CORPORATIONS)
    sender = f"{{random.choice(KEY_PERSONNEL).lower().replace(' ', '.')}}@{{sender_corp.lower()}}.com"
    recipient = f"{{''.join(random.choices(string.ascii_lowercase, k=5))}}@{{recipient_corp.lower()}}.com"

    subjects = [
        f"URGENT: Regarding Project {{random.choice(PROJECTS)}}",
        "Weekly Performance Review", "Server Maintenance Downtime",
        f"Suspicious activity detected on node {{random.randint(1, 100)}}",
        f"Re: Inquiry about the {{random.choice(CONCEPTS)}}"
    ]
    
    # Adicionar pistas narrativas
    body_fragments = [
        "We need to discuss the implications of the latest findings.",
        "Stop mentioning the 'Phantoms' in open comms. We use designated channels for a reason.",
        "Have you seen the latest report from Dr. Aris? It's... concerning.",
        "RivalCorp is getting too close to the truth about Alpine.",
        "The server farm in sector Gamma went dark. No logs, just... silence. It's happening again.",
        "Delete this email after reading."
    ]

    body = f"From: {{sender}}\nTo: {{recipient}}\nSubject: {{random.choice(subjects)}}\n\n"
    body += f"All,\n\n{{random.choice(body_fragments)}}\n\n{{generate_random_text(random.randint(200, 500))}}\n\nRegards."
    return body

# --- FUNÇÃO PRINCIPAL DE CRIAÇÃO ---

def create_file_with_content(path, content_generator):
    """Cria um ficheiro com conteúdo gerado, garantindo que o diretório exista."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", errors="ignore") as f:
            f.write(content_generator())
        return True
    except Exception as e:
        # print(f"Could not create file {{path}}: {{e}}")
        return False

def main():
    """Ponto de entrada do gerador de universo."""
    print("--- PROTOCOLO BIG BANG INICIADO ---")
    print(f"Forjando um universo com {{TOTAL_FILES}} ficheiros em '{{BASE_DIR}}'...")
    
    if os.path.exists(BASE_DIR):
        print(f"AVISO: O diretório '{{BASE_DIR}}' já existe. Ficheiros podem ser sobrescritos.")
    
    file_count = 0
    start_time = time.time()

    # Gerar ficheiros corporativos (logs, emails, relatórios)
    for i in range(NUM_CORP_FILES):
        corp = random.choice(CORPORATIONS)
        file_type = random.choice(["logs", "emails", "reports", "personnel"])
        year = random.randint(2020, 2025)
        month = random.randint(1, 12)
        
        if file_type == "logs":
            path = os.path.join(BASE_DIR, "corporate", corp, "servers", f"server-{{random.randint(1,20)}}", "logs", str(year), str(month), f"{{generate_timestamp().split(' ')[0]}}.log")
            create_file_with_content(path, lambda: "".join(generate_log_entry() for _ in range(random.randint(50, 500))))
        
        elif file_type == "emails":
            path = os.path.join(BASE_DIR, "corporate", corp, "comms", "internal", str(year), f"email_archive_{{i}}.eml")
            create_file_with_content(path, generate_email)

        file_count += 1
        print(f"\rProgresso: [{{file_count}}/{{TOTAL_FILES}}]", end="")

    # Gerar ficheiros de lore (fragmentos, manifestos)
    for i in range(NUM_LORE_FILES):
        file_type = random.choice(["fragments", "manifestos", "encrypted"])
        if file_type == "encrypted":
            path = os.path.join(BASE_DIR, "lore", file_type, f"data_shard_{{random.randint(1000,9999)}}.enc")
            create_file_with_content(path, lambda: f"BEGIN PGP MESSAGE-----\n{{generate_random_text(random.randint(1000, 5000))}}\n-----END PGP MESSAGE")
        else:
            path = os.path.join(BASE_DIR, "lore", file_type, f"fragment_{{i}}.txt")
            create_file_with_content(path, lambda: f"// FRAGMENT RECOVERED\n// SUBJECT: {{random.choice(CONCEPTS)}}\n\n{{generate_random_text(300)}}")
        
        file_count += 1
        print(f"\rProgresso: [{{file_count}}/{{TOTAL_FILES}}]", end="")

    # Gerar ficheiros diversos (pessoais, temporários)
    for i in range(NUM_MISC_FILES):
        path = os.path.join(BASE_DIR, "misc", "temp", ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".tmp")
        create_file_with_content(path, generate_random_text)
        file_count += 1
        print(f"\rProgresso: [{{file_count}}/{{TOTAL_FILES}}]", end="")

    end_time = time.time()
    print(f"\n\n--- BIG BANG CONCLUÍDO ---")
    print(f"Realidade forjada em {{end_time - start_time:.2f}} segundos.")
    print(f"Explore o seu novo universo em '{{BASE_DIR}}'.")


if __name__ == "__main__":
    main()