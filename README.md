# UniMiB-Lab

Libreria Python di funzioni per UniMiB-Lab.

## Installazione

### 1. Posizionarsi nella cartella di lavoro

Sostituisci `/path/to/your/working/directory` con la cartella dove vuoi lavorare ai tuoi progetti Python.

```bash
cd /path/to/your/working/directory
```

### 2. Creare e attivare un ambiente virtuale

```bash
python3 -m venv .venv
# Su Linux/Mac:
source .venv/bin/activate
# Su Windows (Prompt dei comandi):
.venv\Scripts\activate
```

### 3. Installare la libreria in modalità "editable"

Sostituisci `/path/to/my/custom/library` con il percorso dove hai clonato o copiato la cartella della libreria UniMiB-Lab.

```bash
cd /path/to/my/custom/library
pip install -e .
```

> L'opzione `-e` ("editable") permette di vedere subito le modifiche fatte al codice della libreria senza dover reinstallare.

## Utilizzo

Dopo l’installazione, puoi importare la libreria in qualsiasi script Python eseguito nello stesso ambiente virtuale:

```python
from unimib_lab import import_txt, fit_leastsquares, plot_errorbar
```

## Note

Per disattivare l'ambiente virtuale:

```bash
deactivate
```
