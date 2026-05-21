# Publicatie-review checklist Platformdienstverlening communitybundel

Status: eerste reviewchecklist, 2026-05-21.

## Doel

Deze checklist maakt de communitybundel publiceerbaar zonder een tweede server. De review controleert of de inhoud begrijpelijk is voor meerdere doelgroepen, veilig te delen is en eerlijk blijft over de Haven/Haven+ uitkomst.

## Reviewlagen

### 1. Doelgroepreview

Controleer dat de bundel drie ingangen heeft:

- niet-technisch: waarde, risico, besluitpunten
- architect / programmamanager: samenhang, lagenmodel, governance, randvoorwaarden
- developer / leverancier: scripts, commando's, gates, stopregels

Klaarcriterium:

- elke doelgroep heeft een eigen document of duidelijke sectie
- elke doelgroep krijgt een concrete vervolgstap

### 2. Haven/Haven+ review

Controleer dat de HCC-uitkomst niet wordt weggelaten of mooier gemaakt.

Verplicht opnemen:

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

Verplicht uitleggen waarom de scan niet slaagt:

- geen meerdere availability zones
- geen 3 master nodes
- geen 3 worker nodes
- geen log aggregation

Verplicht uitleggen wat wel werkt in Haven+:

- automated HTTPS certificate provisioning
- metrics-server

Klaarcriterium:

- de bundel maakt duidelijk dat de huidige dev-omgeving geen productie-Haven-cluster is
- de bundel positioneert HCC als ontwerpgate en niet alleen als eindkeuring

### 3. Veilig-deelbaar review

Controleer dat de communitydocs geen onnodige interne details bevatten.

Niet opnemen:

- secretwaarden
- tokens
- wachtwoorden
- persoonsgegevens
- interne IP-adressen
- organisatie-specifieke hostnames als die niet nodig zijn voor begrip
- incidentdetails die niet nodig zijn voor de herbruikbare les

Wel toegestaan:

- generieke secretnamen als concept
- voorbeeldnamen zoals `acc.platform.example.org`
- scriptnamen, contractvelden en statusregels
- HCC-resultaten zonder gevoelige clusterdata

Klaarcriterium:

- gevoelige details zijn verwijderd of neutraal gemaakt
- uitzonderingen zijn bewust en uitlegbaar

### 4. Bewijsreview

Controleer dat claims terugverwijzen naar bron of bewijs.

Minimale bronnen:

- `docs/havenplus/haven-compliancy-checker-uitvoering-2026-05-20.md`
- `logs/haven-compliancy/20260520T085616Z-haven-check-host-sudo.log`
- `docs/havenplus/kopieerbare-implementatie-uitvoering-2026-05-20.md`
- `docs/install/platformdienstverlening-copyable-install.md`
- `docs/install/generated/platformdienstverlening-dev-live-cutover-checklist.md`

Klaarcriterium:

- statusclaims hebben een bron of logpad
- technische instructies verwijzen naar bestaande scripts of docs

### 5. Publicatievorm

Aanbevolen volgorde voor publicatie:

1. `docs/community/README.md`
2. `docs/community/bestuurlijke-samenvatting.md`
3. `docs/community/referentiearchitectuur.md`
4. `docs/community/technische-handleiding.md`
5. `docs/community/validatie-en-bewijs.md`
6. `docs/community/lessons-learned.md`
7. `docs/community/presentatie-outline.md`

Klaarcriterium:

- de README kan zelfstandig gelezen worden
- technische lezers kunnen vanaf de README naar commando's en gates
- niet-technische lezers krijgen waarde en risico zonder eerst scripts te hoeven begrijpen

## Automatische check

Gebruik:

```sh
scripts/community_publication_check.py
```

De check controleert:

- verplichte communitybestanden bestaan
- HCC/Haven+ termen aanwezig zijn
- scanredenen aanwezig zijn
- geen em-dash in communitydocs
- geen bekende interne domeinen, interne IP-adressen, organisatienamen of e-mailadressen in communitydocs

Deze automatische check vervangt geen menselijke review, maar voorkomt de meest duidelijke publicatiefouten.
