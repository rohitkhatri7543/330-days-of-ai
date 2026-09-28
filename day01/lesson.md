# Day 1: Variables

Northline Plant ki line 1 pe Pump-A chalta hai. Abhi uska temperature `72.5` C hai. Yeh number tabhi kaam ka hai jab baad wali line usi number ko pakad sake.

Socho teeno jagah tumne `72.5` type kar diya: log mein, display pe, aur alarm ke rule mein. Agle minute sensor `80.1` bhejta hai. Tum log update kar dete ho, display update kar dete ho, aur alarm wala number purana reh jata hai. Pump garam ho raha hai, alarm shant hai. Ulta scene bhi plant pe hota hai: ek jagah galat naya number chala gaya, aur ek theek pump ruk gaya. Dono mein plant galat temperature pe faisla kar leta hai. Reading ek naam ke neeche nahi thi, isliye ek badlav har jagah nahi pahuncha.

---

## Variable

**Variable** ek naam hai jo ek **Value** ko pakde rehta hai. Value woh cheez hai jo store ho rahi hai, jaise text `"72.5"` ya `"Pump-A"`.

**Assignment** woh step hai jisme `=` ke left pe naam hota hai aur right pe value. Computer pehle right side ko evaluate karta hai, phir us result ko us naam se baandh deta hai.

```python
temperature_text = "72.5"
temperature_text = "80.1"
```

Pehli line ke baad `temperature_text` ki value `"72.5"` hai. Doosri line usi naam pe nayi assignment hai. Ab `temperature_text` ki value `"80.1"` hai. `"72.5"` us naam pe nahi bachi. Woh tabhi bachi rehti agar kisi aur variable ne pehle hi usko hold kiya ho.

Isliye Northline pe latest reading ek variable mein rehti hai. Har screen alag number type nahi karti. Naam ek hai. Assignment badli, to har jagah jo us naam ko padhta hai woh nayi value dekhta hai.

---

## Finished practical

Neeche wala function aaj ka finished example hai. Idea wahi hai: values ko naam do, phir un naam se ek line banao.

`def` aur `return` is function ke dabbe hain. Baad mein test isi dabbe ko call karega. Function ka idea functions wale din khulega. Aaj andar ke naam dekho.

```python
def format_reading(machine_name, temperature_text):
    unit = "C"
    label = machine_name + " is " + temperature_text + " " + unit
    return label
```

Call:

```python
format_reading("Pump-A", "72.5")
```

Computer yeh karta hai, line by line:

1. Call `machine_name` mein `"Pump-A"` daalti hai, aur `temperature_text` mein `"72.5"`. Yeh dono bhi variables hain. Inki pehli value call se aati hai.
2. `unit = "C"` chalti hai. Naya variable `unit` ab `"C"` hold karta hai. Unit ek hi jagah likha hai, taaki label banate waqt dobara type na karna pade.
3. `label = machine_name + " is " + temperature_text + " " + unit` chalti hai. Computer pehle right side jodta hai. `+` yahan do text ko aage-peeche chipkata hai. Beech ke space wale tukde bhi text hain. Result hota hai `"Pump-A is 72.5 C"`. Phir yeh result `label` naam se bind ho jata hai.
4. `return label` us value ko function ke bahar bhej deta hai.

Output:

```text
Pump-A is 72.5 C
```

Ab doosri reading aati hai. Call nayi hai, isliye andar ke naam nayi values lete hain.

```python
format_reading("Pump-B", "61.0")
```

1. `machine_name` is call mein `"Pump-B"` hai. Assignment is call ki value rakhti hai.
2. `temperature_text` is call mein `"61.0"` hai.
3. `unit = "C"` is call mein phir chalti hai, isliye `unit` phir `"C"` hold karta hai.
4. `label` ab `"Pump-B is 61.0 C"` hold karta hai. Pehli call ka label is call ke andar nahi pada hai.
5. `return` wahi naya text bhejta hai.

Output:

```text
Pump-B is 61.0 C
```

Ek call ke andar `unit` ek baar assign hota hai aur `label` usi naam ko padhta hai. Kal unit badalni ho to woh kaam ek assignment pe simat jata hai. `label` wali line usi `unit` naam ko padhti rehti hai.

Aaj ke words: Variable, Value, Assignment. `GLOSSARY.md` mein yahi teen hain.

Jab yeh clear ho jaye, chalao:

```bash
python today.py understood
```
