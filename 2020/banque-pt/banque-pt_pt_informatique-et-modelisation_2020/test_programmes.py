import cmath
import math
from pathlib import Path
import struct
import tempfile
import unittest
import wave
import programmes as p


class Reverberation(unittest.TestCase):
    def proches(self, lhs, rhs):
        self.assertEqual(len(lhs), len(rhs))
        for a, b in zip(lhs, rhs):
            self.assertLess(abs(a - b), 1e-8)

    def test_champ_energie(self):
        eps, S, e, Q = 1e-11, 1e-4, 1e-5, 2e-10
        C = eps * S / e
        self.assertAlmostEqual(C / 1e-10, 1)
        F = Q * Q / (2 * eps * S)
        E = lambda ep: Q * Q * ep / (2 * eps * S)
        self.assertAlmostEqual((E(e + 1e-7) - E(e)) / (F * 1e-7), 1)
        self.assertAlmostEqual(E(e) / (Q * Q / (2 * C)), 1)

    def test_impedance_et_admittance(self):
        k, m, lam, R, L, C, alpha, S, pression = 8, 0.4, 0.5, 2, 0.25, 0.2, 0.4, 2, 0.8
        for w in (0.25, 1, 3, 12):
            D = k - m*w*w + 1j*w*lam
            E = 1/C - L*w*w + 1j*w*R
            Z0 = E / (1j*w)
            q = alpha * S * pression / (D*E - alpha**2)
            X = -E*q/alpha
            self.assertLess(abs(D*X + alpha*q + S*pression), 1e-12)
            B = alpha**2 / w**2
            Rm, Lm, Cm = B / lam, B / k, m / B
            Zm = 1/(1/Rm + 1/(1j*w*Lm) + 1j*w*Cm)
            self.assertLess(abs(1j*w*D*q/(alpha*S) - pression/(Z0+Zm)), 1e-12)

    def test_signaux_et_trace(self):
        self.assertEqual((len(p.tps), p.tps[0], p.tps[-1]), (1001, 0, 10))
        self.proches(p.sigh([0, 0.25]), [1, math.exp(-0.25)])
        self.proches(p.sigx([0, 1]), [0.6, -1.4])
        from matplotlib import pyplot as plt
        fig, ax = p.tracer(p.tps)
        self.assertEqual([l.get_label() for l in ax.lines], ['x(t)', 'h(t)'])
        self.assertEqual([l.get_color() for l in ax.lines], ['blue', 'green'])
        self.assertEqual(ax.get_xlabel(), 'temps (s)')
        self.assertEqual(ax.get_ylim(), (-1.5, 2))
        self.proches(ax.get_yticks(), [i/2 for i in range(-3, 5)])
        plt.close(fig)

    def test_convolution_et_dernier_rectangle(self):
        x, h, t = [1, 2, 3], [1, 0, 2], [0, 0.5, 1]
        self.proches(p.convolution(x, h, t), [2.5, 1, 1])
        self.proches(p.convolution_tfd(x, h, 0.5, False), [2.5, 1, 1])
        self.proches(p.convolution_tfd(x, h, 0.5), [2.5, 4, 2.5])

    def test_transformees_et_produit(self):
        x = [1+2j, 3, -4j, 7, 2j]
        self.proches(p.Fourier_directe_inverse(p.Fourier_directe(x)), x)
        self.proches(p.Fourier_directe([1, 0, 0, 0]), [1]*4)
        self.proches(p.produit([1j, 2], [1j, 3]), [-1, 6])
        with self.assertRaises(ValueError):
            p.produit([1], [1, 2])

    def test_fft_et_tailles(self):
        for N in (1, 2, 4, 8, 16, 32):
            x = [cmath.exp(2j * math.pi * k / N) + k for k in range(N)]
            self.proches(p.Fourier_rapide(x, N), p.Fourier_directe(x))
            self.proches(p.Fourier_rapide_inverse(p.Fourier_rapide(x, N), N), x)
        with self.assertRaises(ValueError):
            p.Fourier_rapide([1, 2, 3], 3)
        self.assertEqual([p.nextpow2(n) for n in (1, 2, 3, 7, 8, 9, 189100)],
                         [1, 2, 2, 4, 8, 8, 131072])

    def test_zeros_et_repliement(self):
        x = [1, 2, 3]
        self.assertEqual(p.addzeros(x, 4), [1, 2, 3, 0])
        self.assertEqual(x, [1, 2, 3])
        with self.assertRaises(ValueError):
            p.addzeros(x, 2)
        a = p.Fourier_rapide(p.addzeros(x, 4), 4)
        self.proches(p.Fourier_rapide_inverse(p.produit(a, a), 4), [10, 4, 10, 12])

    def test_mots_pcm(self):
        self.assertEqual((-32768).to_bytes(2, 'little', signed=True).hex(), '0080')
        self.assertEqual(int.from_bytes(bytes.fromhex('2a00'), 'little', signed=True), 42)
        self.assertEqual(b''.join(p.coder_paire(2, -1, 2)), struct.pack('<hh', 32767, -16384))
        self.assertEqual(b''.join(p.coder_paire(0, 0, 0)), bytes(4))

    def test_ecriture_et_silence(self):
        with tempfile.TemporaryDirectory() as td:
            dest = Path(td) / 'stereo.wav'
            p.creawave_2oct([2, -1], [1, 0], dest)
            self.assertEqual(p.extrawave_2oct(dest), ([32767, -16384], [16384, 0]))
            with wave.open(str(dest), 'rb') as f:
                self.assertEqual(f.getnframes(), 2)
                self.assertEqual(f.readframes(1), struct.pack('<hh', 32767, 16384))
            p.creawave_2oct([0]*3, [0]*3, dest)
            self.assertEqual(p.extrawave_2oct(dest), ([0]*3, [0]*3))

    def test_convolution_stereo_complete(self):
        def reference(x, h):
            y = [0] * (len(x) + len(h) - 1)
            for i, a in enumerate(x):
                for j, b in enumerate(h):
                    y[i+j] += a*b
            return y
        with tempfile.TemporaryDirectory() as td:
            a, b, c = [Path(td) / name for name in ('a.wav', 'b.wav', 'c.wav')]
            p.creawave_2oct([0, 1, 2], [-1, 0, 1], a)
            p.creawave_2oct([3, 0, 1], [0, 2, -3], b)
            p.convolution_reverb(a, b, c)
            g, d = p.extrawave_2oct(c)
            u, v = p.extrawave_2oct(a)
            r, s = p.extrawave_2oct(b)
            yg, yd = reference(u, r), reference(v, s)
            M = max(map(abs, yg + yd))
            self.proches(g, [round(y*32767/M) for y in yg])
            self.proches(d, [round(y*32767/M) for y in yd])
            self.assertEqual(len(g), 5)
            self.assertNotEqual(g[-1], 0)


if __name__ == '__main__':
    unittest.main()
