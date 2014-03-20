#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask        # Importation du module Flask

webapp = Flask(__name__)        # Création d'une nouvelle application
                                # Flask

@webapp.route("/")    # Chemin depuis la racine du site
                      # http://127.0.0.1:8080/webapp/   
         
def hello():          # Fonction qui sera appelée lorsque
                      # l'on accède au chemin indiqué dans    
                      # @webapp.route("/")    

     # Code renvoyé au navigateur                          
    return "Hello World from the webapp app!"  
    
@webapp.route("/blog/")

def blog():
    titre_h1="Mon voyage aux Etats-Unis"
    titres_h2=["Boston", "New-York City", "Pittsburgh"]
    textes=["Boston est la capitale et la principale ville de l'État du Massachusetts, au nord-est des États-Unis. Elle constitue le centre économique et culturel de la Nouvelle-Angleterre. La ville comptait 617 594 habitants (recensement fédéral de 2010), alors que la zone métropolitaine de Boston-Cambridge-Quincy concentrait environ 4 588 680 habitants, la dixième agglomération des États-Unis. Ses habitants s'appellent les Bostonien(ne)s.", "New York, officiellement City of New York, autrement connue sous les noms et abréviations de New York City ou NYC, est la plus grande ville des États-Unis et l'une des plus importantes du continent américain. Elle se situe dans le Nord-Est des États-Unis, sur la côte atlantique, à l'extrémité sud-est de l'État de New York. La ville de New York se compose de cinq arrondissements appelés boroughs : Manhattan, Brooklyn, Queens, le Bronx et Staten Island. Ses habitants s'appellent les New-Yorkais.", "Pittsburgh est la seconde plus grande ville du Commonwealth de Pennsylvanie, aux États-Unis. La ville est aussi le siège du comté d'Allegheny et fut longtemps un haut lieu de la sidérurgie mondiale et des chemins de fer. Lors du recensement de 2010, elle comptait 305 704 habitants, et l'agglomération 2 356 285 habitants, soit à la 27e place des États-Unis."]
    
    mapage = """
                   <!DOCTYPE html>
                <html>
                   <head>
                     <meta charset="utf-8" />
                     <title>Mon blog</title>
                   </head>

                   <body>
           """
    mapage += "<h1>"+titre_h1+"</h1>"

    for i in range(0,len(titres_h2)):
            mapage+="<h2>"+titres_h2[i]+"</h2>"
            mapage+="<p>"+textes[i]+"</p>"

    mapage+= """      
                   </body>
                 </html>
             """

    return mapage

if __name__ == '__main__':
    "Are we in the __main__ scope? Start test server."
    webapp.run()
