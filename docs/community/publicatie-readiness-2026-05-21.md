# Publicatie-readiness communitybundel Platformdienstverlening

Status: klaar voor eerste communityreview, 2026-05-21.

## Conclusie

De communitybundel is klaar voor eerste review met technische en niet-technische lezers. De bundel is nog geen definitieve eindpublicatie, omdat externe review en tweede-server validatie nog open staan.

## Publiceerbaar nu

De volgende onderdelen zijn publiceerbaar als eerste reviewversie:

- kernverhaal en communitypost
- bestuurlijke samenvatting
- referentiearchitectuur
- technische handleiding
- validatie- en bewijsuitleg
- lessons learned
- begrippenlijst
- demo-draaiboek zonder tweede server
- demo-uitvoering met PASS-bewijs
- reviewverzoeken per doelgroep
- feedbackregister en issue-template
- publicatie-index en release notes

## Bewijsstatus

### Communitypublicatiecheck

```text
COMMUNITY_PUBLICATION_CHECK status=PASS files=19
```

Betekenis:

- verplichte communitybestanden bestaan
- HCC/Haven+ termen zijn aanwezig
- niet-slaagredenen van de HCC-scan zijn aanwezig
- bekende interne patronen worden geblokkeerd
- em-dash is niet aanwezig in communitydocs

### Demo zonder tweede server

```text
DEMO_RUN status=PASS
DEMO_INSTALL_GATE status=PASS
```

Bewijslogs:

- `logs/community-demo/20260521T1150Z/demo-draaiboek-zonder-tweede-server.log`
- `logs/community-demo/20260521T1150Z/demo-install-gate-dry-run.log`

Betekenis:

- environment-generatie werkt
- contractvalidatie werkt
- live cutover checklist wordt gegenereerd
- install-gate werkt op een tijdelijke demo-environment
- tijdelijke demo-output is opgeruimd

### HCC/Haven+

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

Niet geslaagd:

- geen meerdere availability zones
- geen 3 master nodes
- geen 3 worker nodes
- geen log aggregation

Betekenis:

- de huidige dev-omgeving is geen productie-Haven-cluster
- de HCC-uitkomst is geschikt als ontwerpgate en waarschuwing voor productieclaims
- Haven+ is deels aanwezig: automatische HTTPS-certificaten en metrics-server zijn geslaagd; log aggregation is niet geslaagd

## Niet claimen

Deze bundel claimt niet:

- dat er een tweede server live is gereconciled
- dat de huidige dev-server productie-Haven-compliant is
- dat externe reviewers de aanpak al hebben goedgekeurd
- dat alle organisaties dezelfde clusterafwijkingen mogen accepteren

## Klaar voor review door

- niet-technische lezer: bestuurlijke samenvatting, begrippenlijst en communitypost
- architect: referentiearchitectuur, HCC/Haven+ duiding en validatiegates
- developer of leverancier: technische handleiding, demo-draaiboek en bewijsdocument

## Open punten voor volgende fase

1. Externe niet-technische review uitvoeren.
2. Architectuurreview uitvoeren.
3. Developer dry-run door iemand buiten deze sessie laten uitvoeren.
4. Feedback vastleggen in `docs/community/feedback-register.md`.
5. Feedback verwerken met commits.
6. Tweede-server live cutover uitvoeren zodra een doelcluster beschikbaar is.

## Publicatieadvies

Publiceer eerst als reviewversie, niet als definitieve standaard. Gebruik daarbij de tekst uit `docs/community/community-post.md` en verwijs naar `docs/community/publicatie-index.md` als startpunt.
