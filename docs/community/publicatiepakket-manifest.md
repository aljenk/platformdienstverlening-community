# Publicatiepakket manifest Platformdienstverlening communitybundel

Status: eerste manifest, 2026-05-21. Aangevuld op 2026-05-30 met componentkaart-template en architectuur-startgate.

## Doel

Dit manifest bepaalt welke bestanden in het deelbare publicatiepakket horen. Het pakket is bedoeld voor review en distributie, niet als definitieve standaard.

## Inhoud

### Start en publicatie

- `docs/community/publicatie-index.md`
- `docs/community/community-post.md`
- `docs/community/release-notes-communitybundel-2026-05-21.md`
- `docs/community/publicatie-readiness-2026-05-21.md`

### Doelgroepdocumenten

- `docs/community/bestuurlijke-samenvatting.md`
- `docs/community/referentiearchitectuur.md`
- `docs/community/technische-handleiding.md`
- `docs/community/begrippenlijst.md`

### Validatie en bewijs

- `docs/community/validatie-en-bewijs.md`
- `docs/community/componentkaart-template.md`
- `docs/community/architectuur-startgate.md`
- `docs/community/demo-draaiboek-zonder-tweede-server.md`
- `docs/community/demo-uitvoering-2026-05-21.md`
- `docs/community/lessons-learned.md`

### Review en feedback

- `docs/community/presentatie-outline.md`
- `docs/community/publicatie-review-checklist.md`
- `docs/community/persona-review-2026-05-21.md`
- `docs/community/reviewverzoeken.md`
- `docs/community/feedback-register.md`
- `docs/community/distributieplan.md`

### Automatische checks en templates

- `scripts/community_publication_check.py`
- `.github/ISSUE_TEMPLATE/community-feedback.yml`

## Niet in het pakket

- interne logs
- secretmateriaal
- lokale workspace-status
- tijdelijke demo-environments
- cluster-specifieke kubeconfigs

## Exportregel

Maak het pakket met:

```sh
scripts/export_community_publication_bundle.sh
```

Verwachte uitkomst:

```text
COMMUNITY_PUBLICATION_BUNDLE status=PASS
```

## Publicatievoorwaarde

Voor delen moet gelden:

```text
COMMUNITY_PUBLICATION_CHECK status=PASS
COMMUNITY_PUBLICATION_BUNDLE status=PASS
```
