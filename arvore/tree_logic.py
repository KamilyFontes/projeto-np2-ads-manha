
class Node:
    def __init__(self, question, yes=None, no=None):
        """
        se 'yes' e 'no' forem None este nó é uma FOLHA e 'question' guarda a decisão final.
        saso contrário 'question' é o texto da pergunta e 'yes'/'no' são filhos.
        """
        self.question = question
        self.yes = yes
        self.no = no


def is_leaf(node):
    """
    Retorna True se o nó for uma folha (não possui filhos).
    """
    return node is not None and node.yes is None and node.no is None


def navigate_tree(node, answers):
    """
    Percorre a árvore conforme as respostas.
    """
    current = node  # Começa na raiz

    for resposta in answers:
        # Normaliza
        resposta = resposta.strip().lower()
        if resposta == "nao":
            resposta = "não"

        # Valida
        if resposta not in ("sim", "não"):
            raise ValueError(f"Resposta inválida: '{resposta}'. Use apenas 'sim' ou 'não'.")

        # Se já está numa folha
        if is_leaf(current):
            return current.question

        # Caminha pela árvore
        if resposta == "sim":
            current = current.yes
        else:
            current = current.no

        # Caminho inexistente
        if current is None:
            raise ValueError("A sequência de respostas não leva a uma decisão válida.")

    # Se acabou as respostas mas não chegou em uma folha
    if not is_leaf(current):
        raise ValueError("Faltam respostas para concluir a decisão.")

    # É folha → retorna decisão
    return current.question

