# Release notes communitybundel Platformdienstverlening

Datum: 2026-05-21
Status: conceptrelease voor communityreview

## Samenvatting

Deze release maakt de Platformdienstverlening-aanpak deelbaar met de community. De bundel bevat uitleg voor niet-technische lezers, architectuurdocumentatie, technische stappen, validatiegates, feedbackverwerking en publicatiechecks.

## Toegevoegd

- Communitypost voor brede introductie.
- Bestuurlijke samenvatting.
- Referentiearchitectuur.
- Technische handleiding.
- Validatie- en bewijsdocument.
- Lessons learned.
- Presentatie-outline.
- Begrippenlijst.
- Publicatie-review checklist.
- Persona-review.
- Reviewverzoeken per doelgroep.
- Feedbackregister.
- GitHub issue-template voor communityfeedback.
- Automatische publicatiecheck.
- Publicatie-index.
- Demo-draaiboek zonder tweede server.
- Demo-uitvoering zonder tweede server met PASS-bewijs.
- Publicatie-readiness rapport voor eerste communityreview.
- Publicatiepakket-manifest en exportscript.
- Kanaalteksten en go/no-go publicatiechecklist.
- Go/no-go beoordeling voor reviewpublicatie.

## Belangrijkste boodschap

De aanpak maakt overdraagbaarheid toetsbaar. Lokale keuzes worden gescheiden van generieke manifests, secrets blijven buiten Git en gates leveren bewijs voordat een omgeving klaar wordt genoemd.

## Haven/Haven+ uitkomst

De HCC-scan op de huidige dev-server geeft:

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

Niet geslaagd:

- geen meerdere availability zones
- geen 3 master nodes
- geen 3 worker nodes
- geen log aggregation

Duiding:

- de huidige omgeving is een dev-referentie
- productiegebruik vraagt aanvullende infrastructuur
- HCC wordt gebruikt als ontwerpgate, niet alleen als eindkeuring

## Validatie

Automatische publicatiecheck:

```text
COMMUNITY_PUBLICATION_CHECK status=PASS
```

De check controleert verplichte communitybestanden, HCC/Haven+ termen, niet-slaagredenen, em-dash en bekende interne patronen.

## Open punten

- Externe niet-technische review uitvoeren.
- Architectuurreview uitvoeren.
- Developer dry-run uitvoeren.
- Feedback verwerken in `docs/community/feedback-register.md`.
- Tweede-server live cutover uitvoeren zodra een doelcluster beschikbaar is.

## Startpunt

Gebruik voor publicatie of review eerst:

- `docs/community/publicatie-index.md`
- `docs/community/community-post.md`
- `docs/community/reviewverzoeken.md`
