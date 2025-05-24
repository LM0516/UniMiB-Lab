import matplotlib.pyplot as plt
import numpy as np

def plot_errorbar(x, y, x_err=None, y_err=None, xlabel=None, ylabel=None, title=None):
    """
    Funzione per la creazione di un grafico a dispersione con barre di errore.
    Parametri:
    x : array-like
        Valori sull'asse x.
    y : array-like
        Valori sull'asse y.
    x_err : array-like, optional
        Barre di errore per i valori sull'asse x.
    y_err : array-like, optional
        Barre di errore per i valori sull'asse y.
    xlabel : str, optional
        Etichetta per l'asse x.
    ylabel : str, optional 
        Etichetta per l'asse y.
    title : str, optional
        Titolo del grafico.
    """
    plt.figure(figsize=(12, 6))
    plt.errorbar(
        x,
        y,
        yerr=y_err,
        xerr=x_err,
        c="r",
        label="Dati sperimentali",
        fmt="o",
        markersize=4,
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_fit(x_data, y_data, model, params, x_err=None, y_err=None, xlabel=None, ylabel=None, title=None):
    """
    Funzione per la creazione di un grafico a dispersione con barre di errore e il modello di fit.
    Parametri:
    x_data : array-like
        Valori sull'asse x dei dati sperimentali.
    y_data : array-like
        Valori sull'asse y dei dati sperimentali.
    model : callable
        Funzione modello da adattare ai dati. Deve accettare i parametri come argomenti.
    params : tuple
        Valori dei parametri del modello da utilizzare per il fit.
    x_err : array-like, optional
        Barre di errore per i valori sull'asse x.
    y_err : array-like, optional
        Barre di errore per i valori sull'asse y.
    xlabel : str, optional
        Etichetta per l'asse x.
    ylabel : str, optional 
        Etichetta per l'asse y.
    title : str, optional
        Titolo del grafico.
    """
    
    plt.figure(figsize=(12, 6))
    
    # Dati sperimentali
    plt.errorbar(
        x_data,
        y_data,
        yerr=y_err,
        xerr=x_err,
        c="r",
        label="Dati sperimentali",
        fmt="o",
        markersize=4,
    )
    
    x_fit = np.linspace(np.min(x_data), np.max(x_data), 100)
    y_fit = model(x_fit, *params)
    
    plt.plot(x_fit, y_fit, c="b", label="Fit")
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()