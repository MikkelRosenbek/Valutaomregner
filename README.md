# Valutaomregner CLI

Et simpelt Python CLI-program til valutaomregning via [ExchangeRate API](https://www.exchangerate-api.com/).

## Krav
- Python 3.x

## Kom i gang

### 1) Hent projektet fra GitHub
```powershell
git clone https://github.com/MikkelRosenbek/Valutaomregner.git
cd Valutaomregner
```

### 2) Opret virtual environment (Windows)
```powershell
py -m venv .venv
.\.venv\Scripts\activate
```

### 3) Installer dependencies
```powershell
pip install -r requirements.txt
```

### 4) API key
Opret en `.env` fil i projektmappen med:

```env
API_KEY={DIN-API-KEY}
```

## Kør programmet

### Første gang(med key direkte)
```powershell (eksempel)
python valuta.py --key{API_KEY} --from <valutakode> --to <valutakode> --ammount <beløb>
```

### Efterfølgende key fra .env
```powershell
python valuta.py --from <valutakode> --to <valutakode> --amount <beløb>
```

## Argumenter
- `--key` API nøgle (valgfri, hvis `API_KEY` findes i `.env`)
- `--from` fra-valuta (fx `USD`)
- `--to` til-valuta (fx `DKK`)
- `--amount` beløb der skal omregnes (fx `100`)
