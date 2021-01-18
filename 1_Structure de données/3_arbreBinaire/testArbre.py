# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:19:09 2021

@author: SOPHIE
"""

from arbre import ArbreB

arbre_f = ArbreB('f')
arbre_g = ArbreB('g')
arbre_c = ArbreB('c',arbre_f,arbre_g)
arbre_j = ArbreB('j')
arbre_e = ArbreB('e',arbre_j)
arbre_h = ArbreB('h')
arbre_i = ArbreB('i')
arbre_d = ArbreB('d', arbre_h,arbre_i)
arbre_b = ArbreB('b', arbre_d, arbre_e)
arbre = ArbreB('a', arbre_b, arbre_c)
print(arbre)


arbre_vide = ArbreB(None)
assert arbre_vide.est_Vide() == True
assert arbre.est_Vide() == False

assert arbre_vide.estFeuille() == False
assert arbre_f.estFeuille() == True
assert arbre_d.estFeuille() == False

assert arbre_vide.taille() == 0
assert arbre_f.taille() == 1
assert arbre_d.taille() == 3
assert arbre.taille() == 10

assert arbre_vide.hauteur() == 0
assert arbre_f.hauteur() == 1
assert arbre_d.hauteur() == 2
assert arbre.hauteur()==4

prefixe = arbre.parcoursPrefixe()
print("prefixe : ", prefixe)

infixe = arbre.parcoursInfixe()
print("infixe : ", infixe)

suffixe = arbre.parcoursSuffixe()
print("suffixe : ", suffixe)

Largeur = arbre.parcoursLargeur()
print("largeur : ", Largeur)

