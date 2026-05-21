# Demo-uitvoering zonder tweede server 2026-05-21

Status: dry-run uitgevoerd, geen tweede-server live cutover.

## Doel

Bewijzen dat het demo-draaiboek uitvoerbaar is zonder doelcluster en zonder tijdelijke demo-output te committen.

## Uitgevoerde stappen

1. Publicatiecheck draaien.
2. Tijdelijke environment `demo-community` genereren.
3. Environment-contract valideren.
4. Live cutover checklist genereren.
5. Tijdelijke environment en checklist opruimen.
6. Install-gate dry-run draaien op tijdelijke environment.
7. Tijdelijke install-gate environment opruimen.

## Resultaat hoofd-demorun

```text
COMMUNITY_PUBLICATION_CHECK status=PASS files=18
CREATED_ENVIRONMENT path=gitops/environments/demo-community
ENV_CONTRACT_VALIDATE status=PASS FAIL=0 WARN=0 INFO=0
LIVE_CUTOVER_CHECKLIST status=PASS environment=demo-community
DEMO_CLEANUP status=PASS
DEMO_RUN status=PASS
```

Bewijslog:

```text
logs/community-demo/20260521T1150Z/demo-draaiboek-zonder-tweede-server.log
```

## Resultaat install-gate dry-run

```text
COPYABLE_INSTALL_GATE_START environment=demo-community
ENV_CONTRACT_VALIDATE status=PASS FAIL=0 WARN=0 INFO=0
ENV_PREREQ_CHECK status=PASS FAIL=0 WARN=12 INFO=1
SECRET_INVENTORY status=PASS FAIL=0 WARN=0 INFO=22
COPYABILITY_SCAN status=PASS FAIL=0 WARN=0 INFO=10
COPYABLE_RENDER_BUNDLE status=PASS
LIVE_CUTOVER_CHECKLIST status=PASS environment=demo-community
COPYABLE_INSTALL_GATE status=PASS environment=demo-community
DEMO_INSTALL_GATE status=PASS
DEMO_INSTALL_GATE_CLEANUP status=PASS
```

Bewijslog:

```text
logs/community-demo/20260521T1150Z/demo-install-gate-dry-run.log
```

Install-gate sublog:

```text
logs/copyability/install-gate-demo-community-20260521T115136Z
```

## Betekenis

De demo bewijst dat de communityaanpak zonder tweede server kan worden getoond:

- environment genereren
- contract valideren
- cutoverchecklist maken
- install-gate draaien
- tijdelijke output opruimen

De demo bewijst niet:

- echte tweede-server live cutover
- productie-Haven-compliancy
- live Flux-reconcile op een doelcluster

## Publicatieconclusie

Het demo-draaiboek is uitvoerbaar als communitydemo. De waarschuwingen in de prereq-check zijn acceptabel voor deze dry-run, omdat er bewust geen echt doelcluster, echte DNS en echte HCC-run voor de tijdelijke demo-omgeving zijn gebruikt.
