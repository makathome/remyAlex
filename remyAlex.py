import json
import os
import tkinter as tk
from tkinter import messagebox

# Funzione per cercare l'entry_id nel file
def find_entry_id(file_path):
    domain_to_search = "alexa_media"  # Dominio fisso
    try:
        # Verifica se il file esiste nel percorso
        if not os.path.exists(file_path):
            return "Percorso non trovato o accesso negato!"

        # Apri il file in modalità lettura
        with open(file_path, 'r', encoding='utf-8') as file:
            # Carica il contenuto del file come JSON
            config_data = json.load(file)
            
            # Cerca tra le voci per trovare il dominio specificato
            for entry in config_data.get("data", {}).get("entries", []):
                if entry.get("domain") == domain_to_search:
                    # Restituisce l'entry_id se trova il dominio
                    return entry.get("entry_id")
        
        # Se non trova nulla
        return None
    
    except FileNotFoundError:
        return "File non trovato!"
    except json.JSONDecodeError:
        return "Errore nel parsing del file JSON!"

# Funzione per generare l'output file
def generate_output_file(entry_id):
    output_content = f"""alias: alexa reload
description: ""
triggers:
  - minutes: /9
    trigger: time_pattern
conditions: []
actions:
  - action: homeassistant.reload_config_entry
    data:
      entry_id: {entry_id}
mode: single
"""
    # Salva l'output in un file nella directory corrente
    with open("automazione_alexa_reload.txt", "w", encoding="utf-8") as output_file:
        output_file.write(output_content)

# Funzione per mostrare un messaggio temporaneo
def show_temp_message(title, message, duration):
    # Crea una finestra di avviso temporanea
    temp_window = tk.Toplevel(root)
    temp_window.title(title)
    
    # Calcola la posizione per centrare la finestra
    temp_window.update_idletasks()  # Aggiorna per ottenere la dimensione corretta
    x = (temp_window.winfo_screenwidth() // 2) - (temp_window.winfo_width() // 2)
    y = (temp_window.winfo_screenheight() // 2) - (temp_window.winfo_height() // 2)
    temp_window.geometry(f"+{x}+{y}")  # Posiziona al centro

    label = tk.Label(temp_window, text=message, padx=20, pady=20)
    label.pack()
    # Chiude la finestra dopo 'duration' millisecondi
    temp_window.after(duration, temp_window.destroy)

# Funzione chiamata al clic del pulsante
def on_submit():
    ip_address = ip_entry.get().strip()
    port = port_entry.get().strip() or "8123"  # Usa 8123 se la porta non è specificata
    file_path = fr'\\{ip_address}\config\.storage\core.config_entries'

    # Informiamo l'utente che stiamo cercando l'entry_id
    show_temp_message("Informazione", "Sto cercando l'entry_id...", 2000)  # Mostra per 2 secondi

    # Chiama la funzione per trovare l'entry_id
    entry_id = find_entry_id(file_path)

    # Aspetta prima di mostrare il messaggio successivo
    root.after(2000, lambda: process_entry_id(entry_id))

# Funzione per elaborare l'entry_id e mostrare il messaggio finale
def process_entry_id(entry_id):
    if entry_id:
        # Entry ID trovato
        generate_output_file(entry_id)
        show_temp_message("Successo", "File 'automazione_alexa_reload.txt' generato con successo!", 3000)  # Mostra per 3 secondi
    else:
        # Nessun Entry ID trovato
        show_temp_message("Errore", "Nessun Entry ID trovato per il dominio 'alexa_media'", 2000)  # Mostra per 2 secondi

    # Chiude l'applicazione dopo un avviso finale
    root.after(4000, root.quit)  # Aspetta 4 secondi prima di chiudere

# Creazione della finestra principale
root = tk.Tk()
root.title("Trova Entry ID")

# Calcola la posizione per centrare la finestra principale
root.update_idletasks()  # Aggiorna per ottenere la dimensione corretta
x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
root.geometry(f"+{x}+{y}")  # Posiziona al centro

# Creazione dei widget
tk.Label(root, text="Inserisci l'IP del server di Home Assistant:").pack(pady=5)
ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=5)

tk.Label(root, text="Inserisci la porta (default: 8123):").pack(pady=5)
port_entry = tk.Entry(root, width=30)
port_entry.pack(pady=5)

submit_button = tk.Button(root, text="Cerca Entry ID", command=on_submit)
submit_button.pack(pady=20)

# Avvio della GUI
root.mainloop()
