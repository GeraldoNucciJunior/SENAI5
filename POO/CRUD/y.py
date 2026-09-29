import sys

from database import Database

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.selected_id = None
        self.resize(650, 500)
        self.init_ui()

    def init_ui(self):
        # Configurações da janela
        self.setWindowTitle("Formulário de Cadastro")
        self.setMinimumSize(400, 200)

        # Widget central (obrigatório no QMainWindow)
        central = QWidget()
        self.setCentralWidget(central)

        # Layout principal vertical
        layout_principal = QVBoxLayout(central)

        # Layout do formulário (Label e Input lado a lado)
        layout_form = QFormLayout()
        layout_form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        # Campos de entrada
        self.txt_nome = QLineEdit()
        self.txt_nome.setPlaceholderText("Digite o nome completo")

        self.txt_telefone = QLineEdit()
        self.txt_telefone.setPlaceholderText("(00) 00000-0000")

        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("exemplo@email.com")

        layout_form.addRow("Nome:", self.txt_nome)
        layout_form.addRow("Telefone:", self.txt_telefone)
        layout_form.addRow("E-mail:", self.txt_email)

        # Botão de envio
        btn_enviar = QPushButton("Salvar Cadastro")
        btn_enviar.clicked.connect(self.salvar_dados)

        layout_principal.addLayout(layout_form)
        layout_principal.addWidget(btn_enviar)

    def salvar_dados(self):
        nome = self.txt_nome.text().strip()
        telefone = self.txt_telefone.text().strip()
        email = self.txt_email.text().strip()

        # Validação simples
        if not nome or not telefone or not email:
            QMessageBox.warning(self, "Aviso", "Por favor, preencha todos os campos!")
            return

        mensagem = (
            "Dados salvos com sucesso!\n\n"
            f"Nome: {nome}\nTelefone: {telefone}\nE-mail: {email}"
        )
        QMessageBox.information(self, "Sucesso", mensagem)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())