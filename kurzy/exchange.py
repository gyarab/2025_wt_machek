import httpx

url = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

lines = url.text.splitlines()
header = lines[0].split(" #")[0]

line_euro = ""
for line in lines:
    if "EUR" in line:
        line_euro = line
        break

parts = line_euro.split('|')
rate = float(parts[-1].replace(',', '.'))

print("=" * 30)
print(f"ČNB kurzy pro den: {header}")
print("=" * 30)
print(f"aktuální kurz: 1 EUR = {rate} CZK")
print("-" * 30)

print("vyber směr převodu:")
print("1: EUR -> CZK")
print("2: CZK -> EUR")

volba = input("tvoje volba: ")

try:
    if volba == "1":
        castka = float(input("Zadejte částku v EUR: ").replace(',', '.'))
        vysledek = castka * rate
        print(f"{castka} EUR = {vysledek:.2f} CZK")
    elif volba == "2":
        castka = float(input("Zadejte částku v CZK: ").replace(',', '.'))
        vysledek = castka / rate
        print(f"{castka} CZK = {vysledek:.2f} EUR")
    else:
        print("neplatný vstup. zvol 1 nebo 2.")
except ValueError:
    print("neplatná číselná hodnota.")

print("=" * 30)