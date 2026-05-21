# Feedbackregister communitybundel Platformdienstverlening

Status: leeg register, klaar voor reviewronde, 2026-05-21.

## Doel

Dit register legt feedback op de communitybundel vast, zodat opmerkingen uit gesprekken, GitHub-discussies, issues of sessies niet verloren gaan.

## Rubric

Gebruik één van deze classificaties:

- `blokkerend`: moet vóór publicatie worden opgelost
- `belangrijk`: verwerken vóór brede verspreiding
- `verbetering`: verwerken als tijd beschikbaar is
- `later`: bewaren voor tweede-server validatie of vervolgversie

## Statussen

- `nieuw`: ontvangen, nog niet beoordeeld
- `gepland`: verwerking gekozen
- `verwerkt`: verwerkt in documentatie of scripts
- `afgewezen`: bewust niet verwerkt, reden vastgelegd
- `later`: doorgeschoven naar vervolgversie

## Feedbacktemplate

```markdown
### FB-YYYYMMDD-001

- Datum:
- Bron:
- Doelgroep: niet-technisch | architectuur | developer | gemengd
- Document:
- Sectie:
- Classificatie: blokkerend | belangrijk | verbetering | later
- Status: nieuw | gepland | verwerkt | afgewezen | later
- Feedback:
- Gekozen verwerking:
- Commit:
```

## Open feedback

Nog geen externe feedback ontvangen.

## Verwerkte feedback

Nog geen feedback verwerkt.

## Publicatiebesluit

Brede publicatie pas doen als:

- alle `blokkerend` feedback is verwerkt of formeel afgewezen
- `COMMUNITY_PUBLICATION_CHECK status=PASS` is gedraaid na verwerking
- menselijke review op toon en kanaalkeuze is gedaan
