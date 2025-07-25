from cs_manim import (
    CLIENT_COLOR,
    FONT_NAME,
    REQUEST_COLOR,
    RESPONSE_COLOR,
    SERVER_COLOR,
    MobilePhone,
    Server,
)
from manim import (
    BLACK,
    DOWN,
    GRAY,
    LEFT,
    PI,
    RIGHT,
    UP,
    WHITE,
    Arrow,
    Circle,
    Create,
    DashedLine,
    FadeIn,
    FadeOut,
    Rectangle,
    Rotate,
    Scene,
    SurroundingRectangle,
    Text,
    VGroup,
    Write,
)


class SignalR(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Ces variables seront initialisées dans setup_scene() avant d'être utilisées
        self.client: MobilePhone
        self.server: Server
        self.client_to_server_line: DashedLine
        self.server_to_client_line: DashedLine
        self.request_label: Text
        self.response_label: Text

    def create_client(self):
        """Crée le client"""
        client = MobilePhone(name="Client", color=CLIENT_COLOR)
        client.shift(LEFT * 4)
        return client

    def create_server(self):
        """Crée le serveur API"""
        server = Server(name="Serveur", color=SERVER_COLOR)
        server.shift(RIGHT * 4)
        return server

    def create_communication_lines(self):
        """Crée les lignes de communication bidirectionnelles"""
        # Calcul des positions Y communes pour des lignes parfaitement horizontales
        client_center_y = self.client.get_center()[1]
        server_center_y = self.server.get_center()[1]
        average_y = (client_center_y + server_center_y) / 2

        # Ligne pour les messages client -> serveur (en haut) - parfaitement horizontale
        client_to_server_line = DashedLine(
            [self.client.get_right()[0] + 0.5, average_y + 0.3, 0],
            [self.server.get_left()[0] - 0.5, average_y + 0.3, 0],
            color=REQUEST_COLOR,
            stroke_width=2,
        )

        # Ligne pour les messages serveur -> client (en bas) - parfaitement horizontale
        server_to_client_line = DashedLine(
            [self.server.get_left()[0] - 0.5, average_y - 0.3, 0],
            [self.client.get_right()[0] + 0.5, average_y - 0.3, 0],
            color=RESPONSE_COLOR,
            stroke_width=2,
        )

        return client_to_server_line, server_to_client_line

    def create_direction_labels(self):
        """Crée les étiquettes pour les directions"""
        request_label = Text("Requêtes", font_size=14, color=REQUEST_COLOR, font=FONT_NAME)
        request_label.next_to(self.client_to_server_line, UP, buff=0.1)

        response_label = Text("Réponses", font_size=14, color=RESPONSE_COLOR, font=FONT_NAME)
        response_label.next_to(self.server_to_client_line, DOWN, buff=0.1)

        return request_label, response_label

    def setup_scene(self):
        """Configure la scène initiale avec tous les éléments de base"""
        # Création des éléments
        self.client = self.create_client()
        self.server = self.create_server()
        self.client_to_server_line, self.server_to_client_line = self.create_communication_lines()
        self.request_label, self.response_label = self.create_direction_labels()

        # Animation d'introduction
        self.play(
            FadeIn(self.client),
            FadeIn(self.server),
            Create(self.client_to_server_line),
            Create(self.server_to_client_line),
            Write(self.request_label),
            Write(self.response_label),
        )
        self.wait(1)

        self.wait(1)

    def animate_request(self):
        """Anime l'envoi de la requête API du client vers le serveur"""
        # Création de la requête API
        request_text = VGroup(
            Text("GET /api/amis", font_size=16, color=REQUEST_COLOR, font=FONT_NAME),
        ).arrange(DOWN, aligned_edge=LEFT)

        request_box = SurroundingRectangle(request_text, color=REQUEST_COLOR, buff=0.3)
        request_group = VGroup(request_box, request_text)
        request_group.scale(0.8)

        # Position initiale de la requête
        request_group.move_to(self.client.get_center() + UP * 1.5)

        self.play(FadeIn(request_group))
        self.wait(0.5)

        # Animation de la requête vers le serveur (utilise la ligne du haut)
        request_arrow = Arrow(
            self.client.get_right() + RIGHT * 0.2 + UP * 0.3,
            self.server.get_left() + LEFT * 0.2 + UP * 0.3,
            color=REQUEST_COLOR,
            stroke_width=4,
        )

        self.play(
            Create(request_arrow),
            request_group.animate.move_to((self.client.get_right() + self.server.get_left()) / 2 + UP * 1.5),
        )
        self.wait(0.5)

        self.play(
            request_group.animate.move_to(self.server.get_center() + UP * 1.5),
            FadeOut(request_arrow),
        )
        self.wait(1)

        return request_group

    def animate_server_processing(self):
        """Anime le traitement sur le serveur API"""
        processing_text = Text(
            "Requete base de donnees...",
            font_size=16,
            color=SERVER_COLOR,
            font=FONT_NAME,
        )
        processing_text.next_to(self.server, DOWN, buff=0.5)

        self.play(Write(processing_text))

        # Animation de traitement (rotation)
        processing_circle = Circle(radius=0.3, color=SERVER_COLOR).next_to(self.server, DOWN, buff=0.5)
        self.play(Create(processing_circle))
        self.play(Rotate(processing_circle, 2 * PI), run_time=1.5)
        self.play(FadeOut(processing_circle), FadeOut(processing_text))

    def animate_response(self, request_group):
        """Anime l'envoi de la réponse JSON avec la liste des amis"""
        # Création de la réponse JSON
        response_text = VGroup(
            Text("HTTP/1.1 200 OK", font_size=16, color=RESPONSE_COLOR, font=FONT_NAME),
            Text(
                "Content-Type: application/json",
                font_size=14,
                color=RESPONSE_COLOR,
                font=FONT_NAME,
            ),
            Text("", font_size=6),
            Text("{", font_size=14, color=RESPONSE_COLOR, font=FONT_NAME),
            Text('  "friends": [', font_size=13, color=RESPONSE_COLOR, font=FONT_NAME),
            Text(
                '    {"name": "Alice", "id": 123},',
                font_size=12,
                color=RESPONSE_COLOR,
                font=FONT_NAME,
            ),
            Text(
                '    {"name": "Bob", "id": 456},',
                font_size=12,
                color=RESPONSE_COLOR,
                font=FONT_NAME,
            ),
            Text(
                '    {"name": "Charlie", "id": 789}',
                font_size=12,
                color=RESPONSE_COLOR,
                font=FONT_NAME,
            ),
            Text("  ]", font_size=13, color=RESPONSE_COLOR, font=FONT_NAME),
            Text("}", font_size=14, color=RESPONSE_COLOR, font=FONT_NAME),
        ).arrange(DOWN, aligned_edge=LEFT)

        response_box = SurroundingRectangle(response_text, color=RESPONSE_COLOR, buff=0.3)
        response_group = VGroup(response_box, response_text)
        response_group.scale(0.7)
        response_group.move_to(self.server.get_center() + UP * 1.5)

        # Faire disparaître la requête et afficher la réponse
        self.play(FadeOut(request_group), FadeIn(response_group))
        self.wait(0.5)

        # Animation de la réponse vers le client (utilise la ligne du bas)
        response_arrow = Arrow(
            self.server.get_left() + LEFT * 0.2 + DOWN * 0.3,
            self.client.get_right() + RIGHT * 0.2 + DOWN * 0.3,
            color=RESPONSE_COLOR,
            stroke_width=4,
        )

        self.play(
            Create(response_arrow),
            response_group.animate.move_to((self.client.get_right() + self.server.get_left()) / 2 + UP * 1.5),
        )
        self.wait(0.5)

        self.play(
            response_group.animate.move_to(self.client.get_center() + UP * 1.5),
            FadeOut(response_arrow),
        )
        self.wait(1)

        return response_group

    def animate_client_display(self, response_group):
        """Anime l'affichage de la liste d'amis dans l'application"""
        friends_list = VGroup(
            Rectangle(width=2.5, height=2.2, color=WHITE, fill_opacity=0.9, stroke_color=GRAY),
            Text("Liste d'amis", font_size=18, color=BLACK, font=FONT_NAME).shift(UP * 0.7),
            Text("• Alice", font_size=16, color=BLACK, font=FONT_NAME).shift(UP * 0.2),
            Text("• Bob", font_size=16, color=BLACK, font=FONT_NAME).shift(DOWN * 0.1),
            Text("• Charlie", font_size=16, color=BLACK, font=FONT_NAME).shift(DOWN * 0.4),
            Text("3 amis connectes", font_size=12, color=GRAY, font=FONT_NAME).shift(DOWN * 0.7),
        )
        friends_list.next_to(self.client, DOWN, buff=0.5)

        self.play(FadeOut(response_group), FadeIn(friends_list))

        return friends_list

    def show_explanation_steps(self):
        """Affiche les messages explicatifs pour l'API REST"""
        step1 = Text(
            "1. L'app demande la liste d'amis via API",
            font_size=18,
            color=WHITE,
            font=FONT_NAME,
        )
        step2 = Text(
            "2. Le serveur interroge la base de donnees",
            font_size=18,
            color=WHITE,
            font=FONT_NAME,
        )
        step3 = Text(
            "3. Le serveur renvoie les donnees JSON",
            font_size=18,
            color=WHITE,
            font=FONT_NAME,
        )
        step4 = Text(
            "4. L'app affiche la liste des amis",
            font_size=18,
            color=WHITE,
            font=FONT_NAME,
        )

        steps = VGroup(step1, step2, step3, step4).arrange(DOWN, aligned_edge=LEFT)
        steps.to_edge(DOWN).shift(UP * 0.5)

        for step in steps:
            self.play(Write(step), run_time=0.8)
            self.wait(0.5)

        return steps

    def final_animation(self, friends_list, steps):
        """Animation finale - zoom out pour voir l'ensemble"""
        everything = VGroup(
            self.client,
            self.server,
            self.client_to_server_line,
            self.server_to_client_line,
            self.request_label,
            self.response_label,
            friends_list,
            steps,
        )
        self.play(everything.animate.scale(0.8))
        self.wait(2)

    def construct(self):
        """Méthode principale qui orchestre toute l'animation"""
        # 1. Configuration de la scène
        self.setup_scene()

        # 2. Animation de la requête HTTP
        request_group = self.animate_request()

        # 3. Traitement sur le serveur
        self.animate_server_processing()

        # 4. Animation de la réponse HTTP
        response_group = self.animate_response(request_group)

        # 5. Affichage de la liste d'amis dans l'app
        friends_list = self.animate_client_display(response_group)

        # 6. Messages explicatifs
        steps = self.show_explanation_steps()

        # 7. Animation finale
        self.wait(3)
        self.final_animation(friends_list, steps)
