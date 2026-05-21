# Kanaalteksten reviewpublicatie Platformdienstverlening

Status: conceptteksten voor reviewpublicatie, 2026-05-21.

## Doel

Deze teksten zijn bedoeld om de communitybundel gericht te delen voor review. Ze zijn nog geen externe publicatie. Gebruik ze pas na expliciet akkoord op kanaal en doelgroep.

## Korte communitypost

Titel:

```text
Review gevraagd: Platformdienstverlening overdraagbaar maken met GitOps, gates en Haven-duiding
```

Tekst:

```text
We hebben een eerste communityversie gemaakt van een aanpak om een Platformdienstverlening-omgeving overdraagbaar te maken naar andere teams, leveranciers of gemeenten.

De kern: scheid generieke GitOps-manifests van lokale omgevingskeuzes, houd secrets buiten Git en gebruik gates om te bewijzen dat een omgeving klaar is voor de volgende stap.

Dit is bewust een reviewversie. Er is nog geen tweede-server live cutover uitgevoerd. De huidige dev-omgeving is functioneel gevalideerd, maar de Haven Compliancy Checker laat ook zien dat dit geen productie-Haven-cluster is: 11 van 15 checks zijn geslaagd. Niet geslaagd zijn availability zones, 3 masters, 3 workers en log aggregation.

Feedback gezocht op:
- missen er gates of contractvelden?
- is de uitleg bruikbaar voor niet-technische lezers?
- klopt de Haven/Haven+ duiding?
- kan een developer of leverancier hiermee een dry-run uitvoeren?

Startpunt: docs/community/publicatie-index.md
```

## GitHub Discussion tekst

```markdown
## Review gevraagd: kopieerbare Platformdienstverlening

We delen een eerste communityversie van een aanpak om een Platformdienstverlening-omgeving overdraagbaar te maken.

### Waarom

Veel platformomgevingen werken technisch, maar zijn lastig te herhalen. Lokale DNS, secrets, storagekeuzes, handmatige fixes en clusterafhankelijkheden zitten vaak impliciet in de implementatie.

Deze aanpak maakt die afhankelijkheden expliciet met:

- `gitops/base/` voor generieke manifests
- `gitops/environments/<naam>/` voor omgevingskeuzes
- een environment-contract
- secrets buiten Git
- gates voor contract, prereqs, secrets, render, install, CI, DNS/TLS, Flux, smoke en drift

### Belangrijke beperking

Dit is een reviewversie. Er is nog geen echte tweede-server live cutover uitgevoerd.

De huidige dev-server is ook geen productie-Haven-cluster. HCC geeft:

```text
11 out of 15 checks passed
This is NOT a Haven Compliant cluster
```

Niet geslaagd:

- geen meerdere availability zones
- geen 3 master nodes
- geen 3 worker nodes
- geen log aggregation

### Waar graag feedback op

- Welke gates missen voor jullie organisatie?
- Is het environment-contract compleet genoeg?
- Is de HCC/Haven+ duiding bruikbaar?
- Is de technische handleiding uitvoerbaar voor een dry-run?
- Welke uitleg mist voor niet-technische lezers?

### Startpunten

- `docs/community/publicatie-index.md`
- `docs/community/community-post.md`
- `docs/community/reviewverzoeken.md`
- `docs/community/technische-handleiding.md`
- `docs/community/publicatie-readiness-2026-05-21.md`
```

## Bericht voor architectuuroverleg

```text
Ik wil een eerste reviewversie delen van een referentieaanpak voor kopieerbare Platformdienstverlening.

De aanpak scheidt generieke GitOps-manifests van omgevingskeuzes via een environment-contract. Daarnaast gebruikt de aanpak gates voor contractvalidatie, prereqs, secrets, render, install, CI, DNS/TLS, Flux source-sync, smoke en drift.

Specifieke reviewvraag voor architectuur: is de scheiding tussen generieke laag, environment-laag en contractlaag voldoende om dev, acceptatie en productie beheersbaar te maken?

Belangrijke context: de huidige dev-server is niet productie-Haven-compliant. HCC scoort 11/15. De ontbrekende punten zijn meerdere availability zones, 3 masters, 3 workers en log aggregation. We positioneren HCC daarom als ontwerpgate en niet als eindstempel.

Startpunt: docs/community/referentiearchitectuur.md
```

## Bericht voor developer of leverancier

```text
Kun je een technische dry-run reviewen van onze kopieerbare Platformdienstverlening-aanpak?

De handleiding laat zien hoe je een environment genereert, het contract valideert, secrets buiten Git houdt, gates draait en een live cutover checklist maakt zonder direct een tweede server te gebruiken.

Graag feedback op:
- zijn de commando's logisch en uitvoerbaar?
- geven de gates genoeg informatie bij fouten?
- ontbreken er validators of voorbeeldcontracten?
- kun je dit volgen zonder secretwaarden nodig te hebben?

Startpunten:
- docs/community/technische-handleiding.md
- docs/community/demo-draaiboek-zonder-tweede-server.md
- docs/community/demo-uitvoering-2026-05-21.md
```

## Kort bericht voor chat

```text
We hebben een reviewversie klaar van de aanpak om Platformdienstverlening overdraagbaar te maken: generieke GitOps-laag, environment-contracten, secrets buiten Git en gates met bewijslogs.

Belangrijke nuance: geen tweede-server live cutover, en de huidige dev-server is niet productie-Haven-compliant. HCC: 11/15 checks geslaagd; rood op availability zones, 3 masters, 3 workers en log aggregation.

Startpunt voor review: docs/community/publicatie-index.md
Feedback graag op gates, contractvelden, Haven/Haven+ duiding en begrijpelijkheid voor niet-technische lezers.
```

## Niet gebruiken zonder expliciet akkoord

- externe publicatie op sociale media
- mail naar externe groepen
- GitHub Discussion openen
- repository release maken
- pakket uploaden of delen buiten de huidige omgeving
