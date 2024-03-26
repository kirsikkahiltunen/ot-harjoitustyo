import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein_alussa(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.00)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 8.00)

    def test_saldo_ei_vahene_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_metodi_palautaa_True_jos_rahat_riittävät(self):
        self.assertEqual(self.maksukortti.ota_rahaa(300), True)

    def test_metodi_palauttaa_False_jos_rahat_eivät_riitä(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

    def test_saldo_euroina_tulostuu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

