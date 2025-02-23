import re

def verifica_factura(cale_fisier):
    errors = []
    
    client_re = r"^client: [A-Za-z ]+$"
    email_re = r"^email: [\w.-]+@[a-zA-Z-]+\.[a-zA-Z]{2,}$"
    produs_re = r"^produs: [\w ]+$"
    pret_re = r"^pret: \d+(\.\d{2})?$"
    tva_re = r"^TVA: (0|5|19)%$"
    cantitate_re = r"^cantitate: \d+$"
    
    try:
        with open(cale_fisier, 'r', encoding='utf-8') as f:
            factura_text = f.read()
        
        
        client_matches = re.findall(client_re, factura_text, re.MULTILINE)
        if len(client_matches) > 1:
            errors.append("Error: 'client' apare de mai multe ori")
        elif len(client_matches) == 0:
            errors.append("Error: 'client' lipseste")
        
        
        email_matches = re.findall(email_re, factura_text, re.MULTILINE)
        if len(email_matches) != 1:
            errors.append("Error: 'email' apare de mai multe ori" if len(email_matches) > 1 else "Error: 'email' lipseste")
        else:
            if not re.match(email_re, email_matches[0]):
                errors.append("Error: 'email' are un format incorect")


        produse_matches = re.findall(produs_re, factura_text, re.MULTILINE)
        if not produse_matches:
            errors.append("Error: Nu exista produse")
        
        
        pret_matches = re.findall(pret_re, factura_text, re.MULTILINE)
        if len(pret_matches) < len(produse_matches):
            errors.append("Error: Produse cu pret invalid")
        elif len(pret_matches) > len(produse_matches):
            errors.append("Error: Sunt mai multe preturi decât produse")
        
       
        tva_matches = re.findall(tva_re, factura_text, re.MULTILINE)
        if len(tva_matches) < len(produse_matches):
            errors.append("Error: Produse cu TVA invalid ")
        elif len(tva_matches) > len(produse_matches):
            errors.append("Error: Sunt mai multe valori TVA decat produse")
        
       
        cantitate_matches = re.findall(cantitate_re, factura_text, re.MULTILINE)
        if len(cantitate_matches) < len(produse_matches):
            errors.append("Error: Produse cu cantitate invalida")
        elif len(cantitate_matches) > len(produse_matches):
            errors.append("Error: Sunt mai multe cantitati decat produse")
        
        
        if errors:
            print("Erori gasite în factura:")
            for error in errors:
                print(" -", error)
        else:
            print("Factura respecta formatul specificat.")
    except FileNotFoundError:
        print("Error: Fisierul nu a fost gasit.")
    except Exception as e:
        print(f"Error: {e}")



cale_fisier = input("Introduceti calea: ")
verifica_factura(cale_fisier)


#  C:\Users\Lenovo\Desktop\Limbaje\lab2\ex4\factura.txt
