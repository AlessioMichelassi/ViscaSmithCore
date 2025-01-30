A powerful yet easy-to-use VISCA over IP utility designed to simplify communication with cameras supporting the VISCA protocol. This library provides everything you need to send commands, manage responses, and handle retries over UDP, ensuring reliable camera control.

Key Features:

    Complete VISCA Support: Supports commands like Set, Inquiry, and more.
    Retry Mechanism: Ensures reliable message delivery over UDP with retransmissions.
    Extensible: Built with Python, easily adaptable for advanced use cases.
    Quick Start: Check example01 for a step-by-step implementation.

Whether you're controlling a physical camera or an emulated one, this utility makes the process seamless. Perfect for developers working on broadcasting, streaming, or robotics projects.

to use this library, you need to install the following dependencies:

pip install -r requirements.txt

There is a ton of documentation in the doc folder, so make sure to check it out!

# Changelog

Version 0.4.7
- fixed some bugs in the dictionary

Version 0.4.6
- Fixed Coherence name camelCase for all Function, snake_case for all variables

0.4.5 modifiche
- c'era un errore dovuto all'uso del vecchio dizionario dove i comandi era non nella forma white_balance_mode piuttosto che whiteBalanceMode. I nomi ora sono consistenti e sono stati testati tutti i comandi.

Versione 0.4.4
-E' stato sistemato l'errore che impediva di caricare correttamente il dizionario json.