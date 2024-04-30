### Viikko 3

- Hahmotelma graafisen käyttöliittymän kirjautumissivusta tehty
- Alustava luokka Card (löytyy tiedostosta cards.py) luotu ja siihen lisätty funktiot generate_variable ja solve
- Kolme testitapausta luotu luokalle Card
    - testi, joka tarkistaa, että luodun luokan variables -lista on tyhjä, kun mitään funktiota ei ole ajettu
    - testi, joka tarkistaa, että seed on arvoltansa None silloin kun sitä ei ole erikseen määritetty
    - testi, joka tarkistaa, että muuttujat tallennetaan onnistuneesti listaan variables

### Viikko 4

- Luokkaa Card muokattu vastaamaan toiminnallisuudeltaan paremmin lopullista käyttötarkoitusta
- Muutettu ja laajennettu luokan Card testitapauksia
    - luotu testit, jotka tarkistavat, että generate_variables funktio tallentaa generoidut arvot oikeisiin muuttujiin. 
- Luotu ja toteutettu terminaalikäyttöliittymä sovellukselle, jotta sovelluksen osia pääsee kokeilemaan jo ennen kuin graafinen käyttöliittymä on valmis (löytyy terminalui.py tiedostosta)
    - terminaalikäyttöliittymän kautta käyttäjä voi tehdä nyt paineeseen tai liike-energiaan liittyviä tehtäviä sekä tarkistaa, onko tehtävän ratkaisu oikein
- Kehitetty sovelluksen graafista käyttöliittymää eteenpäin
    - Käyttäjä voi nyt kokeilla kirjautumista oletussalasanoilla sekä testata rekisteröitymissivua (tietoja ei vielä talleneta tai etsitä tietokannasta)
- Sovelluksen rakennetta on hahmoteltu pidemmälle (lisätty services ja ui hakemistot ja index.py tiedosto)
- Koodin laatua on parannettu pylint:in kehotusten perusteella
- Alustava luokkakaavio ohjelman rakenteesta tehty arkkitehtuuri.md tiedostoon, joka löytyy dokumentaatio hakemistosta

### Viikko 5

- Luokkaa Card muokattu, lisätty get_hint funktio.
- TerminalUI:ssä uusi toiminnallisuus; laskuri, joka pitää kirjaa tehtyjen tehtävien yhteismäärästä sekä ensimmäisellä yrityksellä onnistuneiden tehtävien määrästä.
- Sovelluksen rakennetta muokattu tulevaa SQL tietokantaa varten, vielä tietokanta ei toimi.
- Tehty sekvenssikaavio, joka kuvaa Card-luokan toimintaa, kun käytetään TerminalUI:tä
- Lisätty testejä Card luokalle

### Viikko 6

- SQLite tietokanta otettu käyttöön
- Ohjelmaan lisätty kirjautuminen ja rekisteröityminen TerminalUI luokkaan.
- UserRepository luokkaan lisätty tietokantaoperaatioita.
- CardRepository luokkaan lisätty tietokantaoperaatioita.
- LoginView luokkaa muokattu niin, että kirjautuminen toimii tietokannasta löytyvillä tunnuksilla.
- CreateUserView luokkaa muokattu niin, että uudet tunnukset tallennetaan tietokantaan.
- ExerciseList luokkaa muokattu niin, että näkymässä listataan allekain exercises tietokannasta löytyvien tehtävien tehtäväkategoriat.
- Luotu uusia testejä TestUserRepo luokkaan.
- Lisätty uusi tehtävä "initialize_db" task.py tiedostoon.