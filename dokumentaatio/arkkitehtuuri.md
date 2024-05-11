# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on pääasiassa mukaelma kurssin referenssisovelluksen kerrosarkkitehtuurista. Ohjelman koodi on src hakemiston sisällä jaettu hakemistoihin repositories ja ui. 
Sovelluksessa on käytössä Tkinter kirjaston avulla toteutettu graafinen käyttöliittymä, johon liittyvä koodi löytyy ui hakemistosta. Ohjelman suorittaminen graafisessa käyttöliittymässä alkaa kutsumalla index.py tiedostoa, joka kutsuu ui-hakemistossa olevia funktioita. Tietokantaoperaatioista vastaa repositories-hakemistosta löytyvät luokat CardRepository ja UserRepository. Tehtäväkortin sisältämän tiedon käsittelyyn käytetään cards.py tiedoston Card-luokkaa.

## Käyttöliittymä

Käyttöliittymässä on seuraavat näkymät:

- Kirjautumisnäkymä
- Rekisteröitymisnäkymä
- Tehtäväaiheiden listanäkymä
- Tehtävänäkymä

Käyttöliittymässä nämä kaikki on toteutettu omiin luokkiinsa, joista jokainen sijaitsee omassa python tiedostossa ui-alihakemistossa. Sovelluksen UI-luokka vastaa graafisessa käyttöliittymässä eri näkymien näyttämisestä, piilottamisesta ja tuhoamisesta. Käyttöliittymä kutsuu muita luokkia eri funktioiden ja metodien toteuttamiseen.

## Sovelluslogiikka

Sovelluksen logiikka perustuu pääasiassa luokkaan Card sekä luokkiin CardRepository ja UserRepository. Luokka Card vastaa tehtäväkortin (card) toiminnoista kuten muuttujien arvojen generoinnista, oikean vastauksen generoinnista ja tehtävänannon tulostamisesta. CardRepository vastaa niistä tehtäviin liittyvistä toiminnoista, joissa tehdään tietokantaoperaatioita tai vuorovaikutetaan läheisesti tietokantaoperaatioiden kesken. 

Sovelluksen käyttäjää ja luokkaa Card voidaan havainnollistaa seuraavalla kaaviolla:

```mermaid
 classDiagram
    User "1" <-- "*" Card

    class User{
        id
        username
        password
    }

    class Card{
        id
        category
        variables
        question
    }
```
Eli siis käyttäjä vuorovaikuttaa sovelluksessa Card luokan kanssa, joka kuvastaa tehtäväkorttia. Jokaisella käyttäjällä on käyttäjätunnus ja salasana sekä users tietokantataulussa id (integer primary key). Jokaisella kortilla on tehtävän id, kategorian numero, muuttujat ja kysymys (tehtävänanto). 

Sovelluksen luokkien suhdetta voidaan havainnollistaa seuraavalla luokkakaaviolla:

```mermaid
 classDiagram
    User "1" -- "*" Card
    User "1" -- "0..100" Deck
    Card "*" -- "1" Category
    Deck "1" -- "*" Card
    Deck "1" -- "0..1" Category 
```
Sovelluksessa on tehtäväkortteja, joita käyttäjällä voi olla useita, tehtävillä on sovelluksen suorituksenaikana yksi käyttäjä, joka ratkaisee tehtäviä ja saman kategorian tehtävät muodostavat kokonaisuuden. Eri kategorioiden thtävät muodostavat tehtäväpakan.
 
# Sovelluksen päätoiminnallissudet

### Käyttäjätunnuksen luominen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UserRepository
  User->>UI: click "Rekisteröidy" button
  UI->>UserRepository : create_user(käyttäjä, käyttäjä123)
  UserRepository->>UserRepository: find_user_by_username(käyttäjä)
  UserRepository-->>UI: True
  UI->>UI: _show_login
```
### Sisäänkirjautuminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UserRepository
  User->>UI: click "Kirjaudu" button
  UI->>UserRepository : login(käyttäjä, käyttäjä123)
  UserRepository->>UserRepository: find_user_by_username(käyttäjä)
  UserRepository-->>UI: True
  UI->>UI: _show_exercise_list_view
```

### Tehtävän valinta

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CardRepository
  participant Card
  User->>UI: click "Tee tehtävä" button
  UI->>UI : _show_exercise_view(exercise_id)
  UI->>CardRepository: get_question(exercise_id)
  CardRepository->>CardRepository: find_question_with_id(exercise_id)
  CardRepository->>CardRepository: get_variables(exercise_id)
  CardRepository->>Card: generate_variables(variable_info)
  Card-->>CardRepository: generated_variables
  CardRepository-->>UI: question
``` 
### Tehtävään vastaaminen

Jos tehtävän vastaus on oikein:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CardRepository
  participant Card
  User->>UI: click "Tarkista" button
  UI->>UI: _check_is_numeric()
  UI->>CardRepository : solve_exercise(exercise_id, 25)
  CardRepository->>CardRepository: find_operation(exercise_id)
  CardRepository->>Card: solve(operation, variables)
  Card-->>CardRepository: correct
  CardRepository-->>UI: True
``` 
Jos tehtävän vastaus on väärin:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CardRepository
  participant UserRepository
  participant Card
  User->>UI: click "Tarkista" button
  UI->>UI: _check_is_numeric()
  UI->>CardRepository : solve_exercise(exercise_id, 15)
  CardRepository->>CardRepository: find_operation(exercise_id)
  CardRepository->>Card: solve(operation, variables)
  Card-->>CardRepository: correct
  CardRepository-->>UI: False
  UI->>CardRepository: save_to_review_exercises(exercise_id)
  CardRepository->>CardRepository: get_all_info_from_exercise_with_id(exercise_id)
  CardRepository->>UserRepository: user
  UserRepository-->>CardRepository: user
``` 