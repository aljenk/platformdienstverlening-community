# Technische handleiding kopieerbare Platformdienstverlening

Status: eerste communityversie, 2026-05-21.

## Vooraf

Deze handleiding beschrijft de reproduceerbare route. Er is nog geen tweede-server cutover uitgevoerd. Gebruik dit daarom als dry-run en voorbereidingspad totdat een doelcluster beschikbaar is.

## Stap 1: environment genereren

```sh
scripts/platform/create_copyable_environment.py \
  --name acc \
  --dns-suffix acc.platform.example.org \
  --secret-store acc-secret-store \
  --default-storage-class acc-default \
  --rwx-storage-class acc-rwx \
  --cluster-issuer acc-production-issuer \
  --dev-issuer acc-dev-issuer \
  --db-cluster-name pg-acc-platform \
  --image-pull-secret acc-ghcr-pull
```

Resultaat:

```text
gitops/environments/acc/copyable/environment.yaml
```

## Stap 2: contract valideren

```sh
scripts/platform/validate_environment_contract.py \
  gitops/environments/acc/copyable/environment.yaml
```

Klaarcriterium:

```text
ENV_CONTRACT_VALIDATE status=PASS
```

## Stap 3: prereqs controleren

Lokaal en DNS:

```sh
scripts/platform/check_environment_prereqs.py \
  --contract gitops/environments/acc/copyable/environment.yaml \
  --dns
```

Live op doelcluster:

```sh
scripts/platform/check_environment_prereqs.py \
  --contract gitops/environments/acc/copyable/environment.yaml \
  --live \
  --kubectl "kubectl"
```

## Stap 4: secrets inventariseren

```sh
scripts/platform/check_secret_inventory.py --environment acc
```

Regel:

- geen `data` of `stringData` met secretwaarden in Git
- alleen namen, keynamen, keycount en status in logs

## Stap 5: render en install-gate draaien

```sh
scripts/platform/run_copyable_install_gate.sh acc
```

De install-gate draait:

- contractvalidatie
- prereq-check
- secret inventory
- render bundle
- copyability-scan

## Stap 6: CI-gate draaien

```sh
scripts/platform/run_copyable_ci_gate.sh dev example acc
```

Klaarcriterium:

```text
COPYABLE_CI_GATE status=PASS
```

## Stap 7: live cutover checklist genereren

```sh
scripts/platform/generate_live_cutover_checklist.py \
  --environment acc \
  --output docs/install/generated/platformdienstverlening-acc-live-cutover-checklist.md
```

## Stap 8: Flux source-sync controleren

```sh
scripts/platform/check_flux_source_sync.py --fetch --required-ref HEAD
```

Klaarcriterium:

```text
FLUX_SOURCE_SYNC status=PASS
```

## Stap 9: DNS/TLS smoke

```sh
scripts/platform/check_dns_tls_smoke.py \
  --contract gitops/environments/acc/copyable/environment.yaml
```

Alleen bij expliciete dev-uitzonderingen:

```sh
scripts/platform/check_dns_tls_smoke.py \
  --contract gitops/environments/acc/copyable/environment.yaml \
  --insecure \
  --allow-fail \
  --exception-log <pad> \
  --recovery-action <actie>
```

## Stap 10: live reconcile per laag

Volgorde:

- foundation
- shared-capabilities
- domain-services
- interaction-services

Per component:

```sh
kubectl kustomize gitops/environments/acc/<laag>/<component>
flux reconcile kustomization <naam> -n flux-system --with-source
```

## Stap 11: smoke en drift

```sh
scripts/run_platform_smoke_bundle.sh
scripts/check_ingress_dns_drift.py --help
scripts/check_gzac_route_drift.py --help
```

Klaarcriterium:

- platform smoke groen
- geen niet-vastgelegde livefixes
- geen secretwaarden in logs

## Stap 12: HCC/Haven vastleggen

Voer Haven Compliancy Checker uit op het doelcluster.

Leg vast:

- HCC-versie
- clustercontext
- tekstlog
- JSON-resultaat
- eventuele afwijkingen

Productieclaim alleen doen als productie-eisen zijn gehaald of afwijkingen formeel zijn geaccepteerd.
