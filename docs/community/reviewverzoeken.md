# Reviewverzoeken communitybundel Platformdienstverlening

Status: concept voor externe review, 2026-05-21.

## Doel

Deze reviewverzoeken helpen om gericht feedback op te halen bij drie doelgroepen. De teksten zijn kort genoeg om in mail, chat, issue of GitHub-discussie te gebruiken.

## Reviewverzoek voor niet-technische lezers

### Doelgroep

Bestuurders, programmamanagers, product owners en beleidsmedewerkers zonder dagelijkse Kubernetes- of GitOps-achtergrond.

### Bericht

We hebben een aanpak beschreven om een Platformdienstverlening-omgeving beter overdraagbaar te maken naar andere teams, leveranciers of gemeenten.

Wil je vooral kijken naar de bestuurlijke samenvatting en aangeven:

- is duidelijk welk probleem dit oplost?
- is helder welk risico kleiner wordt?
- is duidelijk dat de huidige dev-omgeving geen productie-Haven-cluster is?
- zijn de besluitpunten concreet genoeg?
- mis je informatie om prioriteit of vervolg te bepalen?

Startdocumenten:

- `docs/community/README.md`
- `docs/community/bestuurlijke-samenvatting.md`
- `docs/community/begrippenlijst.md`

Gewenste feedbackvorm:

- maximaal 5 opmerkingen
- markeer wat onduidelijk is
- geef aan welke zin of sectie scherper moet

## Reviewverzoek voor architecten en programmamanagers

### Doelgroep

Enterprise-architecten, solution-architecten, programmamanagers, platform owners en technisch coördinatoren.

### Bericht

We hebben een referentieaanpak uitgewerkt voor een kopieerbare Platformdienstverlening-omgeving. De kern is een scheiding tussen generieke GitOps-manifests, environment-specifieke overlays en een environment-contract.

Wil je vooral toetsen:

- klopt de scheiding tussen generieke laag, environment-laag en contractlaag?
- zijn de gates compleet genoeg voor dev, acceptatie en productie?
- is de Haven/Haven+ interpretatie bruikbaar als ontwerpgate?
- zijn de HCC-afwijkingen duidelijk genoeg vertaald naar architectuurkeuzes?
- missen er principes rond beheer, eigenaarschap, security of overdracht?

Startdocumenten:

- `docs/community/referentiearchitectuur.md`
- `docs/community/validatie-en-bewijs.md`
- `docs/community/publicatie-review-checklist.md`
- `docs/community/bestuurlijke-samenvatting.md`

Gewenste feedbackvorm:

- benoem blokkerende punten apart
- geef per punt aan of het een architectuurrisico, governancepunt of tekstverbetering is

## Reviewverzoek voor developers en leveranciers

### Doelgroep

Developers, platform engineers, Kubernetes-beheerders, leveranciers en implementatiepartners.

### Bericht

We hebben een technische handleiding gemaakt om een Platformdienstverlening-omgeving reproduceerbaar op te bouwen met een environment-contract, gates en bewijslogs.

Wil je vooral toetsen:

- zijn de commando's uitvoerbaar en logisch geordend?
- zijn de stopregels concreet genoeg?
- zijn de gate-uitkomsten voldoende duidelijk?
- ontbreken er validators, voorbeeldcontracten of foutmeldingen?
- kun je hiermee een dry-run uitvoeren zonder secrets?

Startdocumenten:

- `docs/community/technische-handleiding.md`
- `docs/community/validatie-en-bewijs.md`
- `docs/community/lessons-learned.md`
- `docs/community/begrippenlijst.md`

Gewenste feedbackvorm:

- noteer bij elk probleem het commando of de sectie
- geef aan of het documentatie, scriptgedrag of ontbrekende prereq is
- voeg waar mogelijk verwachte output toe

## Reviewverzoek voor communitydiscussie

### Doelgroep

Gemengde community: beleid, architectuur, beheer, ontwikkeling en leveranciers.

### Bericht

We delen een eerste communityversie van een aanpak om Platformdienstverlening overdraagbaar te maken.

De centrale vraag:

> Welke gates, contractvelden of uitleg ontbreken om deze aanpak herbruikbaar te maken voor andere organisaties?

Belangrijke context:

- er is nog geen tweede-server live cutover uitgevoerd
- de huidige dev-omgeving is functioneel gevalideerd
- de Haven Compliancy Checker toont dat het huidige dev-cluster geen productie-Haven-cluster is
- de HCC-uitkomst is bewust onderdeel van de aanpak, zodat dev-afwijkingen zichtbaar blijven

Startdocument:

- `docs/community/community-post.md`

Feedbackvragen:

- wat is direct bruikbaar?
- wat is te project-specifiek?
- welke productie-eisen ontbreken?
- welke uitleg helpt niet-technische lezers?
- welke technische gate mist nog?

## Verwerking van feedback

Gebruik deze rubric:

- `blokkerend`: moet vóór publicatie worden opgelost
- `belangrijk`: verwerken vóór brede verspreiding
- `verbetering`: verwerken als tijd beschikbaar is
- `later`: bewaren voor tweede-server validatie of vervolgversie

Leg feedback vast in `docs/community/feedback-register.md` of via `.github/ISSUE_TEMPLATE/community-feedback.yml`.

Leg feedback vast met:

- doelgroep
- document
- sectie
- opmerking
- gekozen verwerking
- commit waarin de verwerking staat
