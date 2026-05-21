# Review-PR tekst communitybundel Platformdienstverlening

Status: klaar om in GitHub PR te plakken, 2026-05-21.

## PR-titel

```text
Reviewversie: kopieerbare Platformdienstverlening communitybundel
```

## PR-body

```markdown
## Doel

Deze PR bevat een eerste reviewversie van de communitybundel voor kopieerbare Platformdienstverlening.

De aanpak maakt overdraagbaarheid toetsbaar door:

- generieke GitOps-manifests te scheiden van omgevingskeuzes
- environment-contracten te gebruiken
- secrets buiten Git te houden
- gates te gebruiken voor contract, prereqs, secrets, render, install, CI, DNS/TLS, Flux, smoke en drift
- HCC/Haven+ expliciet als ontwerpgate op te nemen

## Belangrijke beperking

Dit is een reviewversie, geen definitieve standaard.

Niet geclaimd:

- geen echte tweede-server live cutover
- geen productie-Haven-compliancy op de huidige dev-server
- geen externe communityacceptatie

## HCC/Haven+ duiding

De huidige dev-server scoort:

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

Niet geslaagd:

- geen meerdere availability zones
- geen 3 master nodes
- geen 3 worker nodes
- geen log aggregation

De bundel positioneert HCC daarom als ontwerpgate, niet als eindstempel.

## Startpunten voor review

- `docs/community/publicatie-index.md`
- `docs/community/community-post.md`
- `docs/community/publicatie-readiness-2026-05-21.md`
- `docs/community/reviewverzoeken.md`
- `docs/community/technische-handleiding.md`

## Wat zit in deze PR

- doelgroepdocumenten voor niet-technisch, architectuur en technisch publiek
- validatie- en bewijsdocumentatie
- demo-draaiboek zonder tweede server
- demo-uitvoering met PASS-bewijs
- feedbackregister en issue-template
- publicatiecheckscript
- exportscript en lokaal distributiepakket met checksum

## Validatie

Laatste lokale checks:

```text
COMMUNITY_PUBLICATION_CHECK status=PASS files=24
COMMUNITY_PUBLICATION_BUNDLE status=PASS files=21
```

Distributiepakket:

```text
dist/platformdienstverlening-community-publication-20260521T1206Z.tar.gz
SHA256 bfcd1d9e15153569e2ee2999c7ca553d98b23b95433e61a0e0e0461e14dc08f4
```

## Reviewvragen

Graag feedback op:

- missen er gates of contractvelden?
- is de uitleg bruikbaar voor niet-technische lezers?
- klopt de HCC/Haven+ duiding?
- kan een developer of leverancier hiermee een dry-run uitvoeren?
- welke onderdelen zijn te project-specifiek voor communitygebruik?
```

## PR-link

Branch is gepusht naar:

```text
maurice/community-publication-review-20260521
```

PR-aanmaaklink:

```text
https://github.com/aljenk/platformdienstverlening-gitops/pull/new/maurice/community-publication-review-20260521
```
