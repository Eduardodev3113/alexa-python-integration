# Assistente Pessoal com Alexa + Python

Controle seu PC com a voz usando a Alexa como interface. Fale um comando, o Python executa no seu computador.

---

## Como funciona

```
Você fala → Alexa ouve → chama a Skill → servidor Python recebe → executa no PC
```

---

## Estrutura do projeto

```
assistente-alexa/
│
├── app.py              # Servidor Flask + handlers da Alexa
├── acoes.py            # Todas as ações que o PC pode executar
├── iniciar.bat         # Sobe tudo automaticamente com 2 cliques
├── requirements.txt    # Dependências do projeto
├── .env                # Seus contatos privados (não sobe pro GitHub)
├── .env.example        # Modelo do .env para quem clonar
└── .gitignore
```

---

## ⚙️ Requisitos

- Python 3.12+
- Conta gratuita na [Alexa Developer Console](https://developer.amazon.com/alexa/console/ask)
- Conta gratuita no [ngrok](https://ngrok.com)
- Windows 10/11

---

## Instalação

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/alexa-python-integration.git
cd alexa-python-integration/assistente_alexa
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure o ngrok**
```bash
ngrok config add-authtoken SEU_TOKEN_AQUI
```
> Seu token está em [ngrok.com/dashboard](https://dashboard.ngrok.com) → Your Authtoken

---

## Como usar no dia a dia

Dê dois cliques no `iniciar.bat` — ele sobe o servidor Python e o ngrok automaticamente.

O domínio ngrok já está fixo (`sippingly-scalene-abrielle.ngrok-free.dev`), então a URL nunca muda e você não precisa atualizar nada na Alexa.

---

##  Comandos disponíveis

Após falar **"Alexa, abrir meu assistente"**, você pode dizer:

### Navegadores
| Comando | Ação |
|---|---|
| "abrir chrome" | Abre o Google Chrome |
| "abrir brave" | Abre o Brave |
| "abrir firefox" | Abre o Firefox |

### Programas
| Comando | Ação |
|---|---|
| "abrir spotify" | Abre o Spotify |
| "abrir vs code" | Abre o VS Code |
| "abrir calculadora" | Abre a Calculadora |
| "abrir bloco de notas" | Abre o Bloco de Notas |
| "abrir paint" | Abre o Paint |
| "abrir explorador" | Abre o Explorador de Arquivos |
| "abrir word" | Abre o Word |
| "abrir excel" | Abre o Excel |

### Sites
| Comando | Ação |
|---|---|
| "abrir youtube" | Abre o YouTube |
| "abrir google" | Abre o Google |
| "abrir gmail" | Abre o Gmail |
| "abrir whatsapp" | Abre o WhatsApp Web |
| "abrir instagram" | Abre o Instagram |
| "abrir netflix" | Abre a Netflix |
| "abrir github" | Abre o GitHub |
| "abrir sigaa" | Abre o SIGAA |

###  Sistema
| Comando | Ação |
|---|---|
| "desligar" | Desliga o PC em 10 segundos |
| "reiniciar" | Reinicia o PC em 10 segundos |
| "cancelar desligamento" | Cancela o desligamento |

###  Encerrar
| Comando | Ação |
|---|---|
| "fechar" / "cancelar" / "parar" | Encerra o assistente |

---

##  Adicionando novos comandos

Abra o `acoes.py` e adicione uma linha no dicionário correspondente:

**Novo programa:**
```python
PROGRAMAS = {
    "steam": (["steam"], [r"C:\Program Files (x86)\Steam\steam.exe"]),
}
```

**Novo site:**
```python
SITES = {
    "twitter": "https://twitter.com",
}
```

Não precisa mexer em mais nada — o código já percorre os dicionários automaticamente.

---

## 🔧 Configuração da Alexa (primeira vez)

1. Acesse [developer.amazon.com/alexa/console/ask](https://developer.amazon.com/alexa/console/ask)
2. Crie uma Skill do tipo **Custom** em **Português (BR)**
3. **Invocation name:** `meu assistente`
4. Crie um Intent chamado `ComandoIntent` com um slot `comando` do tipo `AMAZON.SearchQuery`
5. Adicione as utterances:
   ```
   abrir {comando}
   abre {comando}
   executar {comando}
   execute {comando}
   ```
6. Em **Endpoint → HTTPS**, cole a URL do ngrok:
   ```
   https://sippingly-scalene-abrielle.ngrok-free.dev
   ```
7. Selecione o certificado: *My development endpoint is a sub-domain of a domain that has a wildcard certificate*
8. Salve e clique em **Build Skill**

---

## 📦 Dependências

```
flask
ask-sdk-core
flask-ask-sdk
python-dotenv
```

---

## 📝 Licença

MIT — use à vontade, modifique e compartilhe.
