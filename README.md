# Fysiikan kertaus sovellus


**Tähän repositorioon** on toteutettu kurssin *Aineopintojen harjoitustyö: ohjelmistotekniikka, kevät 2024* harjoitustyö. Harjoitustyön aiheena on **tehtävägeneraattorisovellus**, jonka avulla käyttäjä pystyy harjoittelemaan fysiikan ja kemian laskutehtäviä.

Sovelluksen loppupalautuksen [release](https://github.com/kirsikkahiltunen/ot-harjoitustyo/releases/tag/Viikko6)

### Dokumentaatio

- [vaatimusmäärittely](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [changelog](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [arkkitehtuuri](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [käyttöohje](https://github.com/kirsikkahiltunen/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

### Asennusohjeet

1. Kloonaa tämä repositorio omalle koneellesi
2. Asenna sovelluksen riippuvuudet terminaalissa ajamalla komento "poetry install"
3. Alusta tietokanta ajamalla komento "poetry run invoke initialize-db"
4. Käynnistä sovellus ajamalla komento "poetry run invoke start".

### Sovelluksen testaaminen 

Voit suorittaa testit kirjoittamalla terminaaliin komennon "poetry run invoke test"

Testikattavuusraportin saa luotua komennolla "poetry run invoke coverage-report"

Pylint-tarkistuksen pystyyy suorittamaan komennolla "poetry run invoke lint"