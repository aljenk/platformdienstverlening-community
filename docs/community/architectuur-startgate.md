# Architectuur-startgate voor platformcomponenten

Status: communityversie, 2026-05-30.
Doelgroep: architecten, platform owners, developers en leveranciers.

## Doel

De architectuur-startgate voorkomt dat een platformcomponent start met ontbrekende bronkeuze, onduidelijk hergebruik, impliciete API-keuzes, niet-testbare secrets of IAM, of een ontbrekend smoke- en rollbackpad.

Gebruik de gate vóór technische implementatie, activatie of grote wijziging van een component.

## Wanneer gebruiken

Gebruik deze gate vóór:

- een nieuw Kubernetes-component in een platformlaag
- een grote wijziging aan een bestaand component
- nieuwe API-koppelingen of registerkoppelingen
- nieuwe secrets, serviceaccounts of gebruikersauth
- patronen die overdraagbaar moeten blijven naar andere omgevingen

## Startgate-checklist

Een startgate is groen als alle punten `PASS` hebben of een expliciete architectuurexceptie met eigenaar en herzienmoment hebben.

| Gate | Minimumeis | Bewijs |
| --- | --- | --- |
| Componentkaart | Template ingevuld voor dienstverlening, proces, informatie, API, logging, IAM, secrets, smoke, rollback en governance | Pad naar componentkaart |
| Bronmatrix | Leidende bron, cache, lokale kopie, synchronisatie, bewaartermijn en correctiepad ingevuld | Tabel of runbooksectie |
| Hergebruikscan | Bouwblokken, businessservices, registers en API's gecontroleerd vóór nieuwbouw | Scanresultaat met besluit |
| API-compatibiliteit | Patroon, specificatie, versiebeleid, foutafhandeling en backwards compatibility gekozen | API-sectie of contractpad |
| Secrets testbaar | Secretstrategie, bronpad, keynamen en bewijs zonder waarden beschreven | Secret inventory, ExternalSecret status of dev-exceptie |
| IAM testbaar | Authenticatie, autorisatie, rollen, claims, context en beheerpad beschreven | Smokeplan of login/service-auth bewijsplan |
| Smoke beschreven | Minimale publieke of service-interne rooktest beschreven | Commando, jobnaam of scriptpad |
| Rollback beschreven | Terugvalpad voor image, release, config of databasewijziging beschreven | Rollbacksectie |
| Governance | Afwijkingen en lifecycle-eigenaars bekend | Exceptielijst met eigenaar en datum |

## Gate-output

Gebruik dit compacte blok in uitvoerdocumenten:

```markdown
## Architectuur-startgate

Status: PASS | FAIL | PASS met exceptie
Datum: <YYYY-MM-DD>
Componentkaart: <pad>
Bronmatrix: PASS | FAIL, bewijs: <pad>
Hergebruikscan: PASS | FAIL, bewijs: <pad>
API-compatibiliteit: PASS | FAIL, bewijs: <pad>
Secrets/IAM testbaar: PASS | FAIL, bewijs: <pad>
Smoke/rollback beschreven: PASS | FAIL, bewijs: <pad>
Governance-excepties: geen | <lijst met eigenaar en herzienmoment>
Controle: akkoord | afwijking, bewijs: <pad>
```

## Stopregel

Bij een `FAIL` start implementatie niet. Leg vast:

- Oorzaak: welke gate ontbreekt
- Eerste herstelactie: welk document, testplan of besluit wordt aangevuld
- Status: niet afgerond

## Relatie met releasegates

Deze startgate vervangt geen technische releasegates. Na een groene startgate blijven technische gates nodig, zoals contractcontrole, prereqs, secret inventory, render, install, Flux source-sync, DNS/TLS, smoke en driftcontrole.

## Minimale werkwijze

1. Vul de componentkaart in.
2. Controleer bronmatrix en hergebruikscan.
3. Kies API-patroon en compatibiliteitsbeleid.
4. Maak secrets en IAM testbaar zonder waarden te publiceren.
5. Beschrijf smoke en rollback.
6. Leg governance-excepties vast.
7. Start pas implementatie na `PASS` of na expliciet geaccepteerde exceptie.
