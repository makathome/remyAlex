# RemyAlex 1.0

**RemyAlex** è un semplice strumento progettato per facilitare la gestione dell'integrazione **alexa_media_player** su Home Assistant. Negli ultimi tempi, questa integrazione ha riscontrato problemi di stabilità, richiedendo un riavvio manuale ogni 10 minuti. RemyAlex automatizza questo processo.

## Funzionalità principali:

- **Ricerca Automatica dell'ID**: Il programma identifica automaticamente l'ID dell'integrazione **alexa_media_player** necessario per ricaricare il componente.
- **Generazione Automazione**: Una volta trovato l'ID, il programma crea un file di testo contenente l'automazione per riavviare il componente ogni 10 minuti.
- **Interfaccia Grafica Intuitiva**: L'utente può facilmente inserire l'indirizzo IP e la porta del server Home Assistant senza bisogno di competenze tecniche.

Con RemyAlex, l'integrazione diventerà più stabile, ma richiederà la reinstallazione ogni volta che il componente darà problemi. Leggi sotto per ulteriori dettagli.

## Requisiti

Per utilizzare RemyAlex, assicurati di soddisfare i seguenti requisiti:

- **Sistema Operativo**: Windows
- **Installazione di Home Assistant**: È necessario avere Home Assistant correttamente installato e funzionante.
- **Connessione al Server**: Conoscere esattamente l'indirizzo IP del server Home Assistant e la porta utilizzata per il collegamento.
- **Samba**: Devi avere installato il componente aggiuntivo Samba su Home Assistant. Puoi farlo seguendo la [guida qui](https://domhouse.it/installare-samba-su-home-assistant). Per installare Samba, vai su **Impostazioni > Componenti Aggiuntivi > Samba Share**.

