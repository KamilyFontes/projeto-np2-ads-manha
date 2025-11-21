

class Node:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes #esquerda
        self.no = no   #direita

def is_leaf (node): #Verifica se nó é uma folha leaf == folha
    return node is not None and node.yes is None and node.no is None



def navigate_tree(node, answers): #_navegar_arvore; answers == respostas
    
    raiz_noh = node
    answers = []

    # Estrutura para percorrer a arvore

    for resposta in answers:
        
        if is_leaf(raiz_noh):
            break 

        resposta = resposta.lower() 
        resposta_len = len(resposta)

        #Validar tipos de respostas
        if resposta in ["sim", "s"]:

            answers.append("sim")
            raiz_noh = raiz_noh.yes #mudar para o próximo nó

        elif resposta in ["nao", "n"]:

            answers.append("não") 
            raiz_noh = raiz_noh.no
        
        #usar len para contar a quantidade

        elif resposta_len == 0:
            raise ValueError("É preciso escrever uma reposta: [Sim/Não]")

        else:
            raise ValueError(f"A resposta '{resposta}' é inválida. Use apenas Sim/Não.")


        if raiz_noh is None:
            print("Fim.")
            break
        
    if is_leaf(raiz_noh):
        return raiz_noh.question

    else:
        return "Não foi possível chegar a uma conclusão."  



# root = Node("O animal voa?",
#         yes=Node("É noturno?",
#                     yes=Node("É um mocho/coruja"),
#                     no=Node("É um pardal/pássaro diurno")),
#         no=Node("Vive na água?",
#                 yes=Node("É um peixe"),
#                 no=Node("É um cão/gato (mamífero terrestre)")))

# def parse_answers(s: str):
#     # Aceita: "sim, não", "sim nao", "SIM;NAO" etc.
#     raw = s.replace(",", " ").replace(";", " ").strip().split()
#     ans = []
#     for x in raw:
#         x = x.strip().lower()
#         if x in ("sim", "s"):
#             ans.append("sim")
#         elif x in ("nao", "não", "n"):
#             ans.append("não")
#         else:
#             # deixa o navigate_tree validar também, mas já avisamos aqui
#             ans.append(x)
#     return ans
