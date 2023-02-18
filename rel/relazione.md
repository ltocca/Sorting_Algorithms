---
author:

- Leonardo Toccafondi   
  date: February, 2023
  title: Comparazione tra algoritmi di ordinamento: Insertion Sort, Shell Sort, Quick Sort

---

# Introduzione

Una delle classi di problemi più studiate nel campo dell’informatica sono i problemi di ordinamento. Essi possono essere
descritti nel seguente modo:

> *A partire da una sequenza di dati $S = \{x_1, \dotsc, x_n\}$ in ingresso trovare una permutazione $S^{\prime} =
\{x_1^{\prime}, \dotsc , x_n^{\prime}\}$ di essa tale che $x_1^{\prime} \leq x_2^{\prime} \leq \dotsc \leq x_n^\prime$.*

Per la loro risoluzione sono stati pensati numerosi algoritmi di ordinamento: ogni implementazione differisce
soprattutto per i campi di applicazione e per il comportamento rispetto a certe sequenze di ingresso.
Per valutare quale sia meglio usare è quindi necessario valutare la loro efficienza, ovvero quanto tempo impiegano ad
essere eseguiti su insiemi di dati particolari e con dimensione sempre crescente.
In questa relazione andrò ad analizzare le differenze, in senso di complessità temporale*, di tre algoritmi di
ordinamento in particolare: **Insertion Sort, Shell Sort, Quick Sort**. In particolare saranno analizzati i loro
andamenti temporali all'aumentare del numero di elementi delle liste da ordinare.

# Teoria

### Insertion_sort

#### Descrizione dell’algoritmo

Insertion_sort è un algoritmo di ordinamento sul posto che prende prende in
ingresso una sequenza di $n$ numeri memorizzati in un array A, e restituisce una loro permutazione $\{A'_{1}, A'_{2},
\dotsc , A'_{n} \}$ ordinata. Il funzionamento è simile a come si ordinano le carte in mano: alla j-esima iterazione
l’algoritmo "sposta" la chiave indietro nell’array, finché non si trova n elemento minore oppure si è arrivati alla fine
dell’array. In questo modo la chiave viene inserita nella posizione corretta (j+1-esima posizione). Quindi ad ogni
iterazione il sottoarray $A[1, \dotsc, j-1]$ è formato da elementi che originariamente erano in $A[1, \dotsc, j-1]$, ma
adesso sono **ordinati**.

INSERIRE PSEUDOCODICE

#### Prestazioni attese

Per definire le prestazioni attese di Insertion_sort è necessario analizzare il suo costo. Per come è strutturato
l’algoritmo, la complessità dipende sia dalla dimensione dell’input, sia da come sono ordinati i dati. Quindi, a parità
di quantità di dati, l’algoritmo può essere più o meno veloce a seconda della loro disposizione nella
sequenza. Per questo motivo si distinguono 3 casi:

- **Caso migliore:** gli elementi sono già ordinati. In questo caso il costo è $\Theta(n)$

- **Caso peggiore:** gli elementi sono ordinati al contrario. In questo caso il costo è $\Theta(n^{2})$

- **Caso medio:** gli elementi sono ordinati in modo casuale. Questo caso è simile al caso peggiore ed ha la stessa
  complessità

Rispetto ad un algoritmo *divide-et-impera*

### Quick Sort

####Descrizione dell’algoritmo

Quick sort è un algoritmo di ordinamento sul posto ma, a differenza di insertion sort, è ricorsivo e si basa su
principio *divide et impera*. Per ordinare un array $A[p,\_\_\_, r]$:

- **Divide:** partiziona l’array A in due sottoarray $A[p,\dotsc, q-1]$ e $A[q+1,\dotsc, r]$ tali che ogni elemento del
  primo sottoarray è minore di q (o uguale) e ogni elemento del secondo sottoarray è maggiore di q (o uguale).
  L’elemento $A[q]$ prende il nome di *pivot*.

- **Impera:** ordina i due sottoarray con chiamate ricorsive a se stessa.

- **Combina:** combina i due sottoarray ordinati per restituire l’array
  $A[p,\dotsc, r]$ ordinato.

L'algoritmo è composto da due

#### Prestazioni attese

Il tempo di esecuzione del Quick_sort dipende dal partizionamento dei
sottoarray, ovvero se questi ultimi sono bilanciati o sbilanciati:

- **Partizionamento nel caso peggiore:** si ha quando l’array è già
  ordinato. Infatti in questo caso la funzione partition divide il
  problema in due sottoproblemi, uno di grandezza $n - 1$ e l’altro di
  grandezza $0$. Il costo è, quindi, $\Theta(n^{2})$.

- **Partizionamento nel caso migliore:** si ha quando, ad ogni
  iterazione, il pivot scelto è l’elemento che divide l’array in due
  sottoprobeni di dimensione uguale. Quindi ciascun sottoarray avrà
  dimensione $\dfrac{n}{2}$. In questo caso il costo è
  $\mathcal{O}(n\log{}n)$

- **Partizionamento nel caso medio:** i due sottoarray sono divisi in
  modo casuale. Questo caso è simile al caso migliore ed ha la stessa
  complessità.    
