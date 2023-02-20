---
author:

- Leonardo Toccafondi   
  date: February, 2023
  title: Comparazione tra algoritmi di ordinamento Insertion Sort, Shell Sort, Quick Sort

---

# Introduzione

Una delle classi di problemi più studiate nel campo dell’informatica sono i problemi di ordinamento. Essi possono essere
descritti nel seguente modo:

> *A partire da una sequenza di dati $S = \{x_1, \dotsc, x_n\}$ in ingresso trovare una permutazione $S^{\prime} = > >
\{x_1^{\prime}, \dotsc , x_n^{\prime}\}$ di essa tale che $x_1^{\prime} \leq x_2^{\prime} \leq \dotsc \leq x_n^\prime$.*

Per la loro risoluzione sono stati pensati numerosi algoritmi di ordinamento: ogni implementazione differisce
soprattutto per i campi di applicazione e per il comportamento rispetto a certe sequenze di ingresso. Per valutare quale
sia meglio usare è quindi necessario valutare la loro efficienza, ovvero quanto tempo impiegano ad essere eseguiti su
insiemi di dati particolari e con dimensione sempre crescente.
In questa relazione saranno analizzate le differenze, in senso di *complessità temporale*, di tre algoritmi di
ordinamento: **Quick Sort**, **Insertion Sort e Shell Sort**. In particolare saranno analizzati i loro andamenti
temporali all'aumentare del numero di elementi delle liste da ordinare.

# Teoria

### Insertion_sort

#### Descrizione dell’algoritmo

Insertion_sort è un algoritmo di ordinamento sul posto che prende prende in ingresso una sequenza di $n$ numeri
memorizzati in un array A, e restituisce una loro permutazione $\{A'_{1}, A'_{2}, \dotsc , A'_{n} \}$ ordinata.

Il funzionamento è simile a come si ordinano le carte in mano: alla j-esima iterazione l’algoritmo sposta" la chiave
indietro nell’array, finché non si trova n elemento minore oppure si è arrivati alla fine dell’array. In questo modo la
chiave viene inserita nella posizione corretta (j+1-esima posizione). Quindi ad ogni iterazione il sottoarray
$A[1, \dotsc, j-1]$ è formato da elementi che originariamente erano in $A[1, \dotsc, j-1]$, ma adesso sono **ordinati**.

Insertion sort è un algoritmo **stabile**, in quanto ordina gli elementi uguali nello stesso ordine in cui appaiono
nell'input. Inoltre ordina sul posto, senza l'ausilio di liste ulteriori. Inoltre è **adattivo**, in quanto è efficiente
per insiemi di dati che sono già sostanzialmente ordinati.

INSERIRE PSEUDOCODICE

#### Prestazioni attese

Per definire le prestazioni attese di Insertion_sort è necessario analizzare il suo costo. Per come è strutturato
l’algoritmo, la complessità dipende sia dalla dimensione dell’input, sia da come sono ordinati i dati. Quindi, a parità
di quantità di dati, l’algoritmo può essere più o meno veloce a seconda della loro disposizione nella sequenza. Per
questo motivo si distinguono tre casi:

- **Caso migliore:** gli elementi sono già ordinati. In questo caso il costo è $\Theta(n)$;

- **Caso peggiore:** gli elementi sono ordinati al contrario. In questo caso il costo è $\Theta(n^{2})$;

- **Caso medio:** gli elementi sono ordinati in modo casuale. Questo caso è simile al caso peggiore ed ha la stessa
  complessità

Rispetto ad un algoritmo *divide-et-impera* performa peggio per set di dati molto grandi, mentre ha ottime prestazioni
per set di dati più ridotti

### Shell Sort

#### Descrizione dell'algoritmo

Shell sort è un algortimo di ordinamento Il metodo inizia ordinando coppie di elementi molto distanti l'uno dall'altro,
per poi ridurre progressivamente il divario tra gli elementi da confrontare. Iniziando con elementi molto distanti, può
spostare in posizione alcuni elementi fuori posto più velocemente di un semplice scambio di prossimità.

Shell sort non è stabile: può cambiare l'ordine relativo di elementi con valori uguali. Come Insertion sort, è un
algoritmo adattivo, in quanto viene eseguito più velocemente quanto più l'input è parzialmente ordinato.

#### Prestazioni attese

Per questo algoritmo ci sono varie implementazioni, con tempi e costi differenti: l'implementazione originale (e che è
stata utilizzata per questo esperimento) prevede che la dimensione dell'intervallo iniziale sia $n / 2$ con $n$
dimensione della lista e che ad ogni i-esima iterazione sia divisa per $2^{i}$.

Si distinguono sempre tre casi:

- **Caso peggiore**: si verifica per N uguale a una potenza di due, quando gli elementi maggiori e minori della mediana
  occupano rispettivamente posizioni pari e dispari, poiché vengono confrontati solo nell'ultimo passaggio. Di
  conseguenza la complessità sarà un $O\left(n^{2}\right)$ come Insertion Sort.

- **Caso medio**: è compreso tra $O(n \log (n))$ e $O\left(n^{1.25}\right)$, quindi abbastanza veloce.

- **Caso migliore**: $O(n \log (n))$

### Quick Sort

#### Descrizione dell’algoritmo

Quick sort è un algoritmo di ordinamento sul posto ma, a differenza di insertion sort, è ricorsivo e si basa sul
principio *divide et impera*. Per ordinare un array $A[p,\_\_\_, r]$:

- **Divide:** partiziona l’array A in due sottoarray $A[p,\dotsc, q-1]$ e $A[q+1,\dotsc, r]$ tali che ogni elemento del
  primo sottoarray è minore di q (o uguale) e ogni elemento del secondo sottoarray è maggiore di q (o uguale).
  L’elemento $A[q]$ prende il nome di *pivot*.

- **Impera:** ordina i due sottoarray con chiamate ricorsive a se stessa.

- **Combina:** combina i due sottoarray ordinati per restituire l’array $A[p,\dotsc, r]$ ordinato.

INSERIRE PSEUDOCODICE

#### Prestazioni attese

Il tempo di esecuzione del Quick_sort dipende dal partizionamento dei sottoarray, ovvero se questi ultimi sono
bilanciati o sbilanciati:

- **Partizionamento nel caso peggiore:** si ha quando l’array è già ordinato. Infatti in questo caso la funzione
  partition divide il problema in due sottoproblemi, uno di grandezza $n - 1$ e l’altro di grandezza $0$. Il costo è,
  quindi, $\Theta(n^{2})$.

- **Partizionamento nel caso migliore:** si ha quando, ad ogni iterazione, il pivot scelto è l’elemento che divide
  l’array in due sottoprobeni di dimensione uguale. Quindi ciascun sottoarray avrà dimensione $\dfrac{n}{2}$. In questo
  caso il costo è $\mathcal{O}(n\log{}n)$

- **Partizionamento nel caso medio:** i due sottoarray sono divisi in modo casuale. Questo caso è simile al caso
  migliore ed ha la stessa complessità.

# Esperimenti svolti

In questa relazione, sono stati misurati i tempi di esecuzione degli algoritmi di ordinamento all'aumentare del numero
di elementi nella lista da passare agli stessi.
Gli esperimenti sono stati fatti su un numero massimo di nodi pari a 10000, andando a misurare sia i tempi di esecuzione
per array già ordinati, sia per un array randomizzato (viene passato lo stesso in tutti e tre i casi). Le misurazioni,
in questo caso, avvengono ogni incremento di 100 nodi. Inoltre, sono stati testati gli algoritmi nel caso randomizzato
con un numero massimo di nodi pari a 1000000, con misurazioni effettuate ogni incremento di 10000 nodi.
I tempi di esecuzione sono stati salvati in delle liste separate, una per ciascun algoritmo, inserendo successivamente i
valori in una tabella, poi salvata in formato txt. Infine questi valori sono stai utilizzati per creare grafici
rappresentanti andamenti temporali.

Viene distinto il caso ordinato, da quello non ordinato, con un controllo sulla variabile booleana *shuffle*, grazie
alla quale il programma sa se randomizzare o meno i valori della lista da ordinare, se questa è pari a True. Altrimenti,
l'input non viene randomizzato e avrò come risultato il caso migliore di Shell e di Insertion sort.

# Implementazione pratica

Il programma è suddiviso in più file:

- insertion_sort.py, quick_sort.py e shell_sort.py, i quali si occupano dell'implementazione degli algoritmi di
  ordinamento da testare;
- test.py: è il programma principale, si occupa del test degli algoritmi e della creazione dei grafici.

#### Ambiente di test

L'esperimento è stato svolto su un computer con le seguenti caratteristiche:

- Sistema operativo: Linux Mint 21.1 con kernel 5.15

- CPU: Inter Core i7-9750H

- RAM: 16 GB

- Interprete Python: conda 22.11.1 e python v

- IDE: Pycharm Community Edition 2022.3.2

# Risultati

### 10000 nodi

<img src="../img/ord/ord_comparison10000.png" title="Figura 1 - Array ordinato" alt="" data-align="inline">
<img src="../img/rand/rand_comparison10000.png" title="Figura 2 - array randomizzato" alt="" data-align="inline">
