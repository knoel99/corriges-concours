import math
import inspect
import unittest
import matplotlib

matplotlib.use("Agg")
import numpy as np
import programmes as p


class Controles(unittest.TestCase):
    def test_statistiques_et_traitement(self):
        a = [1, 2, 5]
        self.assertEqual(p.somme(a), 8)
        self.assertAlmostEqual(p.moyenne(a), 8 / 3)
        self.assertAlmostEqual(p.variance(a), 26 / 9)
        self.assertEqual(p.variance([7]), 0)
        np.testing.assert_allclose(p.traitement([a, [0, 3, 6]]), [[8 / 3, 26 / 9], [3, 6]])
        self.assertEqual(p.variance(np.array([1e12 + 1, 1e12 - 1])), 1)

    def test_regression_simple(self):
        x = [8, 2, 5, -4]
        y = [1.25 - 2.5 * t for t in x]
        np.testing.assert_allclose(p.regression_lineaire(x, y), [1.25, -2.5])
        with self.assertRaises(ValueError):
            p.regression_lineaire([4] * 3, [1, 3, 4])

    def test_trace(self):
        fig, ax = p.tracer_regression([3, 0, 1], [7, 1, 3])
        self.assertEqual(len(ax.lines), 2)
        np.testing.assert_allclose(ax.lines[0].get_ydata(), [7, 1, 3])
        np.testing.assert_allclose(ax.lines[1].get_xdata(), [0, 3])
        np.testing.assert_allclose(ax.lines[1].get_ydata(), [1, 7])
        p.plt.close(fig)

    def test_ponderation_telle_qu_imprimee(self):
        valeurs = [[1, 1], [3, 2], [6, 1]]
        fonctions = [lambda t: 1, lambda t: t]
        a = p.regression_lineaire_gen([0, 1, 2], valeurs, fonctions)
        np.testing.assert_allclose(a, [17 / 18, 5 / 2], atol=1e-12)
        with self.assertRaises(ValueError):
            p.regression_lineaire_gen([0, 1, 2], [[1, 0], [3, 2], [6, 1]], fonctions)

    def test_bases_non_affines(self):
        x = [0., 1., 2., 3., 4.]
        yv = [[2 - z + 3 * z**2, 1 + z] for z in x]
        a = p.regression_lineaire_gen(x, yv, [lambda t: 1, lambda t: t, lambda t: t**2])
        np.testing.assert_allclose(a, [2, -1, 3], atol=1e-11)

    def test_integration_trapezes(self):
        self.assertEqual(p.aire([0, 1, 3], [2, 5, 11]), 19.5)
        self.assertEqual(p.aire([2], [8]), 0)
        with self.assertRaises(ValueError):
            p.aire([2, 1], [3, 4])

    def test_derivees_par_differences_centrees(self):
        delta = 1e-6
        f, a, b = 1.7, 2.3, 0.8
        da = (p.G(f, a + delta, b) - p.G(f, a - delta, b)) / (2 * delta)
        db = (p.G(f, a, b + delta) - p.G(f, a, b - delta)) / (2 * delta)
        self.assertAlmostEqual(p.dG_da0(f, a, b), da, places=8)
        self.assertAlmostEqual(p.dG_da1(f, a, b), db, places=8)

    def test_gradient_depuis_un_point_non_stationnaire(self):
        f = [.5, 1, 2, 3, 4]
        Su = [2 / (1 + fi**2) for fi in f]
        fit = p.methode_gradient(p.G, p.dG_da0, p.dG_da1, Su, f, 0.05, 1.6, 1.2, 1e-11)
        np.testing.assert_allclose(fit, (2, 1), atol=2e-9, rtol=0)
        self.assertAlmostEqual(p.aire(f, Su), 123 / 68)

    def test_non_annulation_des_composantes(self):
        def affine(x, a, b):
            return a + b*x
        # Au départ, g0 = -g1 = 8. Aucune composante n’est stationnaire.
        x = [0., 1.0]
        y = [-8., 4.]
        fit = p.methode_gradient(affine, lambda x, a, b: 1,
                                lambda x, a, b: x, y, x, .1, 0., 0., 1e-11)
        np.testing.assert_allclose(fit, (-8, 12), atol=1e-9, rtol=0)

    def test_force_valeur_et_signe(self):
        f = [.5, 1, 2, 3, 4]
        Su = [2 / (1 + fi**2) for fi in f]
        gamma, T = 1e-8, 300
        coef = math.sqrt(2 * math.pi * gamma * 1.380649e-23 * T / (123 / 68))
        for U in [1e-3, -1e-3, 0]:
            force = p.configurer_force(U, gamma, T, 1e-10)
            self.assertEqual(list(inspect.signature(force).parameters),
                             ["Su", "f", "h", "a00", "a10"])
            res = force(Su, f, .05, 2., -1.)
            self.assertTrue(math.isclose(res, U * coef, rel_tol=1e-13, abs_tol=0))
        with self.assertRaises(ValueError):
            force([0, 0], [1, 2], .05, 2., 1.)

if __name__ == "__main__":
    unittest.main(verbosity=2)
