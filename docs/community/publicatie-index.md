# Publicatie-index Platformdienstverlening communitybundel

Status: eerste publicatie-index, 2026-05-21.

## Doel

Deze index is de startpagina voor het delen van de communitybundel. De bundel beschrijft hoe een Platformdienstverlening-omgeving overdraagbaar wordt gemaakt met GitOps, environment-contracten, secrets buiten Git en bewijsbare gates.

## Snel kiezen

### Ik wil de kern begrijpen

Lees:

- `docs/community/community-post.md`
- `docs/community/bestuurlijke-samenvatting.md`
- `docs/community/begrippenlijst.md`

Voor:

- bestuurders
- programmamanagers
- product owners
- geïnteresseerde communityleden zonder dagelijkse Kubernetes-achtergrond

### Ik wil de architectuur toetsen

Lees:

- `docs/community/referentiearchitectuur.md`
- `docs/community/validatie-en-bewijs.md`
- `docs/community/publicatie-review-checklist.md`

Voor:

- architecten
- platform owners
- technisch coördinatoren
- security- en governancebetrokkenen

### Ik wil het technisch uitvoeren of reviewen

Lees:

- `docs/community/technische-handleiding.md`
- `docs/community/validatie-en-bewijs.md`
- `docs/community/lessons-learned.md`

Voor:

- developers
- platform engineers
- Kubernetes-beheerders
- leveranciers

### Ik wil een demo geven zonder tweede server

Lees:

- `docs/community/demo-draaiboek-zonder-tweede-server.md`
- `docs/community/demo-uitvoering-2026-05-21.md`
- `docs/community/presentatie-outline.md`
- `docs/community/technische-handleiding.md`

Voor:

- meetup
- architectuuroverleg
- leveranciersgesprek
- interne kennissessie

### Ik wil feedback geven

Gebruik:

- `docs/community/reviewverzoeken.md`
- `docs/community/feedback-register.md`
- `.github/ISSUE_TEMPLATE/community-feedback.yml`

## Wat deze bundel wel claimt

- De methode voor kopieerbaarheid is uitgewerkt.
- De communitydocs bevatten aparte lagen voor niet-technische, architectuur- en technische lezers.
- De huidige dev-omgeving is met gates en bewijslogs gevalideerd.
- De HCC/Haven+ uitkomst is expliciet opgenomen.
- De publicatiecheck is automatisch uitvoerbaar.

## Wat deze bundel niet claimt

- Er is nog geen echte tweede-server live cutover uitgevoerd.
- De huidige dev-server is geen productie-Haven-cluster.
- De communityversie vervangt geen menselijke review op toon, context en kanaalkeuze.

## HCC/Haven+ kern

De huidige dev-server scoorde:

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

Niet geslaagd:

- geen meerdere availability zones
- geen 3 master nodes
- geen 3 worker nodes
- geen log aggregation

Haven+ samenvatting:

- automatische HTTPS-certificaten: geslaagd
- metrics-server: geslaagd
- log aggregation: niet geslaagd

## Publicatie-readiness

Lees voor de huidige publicatiestatus:

- `docs/community/publicatie-readiness-2026-05-21.md`

## Publicatieteksten en go/no-go

Gebruik vóór externe verspreiding:

- `docs/community/kanaalteksten-reviewpublicatie.md`
- `docs/community/go-no-go-publicatiechecklist.md`
- `docs/community/go-no-go-beoordeling-2026-05-21.md`

## Publicatiepakket

Maak een lokaal deelpakket met:

```sh
scripts/export_community_publication_bundle.sh
```

Manifest:

- `docs/community/publicatiepakket-manifest.md`

## Publicatievoorwaarde

Voor publicatie moet deze check groen zijn:

```sh
scripts/community_publication_check.py
```

Verwachte output:

```text
COMMUNITY_PUBLICATION_CHECK status=PASS
```
