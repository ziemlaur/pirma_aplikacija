import re
from datetime import datetime
# Skaitymas iš failo "Info.txt"
filePath = r"D:\PYTON\pirma_aplikacija\info.txt"


# Atidarome failą ir skaitome jo turinį
with open(filePath, "r") as file:
    csv_content = file.read()

# Konvertuojame CSV turinį į sąrašą
lines = csv_content.strip().split("\n")
header = lines[0].split(";")
data = [dict(zip(header, line.split(";"))) for line in lines[1:]]

# Dabartiniai metai
current_year = datetime.now().year

# 1. Pirma sąlyga: Vartotojai, kurių slaptažodyje nėra skaičių

filtered_no_numbers = []
for row in data:
    has_number = False
    for char in row["SLAPTAZODIS"]:
        if char.isdigit():
            has_number = True
            break
    if not has_number:
        filtered_no_numbers.append(row)
print(f'pirma salyga: {filtered_no_numbers}')


# 2. Antra sąlyga: Vartotojai, kurie neturi gimimo metų
filtered_no_birth_year = []
for row in data:
    if not row["GIMIMO METAI"]:
        filtered_no_birth_year.append(row)
print(f'antra salyga: {filtered_no_birth_year}')

# 3. Trečia sąlyga: Visų vartotojų amžiaus vidurkis
ages = []
for row in data:
    if row["GIMIMO METAI"]:
        ages.append(current_year - int(row["GIMIMO METAI"]))
average_age = sum(ages) / len(ages) if ages else None
print(f'trecia salyga: {ages}')


# 4. Ketvirta sąlyga: Vartotojai su neteisingais el. paštais
valid_email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
filtered_invalid_emails = []
for row in data:
    if not re.match(valid_email_pattern, row["EL.PASTAS"]):
        filtered_invalid_emails.append(row)

print(f'ketvirta salyga: {filtered_invalid_emails}')

# 5. Penkta sąlyga: Vartotojai, kurių slaptažodžiai trumpesni nei 5 simboliai
filtered_short_passwords = []
for row in data:
    if len(row["SLAPTAZODIS"]) < 5:
        filtered_short_passwords.append(row)


print(f'penkta salyga: {filtered_short_passwords}')

# 6. Šešta sąlyga: Vartotojai, kurie nėra įvedę pavardės
filtered_no_surname = []
for row in data:
    if not row["PAVARDE"]:
        filtered_no_surname.append(row)
print(f'sesta salyga: {filtered_no_surname}')



