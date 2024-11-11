# pip install python-dotenv

# tsekkaa, muokkaa koneen ympäristömuuttujia, käyttäjä ja systeemitasoiset muuttuja
# .env-tiedostoon voi laittaa ympäristömuuttujia

from dotenv import load_dotenv
import os

load_dotenv(override=True) # lukee .env -tiedoston, mikäli ko. ympäristömuuttujaa ei ole tai sitä ei yliajeta

print(os.getenv("PASSWORD"))
print(os.getenv("PORT"))