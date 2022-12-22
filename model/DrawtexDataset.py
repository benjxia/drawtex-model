import numpy as np
import cv2
import matplotlib.pyplot as plt
import torch
import os
import pandas as pd
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms


class DrawtexDataset(Dataset):
    classes = ['5', '\\mathcal{L}', '\\epsilon', '\\partial', '\\hbar', '\\succ', '\\mathbb{H}', '\\mu', '\\mathscr{E}', '\\Leftarrow', '\\lozenge', '\\Psi', '\\aleph', '\\ltimes', '\\bullet', '\\mathscr{S}', '\\astrosun', '\\subsetneq', 'F', '\\wr', '\\pi', '\\frown', '\\pounds', 'O', '\\parallel', '\\searrow', '\\mathscr{L}', '\\prec', '\\mathds{E}', '\\subset', '\\Lambda', '\\lhd', '\\iota', '\\nsubseteq', '\\curvearrowright', '\\mathfrak{A}', '\\nabla', '\\mathscr{C}', '\\ell', '\\chi', '\\geq', '\\Theta', '/', '\\nvDash', '\\coprod', '\\nRightarrow', 'Y', '\\theta', '\\mathcal{B}', 'D', '\\vDash', '\\downarrow', '\\mathscr{A}', '\\otimes', '\\rho', '\\pm', '\\sim', '\\perp', 'X', '\\vdots', '\\mathcal{O}', '\\dots', '\\celsius', '\\mathcal{H}', '\\|', '\\cong', '\\emptyset', '\\varepsilon', '\\mathds{C}', '\\leadsto', '\\square', '\\iddots', '\\lesssim', '\\wedge', '\\rtimes', '\\asymp', '9', '\\between', '\\nearrow', '\\mathcal{U}', '\\female', '\\mathcal{S}', '\\zeta', '\\rightarrow', '\\circlearrowleft', '\\backsim', '\\top', '\\o', '\\nrightarrow', '\\mathcal{X}', '\\mathcal{A}', '\\mathscr{P}', '\\mapsto', '\\mathds{Z}', '\\llbracket', '\\Re', '\\doteq', '\\mapsfrom', '\\varrho', '\\barwedge', '\\lightning', '\\succeq', '\\rfloor', '\\int', '\\sphericalangle', ']', '\\sun', '\\Vdash', 'R', '\\tan', 'H', '\\phi', 'E', '\\prod', '\\prime', '\\heartsuit', '\\Im', '\\beta', '\\triangleright', '\\cdot', '\\&', '\\equiv', '\\mathcal{T}', '\\fullmoon', '\\Bowtie', '\\Omega', '\\oint', '\\sigma', '<', '\\sqcup', '\\dag', '[', '\\kappa', '\\xi', '\\mathcal{F}', '7', '\\leftrightarrow', 'P', '\\approx', '\\rceil', '\\L', '\\varpi', '\\rrbracket', '\\Phi', 'B', 'G', '\\pitchfork', '\\flat', 'T', '\\dashv', 'U', '\\sum', 'Z', '\\triangleleft', '\\diameter', '\\circ', '\\ae', '\\leftarrow', '\\blacksquare', '\\%', '\\langle', '\\mathscr{H}', '\\eta', '\\oplus', '\\hookrightarrow', '\\Downarrow', 'L', '\\varphi', '2', '\\varoiint', '\\venus', '\\Xi', '\\Sigma', '\\sqcap', '|', '\\therefore', '\\O', '\\ni', '\\AA', '\\{', '\\vdash', '\\bot', '\\mathds{R}', '\\male', '\\mp', '\\propto', '3', '\\mathfrak{M}', '\\subseteq', '\\sqsubseteq', '\\mathds{N}', '\\odot', '\\vee', '\\notin', '\\angle', '\\preceq', '\\nu', '\\twoheadrightarrow', '\\boxplus', '\\times', '\\varnothing', '\\exists', '\\Leftrightarrow', '\\cap', '\\multimap', '\\bowtie', '\\Gamma', '\\omega', 'K', '\\geqslant', '\\triangleq', '\\tau', '\\vartheta', '\\gtrless', '\\div', '6', '\\mathds{P}', '\\diamond', '\\mathds{1}', '\\ddots', '\\lambda', '\\forall', '\\rightleftarrows', '\\cup', '\\oiint', '\\ominus', '1', '\\clubsuit', '\\mathcal{Z}', '\\checkmark', '\\mathscr{F}', '\\mathcal{M}', '\\rightleftharpoons', '\\#', '\\rangle', '\\mathcal{D}', '\\varsubsetneq', '\\mars', '\\backslash', '\\rightrightarrows', '\\ss', '\\mathcal{N}', '\\models', '\\$', 'C', '+', '\\varkappa', '\\gtrsim', '\\leqslant', '\\mathbb{1}', '\\rightharpoonup', '\\diamondsuit', '\\S', '\\infty', '\\fint', '\\neq', '\\mathscr{D}', '\\star', '\\mathcal{P}', '\\preccurlyeq', '\\lceil', '\\AE', '\\Delta', '\\because', '>', '\\wp', '\\supseteq', 'I', '\\uplus', 'J', '\\alpha', '\\mathfrak{S}', '\\blacktriangleright', 'N', '\\circlearrowright', '\\mathfrak{X}', '\\amalg', '\\log', '0', '\\psi', '\\sharp', '\\mathcal{E}', '\\parr', '\\supset', 'V', '\\Pi', 'Q', '\\leq', 'M', '\\delta', '\\guillemotleft', '\\trianglelefteq', '\\circledR', '\\lfloor', '\\nexists', '\\}', '\\neg', '\\mathcal{C}', '\\boxdot', '\\aa', '\\gamma', '\\copyright', '\\circledast', '-', '4', '\\mathds{Q}', '\\mathcal{G}', '\\Longleftrightarrow', '\\uparrow', 'W', '\\lim', '\\circledcirc', '\\not\\equiv', 'S', '\\ast', '\\upharpoonright', '\\leftmoon', '\\degree', '\\sqrt{}', 'A', '\\nmid', '\\Rightarrow', '8', '\\mathcal{R}', '\\sin', '\\simeq', '\\boxtimes', '\\in', '\\cos', '\\rightsquigarrow', '\\ohm']
    lab_map = {'5': 0, '\\mathcal{L}': 1, '\\epsilon': 2, '\\partial': 3, '\\hbar': 4, '\\succ': 5, '\\mathbb{H}': 6, '\\mu': 7, '\\mathscr{E}': 8, '\\Leftarrow': 9, '\\lozenge': 10, '\\Psi': 11, '\\aleph': 12, '\\ltimes': 13, '\\bullet': 14, '\\mathscr{S}': 15, '\\astrosun': 16, '\\subsetneq': 17, 'F': 18, '\\wr': 19, '\\pi': 20, '\\frown': 21, '\\pounds': 22, 'O': 23, '\\parallel': 24, '\\searrow': 25, '\\mathscr{L}': 26, '\\prec': 27, '\\mathds{E}': 28, '\\subset': 29, '\\Lambda': 30, '\\lhd': 31, '\\iota': 32, '\\nsubseteq': 33, '\\curvearrowright': 34, '\\mathfrak{A}': 35, '\\nabla': 36, '\\mathscr{C}': 37, '\\ell': 38, '\\chi': 39, '\\geq': 40, '\\Theta': 41, '/': 42, '\\nvDash': 43, '\\coprod': 44, '\\nRightarrow': 45, 'Y': 46, '\\theta': 47, '\\mathcal{B}': 48, 'D': 49, '\\vDash': 50, '\\downarrow': 51, '\\mathscr{A}': 52, '\\otimes': 53, '\\rho': 54, '\\pm': 55, '\\sim': 56, '\\perp': 57, 'X': 58, '\\vdots': 59, '\\mathcal{O}': 60, '\\dots': 61, '\\celsius': 62, '\\mathcal{H}': 63, '\\|': 64, '\\cong': 65, '\\emptyset': 66, '\\varepsilon': 67, '\\mathds{C}': 68, '\\leadsto': 69, '\\square': 70, '\\iddots': 71, '\\lesssim': 72, '\\wedge': 73, '\\rtimes': 74, '\\asymp': 75, '9': 76, '\\between': 77, '\\nearrow': 78, '\\mathcal{U}': 79, '\\female': 80, '\\mathcal{S}': 81, '\\zeta': 82, '\\rightarrow': 83, '\\circlearrowleft': 84, '\\backsim': 85, '\\top': 86, '\\o': 87, '\\nrightarrow': 88, '\\mathcal{X}': 89, '\\mathcal{A}': 90, '\\mathscr{P}': 91, '\\mapsto': 92, '\\mathds{Z}': 93, '\\llbracket': 94, '\\Re': 95, '\\doteq': 96, '\\mapsfrom': 97, '\\varrho': 98, '\\barwedge': 99, '\\lightning': 100, '\\succeq': 101, '\\rfloor': 102, '\\int': 103, '\\sphericalangle': 104, ']': 105, '\\sun': 106, '\\Vdash': 107, 'R': 108, '\\tan': 109, 'H': 110, '\\phi': 111, 'E': 112, '\\prod': 113, '\\prime': 114, '\\heartsuit': 115, '\\Im': 116, '\\beta': 117, '\\triangleright': 118, '\\cdot': 119, '\\&': 120, '\\equiv': 121, '\\mathcal{T}': 122, '\\fullmoon': 123, '\\Bowtie': 124, '\\Omega': 125, '\\oint': 126, '\\sigma': 127, '<': 128, '\\sqcup': 129, '\\dag': 130, '[': 131, '\\kappa': 132, '\\xi': 133, '\\mathcal{F}': 134, '7': 135, '\\leftrightarrow': 136, 'P': 137, '\\approx': 138, '\\rceil': 139, '\\L': 140, '\\varpi': 141, '\\rrbracket': 142, '\\Phi': 143, 'B': 144, 'G': 145, '\\pitchfork': 146, '\\flat': 147, 'T': 148, '\\dashv': 149, 'U': 150, '\\sum': 151, 'Z': 152, '\\triangleleft': 153, '\\diameter': 154, '\\circ': 155, '\\ae': 156, '\\leftarrow': 157, '\\blacksquare': 158, '\\%': 159, '\\langle': 160, '\\mathscr{H}': 161, '\\eta': 162, '\\oplus': 163, '\\hookrightarrow': 164, '\\Downarrow': 165, 'L': 166, '\\varphi': 167, '2': 168, '\\varoiint': 169, '\\venus': 170, '\\Xi': 171, '\\Sigma': 172, '\\sqcap': 173, '|': 174, '\\therefore': 175, '\\O': 176, '\\ni': 177, '\\AA': 178, '\\{': 179, '\\vdash': 180, '\\bot': 181, '\\mathds{R}': 182, '\\male': 183, '\\mp': 184, '\\propto': 185, '3': 186, '\\mathfrak{M}': 187, '\\subseteq': 188, '\\sqsubseteq': 189, '\\mathds{N}': 190, '\\odot': 191, '\\vee': 192, '\\notin': 193, '\\angle': 194, '\\preceq': 195, '\\nu': 196, '\\twoheadrightarrow': 197, '\\boxplus': 198, '\\times': 199, '\\varnothing': 200, '\\exists': 201, '\\Leftrightarrow': 202, '\\cap': 203, '\\multimap': 204, '\\bowtie': 205, '\\Gamma': 206, '\\omega': 207, 'K': 208, '\\geqslant': 209, '\\triangleq': 210, '\\tau': 211, '\\vartheta': 212, '\\gtrless': 213, '\\div': 214, '6': 215, '\\mathds{P}': 216, '\\diamond': 217, '\\mathds{1}': 218, '\\ddots': 219, '\\lambda': 220, '\\forall': 221, '\\rightleftarrows': 222, '\\cup': 223, '\\oiint': 224, '\\ominus': 225, '1': 226, '\\clubsuit': 227, '\\mathcal{Z}': 228, '\\checkmark': 229, '\\mathscr{F}': 230, '\\mathcal{M}': 231, '\\rightleftharpoons': 232, '\\#': 233, '\\rangle': 234, '\\mathcal{D}': 235, '\\varsubsetneq': 236, '\\mars': 237, '\\backslash': 238, '\\rightrightarrows': 239, '\\ss': 240, '\\mathcal{N}': 241, '\\models': 242, '\\$': 243, 'C': 244, '+': 245, '\\varkappa': 246, '\\gtrsim': 247, '\\leqslant': 248, '\\mathbb{1}': 249, '\\rightharpoonup': 250, '\\diamondsuit': 251, '\\S': 252, '\\infty': 253, '\\fint': 254, '\\neq': 255, '\\mathscr{D}': 256, '\\star': 257, '\\mathcal{P}': 258, '\\preccurlyeq': 259, '\\lceil': 260, '\\AE': 261, '\\Delta': 262, '\\because': 263, '>': 264, '\\wp': 265, '\\supseteq': 266, 'I': 267, '\\uplus': 268, 'J': 269, '\\alpha': 270, '\\mathfrak{S}': 271, '\\blacktriangleright': 272, 'N': 273, '\\circlearrowright': 274, '\\mathfrak{X}': 275, '\\amalg': 276, '\\log': 277, '0': 278, '\\psi': 279, '\\sharp': 280, '\\mathcal{E}': 281, '\\parr': 282, '\\supset': 283, 'V': 284, '\\Pi': 285, 'Q': 286, '\\leq': 287, 'M': 288, '\\delta': 289, '\\guillemotleft': 290, '\\trianglelefteq': 291, '\\circledR': 292, '\\lfloor': 293, '\\nexists': 294, '\\}': 295, '\\neg': 296, '\\mathcal{C}': 297, '\\boxdot': 298, '\\aa': 299, '\\gamma': 300, '\\copyright': 301, '\\circledast': 302, '-': 303, '4': 304, '\\mathds{Q}': 305, '\\mathcal{G}': 306, '\\Longleftrightarrow': 307, '\\uparrow': 308, 'W': 309, '\\lim': 310, '\\circledcirc': 311, '\\not\\equiv': 312, 'S': 313, '\\ast': 314, '\\upharpoonright': 315, '\\leftmoon': 316, '\\degree': 317, '\\sqrt{}': 318, 'A': 319, '\\nmid': 320, '\\Rightarrow': 321, '8': 322, '\\mathcal{R}': 323, '\\sin': 324, '\\simeq': 325, '\\boxtimes': 326, '\\in': 327, '\\cos': 328, '\\rightsquigarrow': 329, '\\ohm': 330}


    device: str = "cuda" if torch.cuda.is_available() else "cpu"

    def __init__(self, transform=None):
        self.df = pd.read_csv("../data/HASYv2/combined2.csv")
        self.transform = transform

    def __len__(self) -> int:
        return len(self.df)

    def __getitem__(self, item: any) -> tuple:
        row = self.df.iloc[[item]]
        path = row["path"].values[0]
        img = cv2.imread(f"../data/HASYv2/hasy-data/{path}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(img, 128, 1, cv2.THRESH_BINARY)[1]
        img = img.reshape((45, 45, 1))

        if self.transform is not None:
            img_tensor = self.transform(img)
        else:
            img_tensor = torch.from_numpy(img)

        label_tensor = torch.tensor(self.lab_map[row["latex"].values[0]])

        return img_tensor, label_tensor

# Debugging stuff below
if __name__ == "__main__":
    training_set = DrawtexDataset(transforms.ToTensor())

    train_load: DataLoader = DataLoader(
        dataset=training_set,
        batch_size=100,
        shuffle=True,
        num_workers=4
    )

    iter = enumerate(train_load)
    idx, (img, lab) = next(iter)
    plt.title(training_set.classes[lab[0].cpu()])
    plt.imshow(img[0][0].cpu(), cmap="gray")
    plt.show()
