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

### Version 2: 326 classes, ~82% accuracy

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
| $\Leftarrow$          | \Leftarrow          | 0       |
| $\theta$              | \theta              | 1       |
| $\mathcal{M}$         | \mathcal{M}         | 2       |
| $\mathcal{L}$         | \mathcal{L}         | 3       |
| $\chi$                | \chi                | 4       |
| $\heartsuit$          | \heartsuit          | 5       |
| $\propto$             | \propto             | 6       |
| $\diameter$           | \diameter           | 7       |
| $\L$                  | \L                  | 8       |
| $\dashv$              | \dashv              | 9       |
| $\dag$                | \dag                | 10      |
| $B$                   | B                   | 11      |
| $\Vdash$              | \Vdash              | 12      |
| $\barwedge$           | \barwedge           | 13      |
| $\hbar$               | \hbar               | 14      |
| $\ell$                | \ell                | 15      |
| $\o$                  | \o                  | 16      |
| $\div$                | \div                | 17      |
| $\prec$               | \prec               | 18      |
| $\succeq$             | \succeq             | 19      |
| $D$                   | D                   | 20      |
| $\iota$               | \iota               | 21      |
| $\AA$                 | \AA                 | 22      |
| $\odot$               | \odot               | 23      |
| $\varpi$              | \varpi              | 24      |
| $+$                   | +                   | 25      |
| $\mathds{Q}$          | \mathds{Q}          | 26      |
| $\varsubsetneq$       | \varsubsetneq       | 27      |
| $\mathcal{O}$         | \mathcal{O}         | 28      |
| $\lambda$             | \lambda             | 29      |
| $\circlearrowright$   | \circlearrowright   | 30      |
| $4$                   | 4                   | 31      |
| $\sum$                | \sum                | 32      |
| $\ohm$                | \ohm                | 33      |
| $\mathds{C}$          | \mathds{C}          | 34      |
| $3$                   | 3                   | 35      |
| $N$                   | N                   | 36      |
| $\Leftrightarrow$     | \Leftrightarrow     | 37      |
| $\lceil$              | \lceil              | 38      |
| $\diamondsuit$        | \diamondsuit        | 39      |
| $\alpha$              | \alpha              | 40      |
| $\Phi$                | \Phi                | 41      |
| $\mathds{P}$          | \mathds{P}          | 42      |
| $\aleph$              | \aleph              | 43      |
| $\mu$                 | \mu                 | 44      |
| $\geq$                | \geq                | 45      |
| $\nmid$               | \nmid               | 46      |
| $\geqslant$           | \geqslant           | 47      |
| $\vdots$              | \vdots              | 48      |
| $\epsilon$            | \epsilon            | 49      |
| $\flat$               | \flat               | 50      |
| $\mathcal{S}$         | \mathcal{S}         | 51      |
| $\downarrow$          | \downarrow          | 52      |
| $\ae$                 | \ae                 | 53      |
| $\simeq$              | \simeq              | 54      |
| $\rangle$             | \rangle             | 55      |
| $\nRightarrow$        | \nRightarrow        | 56      |
| $\bot$                | \bot                | 57      |
| $\#$                  | \#                  | 58      |
| $\backsim$            | \backsim            | 59      |
| $\rightrightarrows$   | \rightrightarrows   | 60      |
| $\aa$                 | \aa                 | 61      |
| $\astrosun$           | \astrosun           | 62      |
| $5$                   | 5                   | 63      |
| $\ss$                 | \ss                 | 64      |
| $A$                   | A                   | 65      |
| $\rightsquigarrow$    | \rightsquigarrow    | 66      |
| $\bowtie$             | \bowtie             | 67      |
| $E$                   | E                   | 68      |
| $T$                   | T                   | 69      |
| $\{$                  | \{                  | 70      |
| $<$                   | <                   | 71      |
| $\exists$             | \exists             | 72      |
| $\mathcal{D}$         | \mathcal{D}         | 73      |
| $\parr$               | \parr               | 74      |
| $\pitchfork$          | \pitchfork          | 75      |
| $\rightleftharpoons$  | \rightleftharpoons  | 76      |
| $\AE$                 | \AE                 | 77      |
| $\gamma$              | \gamma              | 78      |
| $\mathcal{T}$         | \mathcal{T}         | 79      |
| $\wp$                 | \wp                 | 80      |
| $\sphericalangle$     | \sphericalangle     | 81      |
| $\because$            | \because            | 82      |
| $\ominus$             | \ominus             | 83      |
| $X$                   | X                   | 84      |
| $\llbracket$          | \llbracket          | 85      |
| $\Re$                 | \Re                 | 86      |
| $\Omega$              | \Omega              | 87      |
| $\models$             | \models             | 88      |
| $\Longleftrightarrow$ | \Longleftrightarrow | 89      |
| $\int$                | \int                | 90      |
| $R$                   | R                   | 91      |
| $\mathfrak{M}$        | \mathfrak{M}        | 92      |
| $\mathbb{H}$          | \mathbb{H}          | 93      |
| $\neq$                | \neq                | 94      |
| $\circledast$         | \circledast         | 95      |
| $\varphi$             | \varphi             | 96      |
| $\mathscr{P}$         | \mathscr{P}         | 97      |
| $S$                   | S                   | 98      |
| $\pi$                 | \pi                 | 99      |
| $\S$                  | \S                  | 100     |
| $\triangleq$          | \triangleq          | 101     |
| $\preceq$             | \preceq             | 102     |
| $\mathscr{F}$         | \mathscr{F}         | 103     |
| $\mathscr{C}$         | \mathscr{C}         | 104     |
| $\triangleright$      | \triangleright      | 105     |
| $\varkappa$           | \varkappa           | 106     |
| $V$                   | V                   | 107     |
| $\mathcal{B}$         | \mathcal{B}         | 108     |
| $\circlearrowleft$    | \circlearrowleft    | 109     |
| $\Delta$              | \Delta              | 110     |
| $\mathscr{D}$         | \mathscr{D}         | 111     |
| $H$                   | H                   | 112     |
| $\nvDash$             | \nvDash             | 113     |
| $\nu$                 | \nu                 | 114     |
| $\rfloor$             | \rfloor             | 115     |
| $\cdot$               | \cdot               | 116     |
| $\mathcal{C}$         | \mathcal{C}         | 117     |
| $\coprod$             | \coprod             | 118     |
| $\mathcal{H}$         | \mathcal{H}         | 119     |
| $\vdash$              | \vdash              | 120     |
| $\uparrow$            | \uparrow            | 121     |
| $\leftrightarrow$     | \leftrightarrow     | 122     |
| $\gtrsim$             | \gtrsim             | 123     |
| $C$                   | C                   | 124     |
| $\Sigma$              | \Sigma              | 125     |
| $\backslash$          | \backslash          | 126     |
| $\pounds$             | \pounds             | 127     |
| $\mathbb{1}$          | \mathbb{1}          | 128     |
| $\bullet$             | \bullet             | 129     |
| $\Lambda$             | \Lambda             | 130     |
| $\pm$                 | \pm                 | 131     |
| $\lightning$          | \lightning          | 132     |
| $\nexists$            | \nexists            | 133     |
| $\cong$               | \cong               | 134     |
| $\mathcal{P}$         | \mathcal{P}         | 135     |
| $\male$               | \male               | 136     |
| $\vDash$              | \vDash              | 137     |
| $\boxtimes$           | \boxtimes           | 138     |
| $\mathscr{E}$         | \mathscr{E}         | 139     |
| $\mathcal{N}$         | \mathcal{N}         | 140     |
| $\leftmoon$           | \leftmoon           | 141     |
| $\rrbracket$          | \rrbracket          | 142     |
| $\between$            | \between            | 143     |
| $\Rightarrow$         | \Rightarrow         | 144     |
| $Z$                   | Z                   | 145     |
| $\ddots$              | \ddots              | 146     |
| $\lhd$                | \lhd                | 147     |
| $\subset$             | \subset             | 148     |
| $\subseteq$           | \subseteq           | 149     |
| $\rightarrow$         | \rightarrow         | 150     |
| $\sun$                | \sun                | 151     |
| $\infty$              | \infty              | 152     |
| $\mathscr{A}$         | \mathscr{A}         | 153     |
| $\celsius$            | \celsius            | 154     |
| $\omega$              | \omega              | 155     |
| $\nsubseteq$          | \nsubseteq          | 156     |
| $\mathds{1}$          | \mathds{1}          | 157     |
| $P$                   | P                   | 158     |
| $\nabla$              | \nabla              | 159     |
| $\tau$                | \tau                | 160     |
| $1$                   | 1                   | 161     |
| $\uplus$              | \uplus              | 162     |
| $\otimes$             | \otimes             | 163     |
| $\cup$                | \cup                | 164     |
| $G$                   | G                   | 165     |
| $\oplus$              | \oplus              | 166     |
| $\%$                  | \%                  | 167     |
| $\Psi$                | \Psi                | 168     |
| $\blacktriangleright$ | \blacktriangleright | 169     |
| $W$                   | W                   | 170     |
| $\mathcal{U}$         | \mathcal{U}         | 171     |
| $\mathscr{L}$         | \mathscr{L}         | 172     |
| $\psi$                | \psi                | 173     |
| $\top$                | \top                | 174     |
| $\oint$               | \oint               | 175     |
| $\rightharpoonup$     | \rightharpoonup     | 176     |
| $\|$                  | \|                  | 177     |
| $\subsetneq$          | \subsetneq          | 178     |
| $\beta$               | \beta               | 179     |
| $\varrho$             | \varrho             | 180     |
| $\mars$               | \mars               | 181     |
| $\fint$               | \fint               | 182     |
| $6$                   | 6                   | 183     |
| $\}$                  | \}                  | 184     |
| $\in$                 | \in                 | 185     |
| $\boxplus$            | \boxplus            | 186     |
| $\ast$                | \ast                | 187     |
| $\mathcal{G}$         | \mathcal{G}         | 188     |
| $\$$                  | \$                  | 189     |
| $\preccurlyeq$        | \preccurlyeq        | 190     |
| $\varoiint$           | \varoiint           | 191     |
| $\iddots$             | \iddots             | 192     |
| $-$                   | -                   | 193     |
| $\vee$                | \vee                | 194     |
| $\rightleftarrows$    | \rightleftarrows    | 195     |
| $\square$             | \square             | 196     |
| $\mathfrak{X}$        | \mathfrak{X}        | 197     |
| $\mp$                 | \mp                 | 198     |
| $\twoheadrightarrow$  | \twoheadrightarrow  | 199     |
| $\equiv$              | \equiv              | 200     |
| $\searrow$            | \searrow            | 201     |
| $\sqcap$              | \sqcap              | 202     |
| $\fullmoon$           | \fullmoon           | 203     |
| $\supset$             | \supset             | 204     |
| $\prod$               | \prod               | 205     |
| $\not\equiv$          | \not\equiv          | 206     |
| $F$                   | F                   | 207     |
| $\Gamma$              | \Gamma              | 208     |
| $\sqsubseteq$         | \sqsubseteq         | 209     |
| $\langle$             | \langle             | 210     |
| $\supseteq$           | \supseteq           | 211     |
| $\sim$                | \sim                | 212     |
| $\clubsuit$           | \clubsuit           | 213     |
| $\mapsto$             | \mapsto             | 214     |
| $8$                   | 8                   | 215     |
| $\multimap$           | \multimap           | 216     |
| $\circledcirc$        | \circledcirc        | 217     |
| $\mathcal{F}$         | \mathcal{F}         | 218     |
| $\mathfrak{S}$        | \mathfrak{S}        | 219     |
| $\mathds{Z}$          | \mathds{Z}          | 220     |
| $\leadsto$            | \leadsto            | 221     |
| $\amalg$              | \amalg              | 222     |
| $\zeta$               | \zeta               | 223     |
| $\cap$                | \cap                | 224     |
| $\mathds{R}$          | \mathds{R}          | 225     |
| $Q$                   | Q                   | 226     |
| $[$                   | [                   | 227     |
| $\mathds{N}$          | \mathds{N}          | 228     |
| $J$                   | J                   | 229     |
| $\therefore$          | \therefore          | 230     |
| $\mathscr{S}$         | \mathscr{S}         | 231     |
| $0$                   | 0                   | 232     |
| $\varepsilon$         | \varepsilon         | 233     |
| $\hookrightarrow$     | \hookrightarrow     | 234     |
| $\mathcal{R}$         | \mathcal{R}         | 235     |
| $\ltimes$             | \ltimes             | 236     |
| $\diamond$            | \diamond            | 237     |
| $\triangleleft$       | \triangleleft       | 238     |
| $]$                   | ]                   | 239     |
| $\checkmark$          | \checkmark          | 240     |
| $\dots$               | \dots               | 241     |
| $\rho$                | \rho                | 242     |
| $\circledR$           | \circledR           | 243     |
| $\times$              | \times              | 244     |
| $\mathcal{E}$         | \mathcal{E}         | 245     |
| $\leftarrow$          | \leftarrow          | 246     |
| $\upharpoonright$     | \upharpoonright     | 247     |
| $\trianglelefteq$     | \trianglelefteq     | 248     |
| $\nearrow$            | \nearrow            | 249     |
| $\mathcal{A}$         | \mathcal{A}         | 250     |
| $\wr$                 | \wr                 | 251     |
| $\prime$              | \prime              | 252     |
| $\sqcup$              | \sqcup              | 253     |
| $\succ$               | \succ               | 254     |
| $\parallel$           | \parallel           | 255     |
| $\leqslant$           | \leqslant           | 256     |
| $\Bowtie$             | \Bowtie             | 257     |
| $\partial$            | \partial            | 258     |
| $\rceil$              | \rceil              | 259     |
| $O$                   | O                   | 260     |
| $\forall$             | \forall             | 261     |
| $\emptyset$           | \emptyset           | 262     |
| $\circ$               | \circ               | 263     |
| $\venus$              | \venus              | 264     |
| $\sharp$              | \sharp              | 265     |
| $\angle$              | \angle              | 266     |
| $Y$                   | Y                   | 267     |
| $\boxdot$             | \boxdot             | 268     |
| $2$                   | 2                   | 269     |
| $L$                   | L                   | 270     |
| $\neg$                | \neg                | 271     |
| $\oiint$              | \oiint              | 272     |
| $\sigma$              | \sigma              | 273     |
| $\Pi$                 | \Pi                 | 274     |
| $\mathds{E}$          | \mathds{E}          | 275     |
| $\female$             | \female             | 276     |
| $\leq$                | \leq                | 277     |
| $\approx$             | \approx             | 278     |
| $\lfloor$             | \lfloor             | 279     |
| $\degree$             | \degree             | 280     |
| $\sqrt{}$             | \sqrt{}             | 281     |
| $I$                   | I                   | 282     |
| $\notin$              | \notin              | 283     |
| $\kappa$              | \kappa              | 284     |
| $\ni$                 | \ni                 | 285     |
| $\guillemotleft$      | \guillemotleft      | 286     |
| $\blacksquare$        | \blacksquare        | 287     |
| $\gtrless$            | \gtrless            | 288     |
| $>$                   | >                   | 289     |
| $\delta$              | \delta              | 290     |
| $\Theta$              | \Theta              | 291     |
| $\doteq$              | \doteq              | 292     |
| $\nrightarrow$        | \nrightarrow        | 293     |
| $\wedge$              | \wedge              | 294     |
| $/$                   | /                   | 295     |
| $|$                   | |                   | 296     |
| $7$                   | 7                   | 297     |
| $\frown$              | \frown              | 298     |
| $U$                   | U                   | 299     |
| $\phi$                | \phi                | 300     |
| $\lesssim$            | \lesssim            | 301     |
| $\varnothing$         | \varnothing         | 302     |
| $\Im$                 | \Im                 | 303     |
| $\copyright$          | \copyright          | 304     |
| $M$                   | M                   | 305     |
| $\xi$                 | \xi                 | 306     |
| $\star$               | \star               | 307     |
| $\mathfrak{A}$        | \mathfrak{A}        | 308     |
| $\curvearrowright$    | \curvearrowright    | 309     |
| $\mathcal{X}$         | \mathcal{X}         | 310     |
| $\&$                  | \&                  | 311     |
| $\vartheta$           | \vartheta           | 312     |
| $\perp$               | \perp               | 313     |
| $\mathcal{Z}$         | \mathcal{Z}         | 314     |
| $\eta$                | \eta                | 315     |
| $\mapsfrom$           | \mapsfrom           | 316     |
| $\asymp$              | \asymp              | 317     |
| $\rtimes$             | \rtimes             | 318     |
| $\O$                  | \O                  | 319     |
| $\lozenge$            | \lozenge            | 320     |
| $\Downarrow$          | \Downarrow          | 321     |
| $\mathscr{H}$         | \mathscr{H}         | 322     |
| $\Xi$                 | \Xi                 | 323     |
| $K$                   | K                   | 324     |
| $9$                   | 9                   | 325     |

