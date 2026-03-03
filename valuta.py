import argparse #Bruges til at parse argumenter fra kommandolinjen (CLI)
import os #Bruges til at håndtere fil- og mappestrukturer
import sys #Bruges til interaktion med Python-runtime
import requests #Bruges til at lave HTTP-forespørgsler til API'er

from dotenv import load_dotenv #Bruges til at indlæse miljøvariabler fra en .env-fil


def parse_args():

    parser = argparse.ArgumentParser()
    
    #Bruges til at indlæse API-nøglen fra en .env-fil
    parser.add_argument("--key",help="API_KEY")
    
    #Valuta man vil omregne fra
    parser.add_argument(
        "--from",
        dest="from_currency",
        required=True,
        help="Valuta du vil konvertere fra (f.eks. EUR)"
    )
    #Valuta man vil omregne til
    parser.add_argument(
        "--to",
        dest="to_currency",
        required=True,
        help="Valuta du vil konvertere til (f.eks. DKK)"
    )

    #Beløb man vil omregne
    parser.add_argument(
        "--amount",
        dest="amount",
        type=float,
        required=True,
        help="Beløb du vil konvertere (f.eks. 100)"
    )

    #Returnerer alle argumenter i et samlet objekt
    return parser.parse_args()


def get_api_key(arg_key):
    
    #Hvis API-nøglen er angivet som et argument, returner den
    if arg_key:
        return arg_key

    #Ellers, prøv at hente den fra miljøvariablerne
    load_dotenv() 

    #Returnerer API-nøgel fra miljøvariabler
    return os.getenv("API_KEY")
    
#Tjekker om input er gyldigt
def validate_input(args, api_key):
   
   #Hvis ingen API-nøgle
    if not api_key:
        print("Fejl: API-nøgle er påkrævet. Angiv den via --key eller i .env-filen.")
        sys.exit(1)

    #Tjekker om beløbet er større end 0
    if args.amount <= 0:
        print("Fejl: Beløbet skal være større end 0.")
        sys.exit(1)

    #Tjekker om valutakoderne er 3 bogstaver lange og kun indeholder bogstaver
    if len(args.from_currency) != 3:
        print("Fejl: Fra-valuta skal vaere 3 bogstaver (fx USD).")
        sys.exit(1)
    
    #Tjekker om valutakoderne er 3 bogstaver lange og kun indeholder bogstaver
    if len(args.to_currency) != 3:
        print("Fejl: Til-valuta skal vaere 3 bogstaver (fx DKK).")
        sys.exit(1)


def convert_currency(api_key, from_currency, to_currency, amount):
    url = (
        f"https://v6.exchangerate-api.com/v6/{api_key}/pair/"
        f"{from_currency.upper()}/{to_currency.upper()}/{amount}"
    )

    try: 
        response = requests.get(url)
        response.raise_for_status() #Tjekker for HTTP-fejl
        data = response.json()

    except requests.RequestException as e:
            print(f"Fejl: Netværksfejl ved API-kald - {e}")
            sys.exit(1)

    if data["result"] != "success":
         print(f"Fejl: API-fejl - {data.get('error-type', 'Ukendt fejl')}")
         sys.exit(1)

    conversion_rate = data["conversion_rate"]
    converted_amount = data["conversion_result"]

    return conversion_rate, converted_amount

   

def main():

    #Læser argumenter fra kommandolinjen
    args = parse_args()

    #Finder API-nøglen enten fra argumentet eller fra miljøvariablerne
    API_KEY = get_api_key(args.key)

    #Validerer input og API-nøgle
    validate_input(args, API_KEY)

    rate, converted_amount = convert_currency(
        API_KEY,
        args.from_currency,
        args.to_currency,
        args.amount
    )




    print(f"Kurs: 1 {args.from_currency.upper()} = {rate:.3f} {args.to_currency.upper()}")
    print(
        f"Resultat: {args.amount:.2f} {args.from_currency.upper()} = "
        f"{converted_amount:.2f} {args.to_currency.upper()}"
    )


# Main kører kun hvis scriptet køres direkte, ikke hvis det importeres som et modul
if __name__ == "__main__":
    main()
