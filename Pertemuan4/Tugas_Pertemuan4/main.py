from kurs import kurs
from konverter import idr_to_currency, currency_to_idr
from tabulate import tabulate

def display_kurs():
    headers = [" Kode ", " Kurs "]
    table = [[ currency, f"{rate:,} "] for currency, rate in kurs.items()]
    print(tabulate(table, headers, tablefmt="pretty"))

def main():
    print("=== KONVERTER MATA UANG ===")
    display_kurs()

    dari_mata_uang = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    ke_mata_uang = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))

    print(" ")
    if dari_mata_uang == "IDR":
        hasil = idr_to_currency(jumlah, ke_mata_uang)
    elif ke_mata_uang == "IDR":
        hasil = currency_to_idr(jumlah, dari_mata_uang)
    else: 
         jumlah_dalam_idr = currency_to_idr(jumlah, dari_mata_uang)
         hasil = idr_to_currency(jumlah_dalam_idr, ke_mata_uang)

    print(f"{jumlah} {dari_mata_uang} = {hasil:,.2f} {ke_mata_uang}")

if __name__ == "__main__":
    main()
