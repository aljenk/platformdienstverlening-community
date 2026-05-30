# Componentkaart-template Platformdienstverlening

Status: communityversie, 2026-05-30.
Doelgroep: architecten, platform owners, developers en leveranciers.

## Waarom deze kaart bestaat

Een platformcomponent is pas overdraagbaar als duidelijk is welke dienst het ondersteunt, welke gegevens het gebruikt, welke bron leidend is, hoe koppelingen werken en hoe beheer, logging, IAM en governance zijn geregeld.

Gebruik deze template vóór implementatie of grote wijziging van een component.

## Template

```markdown
# Componentkaart: <componentnaam>

Status: concept | klaar voor startgate | in uitvoering | gevalideerd | afwijking
Owner: <team/persoon>
Datum: <YYYY-MM-DD>
Scope: <dev/acc/prod/generiek>
GitOps-pad: <pad of n.v.t.>
Namespace: <namespace of n.v.t.>
Hostnames: <hostnames of n.v.t.>

## 1. Dienstverlening, proces en informatie

- Dienstverlening of businessservice: <welke dienst ondersteunt dit component>
- Proceslaag: <welke processtap of procesbouwblok>
- Informatielaag: <welke informatieobjecten, registers of datasets>
- Interactielaag: <portaal, formulier, API, UI of kanaal>
- Buiten scope: <wat doet dit component expliciet niet>

## 2. Leidende bron, cache en kopie

| Gegeven of object | Leidende bron | Cache toegestaan | Lokale kopie toegestaan | Synchronisatie | Bewaartermijn | Correctiepad |
| --- | --- | --- | --- | --- | --- | --- |
| <gegeven> | <bron> | ja/nee + reden | ja/nee + reden | <trigger/frequentie> | <termijn> | <wie/welk proces> |

Regel: lokale opslag vervangt de leidende bron niet zonder expliciet besluit.

## 3. Hergebruikscan

- Gecontroleerde bouwblokken: <lijst>
- Gecontroleerde businessservices: <lijst>
- Gecontroleerde registers: <lijst>
- Gecontroleerde API's of standaarden: <lijst>
- Uitkomst: hergebruik | uitbreiding | nieuwbouw | architectuurexceptie
- Besluit en reden: <kort>
- Bewijs: <pad/log/link>

## 4. API- en integratiepatroon

- Patroonkeuze: sync API | async events | registerraadpleging | workflowtaak | batch | anders
- API-specificatie: <OpenAPI/AsyncAPI/standaard/pad>
- Versiebeleid: <semver/contractversionering/deprecatie>
- Backwards compatibility: <hoe geborgd>
- Foutafhandeling: <timeouts/retries/idempotency/correlation-id>
- Impactanalyse bij wijziging: <wie beoordeelt mee>

## 5. Logging van techniek en dataverwerking

- Technische logs: <component, logniveau, bestemming>
- Dataverwerkingslogs: <welke verwerkingen worden gelogd>
- Auditdoel: <beheer/security/verantwoording/incidentanalyse>
- Persoonsgegevens in logs: nee | ja, met motivatie en beperking
- Retentie: <termijn>
- Toegang: <rollen/groepen>
- Correlatie-ID: <header/veld/patroon>

## 6. IAM en policy based autorisatie

- Authenticatie: <identity provider, service-account of anders>
- Autorisatie: <rollen/claims/context/policies>
- Policy-context: <welke context bepaalt toegang>
- Service-auth: <client/serviceaccount/secretpad zonder waarden>
- Gebruikersauth: <flow en callback, indien relevant>
- Beheerrechten: <wie mag configureren>
- Testbaar bewijs: <smoke/log/pad>

## 7. Secrets en configuratie

- Secretstrategie: ExternalSecret | handmatige dev-fallback | anders
- SecretStore of bronpad: <naam zonder waarde>
- Verwachte keys: <keynamen, geen waarden>
- Configpad: <values/manifests/environment-contract>
- Bewijs zonder secretwaarden: <keycount/status/hash/lengte/logpad>

## 8. Smoke, rollback en releasebewijs

- Minimale smoke: <commando/job/API/UI-smoke>
- One-off Kubernetes smoke Job nodig: ja/nee
- Rollbackpad: <image/tag/release/config/DB-migratiepad>
- Driftcontrole: <script/commando>
- Klaarbewijs: <logpad en verwachte PASS-regel>

## 9. Governance en excepties

- Eigenaar component: <team/persoon>
- Besluitvorming API-wijzigingen: <gremium/owner>
- Lifecycle en deprecatiepad: <beleid>
- Architectuurexcepties: <geen of lijst>
- Per exceptie: reden, eigenaar, einddatum of herzienmoment
```

## Wanneer is de kaart klaar

Een componentkaart is klaar voor de startgate als:

1. Dienstverlening, proces en informatie concreet zijn ingevuld.
2. Bronmatrix voor leidende bron, cache, kopie, synchronisatie, bewaartermijn en correctiepad is ingevuld.
3. Hergebruikscan is uitgevoerd en gemotiveerd.
4. API-patroon, versiebeleid, foutafhandeling en compatibiliteit zijn gekozen.
5. Logging van dataverwerking naast technische logging is beschreven.
6. IAM en policy based autorisatie testbaar zijn beschreven.
7. Secrets en configuratie bewijsbaar zijn zonder secretwaarden.
8. Smoke en rollback concreet zijn.
9. Governance-excepties eigenaar en herzienmoment hebben.

## Publicatieregel

De kaart bevat geen secretwaarden, geen tokens, geen wachtwoorden en geen persoonsgegevens tenzij daar een expliciete logging- of auditgrond voor is vastgelegd.
