# Go/no-go publicatiechecklist Platformdienstverlening communitybundel

Status: concept, 2026-05-21.

## Doel

Deze checklist voorkomt dat de communitybundel extern wordt gedeeld zonder laatste controle en expliciet akkoord.

## Go-criteria

Publicatie mag pas door als alle punten `ja` zijn.

### Inhoud

- [ ] `docs/community/publicatie-index.md` is het startpunt.
- [ ] `docs/community/community-post.md` past bij het gekozen kanaal.
- [ ] `docs/community/publicatie-readiness-2026-05-21.md` is actueel.
- [ ] De tekst noemt dat het een reviewversie is.
- [ ] De tekst noemt dat er nog geen tweede-server live cutover is uitgevoerd.
- [ ] De tekst noemt dat de huidige dev-server geen productie-Haven-cluster is.

### Haven/Haven+

- [ ] HCC-uitkomst `11 out of 15 checks passed` staat in de publicatiecontext.
- [ ] Niet-slaagredenen staan erbij: availability zones, 3 masters, 3 workers, log aggregation.
- [ ] HCC wordt gepositioneerd als ontwerpgate.
- [ ] Haven+ wordt niet volledig groen gepresenteerd omdat log aggregation niet geslaagd is.

### Veilig delen

- [ ] Geen secrets, tokens, wachtwoorden of persoonsgegevens.
- [ ] Geen interne IP-adressen of interne hostnames in de publicatietekst.
- [ ] Geen incidentdetails die niet nodig zijn voor de herbruikbare les.
- [ ] Het lokale distributiepakket is niet automatisch meegestuurd.

### Validatie

- [ ] `scripts/community_publication_check.py` geeft `COMMUNITY_PUBLICATION_CHECK status=PASS`.
- [ ] Indien pakket wordt gedeeld: `scripts/export_community_publication_bundle.sh` geeft `COMMUNITY_PUBLICATION_BUNDLE status=PASS`.
- [ ] Checksum van het pakket is vermeld als het pakket wordt gedeeld.

### Akkoord

- [ ] Kanaal is gekozen.
- [ ] Doelgroep is gekozen.
- [ ] Aljen heeft expliciet akkoord gegeven voor externe publicatie.

## No-go

Niet publiceren als één van deze punten geldt:

- HCC-duiding ontbreekt.
- Tweede-server cutover wordt als afgerond gepresenteerd.
- Productie-Haven-compliancy wordt geclaimd.
- Secretwaarden of gevoelige details staan in tekst of bijlagen.
- Er is geen expliciet akkoord voor het externe kanaal.

## Laatste commando's vóór publicatie

```sh
scripts/community_publication_check.py
scripts/export_community_publication_bundle.sh
```

## Vastlegging na publicatie

Leg vast in `docs/community/feedback-register.md`:

- kanaal
- datum
- doelgroep
- link of referentie
- ontvangen feedback
- opvolging
