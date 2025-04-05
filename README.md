# 📘 Sztringekkel Végzett Aritmetikai Műveletek Algoritmikus Megoldása

## 🧾 Projektleírás

Ez a modul lehetőséget nyújt arra, hogy felhasználói bemenetként adott két pozitív vagy negatív egész számot tartalmazó **sztring** alapján elvégezzen különböző **aritmetikai vagy összehasonlító műveleteket**.

A program képes felismerni a bemeneti adatban szereplő **műveleti jelet**, a számokat **duplán láncolt listába** konvertálni, majd az adott műveletet helyesen végrehajtani.

---

## ⚙️ Támogatott műveletek

A következő operátorokkal dolgozik a rendszer:

- `+` Összeadás  
- `-` Kivonás  
- `*` Szorzás  
- `/` Osztás  
- `<` Kisebb-e  
- `>` Nagyobb-e  
- `=` Egyenlőség

---

## 🧠 Modulok és főbb függvények

### `main()`
A program belépési pontja. Bekéri a felhasználótól a bemenetet, eltávolítja a szóközöket, majd elvégzi az alábbiakat:
- Validálja a bemenetet
- Duplán láncolt listát épít belőle
- Megkeresi az operátort
- Konvertálja a számokat
- Végrehajtja a műveletet
- Kiírja az eredményt

---

### `str_to_num(input_string, num_map)`
A duplán láncolt lista karaktereit egész számmá alakítja, figyelembe véve az előjelet is.

---

### `validate_input(data, number_map, operator_map)`
Ellenőrzi, hogy a bemenet kizárólag érvényes számokat és műveleti jeleket tartalmaz.

---

### `parse_for_operators(data, operator_map, numbers)`
Megkeresi az első érvényes operátor helyét a duplán láncolt listában, és visszaadja annak indexét.

---

## 🧪 Hibakezelés

- **Nullával való osztás** esetén `ZeroDivisionError` kivétel keletkezik.
- **Érvénytelen karakter** esetén a program `ValueError`-rel leáll.

---

## 🧱 Külső modulok

A kód a `dll` modulból importál egy **duplán láncolt listát (DoublyLinkedList)**, amelyet a bemenet karaktereinek tárolására és feldolgozására használ.

---

## 🧑‍💻 Használat

A program futtatása után a felhasználónak be kell írnia egy kifejezést (pl. `123 + -45`). A kimenet a művelet eredménye lesz.

---
