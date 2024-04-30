# Käyttöohje

1. Lataa ensiksi sovelluksen lähdekoodi viimeisimmästä releasesta
2. Asenna sovelluksen riippuvuudet terminaalissa ajamalla komento "poetry install"
3. Alusta tietokanta ajamalla komento "poetry run invoke initialize-db"
4. Käynnistä sovellus ajamalla komento "poetry run invoke start". Sovelluksen graafisen käyttöliittymän voi käynnistää komennolla "poetry run invoke start-GUI" (Huom! vain rekisteröityminen ja kirjautuminen toimii).


# Tekstipohjainen käyttöliittymä

## Rekisteröityminen

Jos olet käynnistänyt sovelluksen komennolla poetry run invoke start, tulostetaan terminaaliin kirjautumisvalikko, jossa on seuraavat valinnat:

"Hei! Tervetuloa käyttämään fysiikankertaus sovellusta

Valitse mitä haluat tehdä

1 kirjaudu sisään

2 rekisteröidy käyttäjäksi"

Valitse vaihtoehto 2 ja paina enter.

Tämän jälkeen tulostuu terminaaliin "käyttäjätunnus:", kirjoita nyt sinulle sopiva käyttäjätunnus ja paina enter.

Seuraavaksi tulostuu "salasana:", keksi itsellesi hyvä salasana ja paina enter. 

Nyt rekisteröityminen on valmis ja pääset seuraavaan näkymään.

## Kirjautuminen

"Hei! Tervetuloa käyttämään fysiikankertaus sovellusta

Valitse mitä haluat tehdä

1 kirjaudu sisään

2 rekisteröidy käyttäjäksi"

Valitse aloitusvalikossa vaihtoehto 1 ja paina enter.

Seuraavaksi tulostuu "käyttäjätunnus:", kirjoita nyt oma käyttäjätunnuksesi ja paina enter.

Tämän jälkeen tulostuu "salasana:", kirjoita nyt salasanasi ja paina enter.

Nyt kirjautuminen on valmis ja pääset seuraavaan näkymään.

## Tehtävä valikko

Kun olet kirjautunut sisään sovellukseen, näet tehtävävalikon, josta voit valita haluamasi fysiikan aihealuen, jota pääset harjoittelemaan.

Terminaaliin tulostuu "Anna harjoiteltavan kategorian numero:", anna nyt numero, joka vastaa sinua kiinnostavaa tehtäväkategoriaa ja paina enter.

Nyt pääset tehtävänäkymään. 

Mikäli et halua tehdä tehtäviä, vaan haluat lopettaa ohjelman suorittamisen, kirjoita terminaaliin "0" ja paina enter.


# Graafinen käyttöliittymä

## Rekisteröityminen

Jos olet käynnistänyt sovelluksen komennolla poetry run invoke start-GUI, näet ruudulle aukeavan ikkunan, jonka alimmalla rivillä on nappula "Rekisteröidy käyttäjäksi". Klikkaa tätä nappia, niin pääset rekisteröitymisnäkymään.

Rekisteröitymisnäkymässä on kolme avointa tekstikenttää: "Käyttäjänimi", "Salasana" ja "Salasana uudelleen". Täytä nämä kaikki kentät ja klikkaa nappia rekisteröidy.  

Nyt rekisteröityminen on valmis ja pääset kirjautumisnäkymään.

## Kirjautuminen

Syötä kirjautumisnäkymän tekstikenttään "Käyttäjänimi" luomasi käyttäjänimi ja kenttään "Salasana" oma salasanasi.

Klikkaa lopuksi "Kirjaudu" painiketta.

Nyt kirjautuminen on valmis ja pääset seuraavaan näkymään.

