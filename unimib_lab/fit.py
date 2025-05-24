from iminuit import Minuit
from iminuit.cost import LeastSquares
from scipy.stats import chi2

def fit_leastsquares(x_exp, y_exp, y_err, model, initial_params, limits=None):
    """Funzione per eseguire un fit ai dati sperimentali utilizzando il metodo dei minimi quadrati.
    Parametri:
    x_exp : array-like
        Valori sull'asse x dei dati sperimentali.
    y_exp : array-like
        Valori sull'asse y dei dati sperimentali.
    y_err : array-like
        Barre di errore per i valori sull'asse y.
    model : callable
        Funzione modello da adattare ai dati. Deve accettare i parametri come argomenti.
    initial_params : tuple
        Valori iniziali dei parametri del modello da ottimizzare.
    limits : dict, optional
        Dizionario contenente i limiti per i parametri. Le chiavi devono essere i nomi dei parametri
        e i valori tuple (min, max) che specificano i limiti inferiori e superiori.
    Restituisce:
    m : Minuit
        Oggetto Minuit contenente i risultati dell'ottimizzazione.  
    """
    least_squares = LeastSquares(x_exp, y_exp, y_err, model)

    m = Minuit(least_squares, *initial_params)

    if limits:
        for param_name, (lower, upper) in limits.items():
            if param_name in m.parameters:
                m.limits[param_name] = (lower, upper)

    print("Esecuzione dell'ottimizzazione...")
    m.migrad()

    if m.valid:
        try:
            print("Calcolo delle incertezze...")
            m.hesse()
        except RuntimeError as e:
            print(f"\nAvviso: non è stato possibile calcolare le incertezze. {e}")

    parameters = m.values
    errors = m.errors
    parameters_name = m.parameters
    ndof = len(x_exp) - len(initial_params)
    p_value = 1 - chi2.cdf(m.fval, ndof)

    print("\nParametri ottimizzati:")

    for i, param in enumerate(parameters):
        print(f"{parameters_name[i]}: {param} ± {errors[i]}")

    print(f"\nChi-quadro: {m.fval}")
    print("Numero di gradi di libertà:", ndof)
    print(f"Chi2/ndof: {m.fval/ndof}")
    print(f"P-value: {p_value}")

    print("\nInterpretazione del risultato:")

    # Interpretazione del risultato

    alpha_threshold = 0.05  # Soglia di significatività
    chi2_reduced = m.fval / ndof

    if p_value > alpha_threshold:
        print(f"\n✓ Il modello è compatibile con i dati (p > {alpha_threshold})")
    else:
        print(f"\n⚠ Il modello potrebbe non essere adeguato (p < {alpha_threshold})")
        
    if 0.9 < chi2_reduced < 1.1:
        print("✓ Il chi-quadro ridotto è vicino a 1, indicando un buon fitting")
    elif chi2_reduced < 0.9:
        print("⚠ Il chi-quadro ridotto è < 0.9, possibile sovrastima degli errori o overfit")
    elif chi2_reduced > 1.1:
        print("⚠ Il chi-quadro ridotto è > 1.1, possibile sottostima degli errori o modello inadeguato")

    return parameters, errors
