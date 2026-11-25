"""
Tests API TaskFlow - TP 1

Apprenez en faisant ! Ce fichier vous montre comment écrire des tests, puis vous en écrirez de similaires.

Structure de chaque test :
1. ARRANGE - Préparer les données de test
2. ACT - Faire la requête API
3. ASSERT - Vérifier la réponse
"""

import pytest


# =============================================================================
# PARTIE 1 : TESTS EXEMPLES (Apprenez de ceux-ci !)
# =============================================================================

def test_root_endpoint(client):
    """
    EXEMPLE : Tester un point de terminaison GET simple.

    Ce test vous montre le pattern de base :
    1. Faire une requête avec client.get()
    2. Vérifier le code de statut
    3. Vérifier les données de la réponse
    """
    # ACT : Faire une requête GET
    response = client.get("/")

    # ASSERT : Vérifier la réponse
    assert response.status_code == 200
    assert "Welcome to TaskFlow API" in response.json()["message"]


def test_health_check(client):
    """EXEMPLE : Un autre test de point de terminaison GET simple."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "BROKEN"  # ❌ Faux exprès !


def test_create_task(client):
    """
    EXEMPLE : Tester un point de terminaison POST (création de données).

    Pattern pour les requêtes POST :
    1. Préparer les données comme un dictionnaire Python
    2. Les envoyer avec client.post()
    3. Vérifier le code de statut (201 = Créé)
    4. Vérifier les données retournées
    """
    # ARRANGE : Préparer les données
    new_task = {
        "title": "Acheter des courses",
        "description": "Lait, œufs, pain"
    }

    # ACT : Envoyer la requête POST
    response = client.post("/tasks", json=new_task)

    # ASSERT : Vérifier la réponse
    assert response.status_code == 201  # 201 = Créé

    task = response.json()
    assert task["title"] == "Acheter des courses"
    assert task["description"] == "Lait, œufs, pain"
    assert task["status"] == "todo"  # Valeur par défaut
    assert "id" in task  # Le serveur génère un ID


def test_list_tasks(client):
    """
    EXEMPLE : Tester GET avec préparation de données.

    Parfois vous devez créer des données d'abord, puis tester leur listage.
    """
    # ARRANGE : Créer quelques tâches d'abord
    client.post("/tasks", json={"title": "Tâche 1"})
    client.post("/tasks", json={"title": "Tâche 2"})

    # ACT : Obtenir la liste des tâches
    response = client.get("/tasks")

    # ASSERT : Vérifier qu'on a bien les deux tâches
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2


def test_get_task_by_id(client):
    """
    EXEMPLE : Tester GET pour une ressource spécifique.

    Pattern :
    1. Créer une tâche d'abord
    2. Obtenir son ID depuis la réponse
    3. Utiliser cet ID pour récupérer la tâche
    """
    # ARRANGE : Créer une tâche
    create_response = client.post("/tasks", json={"title": "Trouve-moi"})
    task_id = create_response.json()["id"]

    # ACT : Obtenir la tâche spécifique
    response = client.get(f"/tasks/{task_id}")

    # ASSERT : Vérifier qu'on a la bonne tâche
    assert response.status_code == 200
    assert response.json()["title"] == "Trouve-moi"


# =============================================================================
# PARTIE 2 : À VOUS ! (Exercices 1 et 2)
# =============================================================================
#
# Écrivez d'abord ces tests : ils échouent, car delete_task() et update_task()
# ne sont pas encore écrites dans src/app.py. Puis écrivez ces fonctions
# jusqu'à ce que les tests passent.
#
# Pour chaque test : supprimez la ligne pytest.fail(...), puis écrivez
# ARRANGE / ACT / ASSERT. La docstring dit ce qu'il faut vérifier.

# --- Exercice 1 : supprimer une tâche ---

def test_delete_task(client):
    """
    VOTRE TÂCHE : Écrire un test qui supprime une tâche.

    Étapes :
    1. Créer une tâche (comme dans test_create_task)
    2. Obtenir son ID
    3. Envoyer une requête DELETE : client.delete(f"/tasks/{task_id}")
    4. Vérifier que le code de statut est 204 (No Content)
    5. Essayer de GET la tâche à nouveau → devrait retourner 404 (Not Found)

    Astuce : Regardez test_get_task_by_id pour voir comment créer et obtenir l'ID
    """
    # TODO : Écrivez votre test ici !
    # ARRANGE : Préparer les données
    new_task = {
        "title": "Test Task",
        "description": "This is a test task for deletion."
    }

    # ACT : Créer la tâche
    create_response = client.post("/tasks", json=new_task)
    task_id = create_response.json()["id"]
    # Supprimer la tâche
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204
    # Vérifier que la tâche a été supprimée
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
    
    pass


# EXERCICE 2 : Écrire un test pour METTRE À JOUR une tâche
# Pattern : Créer → Mettre à jour → Vérifier les changements
def test_update_task(client):
    """
    VOTRE TÂCHE : Écrire un test qui met à jour le titre d'une tâche.

    Étapes :
    1. Créer une tâche avec le titre "Titre Original"
    2. Obtenir son ID
    3. Envoyer une requête PUT : client.put(f"/tasks/{task_id}", json={"title": "Nouveau Titre"})
    4. Vérifier que le code de statut est 200
    5. Vérifier que la réponse contient le nouveau titre

    Astuce : Les requêtes PUT sont comme les POST, mais elles modifient des données existantes
    """
    # TODO : Écrivez votre test ici !
    # ARRANGE : Préparer les données
    new_task = {
            "title": "Titre Original",
            "description": "This is a test task for update."
    }

    create_response = client.post("/tasks", json=new_task)
    task_id = create_response.json()["id"]
    # ACT : Mettre à jour la tâche
    update_response = client.put(f"/tasks/{task_id}", json=new_task)
    # ASSERT : Vérifier la réponse
    assert update_response.status_code == 200
    # Vérifier que le titre a été mis à jour
    updated_task = update_response.json()
    assert updated_task["title"] == "Titre Original"  # Le titre reste le même car on n'a pas changé le titre
    pass


# --- Exercice 2 : modifier une tâche ---
    """
    Étapes :
    1. Essayer de créer une tâche avec title = ""
    2. Vérifier que le code de statut est 422 (Erreur de Validation)

    Astuce : Regardez test_create_task, mais attendez-vous à un échec !
    """
    # TODO :
    create_response = client.post("/tasks", json={"title": ""})
    assert create_response.status_code == 422
    pass


# EXERCICE 4 : Tester la validation - priorité invalide
def test_update_task_with_invalid_priority(client):
    """
    VOTRE TÂCHE : Tester qu'on ne peut pas mettre à jour une tâche avec une priorité invalide.

    Étapes :
    1. Créer une tâche valide
    2. Essayer de la mettre à jour avec priority="urgent" (invalide)
    3. Vérifier que le code de statut est 422 (Erreur de Validation)

    Rappel : Les priorités valides sont "low", "medium", "high" (voir TaskPriority dans app.py)"""

    # TODO : Écrivez votre test ici !
    create_response = client.post("/tasks", json={"title": "Tâche pour test"})
    task_id = create_response.json()["id"]
    update_response = client.put(f"/tasks/{task_id}", json={"priority": "urgent"})
    assert update_response.status_code == 422
    pass


def test_get_nonexistent_task(client):
    """
    VOTRE TÂCHE : Tester qu'obtenir une tâche qui n'existe pas retourne 404.

    Étapes :
    1. Essayer d'obtenir une tâche avec un faux ID : client.get("/tasks/999")
    2. Vérifier que le code de statut est 404 (Not Found)
    """
    # TODO : Écrivez votre test ici !
    get_response = client.get("/tasks/999")
    assert get_response.status_code == 404
    pass


def test_filter_tasks_by_status(client):
    """Créez une tâche "todo" et une tâche "done" : GET /tasks?status=done
    ne renvoie qu'une seule tâche, celle qui est terminée."""
    todo_response = client.post("/tasks", json={"title": "Tâche à faire"})
    done_response = client.post(
        "/tasks",
        json={"title": "Tâche terminée", "status": "done"},
    )

    assert todo_response.status_code == 201
    assert done_response.status_code == 201

    response = client.get("/tasks", params={"status": "done"})

    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["id"] == done_response.json()["id"]


# =============================================================================
# BONUS (si vous avez fini)
# =============================================================================
#
def test_filter_by_status_and_priority(client):
    """GET /tasks?status=todo&priority=high combine les deux filtres."""
    matching_task = client.post(
        "/tasks",
        json={"title": "Tâche correspondante", "status": "todo", "priority": "high"},
    )
    assert matching_task.status_code == 201

    for task in (
        {"title": "Mauvais statut", "status": "done", "priority": "high"},
        {"title": "Mauvaise priorité", "status": "todo", "priority": "low"},
        {"title": "Statut et priorité incorrects", "status": "done", "priority": "low"},
    ):
        response = client.post("/tasks", json=task)
        assert response.status_code == 201

    response = client.get(
        "/tasks",
        params={"status": "todo", "priority": "high"},
    )

    assert response.status_code == 200
    assert [task["id"] for task in response.json()] == [matching_task.json()["id"]]


def test_create_task_with_title_too_long(client):
    """Le titre est limité à 200 caractères : 200 est accepté (201), 201 est refusé (422).
    Astuce : "a" * 200 crée un texte de 200 caractères."""
    accepted_title = "a" * 200
    accepted_response = client.post("/tasks", json={"title": accepted_title})

    assert accepted_response.status_code == 201
    assert accepted_response.json()["title"] == accepted_title

    rejected_response = client.post("/tasks", json={"title": "a" * 201})

    assert rejected_response.status_code == 422


# =============================================================================
# ASTUCES & CONSEILS
# =============================================================================

"""
PATTERNS COURANTS :

1. Tester POST (Créer) :
   response = client.post("/tasks", json={"title": "..."})
   assert response.status_code == 201

2. Tester GET (Lire) :
   response = client.get("/tasks")
   assert response.status_code == 200

3. Tester PUT (Mettre à jour) :
   response = client.put(f"/tasks/{id}", json={"title": "..."})
   assert response.status_code == 200

4. Tester DELETE (Supprimer) :
   response = client.delete(f"/tasks/{id}")
   assert response.status_code == 204

5. Tester les erreurs de validation :
   response = client.post("/tasks", json={"bad": "data"})
   assert response.status_code == 422

6. Tester les erreurs 404 (la ressource demandée n'existe pas) :
   assert response.status_code == 404

CODES DE STATUT COURANTS :
- 200 : OK (GET/PUT réussi)
- 201 : Créé (POST réussi)
- 204 : Pas de Contenu (DELETE réussi)
- 404 : Non Trouvé (la ressource n'existe pas)
- 422 : Erreur de Validation (données invalides)

RAPPELEZ-VOUS :
- La fixture `client` est automatiquement fournie par conftest.py
- Les tâches sont automatiquement effacées avant/après chaque test (fixture clean_tasks)
- Les tests doivent être indépendants (ne pas dépendre d'autres tests)
"""
