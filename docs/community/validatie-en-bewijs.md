# Validatie en bewijs voor kopieerbare Platformdienstverlening

Status: eerste communityversie, 2026-05-21.

## Principe

Geen live-ready claim zonder bewijs. Elk onderdeel van de aanpak heeft een gate, een klaarcriterium en een logpad.

## Gate-overzicht

### Contractgate

Doel:

- controleren dat het environment-contract volledig en veilig is
- voorkomen dat templatewaarden of ontbrekende velden worden gebruikt

Commando:

```sh
scripts/platform/validate_environment_contract.py \
  gitops/environments/<env>/copyable/environment.yaml
```

Bewijs:

```text
ENV_CONTRACT_VALIDATE status=PASS
```

### Prereq-gate

Doel:

- controleren dat DNS, issuers, storageclasses, SecretStore, DB-service en imagePullSecret passen bij de omgeving

Commando:

```sh
scripts/platform/check_environment_prereqs.py \
  --contract gitops/environments/<env>/copyable/environment.yaml \
  --live \
  --kubectl "kubectl"
```

Bewijs:

```text
ENV_PREREQ_CHECK status=PASS
```

### Secret inventory gate

Doel:

- bewijzen dat secrets via de gekozen strategie beschikbaar zijn
- voorkomen dat secretwaarden in Git of logs komen

Commando:

```sh
scripts/platform/check_secret_inventory.py --environment <env>
```

Bewijs:

```text
SECRET_INVENTORY status=PASS
```

Toegestaan bewijs:

- secretnamen
- keynamen
- keycount
- ExternalSecret status
- hashes of lengtes als dat nodig is

Niet toegestaan:

- secretwaarden
- base64-data
- wachtwoorden
- tokens

### Render-gate

Doel:

- controleren dat manifests renderbaar zijn
- hardcoded dev-waarden in de generieke laag blokkeren

Commando:

```sh
scripts/platform/render_copyable_bundle.sh <env>
```

Bewijs:

```text
COPYABLE_RENDER_BUNDLE status=PASS
```

### Install-gate

Doel:

- bundelen van contract-, prereq-, secret-, render- en copyability-checks

Commando:

```sh
scripts/platform/run_copyable_install_gate.sh <env>
```

Bewijs:

```text
COPYABLE_INSTALL_GATE status=PASS
```

### CI-gate

Doel:

- aantonen dat dev, example en nieuwe omgevingen reproduceerbaar blijven

Commando:

```sh
scripts/platform/run_copyable_ci_gate.sh dev example <env>
```

Bewijs:

```text
COPYABLE_CI_GATE status=PASS
```

### Flux source-sync gate

Doel:

- voorkomen dat live wordt gereconciled terwijl de gewenste commit niet op de Flux-branche staat

Commando:

```sh
scripts/platform/check_flux_source_sync.py --fetch --required-ref HEAD
```

Bewijs:

```text
FLUX_SOURCE_SYNC status=PASS
```

### DNS/TLS-smoke

Doel:

- controleren dat hostnames resolven, TLS werkt en routes geen onverwachte 404/502 geven

Commando:

```sh
scripts/platform/check_dns_tls_smoke.py \
  --contract gitops/environments/<env>/copyable/environment.yaml
```

Bewijs:

```text
DNS_TLS_SMOKE status=PASS
```

### Platform smoke bundle

Doel:

- publieke componentroutes controleren

Commando:

```sh
scripts/run_platform_smoke_bundle.sh
```

Bewijs:

```text
PLATFORM_SMOKE_BUNDLE status=PASS
status_counts PASS=<n> WARN=0 FAIL=0
```

### Driftgate

Doel:

- controleren dat livefixes teruggebracht zijn naar GitOps
- voorkomen dat cluster en repository uit elkaar lopen

Voorbeelden:

```sh
scripts/check_ingress_dns_drift.py --help
scripts/check_gzac_route_drift.py --help
```

Bewijs:

- logpad met driftstatus
- commit waarin eventuele livefix is geborgd

## HCC/Haven bewijs

Doel:

- vaststellen of het cluster aan Haven-eisen voldoet
- dev-afwijkingen expliciet maken

Huidig bewijs uit dev:

```text
Results: 11 out of 15 checks passed, 0 checks skipped, 0 checks unknown. This is NOT a Haven Compliant cluster.
```

Niet geslaagd:

- Multiple availability zones in use
- Running at least 3 master nodes
- Running at least 3 worker nodes
- Log aggregation is running

Bewijsbronnen:

- `docs/havenplus/haven-compliancy-checker-uitvoering-2026-05-20.md`
- `logs/haven-compliancy/20260520T085616Z-haven-check-host-sudo.log`

## Stopregels

Stop bij eerste `FAIL` in:

- HCC of expliciete afwijkingsgate
- prereq-check
- secret inventory
- render
- Flux source-sync
- DNS/TLS-smoke
- component-smoke
- driftcontrole

## Minimale bewijsregel voor statusupdates

Gebruik bij afronding minimaal:

```text
Status: <wat is afgerond>
Bewijs: <logpad of bronpad met statusregel>
Commit: <commitcode en korte omschrijving>
```

Bij falen:

```text
Oorzaak: <concrete oorzaak>
Eerste herstelactie: <eerste uitgevoerde of geplande herstelactie>
Status: niet afgerond
```
