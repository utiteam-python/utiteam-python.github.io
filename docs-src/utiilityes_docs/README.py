from zompi.page import BasePage
import zompi.contrib

class Page(BasePage):
    PAGE_TITLE = "Documentazione Utiilityes"

    def __init__(self):
        return zompi.contrib.markdown('''## Funzioni
### Funzioni di index
se avete fatto un `import from utiilityes import Index` o l'equivalente `from utiilityes import Index as ind` potrete usare le seguenti funzioni:

#### Funzioni obbligatori

Per avviare una GUI, dovrete sempre fare prima di qualsiasi cosa:
                                      
```python
    ui = ind()

    ui.init.win("Example")\\
          .size(600, 400)
```
                                      
se non avete aggiunto all'import l'alias ind, sostituite la variabile `ui` con `ui = Index()`

Il Blocco con `.size(600, 400)` può essere cambiato in base alla grandezza della finestra. Anche con `ui.init.win("Example")\` si può cambiare la stringa a seconda delle necessità.

#### Funzioni dei pulsanti

Fate una funzione normale in Python con `def nome_funzione(parametro_1, parametro_2)`

#### Iniziare il Ciclo

Ora che abbiamo tutto pronto, possiamo iniziare il ciclo con run_funct(). Il codice deve essere simile a questo:

```python
ui.run_funct()\\
    .text("Tratto da Documentazione")\\
    .button("Funzione 1", action=nome_funzione_1)\\
    .button("Funzione 2", action=nome_funzione_2)\\
    .render()
```
                                      
### Funzioni di run32
La programmazione è molto più semplice in run32, perchè c'è bisogno di una sola funzione. Questo sara il nostro primo script:

```python
from utiilityes import run32

#Log
run32.log("Log")

#Log in una finestra
run32.log_inui("Guarda l'altra finestra")

#Log multiplo in una finestra
run32.multiple_log_inui("Nella shell", "ci essere", "un log da vedere")
```
                                      
### Funzioni di showbox
Possiamo mostrare messaggi di errore, conferma, informazioni e avvertenza con semplici comandi:

```python
#Per semplificare usiamo l'alias sh
from utiilityes import showbox as sh

#Conferma
sh.confirm("Vuoi vedere il sito?")

#Informazione
sh.info("Ecco il sito:")

#Errore
sh.error("La pagina non è stata trovata :( - 404")

#Avvertenza o Errore Critico
sh.warning("Bad Request! :( - 500")

#Un'alternativa a log di run32
sh.log("Vorrei mostrarti un sito!")
```


## Licenza
E' Distribuito con licenza Apache 2.0

Ecco il file LICENSE:

```
Copyright (c) 2026 Domenico Ruffa

Licensed under the Apache License, Version 2.0 (the "License");

you may not use this file except in compliance with the License.

You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software

distributed under the License is distributed on an "AS IS" BASIS,

WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and

limitations under the License.
```

## Crediti e Disclaimers
### Crediti
Il Progetto è sostenuto da UtiTeam. Se nella community posti anche solo uno snippet o un solo suggerimento, puoi aiutare tantissimo questo progetto.

### Disclaimer Versione
Questa documentazione è aggiornata alla versione 1.2.0 di Utiilityes e non potrebbe avere le ultime novità. Verificate l'ultima versione qui: https://pypi.org/project/utiilityes                                   
''')

    def __str__(self):
        return BasePage.page(zompi.contrib.DOC, 'Markdown')