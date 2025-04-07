from .models import Materia, Assunto, Aula

def run():
    # Criar matérias
    mat_port = Materia.objects.create(nomeMateria='Português')
    mat_mat = Materia.objects.create(nomeMateria='Matemática')
    mat_hist = Materia.objects.create(nomeMateria='História')
    mat_geog = Materia.objects.create(nomeMateria='Geografia')
    mat_socio = Materia.objects.create(nomeMateria='Sociologia')
    mat_filo = Materia.objects.create(nomeMateria='Filosofia')
    mat_biol = Materia.objects.create(nomeMateria='Biologia')
    mat_quimica = Materia.objects.create(nomeMateria='Química')
    mat_fisic = Materia.objects.create(nomeMateria='Física')
    mat_ingl = Materia.objects.create(nomeMateria='Inglês')
    mat_espa = Materia.objects.create(nomeMateria='Espanhol')
    mat_arte = Materia.objects.create(nomeMateria='Artes')
    mat_redacao = Materia.objects.create(nomeMateria='Redação')
    mat_literatura = Materia.objects.create(nomeMateria='Literatura')

    # Português
    assunto_interp_texto = Assunto.objects.create(nomeAssuntos='Interpretação de Texto', materia=mat_port)
    assunto_funcoes_linguagem = Assunto.objects.create(nomeAssuntos='Funções da Linguagem', materia=mat_port)
    assunto_figuras_linguagem = Assunto.objects.create(nomeAssuntos='Figuras de Linguagem', materia=mat_port)

    # Matemática
    assunto_porcentagem = Assunto.objects.create(nomeAssuntos='Porcentagem', materia=mat_mat)
    assunto_regra_tres = Assunto.objects.create(nomeAssuntos='Regra de Três', materia=mat_mat)

    # História
    assunto_brasil_colonia = Assunto.objects.create(nomeAssuntos='Brasil Colônia', materia=mat_hist)
    assunto_brasil_imperio = Assunto.objects.create(nomeAssuntos='Brasil Império', materia=mat_hist)

    # Geografia
    assunto_geopolitica = Assunto.objects.create(nomeAssuntos='Geopolítica', materia=mat_geog)
    assunto_globalizacao = Assunto.objects.create(nomeAssuntos='Globalização', materia=mat_geog)

    # Sociologia
    assunto_cultura_identidade = Assunto.objects.create(nomeAssuntos='Cultura e Identidade', materia=mat_socio)
    assunto_cidadania_democracia = Assunto.objects.create(nomeAssuntos='Cidadania e Democracia', materia=mat_socio)

    # Filosofia
    assunto_filo_antiga = Assunto.objects.create(nomeAssuntos='Filosofia Antiga', materia=mat_filo)
    assunto_filo_moderna = Assunto.objects.create(nomeAssuntos='Filosofia Moderna', materia=mat_filo)

    # Biologia
    assunto_ecologia = Assunto.objects.create(nomeAssuntos='Ecologia', materia=mat_biol)
    assunto_genetica = Assunto.objects.create(nomeAssuntos='Genética', materia=mat_biol)

    # Criar aulas para cada assunto

    # Interpretação de Texto
    Aula.objects.create(
        nomeAula='Interpretação e Compreensão de Textos - Profa. Pamba',
        url='https://www.youtube.com/watch?v=W3XrpIRTgzA',
        descricaoAula='Aula sobre interpretação e compreensão de textos com a Professora Pamba.',
        materia=mat_port,
        assunto=assunto_interp_texto
    )
    Aula.objects.create(
        nomeAula='Compreensão e Interpretação de Textos - Prof. Noslen',
        url='https://www.youtube.com/watch?v=XsN0e_xPyNI',
        descricaoAula='Aula com o Professor Noslen sobre compreensão e interpretação de textos.',
        materia=mat_port,
        assunto=assunto_interp_texto
    )

    # Funções da Linguagem
    Aula.objects.create(
        nomeAula='Funções da Linguagem - Prof. Noslen',
        url='https://www.youtube.com/watch?v=5JrCUWnqHBk',
        descricaoAula='Aula explicando as funções da linguagem com o Professor Noslen.',
        materia=mat_port,
        assunto=assunto_funcoes_linguagem
    )
    Aula.objects.create(
        nomeAula='Funções da Linguagem – Revisão Enem com Prof. Noslen',
        url='https://www.youtube.com/watch?v=d6kS7zj8p2Q',
        descricaoAula='Revisão para o Enem sobre funções da linguagem com o Professor Noslen.',
        materia=mat_port,
        assunto=assunto_funcoes_linguagem
    )

    # Figuras de Linguagem
    Aula.objects.create(
        nomeAula='Figuras de Linguagem - Aula 01 [Prof. Noslen]',
        url='https://www.youtube.com/watch?v=n0e75nRstcU',
        descricaoAula='Primeira aula sobre figuras de linguagem com o Professor Noslen.',
        materia=mat_port,
        assunto=assunto_figuras_linguagem
    )
    Aula.objects.create(
        nomeAula='Figuras de Linguagem - Profa. Pamba',
        url='https://www.youtube.com/watch?v=_VslZ0R9mCA',
        descricaoAula='Aula completa sobre figuras de linguagem com a Professora Pamba.',
        materia=mat_port,
        assunto=assunto_figuras_linguagem
    )

    # Porcentagem
    Aula.objects.create(
        nomeAula='Como Calcular Porcentagem | Prof. Gis',
        url='https://www.youtube.com/watch?v=OjOyNmTt7Mw',
        descricaoAula='Aula ensinando como calcular porcentagem com a Professora Gis.',
        materia=mat_mat,
        assunto=assunto_porcentagem
    )
    Aula.objects.create(
        nomeAula='Porcentagem: Aprenda de uma vez por todas! - Aula 1',
        url='https://www.youtube.com/watch?v=ErplsNHi7YQ',
        descricaoAula='Aula introdutória sobre porcentagem.',
        materia=mat_mat,
        assunto=assunto_porcentagem
    )

    # Regra de Três
    Aula.objects.create(
        nomeAula='Regra de Três Simples - Professora Angela Matemática',
        url='https://www.youtube.com/watch?v=7gK3-QG363o',
        descricaoAula='Aula sobre regra de três simples com a Professora Angela.',
        materia=mat_mat,
        assunto=assunto_regra_tres
    )
    Aula.objects.create(
        nomeAula='Regra de Três Simples e Composta | Resumão',
        url='https://www.youtube.com/watch?v=CQFFaa9fmS0',
        descricaoAula='Resumo sobre regra de três',
        materia=mat_mat,
        assunto=assunto_regra_tres
    )


   