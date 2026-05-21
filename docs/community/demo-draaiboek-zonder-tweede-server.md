# Demo-draaiboek zonder tweede server

Status: eerste demoversie, 2026-05-21.

## Doel

Dit draaiboek laat zien hoe de kopieerbare Platformdienstverlening-aanpak werkt zonder een echte tweede-server cutover. De demo bewijst de methode, niet een productie-uitrol.

## Publiek

- niet-technische lezers die de waarde willen begrijpen
- architecten die het patroon willen toetsen
- developers en leveranciers die de route willen reproduceren

## Kernboodschap

Een tweede server is niet nodig om de overdraagbaarheid van de aanpak te demonstreren. Je kunt laten zien hoe een omgeving wordt gegenereerd, gevalideerd, gerenderd en voorbereid voor live cutover, zonder secrets te publiceren of Flux live te reconciliëren.

## Wat deze demo wel bewijst

- Environment-generatie werkt.
- Environment-contract is valideerbaar.
- Generieke en omgevingsspecifieke laag blijven gescheiden.
- Secretwaarden blijven buiten Git.
- Install- en CI-gates zijn uitvoerbaar.
- Live cutover checklist kan worden gegenereerd.
- HCC/Haven+ afwijkingen worden als gate behandeld.

## Wat deze demo niet bewijst

- Geen echte tweede-server live cutover.
- Geen productie-Haven-compliancy.
- Geen live Flux-reconcile op een nieuw doelcluster.
- Geen echte secrets of productie-DNS.

## Voorbereiding

Werk vanaf de repository-root.

Controleer eerst de publicatiebundel:

```sh
scripts/community_publication_check.py
```

Verwachte uitkomst:

```text
COMMUNITY_PUBLICATION_CHECK status=PASS
```

## Demo-stap 1: leg het probleem uit

Vertel:

- een werkende dev-omgeving is niet automatisch overdraagbaar
- lokale DNS, secrets, storage en clusterkeuzes moeten uit de generieke laag
- gates maken status overdraagbaar tussen teams

Gebruik hiervoor:

- `docs/community/community-post.md`
- `docs/community/bestuurlijke-samenvatting.md`

## Demo-stap 2: toon het lagenmodel

Toon:

```text
gitops/base/
gitops/environments/<naam>/
gitops/environments/<naam>/copyable/environment.yaml
```

Leg uit:

- `gitops/base/` is herbruikbaar
- `gitops/environments/<naam>/` bevat lokale keuzes
- het environment-contract stuurt validators en checklists

Gebruik hiervoor:

- `docs/community/referentiearchitectuur.md`
- `docs/community/begrippenlijst.md`

## Demo-stap 3: genereer een tijdelijke omgeving

Gebruik een tijdelijke naam die niet wordt gecommit, bijvoorbeeld `demo-community`.

```sh
scripts/platform/create_copyable_environment.py \
  --name demo-community \
  --dns-suffix demo.platform.example.org \
  --secret-store demo-secret-store \
  --default-storage-class demo-default \
  --rwx-storage-class demo-rwx \
  --cluster-issuer demo-production-issuer \
  --dev-issuer demo-dev-issuer \
  --db-cluster-name pg-demo-platform \
  --image-pull-secret demo-ghcr-pull
```

Verwachte uitkomst:

```text
gitops/environments/demo-community/copyable/environment.yaml
```

## Demo-stap 4: valideer het contract

```sh
scripts/platform/validate_environment_contract.py \
  gitops/environments/demo-community/copyable/environment.yaml
```

Verwachte uitkomst:

```text
ENV_CONTRACT_VALIDATE status=PASS
```

## Demo-stap 5: draai install-gate als dry-run

Voor een demo-omgeving kunnen DNS en HCC nog waarschuwingen geven. Benoem dat als onderdeel van het verhaal: zonder doelcluster is dit voorbereiding, geen live-ready claim.

```sh
scripts/platform/run_copyable_install_gate.sh demo-community
```

Verwachte boodschap:

- gate-output moet duidelijk maken welke prereqs nog niet live bewezen zijn
- geen secretwaarden in output
- render en contractcontrole moeten toetsbaar zijn

## Demo-stap 6: genereer live cutover checklist

```sh
scripts/platform/generate_live_cutover_checklist.py \
  --environment demo-community \
  --output docs/install/generated/platformdienstverlening-demo-community-live-cutover-checklist.md
```

Toon daarna dat de checklist live stappen bevat voor:

- HCC
- live prereq-check
- DNS/TLS-smoke
- Flux per laag
- component-smoke
- driftcontrole

## Demo-stap 7: ruim tijdelijke demo-output op

Omdat dit een demo zonder doelcluster is, commit je de tijdelijke omgeving en checklist niet.

```sh
rm -rf gitops/environments/demo-community
rm -f docs/install/generated/platformdienstverlening-demo-community-live-cutover-checklist.md
```

Controleer:

```sh
git status --short
```

## Demo-stap 8: sluit af met HCC/Haven+ duiding

Gebruik de bestaande HCC-uitkomst:

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

Leg uit waarom dit belangrijk is:

- de dev-omgeving is een referentie, geen productieclaim
- hoge beschikbaarheid en log aggregation zijn productie-ontwerpkeuzes
- HCC is een ontwerpgate vóór livegang

## Demo-script voor verhaalopbouw

1. Begin met bestuurlijke waarde: overdracht zonder verborgen kennis.
2. Toon het lagenmodel.
3. Genereer een demo-environment.
4. Valideer het contract.
5. Toon de install-gate en bespreek waarschuwingen.
6. Genereer de live cutover checklist.
7. Ruim demo-output op.
8. Eindig met feedbackvraag: welke gate mist voor jullie organisatie?

## Stopregels

- Geen tijdelijke demo-output committen.
- Geen secrets invoeren of tonen.
- Geen live-ready claim doen zonder doelcluster.
- Geen HCC-falen wegpoetsen.

## Bewijs na demo

Leg na een demo minimaal vast:

```text
DEMO status=<PASS|FAIL>
Datum:
Publiek:
Gebruikte documenten:
Belangrijkste feedback:
Vervolgactie:
```
