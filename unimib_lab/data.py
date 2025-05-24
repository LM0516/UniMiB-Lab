import numpy as np

def import_txt(filename):
    """
    Funzione per importare i dati da un file di testo.
    Parametri:
    filename : str
        Nome del file di testo da cui importare i dati.
    Restituisce:
    data : DataFrame
        DataFrame contenente i dati importati dal file di testo.
    """
    try:
        data = np.loadtxt(filename, unpack=True)
        print(f"File {filename} caricato con successo.")
        print(f"Numero di colonne: {data.shape[0]}")
        print(f"Numero di righe: {data.shape[1]}")
        return data
    except FileNotFoundError:
        print(f"File {filename} non trovato.")
        return None

def convert_latex(filename):
    """
    Funzione per convertire un file di testo in formato LaTeX.
    Parametri:
    filename : str
        Nome del file di testo da convertire in LaTeX.
    Restituisce:
    latex_data : str
        Stringa contenente i dati in formato LaTeX.
    """
    try:
        data = np.loadtxt(filename, unpack=True)
        latex_data = "\\begin{tabular}{|c|c|c|}\n\\hline\n"
        for row in data.T:
            latex_data += " & ".join(map(str, row)) + " \\\\\n\\hline\n"
        latex_data += "\\end{tabular}"
        print(f"File {filename} convertito in LaTeX con successo.")
        return latex_data
    except FileNotFoundError:
        print(f"File {filename} non trovato.")
        return None