# fast_spotdl


## Prerequisites
windows, python 3

## Library
spotdl, youtube-dl

## Installation
Per l'installazione si procede con il comando da terminale per youtube-dl: `pip install youtube-dl`, mentre per spotdl: `pip install spotdl` oppure eseguendo il file [setup.bat](\setup.bat).

## Program
Il programma scarica canzoni presenti su Spotify attraverso Youtube mantenendo i dati di Spotify (ad esempio: data di uscita, album, genere, ecc.).

Le canzoni devono essere passate in input nel file [`link.txt`](.\bin\link.txt) (anche più di uno inserendoli nel file uno sotto l'altro) o come link da Spotify (`Tasto destro > Condividi > Copia link brano`) oppure scrivendo il nome della canzone (questo ultimo metodo risulta impreciso in alcuni casi).
Oppure da prompt dei comandi (cmd) passando il link come ultimo parametro.
Se il file di input è vuoto quando si esegue il programma viene chiesto il link, basta incollarlo e confermare con "Invio"

Tramite link è possibile scaricare anche album e playlist solamente se pubbliche.
Per rendere pubblica una playlist aprire il menù della playlist -> Aggiungi al profilo

Le canzoni verranno poi salvate nella cartella [`.\bin\dl`](.\bin\dl) assieme a dei file cache che potranno essere eliminati

## Problems
Se si riscontrano problemi con le librerie youtube-dl e/o spotdl probabilmente bisogna aggiornarle con il comando: `pip install --upgrade youtube_dl` e `pip install --upgrade spotdl` oppure eseguendo il file [setup.bat](\setup.bat).
Per altri problemi provate questi metodi:
- Se non funziona fin da subito provate ad installare Python con la spunta su `Add Python to PATH`
- Provate ad installare Visual C++ 2019 redistributable: https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist
- Usare il comando: `pip install -U --force-reinstall spotdl`

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Author
Vicentini Tommaso
