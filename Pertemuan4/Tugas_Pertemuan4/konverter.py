#Buat file konverter.py berisi fungsi konversi (IDR ke mata uang lain dan sebaliknya).
from kurs import kurs

def idr_to_currency(amount_idr, currency):
    if currency in kurs:
        return amount_idr / kurs[currency]
    else:
        raise ValueError("Mata uang tidak ditemukan dalam kurs.")

def currency_to_idr(amount_currency, currency):
    if currency in kurs:
        return amount_currency * kurs[currency]
    else:
        raise ValueError("Mata uang tidak ditemukan dalam kurs.")
    
