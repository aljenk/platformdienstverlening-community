# Lessons learned kopieerbare Platformdienstverlening

Status: eerste communityversie, 2026-05-21.

## Les 1: werkend is niet hetzelfde als overdraagbaar

Een omgeving kan functioneel werken en toch lastig te kopiëren zijn. Hardcoded DNS, IP's, storageclasses, issuers en secretverwijzingen maken overdracht kwetsbaar.

Herbruikbaar patroon:

- generieke laag schoon houden
- lokale keuzes naar environment-overlays verplaatsen
- contract gebruiken als expliciete invoer

## Les 2: HCC-falen is nuttige informatie

De huidige dev-server is niet Haven-compliant. Dat is geen reden om de methode niet te delen. Het is juist een nuttig onderscheid tussen dev-referentie en productie-eis.

Faalredenen:

- geen meerdere availability zones
- geen 3 masters
- geen 3 workers
- geen log aggregation

Herbruikbaar patroon:

- HCC vóór livegang uitvoeren
- afwijkingen expliciet documenteren
- dev-afwijking niet als productieclaim presenteren

## Les 3: secrets horen niet in Git of statuslogs

Secretwaarden zijn niet nodig om te bewijzen dat een omgeving werkt. Keynamen, keycount, ExternalSecret-status en pod-env aanwezigheid zijn meestal genoeg.

Herbruikbaar patroon:

- secret inventory gate gebruiken
- alleen metadata loggen
- handmatige dev-secrets apart als afwijking documenteren

## Les 4: livefixes moeten terug naar GitOps

Een handmatige livefix lost soms snel een probleem op, maar creëert drift als de repo niet wordt bijgewerkt.

Herbruikbaar patroon:

- livefix toepassen alleen met bewijs
- repo-patch maken
- render of driftcheck draaien
- commit vastleggen

## Les 5: source-sync vóór reconcile voorkomt verkeerde live-acties

Flux kan alleen veilig reconciliëren als de gewenste commit echt op de Flux-branche staat.

Herbruikbaar patroon:

- `check_flux_source_sync.py --fetch --required-ref HEAD`
- pas daarna live reconcile

## Les 6: een tweede-server cutover is geen voorwaarde voor communitywaarde

Zonder tweede server kun je nog steeds de methode delen:

- generator
- contract
- render
- install-gate
- CI-gate
- live cutover checklist
- HCC-interpretatie
- smoke- en driftpatroon

Communitywaarde zit in de reproduceerbare aanpak, niet alleen in één extra installatie.
