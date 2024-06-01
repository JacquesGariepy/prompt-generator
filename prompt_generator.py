from openai import OpenAI
client = OpenAI(api_key='sk-xxxxx')

# Définition de la classe AgentAutonome
class AgentAutonome:
    def __init__(self, model_name='gpt-4o'):
        self.model_name = model_name
    
    def analyser_demande(self, demande):
        """
        Analyse la demande de l'utilisateur pour comprendre les besoins et objectifs.
        """
        analyse_prompt = f"Analyse la demande suivante et identifie les besoins et objectifs : {demande}"
        
        messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": analyse_prompt},
        ]
        analyse_resultat = client.chat.completions.create(model=self.model_name, messages=messages)
        return analyse_resultat.choices[0].message.content
        #return analyse_resultat['choices'][0]['message']['content'].strip()
    
    def generer_prompt(self, analyse):
        """
        Génère des prompts basés sur l'analyse des besoins de l'utilisateur.
        """
        generation_prompt = f"Génère un prompt pour répondre aux besoins suivants : {analyse}"
        messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": generation_prompt},
        ]
        analyse_resultat = client.chat.completions.create(model=self.model_name, messages=messages)
        return analyse_resultat.choices[0].message.content
        #return analyse_resultat['choices'][0]['message']['content'].strip()
    
    def ajuster_prompt(self, feedback):
        """
        Ajuste les prompts en fonction des retours utilisateurs.
        """
        ajustement_prompt = f"Voici le feedback utilisateur : {feedback}. Ajuste le prompt pour mieux répondre aux besoins."
        messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": ajustement_prompt},
        ]
        analyse_resultat = client.chat.completions.create(model=self.model_name, messages=messages)
        return analyse_resultat.choices[0].message.content
        #return analyse_resultat['choices'][0]['message']['content'].strip()

    def prompt_final(self, demande, analyse, prompt_initial, feedback):
        """
        Traite la demande complète de l'utilisateur et retourne le prompt final.
        """
        requete = f"Traite la demande suivante : {demande}. Analyse : {analyse}. Prompt initial : {prompt_initial}. Feedback : {feedback}"
        _prompt_final = self.ajuster_prompt(requete)
        
        return _prompt_final
    
    def traiter_demande(self, prompt_final):
        """
        Traite la demande complète de l'utilisateur et retourne le prompt final.
        """
        messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt_final},
        ]
        reponse_final = client.chat.completions.create(model=self.model_name, messages=messages)
        return reponse_final.choices[0].message.content

# Exemple d'utilisation de l'agent autonome
agent = AgentAutonome()

# Étape 1 : Analyser la demande utilisateur
demande = input("Veuillez entrer votre demande de création de prompt : ")
print("Demande initiale : ", demande)

analyse = agent.analyser_demande(demande)
print("Analyse de la demande : ", analyse)

# Étape 2 : Générer le prompt initial
prompt_initial = agent.generer_prompt(analyse)
print("Prompt initial : ", prompt_initial)

# Étape 3 : Ajuster le prompt basé sur le feedback utilisateur
feedback = input("Veuillez entrer les feedbacks pour ajuster le prompt initial : ")
prompt_final = agent.prompt_final(demande, analyse, prompt_initial, feedback)
print("Prompt final ajusté : ", prompt_final)

# Étape 4 : Utiliser le prompt final pour générer une réponse
reponse = agent.traiter_demande(prompt_final)
print("Réponse finale générée : ", reponse)


