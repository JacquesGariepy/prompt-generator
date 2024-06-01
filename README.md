# Agent Autonome pour la Génération de Prompts

Ce projet utilise l'API OpenAI pour créer un agent autonome capable de générer et d'ajuster des prompts basés sur les demandes et les feedbacks des utilisateurs.

## Prérequis

- Python 3.7 ou supérieur
- La bibliothèque `openai`

## Installation

1. Clonez ce dépôt :

```bash
git clone <URL_DU_DÉPÔT>
cd <NOM_DU_RÉPERTOIRE>
```

2. Installez les dépendances nécessaires :

```bash
pip install openai
```

## Utilisation

1. Configurez votre clé API OpenAI en remplaçant `'sk-xxxxx'` dans le script par votre propre clé API.

2. Exécutez le script :

```bash
python agent_autonome.py
```

3. Suivez les instructions à l'écran pour entrer votre demande, fournir des feedbacks, et obtenir une réponse générée.

## Structure du Code

Le script définit une classe `AgentAutonome` avec les méthodes suivantes :

- `analyser_demande(demande)`: Analyse la demande de l'utilisateur pour comprendre les besoins et objectifs.
- `generer_prompt(analyse)`: Génère des prompts basés sur l'analyse des besoins de l'utilisateur.
- `ajuster_prompt(feedback)`: Ajuste les prompts en fonction des retours utilisateurs.
- `prompt_final(demande, analyse, prompt_initial, feedback)`: Traite la demande complète de l'utilisateur et retourne le prompt final ajusté.
- `traiter_demande(prompt_final)`: Traite la demande complète de l'utilisateur et retourne la réponse finale.

## Exemple d'Utilisation

Voici un exemple d'utilisation de l'agent autonome :

1. Analyser la demande utilisateur :

```python
demande = input("Veuillez entrer votre demande de création de prompt : ")
analyse = agent.analyser_demande(demande)
print("Analyse de la demande : ", analyse)
```

2. Générer le prompt initial :

```python
prompt_initial = agent.generer_prompt(analyse)
print("Prompt initial : ", prompt_initial)
```

3. Ajuster le prompt basé sur le feedback utilisateur :

```python
feedback = input("Veuillez entrer les feedbacks pour ajuster le prompt initial : ")
prompt_final = agent.prompt_final(demande, analyse, prompt_initial, feedback)
print("Prompt final ajusté : ", prompt_final)
```

4. Utiliser le prompt final pour générer une réponse :

```python
reponse = agent.traiter_demande(prompt_final)
print("Réponse finale générée : ", reponse)
```

## Contributions

Les contributions sont les bienvenues. Veuillez soumettre une pull request ou ouvrir une issue pour discuter des modifications.

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
