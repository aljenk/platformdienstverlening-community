# Platformdienstverlening community-outline

Status: eerste community-outline, 2026-05-21. Aangevuld op 2026-05-30 met componentkaart-template en architectuur-startgate.

## Waarom dit document

Deze outline maakt de Platformdienstverlening-aanpak deelbaar met de community. De insteek is bewust breder dan techniek: bestuurders, programmamanagers, architecten, developers en leveranciers moeten elk kunnen zien wat de waarde is en hoe de aanpak toetsbaar wordt.

Er is nog geen tweede server beschikbaar. Daarom delen we nu de methode, de structuur, de gates en het bewijs uit de huidige dev-omgeving. Een echte tweede-server cutover blijft een aparte vervolgstap.

## Kern in één zin

Maak platformdiensten overdraagbaar door generieke GitOps-manifests te scheiden van omgevingskeuzes, secrets buiten Git te houden en elke stap met gates en bewijslogs te valideren.

## Voor wie

### Niet-technisch

Wat je eraan hebt:

- De aanpak vermindert afhankelijkheid van één server, één beheerder of ongeschreven kennis.
- Besluitvorming wordt concreter omdat risico's zichtbaar zijn in gates en bewijslogs.
- Afwijkingen, zoals een dev-cluster dat niet productie-Haven-compliant is, worden niet verstopt.

Wat je moet weten:

- De huidige omgeving werkt als dev-referentie, maar is geen productiecluster.
- De HCC-scan is bewust onderdeel van het verhaal: hij toont welke infrastructuurkeuzes nog nodig zijn voor productie.

### Architect / programmamanager

Wat je eraan hebt:

- Een referentiepatroon voor herhaalbare platformomgevingen.
- Heldere scheiding tussen generieke componenten en lokale keuzes.
- Een checklist om te bepalen of een omgeving klaar is voor live gebruik.

Belangrijke onderdelen:

- `gitops/base/` voor generieke manifests
- `gitops/environments/<naam>/` voor omgevingsspecifieke overlays
- environment-contract voor DNS, issuer, storage, SecretStore, databasehost en imagePullSecret
- releasegates voor prereqs, secrets, render, install, CI, DNS/TLS, Flux, smoke en drift
- componentkaart-template en architectuur-startgate voor bronmatrix, hergebruikscan, API-compatibiliteit, logging, IAM, smoke, rollback en governance

### Developer / leverancier

Wat je eraan hebt:

- Een technische route met scripts en toetsbare criteria.
- Minder handwerk bij het opzetten of overdragen van een omgeving.
- Een duidelijke stopregel: geen live-ready claim zonder bewijslog.

Belangrijke startpunten:

- `scripts/platform/create_copyable_environment.py`
- `scripts/platform/run_copyable_install_gate.sh`
- `scripts/platform/run_copyable_ci_gate.sh`
- `scripts/platform/check_dns_tls_smoke.py`
- `docs/install/generated/platformdienstverlening-dev-live-cutover-checklist.md`

## Haven, Haven+ en waarom de scan niet slaagt

De Haven Compliancy Checker is uitgevoerd op de huidige dev-server. De uitkomst:

```text
Results: 11 out of 15 checks passed, 0 checks skipped, 0 checks unknown. This is NOT a Haven Compliant cluster.
```

De scan slaagt niet door vier punten:

- geen meerdere availability zones
- geen minimaal 3 master nodes
- geen minimaal 3 worker nodes
- geen log aggregation

Dit past bij de aard van de huidige omgeving: een single-node dev-server. Het betekent niet dat de platformaanpak waardeloos is. Het betekent wel dat productiegebruik aanvullende infrastructuur vereist.

Haven+ onderdelen uit de scan:

- Automated HTTPS certificate provisioning: geslaagd
- Metrics-server: geslaagd
- Log aggregation: niet geslaagd

Community-les:

> Gebruik HCC niet alleen als eindkeuring, maar als ontwerpgate. Een afwijking mag in dev, maar moet expliciet, verklaard en toetsbaar zijn.

Bewijs:

- `docs/havenplus/haven-compliancy-checker-uitvoering-2026-05-20.md`
- `logs/haven-compliancy/20260520T085616Z-haven-check-host-sudo.log`

## Wat is al bewezen

- Copyability-scan groen.
- Render-gate groen.
- Install-gate groen.
- CI-gate groen.
- Flux source-sync groen op main.
- DNS/TLS-smoke groen.
- Platform smoke bundle groen.
- Live release gate suite groen.

Belangrijke bewijsbron:

- `docs/havenplus/kopieerbare-implementatie-uitvoering-2026-05-20.md`

Laatste bewijscommit:

- `ca8b578` - post-push main release gate bewijs

## Wat nog niet is bewezen

- Er is nog geen echte tweede-server live cutover uitgevoerd.
- Productie-Haven-compliancy is niet aangetoond op de huidige dev-server.
- Publicatieteksten zijn nog niet allemaal geanonimiseerd en doelgroepgericht uitgewerkt.

## Vervolgdocumenten

Deze outline wordt uitgewerkt naar:

- `docs/community/community-post.md`
- `docs/community/distributieplan.md`
- `docs/community/bestuurlijke-samenvatting.md`
- `docs/community/referentiearchitectuur.md`
- `docs/community/technische-handleiding.md`
- `docs/community/validatie-en-bewijs.md`
- `docs/community/componentkaart-template.md`
- `docs/community/architectuur-startgate.md`
- `docs/community/lessons-learned.md`
- `docs/community/presentatie-outline.md`
- `docs/community/begrippenlijst.md`
- `docs/community/persona-review-2026-05-21.md`
- `docs/community/reviewverzoeken.md`
- `docs/community/feedback-register.md`
- `docs/community/publicatie-index.md`
- `docs/community/release-notes-communitybundel-2026-05-21.md`
- `docs/community/demo-draaiboek-zonder-tweede-server.md`
- `docs/community/demo-uitvoering-2026-05-21.md`
- `docs/community/publicatie-readiness-2026-05-21.md`
- `docs/community/publicatiepakket-manifest.md`
- `docs/community/kanaalteksten-reviewpublicatie.md`
- `docs/community/go-no-go-publicatiechecklist.md`
- `docs/community/go-no-go-beoordeling-2026-05-21.md`

Deze documenten zijn in eerste communityversie aanwezig en bedoeld als startpunt voor review.

## Publicatieprincipe

De community krijgt geen losse dump van scripts, maar een reproduceerbare aanpak:

1. begrijpelijke waarde voor niet-technische lezers
2. architectuurkeuzes en randvoorwaarden voor besluitvorming
3. concrete scripts en gates voor uitvoerders
4. eerlijk bewijs, inclusief wat nog niet voldoet
