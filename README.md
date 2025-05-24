# UniMiB-Lab

Libreria Python di funzioni per UniMiB-Lab.

## Installazione

### 1. Posizionarsi nella cartella di lavoro

```bash
cd /path/to/your/working/directory
```

### 2. Attivare l'ambiente virtuale per quell'ambiente di lavoro

```bash
python3 -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv/Scripts/activate
```

### 3. Installare la libreria

```bash
cd ~/pash/to/my/custom/library
pip install -e
```

## Utilizzo

Una volta installata la libreria con `pip install -e .` è possibile utilizzarla in qualsiasi progetto (cartella) che usa lo stesso ambiente virtuale.

```python
from unimib_lab import import_txt, fit_leastsquares, plot_errorbar
```

## Note
Per disattivare l'ambiente virtuale:

```bash
deactivate
```
