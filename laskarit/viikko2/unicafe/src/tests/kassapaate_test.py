import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti_2e = Maksukortti(200)

    
    #alla olevat testit seuraavaan kommenttiin asti testaavat luodun kassapaatteen alkuasetuksia
    def test_luodun_kassapaatteen_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_luodun_kassapaatteen_edulliset_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luodun_kassapaatteen_maukkaat_maara_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    #alla olevat testit seuraavaan kommenttiin asti testaavat syo_edullisesti_kateisella funktion toimintaa
    def test_syo_edullisesti_kateisella_laskee_vaihtorahan_oikein(self):  
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_syo_edullisesti_kateisella_palauttaa_maksun_jos_maksu_ei_ole_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
    
    def test_syo_edullisesti_kateisella_ei_kasvata_muuttujaa_edulliset_jos_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kateisella_kasvattaa_kassan_saldoa_lounaan_hinnalla(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)

    def test_syo_edullisesti_kateisella_kasvattaa_muuttujan_edulliset_arvoa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)  
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    #alla olevat testit seuraavaan kommenttiin asti testaavat syo_maukkaasti_kateisella funktion toimintaa
    def test_syo_maukkaasti_kateisella_laskee_vaihtorahan_oikein(self):  
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_syo_maukkaasti_kateisella_palauttaa_maksun_jos_maksu_ei_ole_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
    
    def test_syo_maukkaasti_kateisella_ei_kasvata_muuttujaa_maukkaat_jos_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_kasvattaa_kassan_saldoa_lounaan_hinnalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)

    def test_syo_maukkaasti_kateisella_kasvattaa_muuttujan_maukkaat_arvoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)  
        self.assertEqual(self.kassapaate.maukkaat, 1)

    #alla olevat testit seuraavaan kommenttiin asti testaavat korttiostoa edullisen lounaan osalta
    def test_syo_edullisesti_kortilla_palauttaa_True_jos_kortilla_on_tarpeeksi_rahaa(self): 
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_syo_edullisesti_kortilla_kasvattaa_muuttujan_edulliset_arvoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) 
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kortilla_ei_kasvata_muuttujaa_edulliset_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_2e)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_edullisesti_kortilla_palauttaa_False_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_2e), False)

    def test_syo_edullisesti_kortilla_ei_muuta_myytyjen_edullisten_lounaiden_maaraa_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_2e)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kortilla_ei_muuta_kortin_saldoa_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_2e)
        self.assertEqual(str(self.maksukortti_2e), "Kortilla on rahaa 2.00 euroa")

    def test_syo_edullisesti_kortilla_ei_muuta_kateiskassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    #alla olevat testit seuraavaan kommenttiin asti testaavat korttiostoa maukkaan lounaan osalta
    def test_syo_maukkaasti_kortilla_palauttaa_True_jos_kortilla_on_tarpeeksi_rahaa(self): 
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_syo_maukkaasti_kortilla_kasvattaa_muuttujan_maukkaat_arvoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) 
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kortilla_ei_kasvata_muuttujaa_maukkaat_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_2e)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_maukkaasti_kortilla_palauttaa_False_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_2e), False)

    def test_syo_maukkaasti_kortilla_ei_muuta_myytyjen_maukkaiden_lounaiden_maaraa_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_2e)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_ei_muuta_kortin_saldoa_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_2e)
        self.assertEqual(str(self.maksukortti_2e), "Kortilla on rahaa 2.00 euroa")

    def test_syo_maukkaasti_kortilla_ei_muuta_kateiskassan_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_jos_kortille_yritetaan_ladata_negatiivinen_summa_kortin_saldo_ei_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kortille_rahaa_ladattaessa_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)



    
    


    

    

    

    

    

           