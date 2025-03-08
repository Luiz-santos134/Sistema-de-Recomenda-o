# Base de dados de cursos e seus tópicos principais (Dicionário)
cursos = {
    "Python para Iniciantes": ["programação", "python", "lógica"],
    "Marketing Digital": ["marketing", "redes sociais", "estratégia"],
    "Design Gráfico": ["design", "photoshop", "criatividade"],
    "Desenvolvimento Web": ["programação", "web", "javascript"],
    "Fotografia Profissional": ["fotografia", "edição", "criatividade"],
}

def recomendar_curso(interesses):
    """Recomenda um curso com base nos interesses do usuário."""
    
    recomendacoes = {}
    
    # Percorre os cursos e verifica quantos interesses combinam
    for curso, tags in cursos.items():
        similaridade = len(set(interesses) & set(tags))  # Conta interesses em comum
        if similaridade > 0:
            recomendacoes[curso] = similaridade

    # Ordena os cursos pelo número de interesses em comum
    if not recomendacoes:
        return "Nenhuma recomendação encontrada."

    curso_recomendado = max(recomendacoes, key=recomendacoes.get)
    return f"Recomendação: {curso_recomendado}"

# Testando o sistema
interesses_usuario = ["programação", "javascript"]
print(recomendar_curso(interesses_usuario))  # Deve recomendar "Desenvolvimento Web"
