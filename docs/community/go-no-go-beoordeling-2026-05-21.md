# Go/no-go beoordeling reviewpublicatie Platformdienstverlening

Status: intern go/no-go advies, 2026-05-21.

## Conclusie

```text
PUBLICATION_REVIEW_GO_NOGO status=CONDITIONAL_GO_FOR_REVIEW
```

De bundel is klaar om als reviewversie te delen, maar nog niet voor definitieve publicatie. Externe verspreiding blijft geblokkeerd tot Aljen expliciet kanaal en doelgroep goedkeurt.

## Go voor reviewversie

### Inhoud

- [x] `docs/community/publicatie-index.md` is het startpunt.
- [x] `docs/community/community-post.md` past bij reviewpublicatie.
- [x] `docs/community/publicatie-readiness-2026-05-21.md` is aanwezig.
- [x] De tekst noemt dat het een reviewversie is.
- [x] De tekst noemt dat er nog geen tweede-server live cutover is uitgevoerd.
- [x] De tekst noemt dat de huidige dev-server geen productie-Haven-cluster is.

### Haven/Haven+

- [x] HCC-uitkomst `11 out of 15 checks passed` staat in de publicatiecontext.
- [x] Niet-slaagredenen staan erbij: availability zones, 3 masters, 3 workers, log aggregation.
- [x] HCC wordt gepositioneerd als ontwerpgate.
- [x] Haven+ wordt niet volledig groen gepresenteerd omdat log aggregation niet geslaagd is.

### Veilig delen

- [x] Geen secrets, tokens, wachtwoorden of persoonsgegevens in de communitydocs volgens automatische check.
- [x] Geen interne IP-adressen of bekende interne patronen in de communitydocs volgens automatische check.
- [x] Geen incidentdetails die nodig zijn voor interne context maar niet voor de herbruikbare les.
- [x] Het lokale distributiepakket wordt niet automatisch meegestuurd.

### Validatie

- [x] `scripts/community_publication_check.py` geeft `COMMUNITY_PUBLICATION_CHECK status=PASS files=23`.
- [x] `scripts/export_community_publication_bundle.sh 20260521T1206Z` gaf `COMMUNITY_PUBLICATION_BUNDLE status=PASS files=21`.
- [x] Checksum van het lokale pakket is bekend: `bfcd1d9e15153569e2ee2999c7ca553d98b23b95433e61a0e0e0461e14dc08f4`.

## No-go voor definitieve publicatie

Definitieve publicatie is nog niet vrijgegeven, omdat:

- externe niet-technische review nog niet is uitgevoerd
- architectuurreview nog niet is uitgevoerd
- developer dry-run door iemand buiten deze sessie nog niet is uitgevoerd
- er nog geen echte tweede-server live cutover is uitgevoerd
- Aljen nog geen expliciet extern kanaal en doelgroep heeft goedgekeurd

## Advies

Eerstvolgende veilige stap:

1. Kies één reviewkanaal.
2. Kies één doelgroep.
3. Gebruik de bijpassende tekst uit `docs/community/kanaalteksten-reviewpublicatie.md`.
4. Deel alleen als reviewversie.
5. Leg feedback vast in `docs/community/feedback-register.md`.

Aanbevolen eerste kanaal:

```text
Architectuuroverleg of kleine besloten reviewgroep
```

Reden:

- de bundel bevat veel context
- HCC/Haven+ duiding vraagt nuance
- technische en niet-technische framing kan daar eerst worden aangescherpt

## Akkoord nodig

Voor externe actie is nog expliciet akkoord nodig op:

```text
Kanaal: <invullen>
Doelgroep: <invullen>
Tekstvariant: <invullen>
Pakket meesturen: ja/nee
```

Zonder deze vier keuzes blijft externe publicatie geblokkeerd.
