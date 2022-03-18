import phonenumbers

from phonenumbers import geocoder

phone = input('Text your phone number here with Country code + area code + your number: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'EN'))

