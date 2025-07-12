# SignalR

## Sommaire de la vidéo

- Retour sur ce qu'on connait déjà de HTTP : Half-Duplex
- Nouveau concept : Full Duplex
- Librairie : SignalR

## Retour sur ce qu'on connait déjà de HTTP : Half-Duplex

Depuis le début de votre parcours, vous avez appris à faire des appels HTTP.

- Dans le cours où vous utilisiez MVC, vous faisiez une requête HTTP qui permettait d'obtenir une page html
- Dans le cours où vous utilisiez Angular ou autre, vous avez appris à faire des requêtes HTTP pour obtenir des objets JSON
- Idem dans le cours d'applications mobiles, où votre téléphone était capable de faire des appels HTTP pour obtenir des objets JSON

Dans tout ces cas, le principe reste à peu près le même. Un client fait une requête à un serveur, qui lui répond avec de l'information.

Notez que c'est toujours le client qui initie la requête.

"Je veux quelque chose", et le serveur dit "voici cette chose".

Cette manière de communiquer où c'est le client qui initie la communication, et où le serveur répond à la requête s'appelle le Half-Duplex.

## Nouveau concept : Full Duplex

Aujourd'hui on va voir comment fonctionne la communication par Full-Duplex.

En Full-Duplex, autant le client que le serveur peut initier la communication avec l'autre partie.

Donc comme en Half-Duplex, le client peut initier la communication avec le serveur.

La nouveauté est que le serveur peut lui aussi initiser la communication avec le ou les clients.

Vous remarquerez que j'ai parlé des clients au pluriel.

C'est effectivement possible pour un serveur qui utilise le full duplex de communiquer avec plusieurs clients à la fois.

Pour arriver à utiliser le full duplex, on va voir plus tard dans la vidéo comment utiliser SignalR.

## Exemple concret

On va prendre un exemple concret.

Vous développez une application qui permet aux utilisateurs d'échanger des messages entre eux : un chat.

Vous voulez que tous les utilisateurs qui sont connectés dans la même salle de chat soient avertis à chaque fois qu'un nouveau message est envoyé par un utilisateur.

Avec un mode de communication en half-duplex, ce serait possible de faire en sorte que chaque utilisateur dans le chat soit avertis d'un nouveau message.

Il faudrait qu'ils fassent ce qu'on appelle du polling, où chaque client demande à toutes les 5 secondes si un nouveau message est entré dans le serveur.

Vous conviendrez que c'est pas très efficace puisque la grande majorité des requêtes vont être innutiles, puisqu'il n'y aura pas de nouveau message.

Avec un mode de communication en Half-Duplex, c'est le serveur qui va être responsable d'avertir tous les clients qui sont dans la même salle de chat qu'un nouveau message est entré.

On communique donc uniquement lorsque c'est nécessaire.

### Initier la connexion

Pour arriver à entrer en Full-Duplex entre un client et un serveur, il y a un protocole à resecter.

1. Le client demande au serveur d'initier la connexion

### Pourquoi ne pas toujours faire de Full-Duplex?

À ce point ci, vous pourriez vous demande : "Pourquoi ne pas toujours faire de Full-Duplex? Ça permet de faire davantage de choses, non?"

La raison pour laquelle on utilise par toujours Full-Duplex, et vous aller le voir en utilisant SignalR, c'est que ça prend davantage d'effort pour le mettre en place, et présentement dans le web d'aujourd'hui, on se satisfait de Half-Duplex dans la grande majorité des cas.

## Librairie : SignalR

## Autres alternatives

SignalR est développé par Microsoft, et utilise des web sockets en arrière. Mais sachez que c'est possible d'utiliser des web sockets avec tous les quadriciels web moderne. Par exemple Socket.io est un bon exemple de façon de faire du full duplex avec NodeJS.
