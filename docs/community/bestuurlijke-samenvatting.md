# Bestuurlijke samenvatting Platformdienstverlening

Status: eerste communityversie, 2026-05-21.

## Kernboodschap

De Platformdienstverlening-aanpak maakt een werkende platformomgeving beter overdraagbaar. Dat gebeurt door lokale keuzes, zoals DNS, secrets, storage en issuers, los te trekken van de generieke GitOps-laag. Daardoor kunnen gemeenten, leveranciers en beheerpartijen sneller aansluiten zonder impliciete kennis uit één dev-omgeving over te nemen.

## Waarom dit relevant is

Veel platformprojecten werken technisch, maar zijn lastig te herhalen. De oorzaak is vaak niet één kapotte component, maar verborgen afhankelijkheden: lokale secrets, vaste hostnames, handmatige fixes, onduidelijke clusterkeuzes en ontbrekend bewijs. Deze aanpak maakt die afhankelijkheden zichtbaar en toetsbaar.

## Wat de community krijgt

- Een reproduceerbare structuur voor platformomgevingen.
- Een environment-contract waarin lokale keuzes expliciet staan.
- Gates die aantonen of een omgeving klaar is voor de volgende stap.
- Bewijslogs waarmee teams status kunnen overdragen.
- Een eerlijke scheiding tussen dev-geschiktheid en productiegeschiktheid.

## Waarde voor bestuur en programma

- Minder risico bij overdracht tussen teams of leveranciers.
- Snellere onboarding van nieuwe omgevingen.
- Beter zicht op wat klaar is en wat nog een expliciete afwijking is.
- Minder afhankelijkheid van individuele beheerders.
- Betere basis voor besluitvorming over productie-eisen.

## Haven en Haven+

De Haven Compliancy Checker is bewust onderdeel van deze aanpak. De scan helpt om het verschil tussen een werkende dev-omgeving en een productiegeschikte omgeving zichtbaar te maken.

De huidige dev-server scoorde:

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

De scan slaagt niet door:

- geen meerdere availability zones
- geen minimaal 3 master nodes
- geen minimaal 3 worker nodes
- geen log aggregation

Haven+ onderdelen uit de scan:

- Automated HTTPS certificate provisioning: geslaagd
- Metrics-server: geslaagd
- Log aggregation: niet geslaagd

Bestuurlijke betekenis:

- De dev-omgeving is bruikbaar als referentie voor de methode.
- De dev-omgeving mag niet als productie-Haven-compliant worden gepresenteerd.
- Voor productie is een expliciet besluit nodig over hoge beschikbaarheid, schaal, logging en compliancy.

## Besluitpunten

Voor een organisatie die deze aanpak wil gebruiken:

- Welke omgevingen zijn nodig: dev, acceptatie, productie?
- Welke Haven-compliancy-eisen gelden per omgeving?
- Welke afwijkingen zijn tijdelijk acceptabel en wie keurt die goed?
- Wie beheert secrets en SecretStores?
- Wie is eigenaar van de releasegates en bewijslogs?
- Wanneer mag een omgeving live-ready worden genoemd?

## Niet claimen

Deze communityversie claimt niet dat er al een tweede server live is gereconciled. De aanpak is wel voorbereid, gevalideerd met lokale gates en live bewezen op de huidige dev-omgeving.

## Eerstvolgende stap

Werk de referentiearchitectuur en technische handleiding uit, zodat niet-technische besluitvorming en technische uitvoering op dezelfde aanpak aansluiten.
