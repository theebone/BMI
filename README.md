Výpočet BMI a Jídelníček
Tento projekt slouží k výpočtu BMI (Body Mass Index) na základě váhy a výšky uživatele. Aplikace také poskytuje jídelníčky pro různé kategorie BMI. Výsledky výpočtů jsou ukládány do databáze, a uživatelé mohou prohlížet historii výpočtů.

Funkce
1. Výpočet BMI
Aplikace spočítá BMI na základě zadané váhy a výšky uživatele.

Na základě hodnoty BMI aplikace klasifikuje výsledek do jedné z těchto kategorií:

Podváha: BMI < 18.5

Normální: 18.5 ≤ BMI < 24.9

Nadváha: 25 ≤ BMI < 29.9

Obezita: 30 ≤ BMI < 34.9

Extrémní obezita: BMI ≥ 35

2. Jídelníčky
Aplikace poskytuje jídelníčky na základě výsledku BMI, které jsou uloženy v textových souborech. Pro každou kategorii BMI je k dispozici odpovídající jídelníček, který obsahuje seznam doporučených jídel a jejich vyživové hodnoty.

3. Historie výpočtů
Všechny výsledky výpočtů (jméno, věk, BMI a kategorie) jsou ukládány do databáze a uživatelé mohou prohlížet historii výpočtů.

Požadavky
Pro spuštění aplikace je potřeba mít nainstalované následující knihovny:

psycopg2: Pro komunikaci s PostgreSQL databází.

Tento projekt využívá databázi pro uchovávání výsledků BMI výpočtů a poskytování historických dat.


Instalace
Nainstalujte Python knihovny:

Použijte pip pro instalaci potřebných knihoven.
Tento projekt používá PostgreSQL databázi. Ujistěte se, že máte správně nastavenou databázi a že máte přístup k serveru.
Pokud nemáte databázi, vytvořte ji podle potřeby.
Použití
Výpočet BMI:

Zadejte své jméno, věk, váhu (v kg) a výšku (v metrech).

Aplikace vypočítá BMI a klasifikuje ho do jedné z kategorií.

Jídelníček:

Po výpočtu BMI můžete kliknout na tlačítko pro zobrazení jídelníčku odpovídající vaší BMI kategorii.

Jídelníček se otevře v novém okně s přehledem doporučených jídel.

Historie výpočtů:

Můžete si prohlédnout historii všech provedených výpočtů BMI a přehled osobních údajů.

Příklady jídelníčků:
Podváha: Jídelníček s vyšším obsahem kalorií pro zajištění zdravé hmotnosti.

Normální: Jídelníček s vyváženým poměrem živin pro udržení zdravé váhy.

Nadváha: Jídelníček zaměřený na snížení hmotnosti s nižším obsahem kalorií.

Obezita: Jídelníček s cílem snížit hmotnost a zlepšit celkové zdraví.

Extrémní obezita: Jídelníček pro podporu výrazné změny hmotnosti a zlepšení zdravotního stavu.

Databáze
Tento projekt používá PostgreSQL databázi pro ukládání výsledků výpočtů BMI. V databázi je tabulka bmi, která obsahuje následující sloupce:

bmi_id: Unikátní ID pro každý záznam.

jmeno: Jméno uživatele.

vek: Věk uživatele.

bmi_number: Spočítané BMI.

bmi_text: Kategorie BMI (Podváha, Normální, Nadváha, Obezita, Extrémní obezita).

Poznámky
Tento projekt je určen pro demonstraci výpočtu BMI a zobrazení jídelníčků na základě BMI kategorií.
Textové soubory je třeba mít ve stejné složce jako main.py
Mějte na paměti, že jídelníčky nejsou určeny pro konkrétní zdravotní potřeby a pro konkrétní rady by bylo vhodné se poradit s odborníkem na výživu nebo lékařem.
