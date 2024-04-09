```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu "1" -- "1" Aloitus
    Ruutu "2" -- "1" Vankila
    Ruutu "9" -- "1" Sattuma ja yhteismaa
    Ruutu "6" -- "1" Asemat ja laitokset
    Ruutu "22" -- "1" Normaalit kadut
    Aloitus "1" -- "1" Toiminto1
    Vankila "1" -- "1" Toiminto2
    Sattuma ja yhteismaa "1" -- "1" Kortti
    Asemat ja laitokset "1" -- "1" Toiminto3
    Normaalitkadut "1" -- "1" Toiminto4
    Kortti "20" -- "1" toiminto5
    Toiminto4 "1" -- "4" Talo
    Toiminto4 "1" -- "1" Hotelli
    Pelinappula "1" -- "1" Pelaaja
    Normaalitkadut "0..22" -- "0..1" Pelaaja
    Pelaaja "0..1" -- "0..20000" Rahat
    Pelaaja "2..8" -- "1" Monopolipeli
```