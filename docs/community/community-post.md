# Community-post: Platformdienstverlening overdraagbaar maken

Status: concept voor communitypublicatie, 2026-05-21. Aangevuld op 2026-05-30 met componentgerichte startgates.

## Korte versie

We hebben een aanpak uitgewerkt om een Platformdienstverlening-omgeving beter overdraagbaar te maken naar andere teams, leveranciers of gemeenten. De kern: zet generieke GitOps-manifests los van lokale omgevingskeuzes, houd secrets buiten Git en gebruik gates om te bewijzen dat een omgeving klaar is voor de volgende stap.

Dit is bewust geen succesverhaal zonder kanttekeningen. De huidige dev-omgeving is functioneel gevalideerd, maar de Haven Compliancy Checker laat ook zien dat het cluster geen productie-Haven-cluster is. Dat verschil hoort zichtbaar te zijn.

## Waarom dit belangrijk is

Veel platformomgevingen zijn wel werkend, maar niet makkelijk te herhalen. De kennis zit dan in vaste hostnames, handmatige fixes, lokale secrets, specifieke storagekeuzes of aannames over het cluster. Dat maakt overdracht kwetsbaar.

Deze aanpak maakt die afhankelijkheden expliciet:

- generieke manifests in `gitops/base/`
- omgevingskeuzes in `gitops/environments/<naam>/`
- een environment-contract voor DNS, issuer, storage, SecretStore, databasehost en imagePullSecret
- validators en gates voor contract, secrets, render, install, CI, DNS/TLS, Flux, smoke en drift
- componentkaarten en startgates voor bronmatrix, hergebruik, API-compatibiliteit, logging, IAM, smoke, rollback en governance

## Voor niet-technische lezers

De waarde zit vooral in bestuurbaarheid. Teams kunnen beter zien wat klaar is, wat nog risico geeft en welke afwijkingen bewust zijn geaccepteerd. Dat maakt overdracht naar een andere partij of omgeving minder afhankelijk van ongeschreven kennis.

## Voor architecten en programmamanagers

De aanpak geeft een referentiepatroon voor herhaalbare platformomgevingen. De architectuur scheidt generieke componenten van lokale keuzes en gebruikt bewijslogs als overdrachtsmiddel. Daardoor kun je per omgeving bepalen welke voorwaarden gelden voor dev, acceptatie of productie.

## Voor developers en leveranciers

De aanpak is toetsbaar. Je kunt een environment genereren, het contract invullen, secrets buiten Git leveren en daarna gates draaien. Een omgeving is pas klaar voor de volgende stap als de gates groen zijn of een afwijking expliciet is vastgelegd.

## Haven en Haven+

De Haven Compliancy Checker is onderdeel van de aanpak. De huidige dev-server scoorde:

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

De scan slaagt niet door:

- geen meerdere availability zones
- geen minimaal 3 master nodes
- geen minimaal 3 worker nodes
- geen log aggregation

Tegelijk zijn onderdelen uit Haven+ wel aanwezig:

- automatische HTTPS-certificaten
- metrics-server

De les: gebruik HCC niet alleen als eindkeuring, maar als ontwerpgate. Een dev-cluster mag afwijken, maar die afwijking moet zichtbaar, verklaard en toetsbaar zijn.

## Wat al bewezen is

De huidige aanpak heeft bewijs voor:

- copyability-scan
- render-gate
- install-gate
- CI-gate
- Flux source-sync
- DNS/TLS-smoke
- platform smoke bundle
- live release gate suite op de huidige dev-omgeving

## Wat nog niet bewezen is

Er is nog geen echte tweede-server live cutover uitgevoerd. Dat is een bewuste beperking. De communitywaarde zit nu in de methode, de structuur en de gates. Een tweede-server cutover blijft de volgende validatiestap zodra er een doelcluster is.

## Oproep

We zoeken vooral feedback op:

- mist er een gate voor jullie organisatie?
- is het environment-contract compleet genoeg?
- welke HCC- of Haven+ checks moeten als harde eis gelden per omgeving?
- welke documentatie helpt technische en niet-technische teams om dezelfde status te begrijpen?

## Startpunten

- `docs/community/README.md`
- `docs/community/bestuurlijke-samenvatting.md`
- `docs/community/referentiearchitectuur.md`
- `docs/community/technische-handleiding.md`
- `docs/community/validatie-en-bewijs.md`
- `docs/community/lessons-learned.md`
- `docs/community/presentatie-outline.md`
- `docs/community/begrippenlijst.md`
- `docs/community/reviewverzoeken.md`
