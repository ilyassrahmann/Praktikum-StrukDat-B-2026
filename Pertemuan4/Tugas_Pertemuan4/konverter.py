from kurs import kurs

def idr_to_currency(jumlah_idr, currency):
    if currency in kurs:
        return jumlah_idr / kurs[currency]
    else:
        raise ValueError("Mata uang tidak ditemukan dalam kurs.")

def currency_to_idr(jumlah_currency, currency):
    if currency in kurs:
        return jumlah_currency * kurs[currency]
    else:
        raise ValueError("Mata uang tidak ditemukan dalam kurs.")
    
