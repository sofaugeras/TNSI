import os

def define_env(env):
    "Hook function"

    @env.macro
    def script(lang: str, nom: str, indentation=0, stop="") -> str:
        """Renvoie le script dans une balise bloc avec langage spécifié

        - lang: le nom du lexer pour la coloration syntaxique
        - nom: le chemin du script relativement au .md d'appel
        - indentation: nb d'espaces pour l'insertion dans un environnement
        - stop: si cette ligne est rencontrée, elle n'est pas affichée, ni la suite
        """
        # par Franck Chambon
        sortie = []
        with open("docs/" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"/{nom}", 'r') as f:
            for line in f.readlines():
                if line.upper().strip() == stop:
                    break
                nb_agc = 0 # nb accents graves consécutifs
                maxi_agc = 0
                for c in line:
                    if c == '`':
                        nb_agc += 1
                        if nb_agc > maxi_agc: maxi_agc = nb_agc
                    else:
                        nb_agc = 0
                sortie.append(" " * indentation + line)
        n = max(3, 1 + nb_agc)
        sortie = ["`" * n + lang + "\n"] + sortie
        sortie.append(" " * indentation + "`" * n + "\n")
        return "".join(sortie)


    @env.macro
    def py(nom: str, indentation=0, stop="") -> str:
        "macro python rapide"
        return script('python', nom + ".py", indentation, stop)

    @env.macro
    def py_sujet(nom: str, indentation=0, stop="# TESTS") -> str:
        "macro python rapide, pour un sujet sans les tests"
        return script('python', nom + ".py", indentation, stop)


    @env.macro
    def numworks():
        return f"""<iframe src="{env.variables.scripts_url}numworks/simulator.html" width="100%" height="500"></iframe>"""

    @env.macro
    def python_carnet(carnet: str = '', aux: str = '', module: str = '',
                      auxs=None, modules=None,
                      hauteur: int = 700,
                      chemin_relatif: bool = True,
                     ) -> str:
        """Renvoie du HTML pour embarquer un fichier `carnet.ipynb` dans un notebook
        + Basthon est la solution 2021, RGPD ok
        """

        if chemin_relatif:
            chemin = env.variables.site_url + os.path.dirname(env.variables.page.url.rstrip('/'))+'/'
        else:
            chemin = env.variables.scripts_url

        lien = f"https://notebook.basthon.fr/?"
        if carnet != '':
            lien += f"from={chemin}{carnet.lstrip('./')}&"
        else:
            lien += f"from={env.variables.scripts_url}py_vide.ipynb&"
        
        if aux != '':
            lien += f"aux={chemin}{aux.lstrip('./')}&"
        if auxs is not None:
            for aux in auxs:
                lien += f"aux={chemin}{aux.lstrip('./')}&"
        
        if module != '':
            lien += f"module={chemin}{module.lstrip('./')}&"
        if modules is not None:
            for module in modules:
                lien += f"module={chemin}{module.lstrip('./')}&"
        
        return f"<iframe src={lien} width=100% height={hauteur} onload=\"window.scrollTo({{ top: 0, behavior: 'smooth' }});\"></iframe>" + \
                f"[Lien dans une autre page]({lien}){{target=_blank}}"
    
    @env.macro
    def python_ide(script: str = '', aux: str = '', module: str = '',
                      auxs=None, modules=None,
                      hauteur: int = 700,
                      chemin_relatif: bool = True,
                     ) -> str:
        """Renvoie du HTML pour embarquer un fichier `script` dans une console
        + Basthon est la solution 2021, RGPD ok
        """

        if chemin_relatif:
            chemin = env.variables.site_url + os.path.dirname(env.variables.page.url.rstrip('/'))+'/'
        else:
            chemin = env.variables.scripts_url

        lien = f"https://console.basthon.fr/?"
        if script != '':
            lien += f"from={chemin}{script.lstrip('./')}&"
        else:
            lien += f"script=eJwDAAAAAAE"
        
        if aux != '':
            lien += f"aux={chemin}{aux.lstrip('./')}&"
        if auxs is not None:
            for aux in auxs:
                lien += f"aux={chemin}{aux.lstrip('./')}&"
        
        if module != '':
            lien += f"module={chemin}{module.lstrip('./')}&"
        if modules is not None:
            for module in modules:
                lien += f"module={chemin}{module.lstrip('./')}&"
        
        return f"<iframe src={lien} width=100% height={hauteur} onload=\"window.scrollTo({{ top: 0, behavior: 'smooth' }});\"></iframe>" + \
                f"[Lien dans une autre page]({lien}){{target=_blank}}"
    

    @env.macro
    def console(hauteur : int = 200) -> str:
        return "[Console pyodide, dernière en date](https://pyodide.org/en/stable/console.html){target=_blank}"


    env.variables['term_counter'] = 0
    env.variables['IDE_counter'] = 0
    INFTY_SYMBOL = '\u221e'
    from urllib.parse import unquote

    @env.macro
    def terminal() -> str:
        """   
        Purpose : Create a Python Terminal.
        Methods : Two layers to avoid focusing on the Terminal. 1) Fake Terminal using CSS 2) A click hides the fake 
        terminal and triggers the actual Terminal.
        """        
        tc = env.variables['term_counter']
        env.variables['term_counter'] += 1
        return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

    def read_ext_file(nom_script : str, path : str, filetype : str = 'py') -> str:
        """
        Purpose : Read a Python file that is uploaded on the server.
        Methods : The content of the file is hidden in the webpage. Replacing \n by a string makes it possible
        to integrate the content in mkdocs admonitions.
        """
        short_path = f"""docs/"""

        try: 
            if path == "":
                try : # base case 
                    f = open(f"""{short_path}/scripts/{nom_script}.{filetype}""")
                except : # minor subcase : .py directly in docs/ (should not happen...)
                    f = open(f"""{short_path}/{path}/{nom_script}.{filetype}""")
            else:
                f = open(f"""{short_path}/{path}/{nom_script}.{filetype}""")
            content = ''.join(f.readlines())
            f.close()
            content = content + "\n"
            # Hack to integrate code lines in admonitions in mkdocs
            # change backslash_newline by backslash-newline
            return content.replace('\n','bksl-nl').replace('_','py-und').replace('*','py-str')
        except :
            print("The file you're looking for is not where you say it is !")
            return
        
    def generate_content(nom_script : str, path : str, filetype : str = 'py') -> str:
        """
        Purpose : Return content and current number IDE {tc}.
        """
        tc = env.variables['IDE_counter']
        env.variables['IDE_counter'] += 1

        content = read_ext_file(nom_script, path, filetype)

        if content is not None :
            return content, tc
        else : return "", tc

    def create_upload_button(tc : str) -> str:
        """
        Purpose : Create upoad button for a IDE number {tc}.
        Methods : Use an HTML input to upload a file from user. The user clicks on the button to fire a JS event
        that triggers the hidden input.
        """
        path_img = convert_url_to_utf8(env.variables.page.abs_url).split('/')[1]
        return f"""<button class="tooltip" onclick="document.getElementById('input_editor_{tc}').click()"><img src="/{path_img}/images/buttons/icons8-upload-64.png"><span class="tooltiptext">Téléverser</span></button>\
                <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""

    def create_unittest_button(tc: str, nom_script: str, path : str, mode: str, MAX : int = 5) -> str:
        """
        Purpose : Generate the button for IDE {tc} to perform the unit tests if a valid test_script.py is present.
        Methods : Hide the content in a div that is called in the Javascript
        """
        stripped_nom_script = nom_script.split('/')[-1]
        relative_path = '/'.join(nom_script.split('/')[:-1])
        nom_script = f"{relative_path}/{stripped_nom_script}_test"
        content = read_ext_file(nom_script, path)
        if content is not None: 
            path_img = env.variables.page.url.split('/')[1]
            return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span>\
                <button class="tooltip" onclick=\'executeTest("{tc}","{mode}")\'>\
                <img src="/images/buttons/icons8-check-64.png">\
                <span class="tooltiptext">Valider</span></button><span class="compteur">\
                {MAX}/{MAX}\
                </span>"""
        else: 
            return ''


    def blank_space(s=0.3) -> str:
        """ 
        Purpose : Return 5em blank spaces. Use to spread the buttons evenly
        """
        # return f"""<span style="indent-text:{s}em"> </span>"""
        return f"""<span style="display: inline-block; width:{s}em"></span>"""

    def get_max_from_file(content : str) -> tuple:#[str, int]: # compatibilité Python antérieur 3.8
        split_content = content.split('bksl-nl')
        max_var = split_content[0]
        if max_var[:4] != "#MAX":
            MAX = 5 
        else:
            value = max_var.split('=')[1].strip()
            MAX = int(value) if value not in ['+', 1000] else INFTY_SYMBOL
            i = 1
            while split_content[i] == '':
                i += 1
            content = 'bksl-nl'.join(split_content[i:])
        return content, MAX

    def test_style(nom_script : str, element : str) -> bool:
        guillemets = ["'", '"']
        ide_style = ["", "v"]
        styles = [f"""IDE{istyle}({i}{nom_script}{i}""" for i in guillemets for istyle in ide_style]
        return any([style for style in styles if style in element])

    def convert_url_to_utf8(nom : str) -> str:
        return unquote(nom, encoding='utf-8')
        

    @env.macro
    def IDEv(nom_script : str = '', MAX : int = 5, SANS : str = "") -> str:
        """
        Purpose : Easy macro to generate vertical IDE in Markdown mkdocs.
        Methods : Fire the IDE function with 'v' mode.
        """
        return IDE(nom_script, mode = 'v', MAX = MAX, SANS = SANS)

    @env.macro
    def IDE(nom_script : str = '', mode : str = 'h', MAX : int = 5, SANS : str = "") -> str:
        """
        Purpose : Create an IDE (Editor+Terminal) on a Mkdocs document. {nom_script}.py is loaded on the editor if present. 
        Methods : Two modes are available : vertical or horizontal. Buttons are added through functional calls.
        Last span hides the code content of the IDE if loaded.
        """
        path_img = convert_url_to_utf8(env.variables.page.abs_url).split('/')[1]

        path_file = '/'.join(filter(lambda folder: folder != "", convert_url_to_utf8(env.variables.page.abs_url).split('/')[2:-2]))
        content, tc = generate_content(nom_script, path_file)

        try:
            f = open(f"docs/{path_file}/clef.txt", "r", encoding="utf8")
            clef = f.read()            
        except: 
            clef = "" # base case -> no clef.txt file

        content, max_from_file = get_max_from_file(content)
        MAX = max_from_file if MAX == 5 else MAX
        MAX = MAX if MAX not in ['+', 1000] else INFTY_SYMBOL
        corr_content, tc = generate_content(f"""{'/'.join(nom_script.split('/')[:-1])}/{nom_script.split('/')[-1]}_corr""", path_file)
        div_edit = f'<div class="ide_classe" data-max={MAX} data-exclude={"".join(SANS.split(" "))+"eval,exec"} >'

        if mode == 'v':
            div_edit += f'<div class="wrapper"><div class="interior_wrapper"><div id="editor_{tc}"></div></div><div id="term_editor_{tc}" class="term_editor"></div></div>'
        else:
            div_edit += f'<div class="wrapper_h"><div class="line" id="editor_{tc}"></div><div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div>'

        div_edit += f"""<button class="tooltip" onclick='interpretACE("editor_{tc}","{mode}")'><img src="/{path_img}/images/buttons/icons8-play-64.png"><span class="tooltiptext">Lancer</span></button>"""
        div_edit += create_unittest_button(tc, nom_script, path_file, mode, MAX) 
        div_edit += f"""{blank_space(1)}<button class="tooltip" onclick=\'downloadFile("editor_{tc}","{nom_script}")\'><img src="/{path_img}/images/buttons/icons8-download-64.png"><span class="tooltiptext">Télécharger</span></button>{blank_space()}"""
        div_edit += create_upload_button(tc) 
        div_edit += f"""{blank_space(1)}<button class="tooltip" onclick=\'reload("{tc}","content")\'><img src="/{path_img}/images/buttons/icons8-restart-64.png"><span class="tooltiptext">Recharger</span></button>{blank_space()}"""
        div_edit += f"""<button class="tooltip" onclick=\'saveEditor("{tc}","content")\'><img src="/{path_img}/images/buttons/icons8-save-64.png"><span class="tooltiptext">Sauvegarder</span></button>"""
        div_edit += '</div>'

        div_edit += f"""<span id="content_editor_{tc}" class="hide">{content}</span>"""
        div_edit += f"""<span id="corr_content_editor_{tc}" class="hide" data-strudel="{str(clef)}">{corr_content}</span>"""
        
        elt_insertion = [elt for elt in env.page.markdown.split("\n") if test_style(nom_script, elt)]
        elt_insertion = elt_insertion[0] if len(elt_insertion) >=1 else ""
        indent = " "*(len(elt_insertion) - len(elt_insertion.lstrip()))
        if nom_script == '' : indent = " "  # to avoid conflict with empty IDEs
        if indent == "":
            div_edit += f'''
{indent}--8<--- "docs/xtra/start_REM.md"
'''
        div_edit += f'''
{indent}--8<--- "docs/{path_file if path_file != "" else 'scripts'}/{nom_script}_REM.md"''' if clef == "" else f""
        if indent == "":
            div_edit += f'''
{indent}--8<--- "docs/xtra/end_REM.md"
'''
        return div_edit
        
    @env.macro
    def mult_col(*text):
        cmd = """<table style="border-color:transparent;background-color:transparent"><tr>"""
        for column in text:
            cmd += f"""<td><b style="font-size:1.2em">{column}</td>"""
        cmd += f"""</tr></table>"""
        return cmd

    @env.macro
    def affiche_addition(x, y):
        texte = []
        texte.append("Voici une addition")
        texte.append("")
        texte.append(f"{x} + {y} = {x + y}")
        texte.append("")
        texte.append("Avec LaTeX")
        texte.append("")
        texte.append(f"$${x} + {y} = {x + y}$$")
        return "\n".join(texte)
