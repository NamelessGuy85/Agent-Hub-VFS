import os
import random
import datetime
import string
import time

# --- CONFIGURAÇÃO DO UNIVERSO (LOCALIZADO) ---
# Altere estes valores para moldar a sua realidade
BASE_DIR = "Agent-Hub-VFS-Gerado"
NUM_CORP_FILES = 2500
NUM_LORE_FILES = 500
NUM_MISC_FILES = 1000
TOTAL_FILES = NUM_CORP_FILES + NUM_LORE_FILES + NUM_MISC_FILES

# --- ELEMENTOS NARRATIVOS (LOCALIZADO) ---
CORPORACOES = ["ZetaTech", "CorpRival", "OmniGen", "Aetherion"]
PROJECTOS = ["Alpino", "Odisseia", "Helios", "Nyx"]
PESSOAL_CHAVE = ["Dr. Aris", "Kaelen", "Unidade 734", "O Arquivista"]
CONCEITOS = ["Fantasmas", "Ecos", "O Sinal", "A Falha"]

# --- GERADORES DE CONTEÚDO ---

def gerar_texto_aleatorio(comprimento=100):
    """Gera texto aleatório para preencher ficheiros."""
    chars = string.ascii_letters + string.digits + " \n\t."
    return ''.join(random.choice(chars) for _ in range(comprimento))

def gerar_timestamp():
    """Cria um timestamp no formato de log."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def gerar_entrada_log():
    """Gera uma linha de log de sistema variada."""
    niveis_log = ["INFO", "AVISO", "ERRO", "CRITICO", "DEBUG"]
    servicos = ["auth.service", "kernel.sys", "network.manager", "cron.job", "api.v3"]
    mensagens = [
        "Autenticação de utilizador bem-sucedida", "Tentativa de login falhada", "Memória do sistema a aproximar-se do limite",
        "Tempo de ligação esgotado", f"A executar tarefa agendada {random.randint(1000, 9999)}",
        f"Pacote de dados recebido de {random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        f"Exceção de ponteiro NULO no endereço de memória 0x{random.randint(0, 0xFFFFFFFF):08X}",
        "Regra de firewall #4815 bloqueou uma ligação de entrada."
    ]
    return f"{gerar_timestamp()} [{random.choice(niveis_log)}] ({random.choice(servicos)}): {random.choice(mensagens)}\n"

def gerar_email():
    """Gera um e-mail corporativo fictício."""
    corp_remetente = random.choice(CORPORACOES)
    corp_destinatario = random.choice(CORPORACOES)
    remetente = f"{random.choice(PESSOAL_CHAVE).lower().replace(' ', '.')}@{corp_remetente.lower()}.com"
    destinatario = f"{''.join(random.choices(string.ascii_lowercase, k=5))}@{corp_destinatario.lower()}.com"

    assuntos = [
        f"URGENTE: Relativamente ao Projeto {random.choice(PROJECTOS)}",
        "Revisão de Desempenho Semanal", "Paragem para Manutenção do Servidor",
        f"Atividade suspeita detetada no nó {random.randint(1, 100)}",
        f"Re: Pergunta sobre os {random.choice(CONCEITOS)}"
    ]
    
    # Adicionar pistas narrativas
    fragmentos_corpo = [
        "Precisamos de discutir as implicações das últimas descobertas.",
        "Parem de mencionar os 'Fantasmas' em comunicações abertas. Usamos canais designados por uma razão.",
        "Já viu o último relatório do Dr. Aris? É... preocupante.",
        "A CorpRival está a chegar demasiado perto da verdade sobre o Alpino.",
        "A quinta de servidores no setor Gama ficou em silêncio. Sem logs, apenas... silêncio. Está a acontecer de novo.",
        "Apague este e-mail depois de ler."
    ]

    corpo = f"De: {remetente}\nPara: {destinatario}\nAssunto: {random.choice(assuntos)}\n\n"
    corpo += f"A todos,\n\n{random.choice(fragmentos_corpo)}\n\n{gerar_texto_aleatorio(random.randint(200, 500))}\n\nCumprimentos."
    return corpo

# --- FUNÇÃO PRINCIPAL DE CRIAÇÃO ---

def criar_ficheiro_com_conteudo(path, gerador_conteudo):
    """Cria um ficheiro com conteúdo gerado, garantindo que o diretório exista."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", errors="ignore") as f:
            f.write(gerador_conteudo())
        return True
    except Exception as e:
        # print(f"Não foi possível criar o ficheiro {path}: {e}")
        return False

def main():
    """Ponto de entrada do gerador de universo."""
    print("--- PROTOCOLO BIG BANG INICIADO ---")
    print(f"A forjar um universo com {TOTAL_FILES} ficheiros em '{BASE_DIR}'...")
    
    if os.path.exists(BASE_DIR):
        print(f"AVISO: O diretório '{BASE_DIR}' já existe. Ficheiros podem ser sobrescritos.")
    
    contagem_ficheiros = 0
    tempo_inicio = time.time()

    # Gerar ficheiros corporativos (logs, emails, relatórios)
    for i in range(NUM_CORP_FILES):
        corp = random.choice(CORPORACOES)
        tipo_ficheiro = random.choice(["logs", "emails", "relatorios", "pessoal"])
        ano = random.randint(2020, 2025)
        mes = random.randint(1, 12)
        
        if tipo_ficheiro == "logs":
            path = os.path.join(BASE_DIR, "corporativo", corp, "servidores", f"servidor-{random.randint(1,20)}", "logs", str(ano), str(mes), f"{gerar_timestamp().split(' ')[0]}.log")
            criar_ficheiro_com_conteudo(path, lambda: "".join(gerar_entrada_log() for _ in range(random.randint(50, 500))))
        
        elif tipo_ficheiro == "emails":
            path = os.path.join(BASE_DIR, "corporativo", corp, "comms", "interno", str(ano), f"arquivo_email_{i}.eml")
            criar_ficheiro_com_conteudo(path, gerar_email)

        contagem_ficheiros += 1
        print(f"\rProgresso: [{contagem_ficheiros}/{TOTAL_FILES}]", end="")

    # Gerar ficheiros de lore (fragmentos, manifestos)
    for i in range(NUM_LORE_FILES):
        tipo_ficheiro = random.choice(["fragmentos", "manifestos", "encriptados"])
        if tipo_ficheiro == "encriptados":
            path = os.path.join(BASE_DIR, "lore", tipo_ficheiro, f"fragmento_dados_{random.randint(1000,9999)}.enc")
            criar_ficheiro_com_conteudo(path, lambda: f"BEGIN PGP MESSAGE-----\n{gerar_texto_aleatorio(random.randint(1000, 5000))}\n-----END PGP MESSAGE")
        else:
            path = os.path.join(BASE_DIR, "lore", tipo_ficheiro, f"fragmento_{i}.txt")
            criar_ficheiro_com_conteudo(path, lambda: f"// FRAGMENTO RECUPERADO\n// ASSUNTO: {random.choice(CONCEITOS)}\n\n{gerar_texto_aleatorio(300)}")
        
        contagem_ficheiros += 1
        print(f"\rProgresso: [{contagem_ficheiros}/{TOTAL_FILES}]", end="")

    # Gerar ficheiros diversos (pessoais, temporários)
    for i in range(NUM_MISC_FILES):
        path = os.path.join(BASE_DIR, "misc", "temp", ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".tmp")
        criar_ficheiro_com_conteudo(path, gerar_texto_aleatorio)
        contagem_ficheiros += 1
        print(f"\rProgresso: [{contagem_ficheiros}/{TOTAL_FILES}]", end="")

    tempo_fim = time.time()
    print(f"\n\n--- BIG BANG CONCLUÍDO ---")
    print(f"Realidade forjada em {tempo_fim - tempo_inicio:.2f} segundos.")
    print(f"Explore o seu novo universo em '{BASE_DIR}'.")


if __name__ == "__main__":
    main()