import math
from pathlib import Path
import sqlite3
import unittest
import programmes as p


class Moteur(unittest.TestCase):
    def test_cycle(self):
        gamma, alpha, TB, TD = 1.4, 8, 300, 1600
        TC = TB * alpha**(gamma-1)
        TE = TD / alpha**(gamma-1)
        self.assertAlmostEqual(1 - (TE-TB)/(TD-TC), 1-alpha**(1-gamma))

    def test_raccordement(self):
        # La variable réduite z détermine epsilon, puis U/f0 et les deux raccords.
        for z in (0.001, 0.02, 0.1):
            eps = 1 + math.expm1(-z)/z
            d, f0 = 1.3, 2
            U = f0*d*z/eps
            ell = eps * U / f0
            a = f0/(eps*U)
            theta2 = lambda x: 1+a*(x-ell)+a*d*(-math.expm1((x-ell)/d))
            pente2 = lambda x: a*(-math.expm1((x-ell)/d))
            self.assertAlmostEqual(theta2(0), 1-eps)
            self.assertAlmostEqual(pente2(0), (1-eps)/d)
            self.assertAlmostEqual(theta2(ell), 1)
            self.assertAlmostEqual(pente2(ell), 0)

    def test_capteur_et_unites(self):
        self.assertAlmostEqual(p.vitesse_moteur(1/14000), 7000)
        self.assertAlmostEqual(p.vitesse_moteur(0.001), 500)
        with self.assertRaises(ValueError):
            p.vitesse_moteur(0)
        self.assertEqual(320, int('000140', 16))
        self.assertEqual(3 * 2**13, 3 * 1024 * 8)

    def test_indices_aux_bornes(self):
        A = [0.295, 0.390, 0.480, 0.565]
        for n, v in enumerate(A[:-1]):
            self.assertEqual(p.Indice(A, v), n)
        self.assertEqual(p.Indice(A, .435), 1)
        with self.assertRaises(ValueError):
            p.Indice(A, A[-1])

    def test_interpolation_et_sous_table(self):
        P = [.295, .39, .48]
        N = [600, 900, 1300, 1700]
        T = [[2.42,3.454,4.408],[2.702,3.776,4.852],
             [3.064,4.162,5.248],[3.27,4.412,5.552]]
        ST = p.sous_table(T, P, N, .435, 1500)
        self.assertEqual(len(p.T),13)
        self.assertTrue(all(len(ligne)==7 for ligne in p.T))
        self.assertEqual(p.T[6][4],3.388)
        self.assertEqual(ST,p.sous_table(p.T,p.P,p.Nm,.435,1500))
        self.assertEqual(ST, [[4.162,5.248,.39,1300],[4.412,5.552,.48,1700]])
        for i, n in enumerate(N[-2:]):
            for j, v in enumerate(P[-2:]):
                self.assertAlmostEqual(p.interpol(ST, v, n), ST[i][j])
        self.assertAlmostEqual(p.interpol(ST,.435,1500),4.8435)

    def test_pivot(self):
        A = [[0,2,1],[1,1,0],[2,3,4]]
        for res, exact in zip(p.gauss(A,[-1,1,12]),[3,-2,3]):
            self.assertAlmostEqual(res,exact)
        with self.assertRaises(ValueError):
            p.gauss([[1,2],[1,2]], [1,2])

    def test_euler_et_cascade(self):
        self.assertEqual(p.Euler(1, 2, .25, 1, 0), .75)
        self.assertEqual(p.richesse(1, 2, 1, .25, 1, 0, 4), (.875,1))
        self.assertEqual(p.sonde(1), .1)
        self.assertEqual(p.sonde(1.01), .9)

    def test_changement_de_phase(self):
        args = (1.03,.95,.8,.0123)
        t, a = p.duree_injection(.1,*args,0,.001)
        self.assertAlmostEqual(a,.8*.0123*.001)
        self.assertAlmostEqual(t,1.03*.0123+a)
        _, b = p.duree_injection(.9,*args,a,.001)
        self.assertAlmostEqual(b,-a)
        _, c = p.duree_injection(.9,*args,b,.001)
        self.assertAlmostEqual(c,-2*a)
        _, e = p.duree_injection(.1,*args,c,.001)
        self.assertAlmostEqual(e,a)

    def test_simulation_complete(self):
        temps,r,it,u = p.simulation_sujet()
        self.assertEqual([len(a) for a in (temps,r,it,u)], [375001]*4)
        self.assertAlmostEqual(temps[-1],.75)
        instants = [i for i in range(1,len(u)) if u[i] != u[i-1]]
        self.assertEqual([i//3750 for i in instants], [25,42,58,70,83,94])
        self.assertTrue(all(i % 3750 == 0 and u[i] == p.sonde(r[i]) for i in instants))
        self.assertAlmostEqual(max(r),1.018105158,8)
        self.assertAlmostEqual(r[-1],.992762276,8)
        for k in (5,3750,71234):
            self.assertIn(u[k],[.1,.9])
        from matplotlib import pyplot as plt
        fig,ax = p.tracer(temps[::1000],r[::1000])
        self.assertEqual(ax.lines[0].get_label(),'richesse')
        plt.close(fig)

    def test_requetes_sql(self):
        sql=(Path(__file__).parent / 'requetes.sql').read_text()
        q1,q2=sql.split('-- I25')
        with sqlite3.connect(':memory:') as db:
            db.execute('CREATE TABLE table_injection (Id, Pression, Rotation, Durée_injection, Qualité)')
            rows=[(1,.30,1300,4,99),(2,.40,1700,5,99),(3,.35,1500,6,97),
                  (4,.35,1500,7,95),(5,.50,1500,8,100)]
            db.executemany('INSERT INTO table_injection VALUES (?,?,?,?,?)',rows)
            db.executescript(q1)
            self.assertEqual(db.execute('SELECT count(*) FROM table_injection_95').fetchone(),(4,))
            self.assertEqual(set(db.execute(q2)),{(.30,1300,4),(.40,1700,5)})
            db.execute('DELETE FROM table_injection_95')
            self.assertEqual(list(db.execute(q2)),[])


if __name__ == '__main__':
    unittest.main()
