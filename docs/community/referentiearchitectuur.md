# Referentiearchitectuur kopieerbare Platformdienstverlening

Status: eerste communityversie, 2026-05-21. Aangevuld op 2026-05-29 met componentgerichte architectuurgates.

## Architectuurprincipe

Scheid wat herbruikbaar is van wat lokaal is. De generieke laag beschrijft componenten en relaties. De environment-laag beschrijft de keuzes van een specifieke omgeving.

Aanvullende principes:

- data bij de bron
- hergebruik vóór nieuwbouw
- open source en portabiliteit
- servicegerichte componenten met expliciete API-contracten
- logging van techniek én dataverwerking
- platformbrede IAM met Keycloak, DigiD en policy based autorisatie als richting
- governance op afwijkingen, API-wijzigingen en de lifecycle van bouwblokken

## Lagenmodel

### Generieke laag

Pad:

```text
gitops/base/
```

Doel:

- componentmanifests zonder organisatie- of serverkeuzes
- geen vaste DNS-namen
- geen interne IP-adressen
- geen secretwaarden
- geen dev-specifieke storageclass of issuer

### Environment-laag

Pad:

```text
gitops/environments/<naam>/
```

Doel:

- DNS en hostnames
- cluster issuer
- storageclasses
- imagePullSecret
- SecretStore
- databasehost
- patches voor lokale keuzes

### Contractlaag

Pad:

```text
gitops/environments/<naam>/copyable/environment.yaml
```

Doel:

- expliciete invoer voor validators en generators
- één plek voor niet-geheime omgevingskeuzes
- basis voor prereq-checks, DNS/TLS-smoke en cutoverchecklist

## Componentlagen

De implementatie gebruikt deze volgorde:

- foundation: Keycloak en PostgreSQL
- shared-capabilities: objecttypen, objecten en notificaties
- domain-services: redis, zaak, klant, product en gzac-valtimo
- interaction-services: formulieren en nlportal

Deze volgorde voorkomt dat afhankelijke componenten worden gereconciled voordat hun basisdiensten klaar zijn.

## Secretmodel

Uitgangspunt:

- secretwaarden staan niet in Git
- logs tonen geen secretwaarden
- bewijs gebruikt namen, keynamen, keycount, status en eventueel hashes of lengtes

Voorkeursroute:

- ExternalSecrets met een eigen ClusterSecretStore per omgeving

Dev-fallback:

- handmatige Kubernetes secrets alleen als expliciete afwijking
- afwijking apart documenteren
- geen secretwaarden in bewijs opnemen

## GitOps-flow

1. Maak of update het environment-contract.
2. Valideer het contract.
3. Controleer prereqs en secret inventory.
4. Render de bundle.
5. Draai install- en CI-gates.
6. Controleer Flux source-sync.
7. Reconcile per laag.
8. Draai smoke en driftcontrole.
9. Leg bewijslogs vast.

## Haven als architectuurgate

Haven Compliancy Checker wordt vóór livegang gebruikt als architectuurgate.

De huidige dev-scan faalt op beschikbaarheid en logging:

- geen meerdere availability zones
- geen 3 masters
- geen 3 workers
- geen log aggregation

Architectuurconclusie:

- single-node dev is acceptabel als dev-referentie
- productie vraagt een ander clusterprofiel
- Haven+ logging moet vóór productieclaim zijn opgelost

## Klaarcriteria per omgeving

Een omgeving is pas overdraagbaar bewezen als:

- environment-contract volledig is ingevuld
- HCC-resultaat aanwezig is
- prereq-check groen is of afwijkingen expliciet zijn
- secret inventory groen is
- render- en install-gate groen zijn
- DNS/TLS-smoke groen is of dev-uitzondering is vastgelegd
- Flux source-sync groen is
- component-smokes groen zijn
- driftcontrole groen is

## Klaarcriteria per component

Een component is pas architectuurlijk klaar voor implementatie als:

- dienstverlening, proceslaag en informatielaag zijn benoemd
- bronmatrix is ingevuld voor leidende bron, cache, lokale kopie, synchronisatie en correctiepad
- hergebruikscan op bouwblokken, businessservices, registers en API's is uitgevoerd
- API-patroon, versiebeheer en compatibiliteit zijn vastgelegd
- logging van techniek en dataverwerking is beschreven
- authenticatie, autorisatie, rollen, claims en policy-context zijn testbaar beschreven
- eigenaar, lifecycle, deprecatiepad en architectuurexcepties zijn vastgelegd

## Bewijsbronnen

- `docs/install/platformdienstverlening-copyable-install.md`
- `docs/install/generated/platformdienstverlening-dev-live-cutover-checklist.md`
- `docs/havenplus/haven-compliancy-checker-uitvoering-2026-05-20.md`
- `docs/havenplus/kopieerbare-implementatie-uitvoering-2026-05-20.md`
