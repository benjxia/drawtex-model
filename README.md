# DrawTeX

## Overview
This repository contains the deep neural network model used for DrawTeX.

## Raw Data

### Version 1: 78 classes, ~96% accuracy

Download the dataset from [https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols](https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols)  
Decompress the `.rar` file and place the decompressed `extracted_images` folder under the `./data` directory of the repository's root directory.  
In the end, the repository's directory structure should resemble the below.
```
Root
├── data
│   ├── extracted_images
│   │   ├── !
|   |   ├── ...
├── prototypes
├── ├── ...
├── README.md
├── ...
```
Note that unzipping `archive.zip` from the direct download will get you an **incomplete** `extracted_images` folder, unzip the `.rar` file for the complete dataset.

### Version 2: 331 classes, ~82% accuracy

Combined portions of the CROHME dataset from above with the [HASYv2](https://arxiv.org/pdf/1701.08380.pdf) dataset.   
All images were scaled to `45x45`, converted to pure black and white, and skeletonized.  

1. Combined test/train data for HASYv2
2. Consolidated classes
   1. `\varpropto` -> `\propto`
   2. `\mid` -> `|`
   3. `\triangle` -> `\delta`
   4. `\check` -> `\checkmark`
   5. `\setminus` -> `\backslash`
   6. `\with` -> `\&`
   7. `\triangledown` -> `\nabla`
   8. `\longmapsto` -> `\mapsto`
   9. `\dotsc` -> `\dots`
   10. `\mathsection` -> `\S`
   11. `\vartriangle` -> `\delta`
   12. `\mathbb{Z}` -> `\mathds{Z}`
   13. `\mathbb{R}` -> `\mathds{R}`
   14. `\mathbb{Q}` -> `\mathds{Q}`
   15. `\mathbb{N}` -> `\mathds{N}`
   16. Combine lowercase letters w/ capital case
   17. Added letter training data from CROHME dataset.

Dataset download might be put up one day... It's very fat.
```
Root
├── data
│   ├── extracted_images (optional, v2 doesn't require the v1 datset)
│   │   ├── !
|   |   ├── ...
|   ├── HASYv2
│   │   ├── hasy-data
│   │   │   ├── ...png
│   │   ├── combined2.csv
├── prototypes
├── ├── ...
├── README.md
├── ...
```
Image to label mappings are located in `./data/HASYv2/combined2.csv`. 

Label to index mappings are in `mappings.csv`, and below.

| Rendering             | Latex               | Mapping |
|-----------------------|---------------------|---------|
| $5$                   | 5                   | 0       |
| $\mathcal{L}$         | \mathcal{L}         | 1       |
| $\epsilon$            | \epsilon            | 2       |
| $\partial$            | \partial            | 3       |
| $\hbar$               | \hbar               | 4       |
| $\succ$               | \succ               | 5       |
| $\mathbb{H}$          | \mathbb{H}          | 6       |
| $\mu$                 | \mu                 | 7       |
| $\mathscr{E}$         | \mathscr{E}         | 8       |
| $\Leftarrow$          | \Leftarrow          | 9       |
| $\lozenge$            | \lozenge            | 10      |
| $\Psi$                | \Psi                | 11      |
| $\aleph$              | \aleph              | 12      |
| $\ltimes$             | \ltimes             | 13      |
| $\bullet$             | \bullet             | 14      |
| $\mathscr{S}$         | \mathscr{S}         | 15      |
| $\astrosun$           | \astrosun           | 16      |
| $\subsetneq$          | \subsetneq          | 17      |
| $F$                   | F                   | 18      |
| $\wr$                 | \wr                 | 19      |
| $\pi$                 | \pi                 | 20      |
| $\frown$              | \frown              | 21      |
| $\pounds$             | \pounds             | 22      |
| $O$                   | O                   | 23      |
| $\parallel$           | \parallel           | 24      |
| $\searrow$            | \searrow            | 25      |
| $\mathscr{L}$         | \mathscr{L}         | 26      |
| $\prec$               | \prec               | 27      |
| $\mathds{E}$          | \mathds{E}          | 28      |
| $\subset$             | \subset             | 29      |
| $\Lambda$             | \Lambda             | 30      |
| $\lhd$                | \lhd                | 31      |
| $\iota$               | \iota               | 32      |
| $\nsubseteq$          | \nsubseteq          | 33      |
| $\curvearrowright$    | \curvearrowright    | 34      |
| $\mathfrak{A}$        | \mathfrak{A}        | 35      |
| $\nabla$              | \nabla              | 36      |
| $\mathscr{C}$         | \mathscr{C}         | 37      |
| $\ell$                | \ell                | 38      |
| $\chi$                | \chi                | 39      |
| $\geq$                | \geq                | 40      |
| $\Theta$              | \Theta              | 41      |
| $/$                   | /                   | 42      |
| $\nvDash$             | \nvDash             | 43      |
| $\coprod$             | \coprod             | 44      |
| $\nRightarrow$        | \nRightarrow        | 45      |
| $Y$                   | Y                   | 46      |
| $	heta$               | \theta              | 47      |
| $\mathcal{B}$         | \mathcal{B}         | 48      |
| $D$                   | D                   | 49      |
| $\vDash$              | \vDash              | 50      |
| $\downarrow$          | \downarrow          | 51      |
| $\mathscr{A}$         | \mathscr{A}         | 52      |
| $\otimes$             | \otimes             | 53      |
| $\rho$                | \rho                | 54      |
| $\pm$                 | \pm                 | 55      |
| $\sim$                | \sim                | 56      |
| $\perp$               | \perp               | 57      |
| $X$                   | X                   | 58      |
| $\vdots$              | \vdots              | 59      |
| $\mathcal{O}$         | \mathcal{O}         | 60      |
| $\dots$               | \dots               | 61      |
| $\celsius$            | \celsius            | 62      |
| $\mathcal{H}$         | \mathcal{H}         | 63      |
| $\|$                  | \|                  | 64      |
| $\cong$               | \cong               | 65      |
| $\emptyset$           | \emptyset           | 66      |
| $\varepsilon$         | \varepsilon         | 67      |
| $\mathds{C}$          | \mathds{C}          | 68      |
| $\leadsto$            | \leadsto            | 69      |
| $\square$             | \square             | 70      |
| $\iddots$             | \iddots             | 71      |
| $\lesssim$            | \lesssim            | 72      |
| $\wedge$              | \wedge              | 73      |
| $\rtimes$             | \rtimes             | 74      |
| $\asymp$              | \asymp              | 75      |
| $9$                   | 9                   | 76      |
| $\between$            | \between            | 77      |
| $\nearrow$            | \nearrow            | 78      |
| $\mathcal{U}$         | \mathcal{U}         | 79      |
| $\female$             | \female             | 80      |
| $\mathcal{S}$         | \mathcal{S}         | 81      |
| $\zeta$               | \zeta               | 82      |
| $\rightarrow$         | \rightarrow         | 83      |
| $\circlearrowleft$    | \circlearrowleft    | 84      |
| $\backsim$            | \backsim            | 85      |
| $\top$                | \top                | 86      |
| $\o$                  | \o                  | 87      |
| $\nrightarrow$        | \nrightarrow        | 88      |
| $\mathcal{X}$         | \mathcal{X}         | 89      |
| $\mathcal{A}$         | \mathcal{A}         | 90      |
| $\mathscr{P}$         | \mathscr{P}         | 91      |
| $\mapsto$             | \mapsto             | 92      |
| $\mathds{Z}$          | \mathds{Z}          | 93      |
| $\llbracket$          | \llbracket          | 94      |
| $\Re$                 | \Re                 | 95      |
| $\doteq$              | \doteq              | 96      |
| $\mapsfrom$           | \mapsfrom           | 97      |
| $\varrho$             | \varrho             | 98      |
| $\barwedge$           | \barwedge           | 99      |
| $\lightning$          | \lightning          | 100     |
| $\succeq$             | \succeq             | 101     |
| $\rfloor$             | \rfloor             | 102     |
| $\int$                | \int                | 103     |
| $\sphericalangle$     | \sphericalangle     | 104     |
| $]$                   | ]                   | 105     |
| $\sun$                | \sun                | 106     |
| $\Vdash$              | \Vdash              | 107     |
| $R$                   | R                   | 108     |
| $\tan$                | \tan                | 109     |
| $H$                   | H                   | 110     |
| $\phi$                | \phi                | 111     |
| $E$                   | E                   | 112     |
| $\prod$               | \prod               | 113     |
| $\prime$              | \prime              | 114     |
| $\heartsuit$          | \heartsuit          | 115     |
| $\Im$                 | \Im                 | 116     |
| $\beta$               | \beta               | 117     |
| $\triangleright$      | \triangleright      | 118     |
| $\cdot$               | \cdot               | 119     |
| $\&$                  | \&                  | 120     |
| $\equiv$              | \equiv              | 121     |
| $\mathcal{T}$         | \mathcal{T}         | 122     |
| $\fullmoon$           | \fullmoon           | 123     |
| $\Bowtie$             | \Bowtie             | 124     |
| $\Omega$              | \Omega              | 125     |
| $\oint$               | \oint               | 126     |
| $\sigma$              | \sigma              | 127     |
| $<$                   | <                   | 128     |
| $\sqcup$              | \sqcup              | 129     |
| $\dag$                | \dag                | 130     |
| $[$                   | [                   | 131     |
| $\kappa$              | \kappa              | 132     |
| $\xi$                 | \xi                 | 133     |
| $\mathcal{F}$         | \mathcal{F}         | 134     |
| $7$                   | 7                   | 135     |
| $\leftrightarrow$     | \leftrightarrow     | 136     |
| $P$                   | P                   | 137     |
| $\approx$             | \approx             | 138     |
| $\rceil$              | \rceil              | 139     |
| $\L$                  | \L                  | 140     |
| $\varpi$              | \varpi              | 141     |
| $\rrbracket$          | \rrbracket          | 142     |
| $\Phi$                | \Phi                | 143     |
| $B$                   | B                   | 144     |
| $G$                   | G                   | 145     |
| $\pitchfork$          | \pitchfork          | 146     |
| $\flat$               | \flat               | 147     |
| $T$                   | T                   | 148     |
| $\dashv$              | \dashv              | 149     |
| $U$                   | U                   | 150     |
| $\sum$                | \sum                | 151     |
| $Z$                   | Z                   | 152     |
| $\triangleleft$       | \triangleleft       | 153     |
| $\diameter$           | \diameter           | 154     |
| $\circ$               | \circ               | 155     |
| $\ae$                 | \ae                 | 156     |
| $\leftarrow$          | \leftarrow          | 157     |
| $\blacksquare$        | \blacksquare        | 158     |
| $\%$                  | \%                  | 159     |
| $\langle$             | \langle             | 160     |
| $\mathscr{H}$         | \mathscr{H}         | 161     |
| $\eta$                | \eta                | 162     |
| $\oplus$              | \oplus              | 163     |
| $\hookrightarrow$     | \hookrightarrow     | 164     |
| $\Downarrow$          | \Downarrow          | 165     |
| $L$                   | L                   | 166     |
| $\varphi$             | \varphi             | 167     |
| $2$                   | 2                   | 168     |
| $\varoiint$           | \varoiint           | 169     |
| $\venus$              | \venus              | 170     |
| $\Xi$                 | \Xi                 | 171     |
| $\Sigma$              | \Sigma              | 172     |
| $\sqcap$              | \sqcap              | 173     |
| $|$                   | |                   | 174     |
| $\therefore$          | \therefore          | 175     |
| $\O$                  | \O                  | 176     |
| $\ni$                 | \ni                 | 177     |
| $\AA$                 | \AA                 | 178     |
| $\{$                  | \{                  | 179     |
| $\vdash$              | \vdash              | 180     |
| $\bot$                | \bot                | 181     |
| $\mathds{R}$          | \mathds{R}          | 182     |
| $\male$               | \male               | 183     |
| $\mp$                 | \mp                 | 184     |
| $\propto$             | \propto             | 185     |
| $3$                   | 3                   | 186     |
| $\mathfrak{M}$        | \mathfrak{M}        | 187     |
| $\subseteq$           | \subseteq           | 188     |
| $\sqsubseteq$         | \sqsubseteq         | 189     |
| $\mathds{N}$          | \mathds{N}          | 190     |
| $\odot$               | \odot               | 191     |
| $\vee$                | \vee                | 192     |
| $\notin$              | \notin              | 193     |
| $\angle$              | \angle              | 194     |
| $\preceq$             | \preceq             | 195     |
| $\nu$                 | \nu                 | 196     |
| $\twoheadrightarrow$  | \twoheadrightarrow  | 197     |
| $\boxplus$            | \boxplus            | 198     |
| $\times$              | \times              | 199     |
| $\varnothing$         | \varnothing         | 200     |
| $\exists$             | \exists             | 201     |
| $\Leftrightarrow$     | \Leftrightarrow     | 202     |
| $\cap$                | \cap                | 203     |
| $\multimap$           | \multimap           | 204     |
| $\bowtie$             | \bowtie             | 205     |
| $\Gamma$              | \Gamma              | 206     |
| $\omega$              | \omega              | 207     |
| $K$                   | K                   | 208     |
| $\geqslant$           | \geqslant           | 209     |
| $\triangleq$          | \triangleq          | 210     |
| $\tau$                | \tau                | 211     |
| $\vartheta$           | \vartheta           | 212     |
| $\gtrless$            | \gtrless            | 213     |
| $\div$                | \div                | 214     |
| $6$                   | 6                   | 215     |
| $\mathds{P}$          | \mathds{P}          | 216     |
| $\diamond$            | \diamond            | 217     |
| $\mathds{1}$          | \mathds{1}          | 218     |
| $\ddots$              | \ddots              | 219     |
| $\lambda$             | \lambda             | 220     |
| $\forall$             | \forall             | 221     |
| $\rightleftarrows$    | \rightleftarrows    | 222     |
| $\cup$                | \cup                | 223     |
| $\oiint$              | \oiint              | 224     |
| $\ominus$             | \ominus             | 225     |
| $1$                   | 1                   | 226     |
| $\clubsuit$           | \clubsuit           | 227     |
| $\mathcal{Z}$         | \mathcal{Z}         | 228     |
| $\checkmark$          | \checkmark          | 229     |
| $\mathscr{F}$         | \mathscr{F}         | 230     |
| $\mathcal{M}$         | \mathcal{M}         | 231     |
| $\rightleftharpoons$  | \rightleftharpoons  | 232     |
| $\#$                  | \#                  | 233     |
| $\rangle$             | \rangle             | 234     |
| $\mathcal{D}$         | \mathcal{D}         | 235     |
| $\varsubsetneq$       | \varsubsetneq       | 236     |
| $\mars$               | \mars               | 237     |
| $\backslash$          | \backslash          | 238     |
| $\rightrightarrows$   | \rightrightarrows   | 239     |
| $\ss$                 | \ss                 | 240     |
| $\mathcal{N}$         | \mathcal{N}         | 241     |
| $\models$             | \models             | 242     |
| $\$$                  | \$                  | 243     |
| $C$                   | C                   | 244     |
| $+$                   | +                   | 245     |
| $\varkappa$           | \varkappa           | 246     |
| $\gtrsim$             | \gtrsim             | 247     |
| $\leqslant$           | \leqslant           | 248     |
| $\mathbb{1}$          | \mathbb{1}          | 249     |
| $\rightharpoonup$     | \rightharpoonup     | 250     |
| $\diamondsuit$        | \diamondsuit        | 251     |
| $\S$                  | \S                  | 252     |
| $\infty$              | \infty              | 253     |
| $\fint$               | \fint               | 254     |
| $\neq$                | \neq                | 255     |
| $\mathscr{D}$         | \mathscr{D}         | 256     |
| $\star$               | \star               | 257     |
| $\mathcal{P}$         | \mathcal{P}         | 258     |
| $\preccurlyeq$        | \preccurlyeq        | 259     |
| $\lceil$              | \lceil              | 260     |
| $\AE$                 | \AE                 | 261     |
| $\Delta$              | \Delta              | 262     |
| $\because$            | \because            | 263     |
| $>$                   | >                   | 264     |
| $\wp$                 | \wp                 | 265     |
| $\supseteq$           | \supseteq           | 266     |
| $I$                   | I                   | 267     |
| $\uplus$              | \uplus              | 268     |
| $J$                   | J                   | 269     |
| $\alpha$              | \alpha              | 270     |
| $\mathfrak{S}$        | \mathfrak{S}        | 271     |
| $\blacktriangleright$ | \blacktriangleright | 272     |
| $N$                   | N                   | 273     |
| $\circlearrowright$   | \circlearrowright   | 274     |
| $\mathfrak{X}$        | \mathfrak{X}        | 275     |
| $\amalg$              | \amalg              | 276     |
| $\log$                | \log                | 277     |
| $0$                   | 0                   | 278     |
| $\psi$                | \psi                | 279     |
| $\sharp$              | \sharp              | 280     |
| $\mathcal{E}$         | \mathcal{E}         | 281     |
| $\parr$               | \parr               | 282     |
| $\supset$             | \supset             | 283     |
| $V$                   | V                   | 284     |
| $\Pi$                 | \Pi                 | 285     |
| $Q$                   | Q                   | 286     |
| $\leq$                | \leq                | 287     |
| $M$                   | M                   | 288     |
| $\delta$              | \delta              | 289     |
| $\guillemotleft$      | \guillemotleft      | 290     |
| $\trianglelefteq$     | \trianglelefteq     | 291     |
| $\circledR$           | \circledR           | 292     |
| $\lfloor$             | \lfloor             | 293     |
| $\nexists$            | \nexists            | 294     |
| $\}$                  | \}                  | 295     |
| $\neg$                | \neg                | 296     |
| $\mathcal{C}$         | \mathcal{C}         | 297     |
| $\boxdot$             | \boxdot             | 298     |
| $\aa$                 | \aa                 | 299     |
| $\gamma$              | \gamma              | 300     |
| $\copyright$          | \copyright          | 301     |
| $\circledast$         | \circledast         | 302     |
| $-$                   | -                   | 303     |
| $4$                   | 4                   | 304     |
| $\mathds{Q}$          | \mathds{Q}          | 305     |
| $\mathcal{G}$         | \mathcal{G}         | 306     |
| $\Longleftrightarrow$ | \Longleftrightarrow | 307     |
| $\uparrow$            | \uparrow            | 308     |
| $W$                   | W                   | 309     |
| $\lim$                | \lim                | 310     |
| $\circledcirc$        | \circledcirc        | 311     |
| $\not\equiv$          | \not\equiv          | 312     |
| $S$                   | S                   | 313     |
| $\ast$                | \ast                | 314     |
| $\upharpoonright$     | \upharpoonright     | 315     |
| $\leftmoon$           | \leftmoon           | 316     |
| $\degree$             | \degree             | 317     |
| $\sqrt{}$             | \sqrt{}             | 318     |
| $A$                   | A                   | 319     |
| $\nmid$               | \nmid               | 320     |
| $\Rightarrow$         | \Rightarrow         | 321     |
| $8$                   | 8                   | 322     |
| $\mathcal{R}$         | \mathcal{R}         | 323     |
| $\sin$                | \sin                | 324     |
| $\simeq$              | \simeq              | 325     |
| $\boxtimes$           | \boxtimes           | 326     |
| $\in$                 | \in                 | 327     |
| $\cos$                | \cos                | 328     |
| $\rightsquigarrow$    | \rightsquigarrow    | 329     |
| $\ohm$                | \ohm                | 330     |

