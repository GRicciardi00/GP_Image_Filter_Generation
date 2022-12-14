# TESI

##CRONOLOGIA MODIFICHE
### 20/10/2022-24/10/2022
- La cartella ''prova1-3x3-edge-detection'' contiene i risultati dell'esecuzione dell'algoritmo di GP per il riconoscimento dei bordi con una matrice 3x3, il dataset è stato ridotto a 30 immagini a cui viene passato un campione 30x30 dell'immagine (a partire dal centro dell'array np 128x128 originale) e il risultato viene utilizzato per ricostruire l'immagine completa. Ho aggiunto le due variabili effimere, una che varia tra (0,1) e l'altra tra (0,255) ed aumentato la profondità dell'albero ad 8, inoltre per ogni esecuzione vengono salvati e stampati i 3 risultati migliori dell'hallo of fame. Durata esecuzione: 4 minuti e 41 secondi (alcune soluzioni generate dal GP generano errori, da rivedere meglio le operazioni).<br />
- La cartella "prova1-5x5-edge-detection" contiene i risultati dell'esecuzione dell'algoritmo di GP per il riconoscimento dei bordi con una matrice 5x5 (valgono le stesse cose dette per l'algoritmo con filtro di edge detection 3x3).Durata esecuzione 5:56 
- La cartella "prova1-3x3-denoise" contiene i risultati dell'esecuzione dell'algoritmo di GP per il denoise di 30 immagini (a cui è stato applicato lo stesso rumore gaussiano), anche in questo caso vengono campionate prendendo un campione 30x30, e ricostruite applicando i risultati ottenuti all'immagine intera. I parametri dell'algoritmo sono gli stessi degli algoritmi di edge detection. Durata esecuzione 4:23
- La cartella "prova1-5x5-denoise" contiene i risultati dell'esecuzione dell'agloritmo di GP per il denoise di 30 immagini con dimensione del filtro 5x5. Stessi dati e parametri dell'algoritmo utilizzato per il denoise con matrice 3x3. Durata esecuzione 5:22

##HOW TO USE
Lanciare "GP_training" (da console o mediante IDLE), l'algoritmo non richiede nessun parametro da passare in fase di lancio in quanto tutti i path utilizzati dei vari algoritmi si basano su path locali e non globali. Una volta avviato l'algoritmo bisogna inserire il nome della cartella in cui verranno salvati i vari risultati, viene chiesto di inserire un numero tra 1 e 2 per decidere la dimensione della matrice su cui generare il fitro (3x3 o 5x5) e infine che tipo di operazione svolgere: 1 per denoise, 2 per edge detection, 3 per svolgere entrambe e infine 4 per salvare i risultati (una volta terminate le task per ogni immagine il salvataggio viene fatto in automatico, premere 4 serve solo per esportare le immagini nel caso in cui l'algoritmo viene eseguito solo per alcune immagini).

## LIBRERIE
- Opencv
- DEAP
- numpy
- PIL

## STRUTTURA PROGETTO
La cartella "dataset" contiene tutte le immagini, e gli algoritmi (da eseguire senza passare argomenti) usati per:
- Estrarre le immagini dei bordi da MATLAB:boundaries.m
- Invertire colori immagini dei bordi (da sfondo nero e bordi bianchi a sfondo bianco con bordi neri): expected_converter.py
- convertire le immagini in greyscale: grayscale_converter.py
- aggiungere rumore alle immagini: noise_converter.py
- modificare luminosità e contrasto delle immagini: eq_converter.py

## AGGIUNTA RUMORE
Il file noise_converter.py genera nella cartella dataset/train/train_denoise/noise le immagini con il rumore,
sceglie casualmente per ogni immagine il tipo di rumore da aggiungere (gaussiano,salt and pepper, poisson) con valori scelti casualmente per ogni immagine. 
Successivamente bisogna convertire in greyscale i risultati ottenuti tramite grayscale_converter.py (impostando come path d'origine e destinazione   '.../dataset/train/train_denoise/noise')

## BRIGHTNESS & LOOKUPTABLE
La modifica della brightness avviene tramite file eq_converter.py. La brightness di ogni foto viene modificata con un valore generato casualmente (tra 0 e 30) tramite la libreria Opencv, sempre tramite opencv viene creata una LUT di numeri casuali (da 0 a 256) applicata all'immagine con luminosità alterata.
E' riportato un commento con un'alternativa per la composizione della table per la LUT per avere immagini più ''simili'' rispetto alle originali.







