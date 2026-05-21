# Community-publicatieplan Platformdienstverlening

Status: aanpak vastgelegd, eerste outline gemaakt, 2026-05-21.

## Doel

De kopieerbare Platformdienstverlening-aanpak delen met de community zonder te wachten op een tweede server. De publicatie moet bruikbaar zijn voor technische en niet-technische mensen.

Kernboodschap:

> Een platformomgeving wordt pas overdraagbaar als lokale keuzes, secrets en DNS niet in de generieke laag zitten, en als teams met gates kunnen aantonen dat de omgeving voldoet.

## Wat we delen

1. De methode
   - generieke GitOps-laag in `gitops/base/`
   - environment-specifieke laag in `gitops/environments/<naam>/`
   - environment-contract voor DNS, issuer, storage, SecretStore, databasehost en imagePullSecret
   - secrets buiten Git
   - gates vóór claims: contract, prereq, secret inventory, render, install, CI, DNS/TLS, Flux, smoke en drift

2. De reden
   - minder afhankelijk van één server of één ontwikkelomgeving
   - sneller overdraagbaar naar gemeenten, leveranciers of andere teams
   - minder risico op verborgen handmatige fixes
   - objectief bewijs via logs in plaats van mondelinge status

3. De beperkingen
   - een tweede server is nog niet live gereconciled
   - de huidige dev-server is bewust geen productie-Haven-cluster
   - productiegebruik vraagt aanvullende clusterkeuzes, vooral hoge beschikbaarheid en logging

## Doelgroepen

### Niet-technisch

Waarde:

- Sneller en veiliger hergebruik van een werkende platformaanpak.
- Minder afhankelijkheid van individuele beheerders of impliciete kennis.
- Beter bestuurbaar risico doordat gates aantonen wat werkt en wat nog niet.

Boodschap:

- Dit is geen losse technische installatie, maar een overdraagbare werkwijze.
- De aanpak maakt expliciet welke keuzes lokaal zijn en welke onderdelen herbruikbaar zijn.
- Niet alles hoeft direct productiegeschikt te zijn, zolang afwijkingen zichtbaar en bestuurbaar zijn.

Hulpmiddel:

- bestuurlijke samenvatting met waarde, risico's en besluitpunten
- praatplaat of presentatie-outline

### Architect / programmamanager

Waarde:

- Duidelijke scheiding tussen referentiearchitectuur en omgevingskeuzes.
- Herhaalbare validatie per laag.
- Een route om dev, acceptatie en productie met hetzelfde patroon te beheren.

Boodschap:

- De architectuur gebruikt een contractgestuurd GitOps-model.
- De generieke laag bevat geen DNS-, IP-, secret- of serverkeuzes.
- Elke omgeving krijgt een eigen contract en eigen validatiebewijs.

Hulpmiddel:

- referentiearchitectuur
- releasegate-overzicht
- checklist voor live cutover

### Developer / leverancier

Waarde:

- Concreet startpunt met scripts, contractvelden en testbare gates.
- Minder giswerk bij installatie en overdracht.
- Duidelijk bewijs wanneer iets werkt.

Boodschap:

- Genereer een environment, vul het contract in, lever secrets buiten Git en draai de gates.
- Stop bij eerste `FAIL`; los eerst prereq, secret, render, Flux of smoke op.
- Publiceer geen secretwaarden in Git of logs.

Hulpmiddel:

- technische handleiding
- commando-overzicht
- voorbeeldcontract
- validatie- en bewijsdocument

## Haven, Haven+ en HCC

De Haven Compliancy Checker is onderdeel van de publicatie, juist omdat de scan laat zien waar een dev-cluster afwijkt van productie-eisen.

Uitkomst huidige scan:

```text
Results: 11 out of 15 checks passed, 0 checks skipped, 0 checks unknown. This is NOT a Haven Compliant cluster.
```

Waarom de scan niet slaagt:

- Multiple availability zones in use: `NO`
- Running at least 3 master nodes: `NO`
- Running at least 3 worker nodes: `NO`
- Log aggregation is running: `NO`

Betekenis:

- De huidige omgeving is een single-node dev-server en geen productiecluster.
- De technische platformdiensten kunnen werken, maar productiegeschiktheid vraagt aanvullende infrastructuur.
- De HCC-uitkomst wordt daarom geen weggepoetste fout, maar een expliciete prereq- en afwijkingsgate.

Haven+ detail:

- Automated HTTPS certificate provisioning: `YES`
- Metrics-server is running: `YES`
- Log aggregation is running: `NO`

Publicatieboodschap:

- Haven+ is niet alleen een keurmerk achteraf, maar een ontwerpinput voor overdraagbaarheid.
- Een dev-cluster mag afwijken, maar die afwijking moet zichtbaar zijn, verklaard worden en niet als productieclaim worden verkocht.

Bewijsbronnen:

- `docs/havenplus/haven-compliancy-checker-uitvoering-2026-05-20.md`
- `logs/haven-compliancy/20260520T085616Z-haven-check-host-sudo.log`
- `logs/haven-compliancy/20260520T085616Z-haven-check-host-sudo.json`

## Publicatiebundel

1. `docs/community/README.md`
   - korte ingang voor iedereen
   - verwijst naar de overige documenten

2. `docs/community/bestuurlijke-samenvatting.md`
   - waarde, risico's, besluiten en beperkingen

3. `docs/community/referentiearchitectuur.md`
   - lagenmodel, GitOps-flow, environment-contract, secrets en gates

4. `docs/community/technische-handleiding.md`
   - stap-voor-stap uitvoering met commando's

5. `docs/community/validatie-en-bewijs.md`
   - welke gate bewijst wat
   - voorbeeld van bewijsregels zonder secretwaarden

6. `docs/community/lessons-learned.md`
   - wat misging
   - welke patronen herbruikbaar zijn

7. `docs/community/presentatie-outline.md`
   - opbouw voor demo, meetup of communitysessie

## Publicatievoorwaarden

Voor publicatie moet de bundel:

- geen secretwaarden bevatten
- interne hostnames en IP's alleen noemen als bewust voorbeeld of bewijscontext
- incidentdetails neutraliseren naar leerpunten
- duidelijk maken dat er nog geen tweede-server live cutover is gedaan
- HCC/Haven+ uitkomst eerlijk benoemen
- technische stappen toetsbaar houden met scripts en gates
- niet-technische waarde expliciet maken

## Eerste uitvoerstap

Maak een community-outline als ingang voor de hele bundel. De outline moet:

- de drie doelgroepen apart bedienen
- Haven+ en HCC expliciet uitleggen
- duidelijk maken waarom de scan niet slaagt
- verwijzen naar bestaande bewijsdocumenten
- aangeven welke documenten daarna worden uitgewerkt
