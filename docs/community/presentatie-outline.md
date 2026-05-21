# Presentatie-outline kopieerbare Platformdienstverlening

Status: eerste communityversie, 2026-05-21.

## Titel

Van werkende dev-omgeving naar overdraagbare Platformdienstverlening

## Publiek

- bestuurders en programmamanagers
- architecten
- developers en leveranciers
- beheerders

## Verhaallijn

### 1. Het probleem

Veel platformomgevingen werken, maar zijn moeilijk te herhalen. De kennis zit in losse fixes, lokale secrets, specifieke DNS, serverkeuzes en impliciete aannames.

### 2. De keuze

We scheiden generieke platformdefinitie van lokale omgevingskeuzes.

- generiek: `gitops/base/`
- lokaal: `gitops/environments/<naam>/`
- contract: `copyable/environment.yaml`

### 3. De waarde

- sneller aansluiten
- minder overdrachtsrisico
- betere besluitvorming
- objectieve gates in plaats van losse statusupdates

### 4. Haven en Haven+

De HCC-scan toont eerlijk dat de huidige dev-server geen productie-Haven-cluster is.

Niet geslaagd:

- availability zones
- 3 masters
- 3 workers
- log aggregation

Wel geslaagd in Haven+:

- automatische HTTPS-certificaten
- metrics-server

Punt voor de community:

- gebruik HCC als ontwerpgate, niet alleen als eindstempel

### 5. De technische aanpak

Laat de keten zien:

```text
generator -> environment-contract -> secret inventory -> render -> install-gate -> CI -> source-sync -> DNS/TLS -> smoke -> drift
```

### 6. Wat al bewezen is

- copyability-gates groen
- live release gate suite groen op huidige dev
- source-sync groen op main
- HCC-uitkomst vastgelegd

### 7. Wat nog niet bewezen is

- geen echte tweede-server live cutover
- geen productie-Haven-compliancy op de huidige dev-server

### 8. Demo zonder tweede server

Toon:

- environment genereren
- contract valideren
- install-gate draaien
- CI-gate draaien
- cutoverchecklist genereren

### 9. Oproep aan de community

- test de aanpak op andere clusters
- deel ontbrekende gates
- verbeter het contractmodel
- lever voorbeeldomgevingen aan zonder secrets

## Afsluitende boodschap

Een platform is pas schaalbaar als de overdracht schaalbaar is. Deze aanpak maakt overdracht toetsbaar, eerlijk en herhaalbaar.
