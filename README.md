# Ohjelmistotekniikka, harjoitustyö


**Tähän repositorioon** toteutetaan kurssin *harjoitustyö*. Harjoitustyön aiheena on **tehtävägeneraattorisovellus**, jonka avulla käyttäjä pystyy harjoittelemaan fysiikan ja kemian laskutehtäviä.

Sovelluksen [release](https://github.com/kirsikkahiltunen/ot-harjoitustyo/releases/tag/viikko5)

Sovellusta voi testata ajamalla komennon poetry run invoke start. Mikäli haluat, voit myös tutustua sovelluksen graafiseen käyttöliittymään ajamalla komennon poetry run invoke start-GUI. Graafinen käyttöliittymä on vielä hyvin keskeneräinen, mutta kirjautumista voi kokeilla kirjoittamalla käyttäjätunnukseksi ja salasanaksi "Testi". 


### Dokumentaatio

- [vaatimusmäärittely](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [changelog](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [arkkitehtuuri](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

### Asennusohjeet

1. Kloonaa tämä repositorio omalle koneellesi
2. Asenna sovelluksen riippuvuudet terminaalissa ajamalla komento "poetry install"
3. Alusta tietokanta ajamalla komento "poetry run invoke initialize-db"
3. Käynnistä sovellus ajamalla komento "poetry run invoke start". Sovelluksen graafisen käyttöliittymän voi käynnistää komennolla "poetry run invoke start-GUI" (Huom! vain rekisteröityminen ja kirjautuminen toimii).

### Sovelluksen testaaminen 

Voit suorittaa testit kirjoittamalla terminaaliin komennon "poetry run invoke test"

Testikattavuusraportin saa luotua komennolla "poetry run invoke coverage-report"

Pylint-tarkistuksen pystyyy suorittamaan komennolla "poetry run invoke lint"