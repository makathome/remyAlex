# remyAlex 1.0

**remyAlex** è un semplice strumento progettato per facilitare la gestione dell'integrazione **alexa_media_player** su Home Assistant. Negli ultimi tempi, questa integrazione ha riscontrato problemi di stabilità,oltre che necessitare di reinstallazione (semplice rimozione) richiede un riavvio manuale ogni 10 minuti per funzionare in maniera stabile RemyAlex ti aiuta in fase di reinstallazione, in quanto l'id dell'integrazione cambierà e bisognerà aggiornare l'automazione con l'id corrispondente, basterà copiare l'automazione creata e sostituirla con la vecchia automazione, o semplicemente sostituire il vecchio id con quello nuovo.

## Funzionalità principali:

- **Ricerca Automatica dell'ID**: Il programma identifica automaticamente l'ID dell'integrazione **alexa_media_player** necessario per ricaricare il componente.
- **Generazione Automazione**: Una volta trovato l'ID, il programma crea un file di testo contenente l'automazione per riavviare il componente ogni 10 minuti.
- **Interfaccia Grafica Intuitiva**: L'utente può facilmente inserire l'indirizzo IP e la porta del server Home Assistant senza bisogno di competenze tecniche.

Con remyAlex, l'integrazione diventerà più stabile, ma richiederà la reinstallazione ogni volta che il componente darà problemi. Leggi sotto per ulteriori dettagli.

## Requisiti

assicurati di soddisfare i seguenti requisiti:

- **Sistema Operativo**: Windows
- **Installazione di Home Assistant**: È necessario avere Home Assistant correttamente installato e funzionante.
- **Connessione al Server**: Conoscere esattamente l'indirizzo IP del server Home Assistant e la porta utilizzata per il collegamento.
- **Samba**: Devi avere installato il componente aggiuntivo Samba su Home Assistant. Puoi farlo seguendo la [guida qui](https://domhouse.it/installare-samba-su-home-assistant). Per installare Samba, vai su **Impostazioni > Componenti Aggiuntivi > Samba Share**.

