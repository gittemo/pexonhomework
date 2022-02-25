# Pexonhomework von Jonan

Hier sind meine L�sungen zu diesen Aufgaben https://pexon.atlassian.net/wiki/spaces/PXP/pages/213025867/Homework

## Task 1
In dem t1 Ordner findet sich die Flask API sowie die pipenv-generierten Dateien und die requirements.

## Task 2
In t2(docker) befindet sich nur das von mir genutze Volume, wo sich die PostgreSQL Datenbank befindet. Image: https://hub.docker.com/_/postgres

## Task 3
Um den Inhalt von t3 zu nutzen, m�sste man 
1. Ansible installieren (apt install ansible)
2. In `hosts` die IP auf die eigene VM �ndern
3. In `ansible.cfg` den Pfad zum private key �ndern

## Task 4
F�r die Azure Aufgabe habe ich die App aus Task 1 modifiziert, damit sich einfacher ein Dockerimage bauen l�sst. Die App findet sich in t1.1. Mein dev.azure.com Projekt ist privat, denn Microsoft bietet �ffentlichen Projekten keine kostenlose Rechenleistung mehr an. Das Image ist in einer Azure Container Instance deponiert und kann jederzeit in einer Azure Container Instance gestartet werden. 