# Workplan - Valutaomregner CLI

**Dato:** 3. marts 2026  
**Deadline:** 11:45

## Fase 1 - Minimum-setup (lektion 1)
**Maal:** Projektet kan koere lokalt, og repo er klart.

- [x] Opret projektmappe, Git repo og GitHub repo.
- [x] Opret virtual environment (`venv`).
- [x] Installer pakker: `requests` og `python-dotenv`.
- [x] Opret `.gitignore` (mindst `venv/` og `.env`).
- [x] Lav en enkel `valuta.py`, der kan koere.
- [x] Push foerste commit til GitHub.
- [x] Done-kriterie: Repo ligger paa GitHub, og `python valuta.py` virker i dit venv.

## Fase 2 - CLI med argparse (lektion 2)
**Maal:** Programmet tager imod input korrekt.

- [x] Tilfoej argumentet `--key` (valgfri).
- [x] Tilfoej argumentet `--from` (fra-valuta).
- [x] Tilfoej argumentet `--to` (til-valuta).
- [x] Tilfoej argumentet `--amount` (beloeb).
- [x] Brug `--key`, hvis den er angivet.
- [x] Laes API-noegle fra `.env`, hvis `--key` ikke er angivet.
- [x] Tilfoej basal validering (fx `amount > 0` og tom key).
- [x] Done-kriterie: Programmet kan koeres baade med og uden `--key`.

## Fase 3 - API og omregning (lektion 3)
**Maal:** Valutaomregning virker via ExchangeRate API.

- [ ] Kald API med noegle og base-valuta.
- [ ] Find kurs for maalvaluta.
- [ ] Beregn omregning.
- [ ] Print resultat tydeligt i terminalen.
- [ ] Haandter fejl: ugyldig API-noegle.
- [ ] Haandter fejl: ugyldig valutakode.
- [ ] Haandter fejl: netvaerks-/API-fejl.
- [ ] Done-kriterie: Korrekt resultat ved gyldige input og fornuftige fejlbeskeder ved fejl.

## Fase 4 - README, finish og aflevering (lektion 4)
**Maal:** Brugeren kan koere projektet direkte fra GitHub.

- [ ] Skriv README: krav (Python-version).
- [ ] Skriv README: oprettelse/aktivering af venv.
- [ ] Skriv README: installation (`pip install -r requirements.txt`).
- [ ] Skriv README: `.env` opsaetning.
- [ ] Skriv README: eksempler paa koersel (foerste gang med `--key`, derefter uden).
- [ ] Opret `requirements.txt`.
- [ ] Test hele flowet fra frisk clone.
- [ ] Push alt og aflever GitHub-link paa Itslearning.
- [ ] Done-kriterie: En anden kan foelge README og faa programmet til at virke.

## Prioritering hvis tiden er knap
- [x] CLI virker med `argparse`.
- [ ] API-kald virker.
- [x] `--key`/`.env` fallback virker.
- [ ] README + push til GitHub.
