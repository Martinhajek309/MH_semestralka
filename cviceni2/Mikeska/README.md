
# Vytvoření Virtual Environment

## Příprava

Ujistěte se, že máte nainstalován Python 3.8 nebo novější.

## Kroky

### 1. Otevřete terminál
Navigujte do složky projektu:
```bash
cd cviceni2
```

### 2. Vytvořte virtuální prostředí
```bash
python -m venv venv
```

### 3. Aktivujte virtuální prostředí

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Aktualizujte pip
```bash
pip install --upgrade pip
```

### 5. Nainstalujte dependence
Pokud máte `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Deaktivace
Chcete-li ukončit virtuální prostředí:
```bash
deactivate
```
