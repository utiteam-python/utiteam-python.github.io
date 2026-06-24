# Documentazione DeWeb

## Funzioni
### Funzioni di browser
Usa browser per mostrare la pagina web che vuoi tu

```python
from DeWeb.browser import DeWebParser

DeWebParser.prepare_load() #prepare_load() non può essere scartato
DeWebParser.load("https://esempio.com/il/link/della/pagina", "il titolo della pagina") #Questo carica effetivamente la pagina
```
                                      
E con SetFlag potete aggiungere un flag di Qt:
                                      
```python
from DeWeb.browser import DeWebParser

DeWebParser.prepare_load() #prepare_load() non può essere scartato
DeWebParser.SetFlag("JavascriptEnabled", True) #JS Attivato
DeWebParser.load("https://esempio.com/il/link/della/pagina", "il titolo della pagina") #Questo carica effetivamente la pagina
```
### Funzioni di test
per testare se funziona, usate test:

```python
import DeWeb.test
```

### Licenza
                                      
[Clicca per vedere il testo della Licensa](https://github.com/utiteam-python/DeWeb/blob/main/LICENSE)

## Altre Informazioni
                                      
### Disclaimer Versione
È aggiornato alla versione 1.0.4 e non puo avere le ultime funzionalita.

### Altri materiali
Per altri materiali come risoluzione di problemi e FAQs, Visita la  [Community Fandom](https://utiteam-deweb.fandom.com/it/wiki/DeWeb_Wiki).  