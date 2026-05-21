# Distributieplan communitypublicatie Platformdienstverlening

Status: concept, 2026-05-21.

## Doel

De aanpak delen met de community op een manier die begrijpelijk is voor meerdere doelgroepen en veilig is voor publicatie.

## Publicatiepakket

Minimale set:

- `docs/community/README.md`
- `docs/community/community-post.md`
- `docs/community/bestuurlijke-samenvatting.md`
- `docs/community/referentiearchitectuur.md`
- `docs/community/technische-handleiding.md`
- `docs/community/validatie-en-bewijs.md`
- `docs/community/lessons-learned.md`
- `docs/community/presentatie-outline.md`
- `docs/community/publicatie-review-checklist.md`
- `docs/community/begrippenlijst.md`
- `docs/community/persona-review-2026-05-21.md`
- `docs/community/reviewverzoeken.md`
- `docs/community/feedback-register.md`
- `.github/ISSUE_TEMPLATE/community-feedback.yml`
- `docs/community/publicatie-index.md`
- `docs/community/release-notes-communitybundel-2026-05-21.md`
- `docs/community/demo-draaiboek-zonder-tweede-server.md`

## Kanalen

### Community repo of GitHub-discussie

Doel:

- technische review
- pull requests op scripts, gates en contractvelden

Aanpak:

- start met `community-post.md`
- link naar README en technische handleiding
- vraag gericht om feedback op gates en contractvelden

### Meetup of kennissessie

Doel:

- uitleg voor gemengd publiek
- ophalen van adoptievragen en bestuurlijke randvoorwaarden

Aanpak:

- gebruik `presentatie-outline.md`
- begin met waarde en risico, niet met scripts
- eindig met demo van generator en gates

### Architectuuroverleg

Doel:

- toetsen of het lagenmodel en de Haven/Haven+ interpretatie passen

Aanpak:

- gebruik `referentiearchitectuur.md`
- bespreek HCC als ontwerpgate
- bepaal per omgeving welke afwijkingen acceptabel zijn

### Leveranciersgesprek

Doel:

- testen of leveranciers de aanpak kunnen volgen en reproduceren

Aanpak:

- gebruik `technische-handleiding.md`
- vraag om dry-run zonder secrets
- vraag feedback op foutmeldingen en stopregels

## Reviewvolgorde

1. Veilig-deelbaar check draaien.
2. Niet-technische tekst laten lezen door iemand zonder Kubernetes-achtergrond.
3. Architectuurtekst laten toetsen op samenhang en besluitpunten.
4. Technische handleiding laten dry-runnen door een developer.
5. Feedback verwerken.
6. Publicatiecheck opnieuw draaien.
7. Publiceren.

## Feedbackvragen

Voor bestuur en programma:

- maakt dit duidelijk welk risico wordt verkleind?
- is helder wat nog geen productieclaim is?
- zijn de besluitpunten concreet genoeg?

Voor architecten:

- klopt de scheiding tussen generiek en omgeving?
- ontbreken er architectuurprincipes?
- is de HCC/Haven+ interpretatie bruikbaar?

Voor developers en leveranciers:

- zijn de commando's uitvoerbaar?
- geven de gates genoeg informatie bij fouten?
- ontbreken er validators of voorbeeldcontracten?

## Publicatievoorwaarde

Voor publicatie moet gelden:

```text
COMMUNITY_PUBLICATION_CHECK status=PASS
```

Daarna blijft menselijke review nodig op toon, context en kanaalkeuze.
