# Generazione_filtri_ottimi_per_immagini_GP
## LIBRERIE
Gli algoritmi GP funzionano solo su linux in quanto DEAP utilizza il multithreading
- Opencv
- DEAP
- Numpy
- PIL
- Matplotlib
- Graphviz
## HOW TO USE
Nella cartella "dataset" sono presenti tutte le immagini usate per il training ed il testing ed i vari algoritmi usati per le operazioni preliminari.
Per il training eseguire il file "GP_training.py" e seguire la guida sul terminale, successivamente è possibile eseguire il test con i filtri ottenuti modificando il file "GP_test.py" impostando i percorsi dei file _best.pkl necessari ed eseguirlo.
Il file ''image_processing.py'' utilizza openCV per modificare le immagini con metodi comuni di edge detection e denoise.
Nella cartella "risultati" è presente l'algoritmo utilizzato per la valutazione dei risultati ottenuti.


