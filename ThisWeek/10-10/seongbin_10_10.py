from unicodedata import normalize,combining
import string
portugal_raws = ['Rui Patrício',
        'Bruno Alves',
        'Pepe',
        'José Fonte',
        'Raphaël Guerreiro',
        'Ricardo Carvalho',
        'Christiano Ronaldo',
        'João Moutinho',
        'Éder',
        'João Mário',
        'Vieirinha',
        'Anthony Lopes',
        'Danilo',
        'Willian Carvalho',
        'André Gomes',
        'Renato Sanches',
        'Nani',
        'Rafa Silva',
        'Eliseu',
        'Ricardo Quaresma',
        'Cédric Soares',
        'Eduardo',
        'Adrien Silva']
def shave_marks_latin(txt):
        norm_txt = normalize('NFD',txt)
        latin_base = False
        keepers = []
        for c in norm_txt:
                if combining(c) and latin_base:
                        continue
                keepers.append(c)
                if not combining(c):
                        latin_base = c in string.ascii_letters
        shaved = ''.join(keepers)
        return normalize('NFC',shaved)

portugal_enc = [[0]*2 for i in range(len(portugal_raws))]
for i in range(len(portugal_raws)):
    portugal_enc[i][0] = portugal_raws[i]
    portugal_enc[i][1] = shave_marks_latin(portugal_raws[i]).lower()

