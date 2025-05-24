# Esempio di test per unimi_lab
import unittest
from unimib_lab import import_txt, convert_latex, fit_leastsquares, plot_errorbar, plot_fit
import numpy as np

class TestEsempio(unittest.TestCase):
    def test_import_txt(self):
        # Test di esempio: verifica che venga restituito un array numpy
        arr = import_txt('tests/data/test.txt')  # Assicurati che il file esista o modifica il path
        self.assertIsInstance(arr, np.ndarray)

    def test_convert_latex(self):
        # Uso un file di esempio invece di una stringa
        convert_latex("data/test.txt")
        # Non serve assert, la funzione salva un file

    def test_fit_leastsquares(self):
        # Uso dati di esempio e la funzione con i parametri corretti
        x = np.array([1, 2, 3, 4])
        y = np.array([2, 4, 6, 8])
        dy = np.array([0.1, 0.1, 0.1, 0.1])
        # fit_leastsquares(x, y, dy, funzione, p0)
        def f(x, a, b):
            return a * x + b
        p0 = [1, 0]
        result = fit_leastsquares(x, y, dy, f, p0)
        self.assertEqual(len(result), 2)  # parametri e covarianza

    def test_plot_errorbar(self):
        # Test di esempio: verifica che la funzione non sollevi errori
        x = np.array([0, 1, 2])
        y = np.array([1, 2, 3])
        yerr = np.array([0.1, 0.2, 0.1])
        try:
            plot_errorbar(x, y, yerr)
        except Exception as e:
            self.fail(f"plot_errorbar ha sollevato un'eccezione: {e}")

    def test_plot_fit(self):
        # Test di esempio: verifica che la funzione non sollevi errori
        x = np.array([0, 1, 2])
        y = np.array([1, 2, 3])
        def model(x, a, b):
            return a * x + b
        params = [1, 0]
        try:
            plot_fit(model, x, y, params)
        except Exception as e:
            self.fail(f"plot_fit ha sollevato un'eccezione: {e}")

if __name__ == "__main__":
    unittest.main()
