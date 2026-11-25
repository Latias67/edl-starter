# 🛠️ Installation

À faire **avant la première séance**. Vérifiez tout avec la dernière section.

---

## 1. uv (Python)

uv installe Python et les dépendances du projet. Il télécharge Python lui-même si besoin.

*macOS / Linux :*

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*Windows (PowerShell) :*

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Fermez et rouvrez le terminal.

---

## 2. Node.js 24 (frontend)

Il faut **Node.js 22.12 ou plus** (`node -v`). Sinon, installez Node 24 avec un gestionnaire de versions.

**macOS / Linux (nvm) :**

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.41.0/install.sh | bash
# fermez et rouvrez le terminal
nvm install 24
nvm alias default 24
```

**Windows (fnm, dans PowerShell) :**

```powershell
winget install Schniz.fnm
if (-not (Test-Path $PROFILE)) { New-Item $PROFILE -Force }
Add-Content $PROFILE 'fnm env --use-on-cd --shell powershell | Out-String | Invoke-Expression'
# fermez et rouvrez PowerShell
fnm install 24
fnm default 24
```

| Problème | Solution |
|----------|----------|
| `nvm` ou `fnm` introuvable | Rouvrez le terminal (et VS Code entièrement) |
| Windows : « l'exécution de scripts est désactivée » | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, puis rouvrez PowerShell |
| `node -v` affiche une ancienne version | Désinstallez l'ancien Node (installeur nodejs.org) |

---

## 3. Java (facultatif : bonus du TP 1)

Installez **Temurin 21** depuis [adoptium.net](https://adoptium.net/) (macOS, Linux et Windows).

---

## ✅ Vérification

```bash
uv --version
node -v          # v22.12 ou plus
java -version    # seulement pour le bonus Java
```
