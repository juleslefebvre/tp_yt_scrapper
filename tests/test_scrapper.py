from parse import *

video1 = get_soup("fmsoym8I-3o")
video2 = get_soup("ciXIQk7s_QU")
video3 = get_soup("o16h6voegFU")
video4 = get_soup("VaGYUhKDtVM")

def test_parse_video_return():
        # Test if the function returns a dict
        assert type(parse_video("fmsoym8I-3o")) == dict

def test_scrap_title():
        # Test if the function returns the right title
        assert scrap_title(video1) == "Pierre Niney : L’interview face cachée par HugoDécrypte"

def test_scrap_author():
        # Test if the function returns the right author
        assert scrap_author(video1) == "HugoDécrypte"

def test_scrap_empty_description():
        # Test if the function returns "No description available" if it's the case
        assert scrap_description(video2)== "No description available"

def test_scrap_empty_links():
        # Test if the function returns nothing if ther is no link
        assert scrap_links(video3) == []

def test_scrap_desription():
    # Test if the function returns the right description
        assert scrap_description(video1) == "🍿 L'acteur Pierre Niney est dans L’interview face cachée ! Ces prochains mois, le format revient plus fort avec des artistes, sportifs, etc.\\n🔔 Abonnez-vous pour ne manquer aucune vidéo.\\n\\nInterview réalisée à l’occasion de la sortie du film « Mascarade » réalisé par Nicolas Bedos, le 1er novembre 2022 au cinéma. Avec Pierre Niney, Isabelle Adjani, François Cluzet, Marine Vacth.\\n\\nChaleureux remerciements au cinéma mk2 Bibliothèque pour son accueil.\\n\\n—\\n\\n00:00 Intro\\n00:22 1\\n03:32 2\\n10:11 3\\n14:09 4\\n17:28 5\\n20:10 6\\n23:13 7\\n39:22 8\\n\\n—\\n\\nPrésenté par Hugo Travers\\n\\nRéalisateur : Julien Potié\\nJournalistes : Benjamin Aleberteau, Blanche Vathonne\\n\\nChargée de production déléguée : Romane Meissonnier\\nAssistant de production déléguée : Clément Chaulet\\nChargée de production exécutive : Marie Delvallée\\n\\nChef OPV : Lucas Stoll\\nOPV : Pierre Amilhat, Vanon Borget\\nElectricien : Alex Henry\\nChef OPS : Victor Arnaud\\nStagiaire image : Magali Faizeau\\n\\nMaquilleuse : Kim Desnoyers\\nPhotographe plateau : Erwann Tanguy\\n\\nMonteur-étalonneur : Stan Duplan\\nMixeuse : Romane Meissonnier\\n\\nCheffe de projets partenariats : Mathilde Rousseau\\nAssistante cheffe de projets partenariats : Manon Montoriol\\n\\n—\\n\\n© HugoDécrypte / 2022"

def test_scrap_links():
    # Test if the function returns the right links
        assert scrap_links(video4) == [
            "http://www.facebook.com/goldenmoustache",
            "http://www.twitter.com/goldenmoustache",
            "http://www.youtube.com/goldenmoustachevideo",
            "http://www.dailymotion.com/GoldenMoustache",
            "http://www.instagram.com/goldenmoustacheoff",
            "http://www.snapchat.com/add/goldenmousnap"
        ]

def test_scrap_timestamp():
    # Test if the function returns the right timestamp
        assert scrap_links(video1) == [
                "https://youtube.com/watch?v=fmsoym8I-3o&t=0s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=22s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=212s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=611s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=849s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=1048s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=1210s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=1393s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=2362s"
        ]

def test_scrap_likes():
    # Test if the function returns the right amount of likes
    assert scrap_likes(video2) == "10 clics"




test_parse_video_return()
test_scrap_title()
test_scrap_author()
test_scrap_empty_description()
test_scrap_empty_links()
test_scrap_desription()
test_scrap_links()
test_scrap_timestamp()
test_scrap_likes()