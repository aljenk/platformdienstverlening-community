# Begrippenlijst communitypublicatie Platformdienstverlening

Status: eerste communityversie, 2026-05-21.

## Doel

Deze begrippenlijst helpt lezers zonder dagelijkse Kubernetes- of GitOps-achtergrond om de communitybundel te lezen.

## Begrippen

### Platformdienstverlening

Een samenhangende set platformdiensten die samen digitale dienstverlening ondersteunen, zoals formulieren, zaken, objecten, notificaties, klant- en productinformatie en portaalfunctionaliteit.

### Kopieerbaar

Een omgeving is kopieerbaar als een ander team de aanpak kan herhalen zonder verborgen lokale kennis, handmatige secrets of vaste serverkeuzes uit de oorspronkelijke omgeving.

### GitOps

Een werkwijze waarbij gewenste infrastructuur en applicatieconfiguratie in Git staan. Het cluster haalt die gewenste toestand op en past die toe.

### Generieke laag

De gedeelde basis die voor meerdere omgevingen bruikbaar moet zijn. In deze aanpak staat die laag in `gitops/base/`.

### Environment-laag

De laag met keuzes voor één specifieke omgeving, zoals DNS, storageclass, issuer en SecretStore. In deze aanpak staat die laag in `gitops/environments/<naam>/`.

### Environment-contract

Een YAML-bestand waarin niet-geheime omgevingskeuzes expliciet staan. Scripts gebruiken dit contract om te valideren, renderen en checklists te maken.

### Secret

Een gevoelige waarde zoals een wachtwoord, token of sleutel. Secretwaarden horen niet in Git en niet in openbare logs.

### SecretStore

Een bron of koppeling waar secrets veilig vandaan komen. In Kubernetes kan ExternalSecrets hiermee secrets ophalen zonder de waarden in Git te zetten.

### Gate

Een controlepunt met een duidelijke uitkomst, bijvoorbeeld `PASS` of `FAIL`. Een gate voorkomt dat een omgeving te vroeg live-ready wordt genoemd.

### Smoke-test

Een korte test die bewijst dat een route of component minimaal bereikbaar en functioneel is.

### Drift

Verschil tussen wat in Git staat en wat live in het cluster draait. Drift ontstaat vaak door handmatige livefixes die niet terug naar Git zijn gebracht.

### Flux

Een GitOps-tool die Kubernetes-manifests uit Git toepast op een cluster.

### Flux source-sync

Een gate die controleert of de gewenste commit echt op de branch staat die Flux gebruikt. Dit voorkomt dat live wordt gereconciled vanaf een verkeerde of oude bron.

### Haven

Een set afspraken en hulpmiddelen voor Kubernetes-platformen binnen Common Ground-context. Haven helpt om platformeisen expliciet en toetsbaar te maken.

### Haven+

Aanvullende checks binnen de Haven Compliancy Checker, zoals automatische HTTPS-certificaten, metrics-server en log aggregation.

### Haven Compliancy Checker

Een tool die controleert of een cluster aan Haven-eisen voldoet. In deze aanpak gebruiken we HCC als ontwerpgate: het laat zien welke clusterkeuzes nog ontbreken voor productiegeschiktheid.

### HCC-afwijking

Een expliciet vastgelegde reden waarom een omgeving niet volledig Haven-compliant is. Voor dev kan zo'n afwijking acceptabel zijn. Voor productie vraagt dit een besluit.
