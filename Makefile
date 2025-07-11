# Makefile pour Manim - Gestion de plusieurs projets vidéo
# Usage: make render PROJECT=nom_du_projet QUALITY=qualité
# Exemple: make render PROJECT=signalr QUALITY=1080p60

# Variables par défaut
PROJECT ?= signalr
QUALITY ?= l
SCENE ?= 

# Répertoires
VIDEOS_DIR = videos
PROJECT_DIR = $(VIDEOS_DIR)/$(PROJECT)
PROJECT_FILE = $(PROJECT_DIR)/$(PROJECT).py
MEDIA_OUTPUT = $(PROJECT_DIR)/media/videos/$(PROJECT)

# Qualités disponibles (codes Manim)
# l = low quality (480p15)
# m = medium quality (720p30) 
# h = high quality (1080p60)
# p = production quality (1440p60)
# k = 4k quality (2160p60)
QUALITIES = l m h p k

# Couleurs pour l'affichage
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

.PHONY: help render preview clean list-projects list-qualities show-config

# Cible par défaut
help:
	@echo -e "$(GREEN)Makefile pour Manim - Gestion de projets vidéo$(NC)"
	@echo ""
	@echo -e "$(YELLOW)Usage:$(NC)"
	@echo "  make render PROJECT=nom_du_projet QUALITY=qualité [SCENE=nom_de_la_scene]"
	@echo ""
	@echo -e "$(YELLOW)Exemples:$(NC)"
	@echo "  make render PROJECT=signalr QUALITY=h"
	@echo "  make render PROJECT=signalr QUALITY=l SCENE=IntroScene"
	@echo "  make preview PROJECT=signalr"
	@echo ""
	@echo -e "$(YELLOW)Commandes disponibles:$(NC)"
	@echo "  render          - Rendu de la vidéo"
	@echo "  preview         - Aperçu rapide (qualité l)"
	@echo "  hq              - Haute qualité (qualité h)"
	@echo "  clean           - Nettoie les fichiers générés"
	@echo "  list-projects   - Liste les projets disponibles"
	@echo "  list-qualities  - Liste les qualités disponibles"
	@echo "  show-config     - Affiche la configuration actuelle"
	@echo "  help            - Affiche cette aide"

# Vérification de l'existence du projet
check-project:
	@if [ ! -d "$(PROJECT_DIR)" ]; then \
		echo -e "$(RED)Erreur: Le projet '$(PROJECT)' n'existe pas dans $(VIDEOS_DIR)/$(NC)"; \
		echo -e "$(YELLOW)Projets disponibles:$(NC)"; \
		make list-projects; \
		exit 1; \
	fi
	@if [ ! -f "$(PROJECT_FILE)" ]; then \
		echo -e "$(RED)Erreur: Le fichier '$(PROJECT).py' n'existe pas dans $(PROJECT_DIR)/$(NC)"; \
		exit 1; \
	fi

# Vérification de la qualité
check-quality:
	@if ! echo "$(QUALITIES)" | grep -q "$(QUALITY)"; then \
		echo -e "$(RED)Erreur: Qualité '$(QUALITY)' non supportée$(NC)"; \
		echo -e "$(YELLOW)Qualités disponibles:$(NC)"; \
		make list-qualities; \
		exit 1; \
	fi

# Configuration de l'environnement Python
setup-env:
	@echo -e "$(GREEN)Configuration de l'environnement Python...$(NC)"
	@if [ ! -f "requirements.txt" ]; then \
		echo -e "$(YELLOW)Attention: requirements.txt non trouvé$(NC)"; \
	fi

# Rendu principal
render: check-project check-quality setup-env
	@echo -e "$(GREEN)Rendu du projet: $(PROJECT) en qualité $(QUALITY)$(NC)"
	@echo -e "$(YELLOW)Fichier source: $(PROJECT_FILE)$(NC)"
	@echo -e "$(YELLOW)Sortie: $(MEDIA_OUTPUT)$(NC)"
	@cd $(PROJECT_DIR) && \
	export PYTHONPATH="$(shell pwd):$$PYTHONPATH" && \
	if [ -n "$(SCENE)" ]; then \
		echo -e "$(GREEN)Rendu de la scène: $(SCENE)$(NC)"; \
		manim -q$(QUALITY) $(PROJECT).py $(SCENE); \
	else \
		echo -e "$(GREEN)Rendu de toutes les scènes$(NC)"; \
		manim -q$(QUALITY) $(PROJECT).py; \
	fi
	@echo -e "$(GREEN)Rendu terminé!$(NC)"

# Aperçu rapide en basse qualité
preview: 
	@$(MAKE) render PROJECT=$(PROJECT) QUALITY=l SCENE=$(SCENE)

# Rendu en haute qualité
hq:
	@$(MAKE) render PROJECT=$(PROJECT) QUALITY=h SCENE=$(SCENE)

# Nettoyage des fichiers générés
clean: check-project
	@echo -e "$(YELLOW)Nettoyage des fichiers générés pour le projet $(PROJECT)...$(NC)"
	@if [ -d "$(PROJECT_DIR)/media" ]; then \
		rm -rf $(PROJECT_DIR)/media/videos/$(PROJECT); \
		rm -rf $(PROJECT_DIR)/media/images/$(PROJECT); \
		rm -rf $(PROJECT_DIR)/media/texts; \
		echo -e "$(GREEN)Fichiers de $(PROJECT) nettoyés$(NC)"; \
	else \
		echo -e "$(YELLOW)Aucun fichier à nettoyer pour $(PROJECT)$(NC)"; \
	fi

# Nettoyage complet
clean-all:
	@echo -e "$(YELLOW)Nettoyage complet de tous les projets...$(NC)"
	@find $(VIDEOS_DIR) -name "media" -type d -exec rm -rf {} + 2>/dev/null || true
	@find $(VIDEOS_DIR) -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo -e "$(GREEN)Nettoyage complet terminé$(NC)"

# Liste des projets disponibles
list-projects:
	@echo -e "$(GREEN)Projets disponibles:$(NC)"
	@for dir in $(VIDEOS_DIR)/*/; do \
		if [ -d "$$dir" ] && [ "$$(basename "$$dir")" != "__pycache__" ]; then \
			project=$$(basename "$$dir"); \
			if [ -f "$$dir/$$project.py" ]; then \
				echo -e "  - $$project $(GREEN)✓$(NC)"; \
			else \
				echo -e "  - $$project $(RED)✗ (pas de fichier .py)$(NC)"; \
			fi; \
		fi; \
	done

# Liste des qualités disponibles
list-qualities:
	@echo -e "$(GREEN)Qualités disponibles:$(NC)"
	@echo -e "  - l  (low quality - 480p15)"
	@echo -e "  - m  (medium quality - 720p30)"
	@echo -e "  - h  (high quality - 1080p60)"
	@echo -e "  - p  (production quality - 1440p60)"
	@echo -e "  - k  (4k quality - 2160p60)"

# Affichage de la configuration actuelle
show-config:
	@echo -e "$(GREEN)Configuration actuelle:$(NC)"
	@echo -e "  Projet: $(YELLOW)$(PROJECT)$(NC)"
	@echo -e "  Qualité: $(YELLOW)$(QUALITY)$(NC)"
	@echo -e "  Scène: $(YELLOW)$(if $(SCENE),$(SCENE),toutes)$(NC)"
	@echo -e "  Répertoire du projet: $(YELLOW)$(PROJECT_DIR)$(NC)"
	@echo -e "  Fichier source: $(YELLOW)$(PROJECT_FILE)$(NC)"
	@echo -e "  Sortie vidéo: $(YELLOW)$(MEDIA_OUTPUT)$(NC)"

# Ouverture du dossier de sortie
open-output: check-project
	@if [ -d "$(PROJECT_DIR)/media" ]; then \
		echo -e "$(GREEN)Ouverture du dossier de sortie...$(NC)"; \
		xdg-open "$(PROJECT_DIR)/media" 2>/dev/null || open "$(PROJECT_DIR)/media" 2>/dev/null || echo -e "$(YELLOW)Impossible d'ouvrir le dossier automatiquement$(NC)"; \
	else \
		echo -e "$(RED)Le dossier de sortie n'existe pas encore$(NC)"; \
	fi

# Surveillance et rendu automatique lors de modifications
watch: check-project
	@echo -e "$(GREEN)Surveillance du fichier $(PROJECT_FILE)...$(NC)"
	@echo -e "$(YELLOW)Appuyez sur Ctrl+C pour arrêter$(NC)"
	@while true; do \
		inotifywait -q -e modify "$(PROJECT_FILE)" 2>/dev/null && \
		echo -e "$(GREEN)Fichier modifié, nouveau rendu...$(NC)" && \
		$(MAKE) preview PROJECT=$(PROJECT) SCENE=$(SCENE); \
	done || echo -e "$(RED)inotifywait non disponible. Installez inotify-tools pour cette fonctionnalité$(NC)"

# Installation des dépendances
install-deps:
	@echo -e "$(GREEN)Installation des dépendances...$(NC)"
	@if [ -f "requirements.txt" ]; then \
		pip install -r requirements.txt; \
	else \
		pip install manim; \
	fi

# Création d'un nouveau projet
new-project:
	@if [ -z "$(NAME)" ]; then \
		echo -e "$(RED)Erreur: Spécifiez le nom du projet avec NAME=nom_du_projet$(NC)"; \
		exit 1; \
	fi
	@if [ -d "$(VIDEOS_DIR)/$(NAME)" ]; then \
		echo -e "$(RED)Erreur: Le projet $(NAME) existe déjà$(NC)"; \
		exit 1; \
	fi
	@echo -e "$(GREEN)Création du nouveau projet: $(NAME)$(NC)"
	@mkdir -p "$(VIDEOS_DIR)/$(NAME)"
	@touch "$(VIDEOS_DIR)/$(NAME)/$(NAME).py"
	@touch "$(VIDEOS_DIR)/$(NAME)/script.md"
	@echo -e "$(GREEN)Projet $(NAME) créé avec succès!$(NC)"
	@echo -e "$(YELLOW)Fichiers créés:$(NC)"
	@echo "  - $(VIDEOS_DIR)/$(NAME)/$(NAME).py"
	@echo "  - $(VIDEOS_DIR)/$(NAME)/script.md"
