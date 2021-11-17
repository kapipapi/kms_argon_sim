## Symulacja gazu Argonu
### Instrukcja uruchomienia
#### 1. Otwórz plik `data.txt` i zedytuj go do swoich potrzeb zgodnie z szablonem poniżej:
```text
n
m
a
T_0
Eps
L
f
R
tau
S_o
S_d
S_out
S_xyz
```
Każda linia w pliku jest kolejnym parametrem symulacji.

#### 2. Uruchom symulacje - wygeneruj plik `xyz.dat` oraz `out.dat`.

Jeśli nie masz zainstalowanych wymaganych paczek do Pythona3 uruchom skrypt instalacyjny:

`pip3 install -r requirements.txt`

Po zainstalowaniu paczek uruchom symulacje:

`python3 main.py`

- Plik `xyz.dat` wypełniony jest kolejnymi klatkami symulacji, w każdej klatce zawarte są położenia wszystkich molekuł.
- Plik `out.dat` zawiera tabele chwilowych wartości wygenerowanych zgodnie z legendą w pierwszej linii tego pliku.

#### 3. Uruchom animacje 3D
`python3 sim3d.py`