# main du TP2
# Nathan Chopin
# 26/09/24

import fn_TP2 as fn


phrase1 = "le joli chat mange."
phrase2 = "le ,joli chat ; dort." # OK car on ne prend pas en compte les séparateurs
phrase3 = "Jean dort."
phrase4 = "la verte souris grosse petit mange le bleu verte chat petite."

phrase5 = "."
phrase6 = ""
phrase7 = "le jolichat joue" # pas ’.’ fina
phrase8 = "le joli chat joue." # ’joue’ inconnu


#test :
fn.correcteur(phrase1)
fn.correcteur(phrase2)
fn.correcteur(phrase3)
fn.correcteur(phrase4)

print("\n")

fn.correcteur(phrase5)
fn.correcteur(phrase6)
fn.correcteur(phrase7)
fn.correcteur(phrase8)