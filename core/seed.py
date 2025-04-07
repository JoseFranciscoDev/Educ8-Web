
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
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Sintaxe', materia=mat_port),
        Assunto(nomeAssuntos='Semântica', materia=mat_port),
        Assunto(nomeAssuntos='Tipologia Textual', materia=mat_port),
        Assunto(nomeAssuntos='Variação Linguística', materia=mat_port),
        Assunto(nomeAssuntos='Interpretação de Texto', materia=mat_port),
        Assunto(nomeAssuntos='Funções da Linguagem', materia=mat_port),
        Assunto(nomeAssuntos='Figuras de Linguagem', materia=mat_port),
        Assunto(nomeAssuntos='Ortografia e Acentuação', materia=mat_port),
        Assunto(nomeAssuntos='Regência e Crase', materia=mat_port),
    ])

    # Matemática
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Porcentagem', materia=mat_mat),
        Assunto(nomeAssuntos='Análise Combinatória', materia=mat_mat),
        Assunto(nomeAssuntos='Geometria Plana', materia=mat_mat),
        Assunto(nomeAssuntos='Equações do 1º e 2º grau', materia=mat_mat),
        Assunto(nomeAssuntos='Álgebra', materia=mat_mat),
        Assunto(nomeAssuntos='Geometria Espacial', materia=mat_mat),
        Assunto(nomeAssuntos='Probabilidade e Estatística', materia=mat_mat),
        Assunto(nomeAssuntos='Funções e Gráficos', materia=mat_mat),
        Assunto(nomeAssuntos='Matemática Financeira', materia=mat_mat),
    ])

    # História
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Brasil Colônia', materia=mat_hist),
        Assunto(nomeAssuntos='Brasil Império', materia=mat_hist),
        Assunto(nomeAssuntos='Brasil República', materia=mat_hist),
        Assunto(nomeAssuntos='História Geral: Idade Média', materia=mat_hist),
        Assunto(nomeAssuntos='Ditadura Militar', materia=mat_hist),
    ])

    # Geografia
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Geografia Agrária', materia=mat_geog),
        Assunto(nomeAssuntos='Globalização', materia=mat_geog),
        Assunto(nomeAssuntos='Urbanização', materia=mat_geog),
        Assunto(nomeAssuntos='Climatologia', materia=mat_geog),
        Assunto(nomeAssuntos='Geopolítica', materia=mat_geog),
    ])

    # Sociologia
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Teorias Sociológicas', materia=mat_socio),
        Assunto(nomeAssuntos='Cidadania e Democracia', materia=mat_socio),
        Assunto(nomeAssuntos='Cultura e Sociedade', materia=mat_socio),
        Assunto(nomeAssuntos='Desigualdade Social', materia=mat_socio),
        Assunto(nomeAssuntos='Movimentos Sociais', materia=mat_socio),
    ])

    # Filosofia
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Filosofia Antiga', materia=mat_filo),
        Assunto(nomeAssuntos='Filosofia Moderna', materia=mat_filo),
        Assunto(nomeAssuntos='Filosofia Contemporânea', materia=mat_filo),
        Assunto(nomeAssuntos='Ética e Moral', materia=mat_filo),
        Assunto(nomeAssuntos='Conhecimento e Verdade', materia=mat_filo),
    ])

    # Biologia
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Botânica', materia=mat_biol),
        Assunto(nomeAssuntos='Zoologia', materia=mat_biol),
        Assunto(nomeAssuntos='Bioquímica', materia=mat_biol),
        Assunto(nomeAssuntos='Imunologia', materia=mat_biol),
        Assunto(nomeAssuntos='Citologia', materia=mat_biol),
        Assunto(nomeAssuntos='Genética', materia=mat_biol),
        Assunto(nomeAssuntos='Ecologia', materia=mat_biol),
        Assunto(nomeAssuntos='Fisiologia Humana', materia=mat_biol),
        Assunto(nomeAssuntos='Evolução', materia=mat_biol),
    ])

    # Química
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Química Ambiental', materia=mat_quimica),
        Assunto(nomeAssuntos='Radioatividade', materia=mat_quimica),
        Assunto(nomeAssuntos='Soluções', materia=mat_quimica),
        Assunto(nomeAssuntos='Reações Inorgânicas', materia=mat_quimica),
        Assunto(nomeAssuntos='Estequiometria', materia=mat_quimica),
        Assunto(nomeAssuntos='Química Orgânica', materia=mat_quimica),
        Assunto(nomeAssuntos='Equilíbrios Químicos', materia=mat_quimica),
        Assunto(nomeAssuntos='Tabelas e Ligações', materia=mat_quimica),
        Assunto(nomeAssuntos='Termoquímica', materia=mat_quimica),
    ])

    # Física
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Ondulatória', materia=mat_fisic),
        Assunto(nomeAssuntos='Eletromagnetismo', materia=mat_fisic),
        Assunto(nomeAssuntos='Hidrostática', materia=mat_fisic),
        Assunto(nomeAssuntos='Leis de Newton', materia=mat_fisic),
        Assunto(nomeAssuntos='Cinemática', materia=mat_fisic),
        Assunto(nomeAssuntos='Dinâmica', materia=mat_fisic),
        Assunto(nomeAssuntos='Eletricidade', materia=mat_fisic),
        Assunto(nomeAssuntos='Óptica', materia=mat_fisic),
        Assunto(nomeAssuntos='Termodinâmica', materia=mat_fisic),
    ])

    # Inglês
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Reading Comprehension', materia=mat_ingl),
        Assunto(nomeAssuntos='Text Genres', materia=mat_ingl),
        Assunto(nomeAssuntos='False Cognates', materia=mat_ingl),
        Assunto(nomeAssuntos='Connectors', materia=mat_ingl),
        Assunto(nomeAssuntos='Vocabulary in Context', materia=mat_ingl),
    ])

    # Espanhol
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Comprensión de Lectura', materia=mat_espa),
        Assunto(nomeAssuntos='Falsos Cognados', materia=mat_espa),
        Assunto(nomeAssuntos='Géneros Textuales', materia=mat_espa),
        Assunto(nomeAssuntos='Conectores', materia=mat_espa),
        Assunto(nomeAssuntos='Vocabulario en Contexto', materia=mat_espa),
    ])

    # Artes
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Artes Visuais', materia=mat_arte),
        Assunto(nomeAssuntos='Música', materia=mat_arte),
        Assunto(nomeAssuntos='Teatro', materia=mat_arte),
        Assunto(nomeAssuntos='Cinema', materia=mat_arte),
        Assunto(nomeAssuntos='História da Arte', materia=mat_arte),
    ])

    # Redação
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Estrutura do Texto Dissertativo', materia=mat_redacao),
        Assunto(nomeAssuntos='Coesão e Coerência', materia=mat_redacao),
        Assunto(nomeAssuntos='Tese e Argumentos', materia=mat_redacao),
        Assunto(nomeAssuntos='Proposta de Intervenção', materia=mat_redacao),
        Assunto(nomeAssuntos='Temas de Redação do ENEM', materia=mat_redacao),
    ])

    # Literatura
    Assunto.objects.bulk_create([
        Assunto(nomeAssuntos='Modernismo', materia=mat_literatura),
        Assunto(nomeAssuntos='Romantismo', materia=mat_literatura),
        Assunto(nomeAssuntos='Realismo e Naturalismo', materia=mat_literatura),
        Assunto(nomeAssuntos='Barroco e Arcadismo', materia=mat_literatura),
        Assunto(nomeAssuntos='Análise Literária', materia=mat_literatura),
    ])




def criar_aulas():
    # Buscar os assuntos já existentes
    algebra = Assunto.objects.get(nomeAssuntos='Álgebra')
    geometria_plana = Assunto.objects.get(nomeAssuntos='Geometria Plana')
    porcentagem = Assunto.objects.get(nomeAssuntos='Porcentagem')
    funcao = Assunto.objects.get(nomeAssuntos='Funções e Gráficos')
    analise_combinatoria = Assunto.objects.get(nomeAssuntos='Análise Combinatória')
    matematica_financeira = Assunto.objects.get(nomeAssuntos='Matemática Financeira')
    ecologia = Assunto.objects.get(nomeAssuntos='Ecologia')
    genetica = Assunto.objects.get(nomeAssuntos='Genética')
    citologia = Assunto.objects.get(nomeAssuntos='Citologia')
    fisiologia = Assunto.objects.get(nomeAssuntos='Fisiologia Humana')
    evolucao = Assunto.objects.get(nomeAssuntos='Evolução')
    organica = Assunto.objects.get(nomeAssuntos='Química Orgânica')
    estequiometria = Assunto.objects.get(nomeAssuntos='Estequiometria')
    termoquimica = Assunto.objects.get(nomeAssuntos='Termoquímica')
    equilibrio = Assunto.objects.get(nomeAssuntos='Equilíbrios Químicos')
    cinemática = Assunto.objects.get(nomeAssuntos='Cinemática')
    dinamica = Assunto.objects.get(nomeAssuntos='Dinâmica')
    eletro = Assunto.objects.get(nomeAssuntos='Eletricidade')
    optica = Assunto.objects.get(nomeAssuntos='Óptica')
    termo = Assunto.objects.get(nomeAssuntos='Termodinâmica')
    interpret = Assunto.objects.get(nomeAssuntos='Interpretação de Texto')
    figuras = Assunto.objects.get(nomeAssuntos='Figuras de Linguagem')
    crase = Assunto.objects.get(nomeAssuntos='Regência e Crase')
    ortografia = Assunto.objects.get(nomeAssuntos='Ortografia e Acentuação')
    funcoes = Assunto.objects.get(nomeAssuntos='Funções da Linguagem')
    intervencao = Assunto.objects.get(nomeAssuntos='Proposta de Intervenção')
    coesao = Assunto.objects.get(nomeAssuntos='Coesão e Coerência')
    tese = Assunto.objects.get(nomeAssuntos='Tese e Argumentos')
    estrutura = Assunto.objects.get(nomeAssuntos='Estrutura do Texto Dissertativo')
    temas = Assunto.objects.get(nomeAssuntos='Temas de Redação do ENEM')
    globalizacao = Assunto.objects.get(nomeAssuntos='Globalização')
    cartografia = Assunto.objects.get(nomeAssuntos='Cartografia')
    clima = Assunto.objects.get(nomeAssuntos='Climatologia')
    recursos = Assunto.objects.get(nomeAssuntos='Recursos Naturais')
    urbanizacao = Assunto.objects.get(nomeAssuntos='Urbanização')
    br_colonia = Assunto.objects.get(nomeAssuntos='Brasil Colônia')
    br_imperio = Assunto.objects.get(nomeAssuntos='Brasil Império')
    br_republica = Assunto.objects.get(nomeAssuntos='Brasil República')
    idade_media = Assunto.objects.get(nomeAssuntos='História Geral: Idade Média')
    ditadura = Assunto.objects.get(nomeAssuntos='Ditadura Militar')
    # Buscar os assuntos já existentes
    filosofia_antiga = Assunto.objects.get(nomeAssuntos='Filosofia Antiga')
    filosofia_moderna = Assunto.objects.get(nomeAssuntos='Filosofia Moderna')
    filosofia_contemporanea = Assunto.objects.get(nomeAssuntos='Filosofia Contemporânea')
    etica_moral = Assunto.objects.get(nomeAssuntos='Ética e Moral')
    conhecimento_verdade = Assunto.objects.get(nomeAssuntos='Conhecimento e Verdade')

    teorias_sociologicas = Assunto.objects.get(nomeAssuntos='Teorias Sociológicas')
    cidadania_democracia = Assunto.objects.get(nomeAssuntos='Cidadania e Democracia')
    cultura_sociedade = Assunto.objects.get(nomeAssuntos='Cultura e Sociedade')
    desigualdade_social = Assunto.objects.get(nomeAssuntos='Desigualdade Social')
    movimentos_sociais = Assunto.objects.get(nomeAssuntos='Movimentos Sociais')

    romantismo = Assunto.objects.get(nomeAssuntos='Romantismo')
    modernismo = Assunto.objects.get(nomeAssuntos='Modernismo')
    barroco = Assunto.objects.get(nomeAssuntos='Barroco e Arcadismo')
    realismo = Assunto.objects.get(nomeAssuntos='Realismo e Naturalismo')
    analise_literaria = Assunto.objects.get(nomeAssuntos='Análise Literária')

    artes_visuais = Assunto.objects.get(nomeAssuntos='Artes Visuais')
    musica = Assunto.objects.get(nomeAssuntos='Música')
    teatro = Assunto.objects.get(nomeAssuntos='Teatro')
    cinema = Assunto.objects.get(nomeAssuntos='Cinema')
    historia_arte = Assunto.objects.get(nomeAssuntos='História da Arte')

    leitura_ingles = Assunto.objects.get(nomeAssuntos='Reading Comprehension')
    generos_textuais_ingles = Assunto.objects.get(nomeAssuntos='Text Genres')
    false_cognates_ingles = Assunto.objects.get(nomeAssuntos='False Cognates')
    connectors_ingles = Assunto.objects.get(nomeAssuntos='Connectors')
    vocabulario_ingles = Assunto.objects.get(nomeAssuntos='Vocabulary in Context')

    leitura_espanhol = Assunto.objects.get(nomeAssuntos='Comprensión de Lectura')
    generos_textuais_espanhol = Assunto.objects.get(nomeAssuntos='Géneros Textuales')
    false_cognates_espanhol = Assunto.objects.get(nomeAssuntos='Falsos Cognados')
    connectors_espanhol = Assunto.objects.get(nomeAssuntos='Conectores')
    vocabulario_espanhol = Assunto.objects.get(nomeAssuntos='Vocabulario en Contexto')

    Aula.objects.bulk_create([
        # Matemática
        Aula(nomeAula='Introdução à Álgebra - Parte 1', url='https://www.youtube.com/watch?v=6dV4BzHqXpY', descricaoAula='Fundamentos de Álgebra para o ENEM', materia=algebra.materia, assunto=algebra),
        Aula(nomeAula='Equações de 1º grau', url='https://www.youtube.com/watch?v=KhWg_Vg3h2Q', descricaoAula='Equações básicas com Ferretto', materia=algebra.materia, assunto=algebra),
        Aula(nomeAula='Equações de 2º grau', url='https://www.youtube.com/watch?v=U18jwTz8a5M', descricaoAula='Fórmula de Bhaskara e aplicações', materia=algebra.materia, assunto=algebra),
        Aula(nomeAula='Áreas das Figuras Planas', url='https://www.youtube.com/watch?v=V17qzUncP7U', descricaoAula='Cálculo de áreas no ENEM', materia=geometria_plana.materia, assunto=geometria_plana),
        Aula(nomeAula='Teorema de Pitágoras', url='https://www.youtube.com/watch?v=aQmv0_mNWpI', descricaoAula='Aplicações do Teorema de Pitágoras', materia=geometria_plana.materia, assunto=geometria_plana),
        Aula(nomeAula='Cálculo de Porcentagem', url='https://www.youtube.com/watch?v=R5oqHTrRJyM', descricaoAula='Como resolver problemas de porcentagem', materia=porcentagem.materia, assunto=porcentagem),
        Aula(nomeAula='Porcentagem na Regra de Três', url='https://www.youtube.com/watch?v=nV7FDa7mSv8', descricaoAula='Combinação com proporções', materia=porcentagem.materia, assunto=porcentagem),
        Aula(nomeAula='Função do 1º Grau', url='https://www.youtube.com/watch?v=ZqI8WDY5-a4', descricaoAula='Introdução e gráficos de funções lineares', materia=funcao.materia, assunto=funcao),
        Aula(nomeAula='Função do 2º Grau', url='https://www.youtube.com/watch?v=q9O7gULsFCM', descricaoAula='Parábolas no ENEM', materia=funcao.materia, assunto=funcao),
        Aula(nomeAula='Princípio Fundamental da Contagem', url='https://www.youtube.com/watch?v=29s_KTgzFeM', descricaoAula='Como contar possibilidades', materia=analise_combinatoria.materia, assunto=analise_combinatoria),
        Aula(nomeAula='Permutação e Combinação', url='https://www.youtube.com/watch?v=udDN7jcM1TI', descricaoAula='Casos clássicos da combinatória no ENEM', materia=analise_combinatoria.materia, assunto=analise_combinatoria),
        Aula(nomeAula='Juros Simples', url='https://www.youtube.com/watch?v=EtpvRV3r5AA', descricaoAula='Cálculo de juros simples', materia=matematica_financeira.materia, assunto=matematica_financeira),
        Aula(nomeAula='Juros Compostos', url='https://www.youtube.com/watch?v=ZGmn1KDRLsQ', descricaoAula='Juros compostos e diferenças com simples', materia=matematica_financeira.materia, assunto=matematica_financeira),

        # Biologia
        Aula(nomeAula='Cadeias Alimentares', url='https://www.youtube.com/watch?v=EmjZ-Em9B6Y', descricaoAula='Níveis tróficos e ecossistemas', materia=ecologia.materia, assunto=ecologia),
        Aula(nomeAula='Genética - 1ª Lei de Mendel', url='https://www.youtube.com/watch?v=8xTn4R1OEE0', descricaoAula='Hereditariedade mendeliana', materia=genetica.materia, assunto=genetica),
        Aula(nomeAula='Citologia - Organelas Celulares', url='https://www.youtube.com/watch?v=AXI3cX0BM04', descricaoAula='Funções das organelas celulares', materia=citologia.materia, assunto=citologia),
        Aula(nomeAula='Fisiologia Humana - Sistema Digestório', url='https://www.youtube.com/watch?v=em4ZCkW2aNs', descricaoAula='Processo de digestão e absorção', materia=fisiologia.materia, assunto=fisiologia),
        Aula(nomeAula='Evolução - Darwinismo', url='https://www.youtube.com/watch?v=IQ0ztlXQZIY', descricaoAula='Teoria da seleção natural', materia=evolucao.materia, assunto=evolucao),

        # Química
        Aula(nomeAula='Estequiometria - Introdução', url='https://www.youtube.com/watch?v=fKcbJTkTwtw', descricaoAula='Conceito e resolução de exercícios', materia=estequiometria.materia, assunto=estequiometria),
        Aula(nomeAula='Química Orgânica - Funções', url='https://www.youtube.com/watch?v=Dh2BtrMKttU', descricaoAula='Álcool, éter, cetona, etc.', materia=organica.materia, assunto=organica),
        Aula(nomeAula='Termoquímica - Reações Exotérmicas', url='https://www.youtube.com/watch?v=IM2YxTZB1v0', descricaoAula='Energia nas reações químicas', materia=termoquimica.materia, assunto=termoquimica),
        Aula(nomeAula='Equilíbrio Químico', url='https://www.youtube.com/watch?v=pGKYmMPh2Jg', descricaoAula='Constantes de equilíbrio', materia=equilibrio.materia, assunto=equilibrio),

        # Física
        Aula(nomeAula='Cinemática - MRU e MRUV', url='https://www.youtube.com/watch?v=h-XdeSxvX3s', descricaoAula='Movimentos uniformes e uniformemente variados', materia=cinemática.materia, assunto=cinemática),
        Aula(nomeAula='Dinâmica - Leis de Newton', url='https://www.youtube.com/watch?v=6rWCZ8U96Ao', descricaoAula='1ª, 2ª e 3ª leis de Newton', materia=dinamica.materia, assunto=dinamica),
        Aula(nomeAula='Eletricidade - Corrente e Tensão', url='https://www.youtube.com/watch?v=Zxjz2Fu4d_k', descricaoAula='Conceitos básicos de eletricidade', materia=eletro.materia, assunto=eletro),
        Aula(nomeAula='Óptica - Espelhos Planos', url='https://www.youtube.com/watch?v=E9ByNmtMcRQ', descricaoAula='Reflexão e imagem em espelhos', materia=optica.materia, assunto=optica),
        Aula(nomeAula='Termodinâmica - Calor e Temperatura', url='https://www.youtube.com/watch?v=ZcFzxk7G_Fw', descricaoAula='Conceitos de calor e temperatura', materia=termo.materia, assunto=termo),

        # Português
        Aula(nomeAula='Interpretação de Tirinhas e Charges', url='https://www.youtube.com/watch?v=4m1yOPfXoA4', descricaoAula='Textos não verbais no ENEM', materia=interpret.materia, assunto=interpret),
        Aula(nomeAula='Figuras de Linguagem - Aula Completa', url='https://www.youtube.com/watch?v=4-8iOhq4t6s', descricaoAula='Metáfora, ironia, hipérbole e mais', materia=figuras.materia, assunto=figuras),
        Aula(nomeAula='Regência e Crase - Dicas Práticas', url='https://www.youtube.com/watch?v=2gSwqK3W2sU', descricaoAula='Uso correto da crase e regência verbal', materia=crase.materia, assunto=crase),
        Aula(nomeAula='Ortografia e Acentuação', url='https://www.youtube.com/watch?v=3PYvqHa9XxI', descricaoAula='Regras de ortografia para o ENEM', materia=ortografia.materia, assunto=ortografia),
        Aula(nomeAula='Funções da Linguagem - Exemplos e Aplicações', url='https://www.youtube.com/watch?v=FphBhFQxq4c', descricaoAula='Função referencial, emotiva, conativa...', materia=funcoes.materia, assunto=funcoes),

        # Redação
        Aula(nomeAula='Proposta de Intervenção Nota 1000', url='https://www.youtube.com/watch?v=OWFCM9AAJmY', descricaoAula='Como elaborar propostas completas', materia=intervencao.materia, assunto=intervencao),
        Aula(nomeAula='Coesão e Coerência - Texto Claro', url='https://www.youtube.com/watch?v=DH2WuHE0SNo', descricaoAula='Elementos de conexão e fluidez textual', materia=coesao.materia, assunto=coesao),
        Aula(nomeAula='Tese e Argumentos - Como Desenvolver', url='https://www.youtube.com/watch?v=LKqxQUOQXEc', descricaoAula='Defendendo seu ponto de vista com eficácia', materia=tese.materia, assunto=tese),
        Aula(nomeAula='Estrutura do Texto Dissertativo', url='https://www.youtube.com/watch?v=3qlNGyF59T0', descricaoAula='Introdução, desenvolvimento e conclusão', materia=estrutura.materia, assunto=estrutura),
        Aula(nomeAula='Temas de Redação do ENEM', url='https://www.youtube.com/watch?v=5aNJ2NlfN8E', descricaoAula='Análise dos temas anteriores', materia=temas.materia, assunto=temas),

        # Geografia
        Aula(nomeAula='Globalização - Conceitos e Impactos', url='https://www.youtube.com/watch?v=TTZ4RQaG7zI', descricaoAula='Impactos da globalização no espaço geográfico', materia=globalizacao.materia, assunto=globalizacao),
        Aula(nomeAula='Cartografia - Leitura de Mapas', url='https://www.youtube.com/watch?v=-SR1I2-jb0g', descricaoAula='Escalas, coordenadas e projeções', materia=cartografia.materia, assunto=cartografia),
        Aula(nomeAula='Climatologia - Fatores do Clima', url='https://www.youtube.com/watch?v=dx5_FpXckD8', descricaoAula='Principais tipos climáticos', materia=clima.materia, assunto=clima),
        Aula(nomeAula='Recursos Naturais e Meio Ambiente', url='https://www.youtube.com/watch?v=AsJ4T07sQto', descricaoAula='Uso e preservação dos recursos naturais', materia=recursos.materia, assunto=recursos),
        Aula(nomeAula='Urbanização e Problemas Urbanos', url='https://www.youtube.com/watch?v=9lBevkgGW_A', descricaoAula='Crescimento das cidades e desafios sociais', materia=urbanizacao.materia, assunto=urbanizacao),

        # História
        Aula(nomeAula='Brasil Colônia - Introdução', url='https://www.youtube.com/watch?v=4JhKdDdT2mk', descricaoAula='Aspectos políticos e sociais do Brasil colonial', materia=br_colonia.materia, assunto=br_colonia),
        Aula(nomeAula='Brasil Império - 2º Reinado', url='https://www.youtube.com/watch?v=FqPhsmLyW7A', descricaoAula='D. Pedro II e a crise do Império', materia=br_imperio.materia, assunto=br_imperio),
        Aula(nomeAula='Brasil República - República Velha', url='https://www.youtube.com/watch?v=OIfPzbhJWEk', descricaoAula='Café com leite e coronelismo', materia=br_republica.materia, assunto=br_republica),
        Aula(nomeAula='Idade Média - Feudalismo', url='https://www.youtube.com/watch?v=CBpVjDfKnSY', descricaoAula='Organização da sociedade feudal', materia=idade_media.materia, assunto=idade_media),
        Aula(nomeAula='Ditadura Militar no Brasil', url='https://www.youtube.com/watch?v=r7l2bESp-ZI', descricaoAula='Período de 1964 a 1985', materia=ditadura.materia, assunto=ditadura),
        
        # Filosofia
        Aula(nomeAula='Filosofia Antiga - Sócrates, Platão e Aristóteles', url='https://www.youtube.com/watch?v=V3WVVKDk03A', descricaoAula='Pensamento clássico e ético da antiguidade', materia=filosofia_antiga.materia, assunto=filosofia_antiga),
        Aula(nomeAula='Filosofia Moderna - Descartes e Racionalismo', url='https://www.youtube.com/watch?v=mMrN-MGtu6I', descricaoAula='O método cartesiano e a dúvida', materia=filosofia_moderna.materia, assunto=filosofia_moderna),
        Aula(nomeAula='Filosofia Contemporânea - Foucault e a sociedade', url='https://www.youtube.com/watch?v=lrV47fKjvMA', descricaoAula='Poder e discurso', materia=filosofia_contemporanea.materia, assunto=filosofia_contemporanea),
        Aula(nomeAula='Ética e Moral - Diferenças e aplicações', url='https://www.youtube.com/watch?v=qFJ4OMPlA1Y', descricaoAula='Conceitos fundamentais da filosofia prática', materia=etica_moral.materia, assunto=etica_moral),
        Aula(nomeAula='Conhecimento e Verdade - Epistemologia básica', url='https://www.youtube.com/watch?v=zRUZy-ZRKnM', descricaoAula='Fontes do conhecimento humano', materia=conhecimento_verdade.materia, assunto=conhecimento_verdade),

        # Sociologia
        Aula(nomeAula='Teorias Sociológicas - Marx, Durkheim e Weber', url='https://www.youtube.com/watch?v=0cYfSOD4oQ4', descricaoAula='Principais pensadores da sociologia', materia=teorias_sociologicas.materia, assunto=teorias_sociologicas),
        Aula(nomeAula='Cidadania e Democracia', url='https://www.youtube.com/watch?v=ybWT3CRnZp8', descricaoAula='Direitos políticos e sociais', materia=cidadania_democracia.materia, assunto=cidadania_democracia),
        Aula(nomeAula='Cultura e Sociedade', url='https://www.youtube.com/watch?v=f-WWGGI1WAs', descricaoAula='Identidade cultural e comportamento', materia=cultura_sociedade.materia, assunto=cultura_sociedade),
        Aula(nomeAula='Desigualdade Social no Brasil', url='https://www.youtube.com/watch?v=ECtHVQY3INs', descricaoAula='Problemas estruturais e históricos', materia=desigualdade_social.materia, assunto=desigualdade_social),
        Aula(nomeAula='Movimentos Sociais - História e importância', url='https://www.youtube.com/watch?v=arFcFtd9Nyc', descricaoAula='Lutas por direitos no Brasil', materia=movimentos_sociais.materia, assunto=movimentos_sociais),

        # Literatura
        Aula(nomeAula='Romantismo no Brasil', url='https://www.youtube.com/watch?v=f8LL1HRz3EU', descricaoAula='Autores e características principais', materia=romantismo.materia, assunto=romantismo),
        Aula(nomeAula='Modernismo - Semana de Arte Moderna', url='https://www.youtube.com/watch?v=ELFw9zKhxq8', descricaoAula='Contexto e fases do movimento', materia=modernismo.materia, assunto=modernismo),
        Aula(nomeAula='Barroco e Arcadismo', url='https://www.youtube.com/watch?v=HeRoH9AbjcY', descricaoAula='Contrastes e influências literárias', materia=barroco.materia, assunto=barroco),
        Aula(nomeAula='Realismo e Naturalismo - Machado de Assis', url='https://www.youtube.com/watch?v=f14A9fMs8zU', descricaoAula='Crítica social e análise psicológica', materia=realismo.materia, assunto=realismo),
        Aula(nomeAula='Análise Literária - Como interpretar textos', url='https://www.youtube.com/watch?v=tnUak5Y1Zas', descricaoAula='Estratégias de leitura crítica', materia=analise_literaria.materia, assunto=analise_literaria),

        # Artes
        Aula(nomeAula='Artes Visuais - Elementos e História', url='https://www.youtube.com/watch?v=1PK3Jw1rJpA', descricaoAula='Do Renascimento à arte contemporânea', materia=artes_visuais.materia, assunto=artes_visuais),
        Aula(nomeAula='Música - Gêneros e Funções sociais', url='https://www.youtube.com/watch?v=7ElQZWQIq9E', descricaoAula='Cultura, expressão e arte sonora', materia=musica.materia, assunto=musica),
        Aula(nomeAula='Teatro - Linguagem Cênica', url='https://www.youtube.com/watch?v=0RwhKU1IeqA', descricaoAula='Elementos básicos do teatro', materia=teatro.materia, assunto=teatro),
        Aula(nomeAula='Cinema Brasileiro - História e Autores', url='https://www.youtube.com/watch?v=qPEduSAYi-U', descricaoAula='Movimentos e estilos do cinema nacional', materia=cinema.materia, assunto=cinema),
        Aula(nomeAula='História da Arte - Das cavernas à atualidade', url='https://www.youtube.com/watch?v=1UjcB2RJwR0', descricaoAula='Panorama histórico-artístico mundial', materia=historia_arte.materia, assunto=historia_arte),

        # Inglês
        Aula(nomeAula='Reading Comprehension - Estratégias de Leitura', url='https://www.youtube.com/watch?v=FMqxBWc1Zl8', descricaoAula='Compreensão textual para o ENEM', materia=leitura_ingles.materia, assunto=leitura_ingles),
        Aula(nomeAula='Text Genres - Tirinhas, propagandas e textos técnicos', url='https://www.youtube.com/watch?v=ZFFod6u4nOg', descricaoAula='Identificando o gênero textual', materia=generos_textuais_ingles.materia, assunto=generos_textuais_ingles),
        Aula(nomeAula='False Cognates - Falsos Amigos', url='https://www.youtube.com/watch?v=UeGzIokmvhY', descricaoAula='Palavras parecidas com significados diferentes', materia=false_cognates_ingles.materia, assunto=false_cognates_ingles),
        Aula(nomeAula='Connectors in English', url='https://www.youtube.com/watch?v=sQ2B7BcvQPU', descricaoAula='Conectivos e relações de sentido', materia=connectors_ingles.materia, assunto=connectors_ingles),
        Aula(nomeAula='Vocabulary in Context - Aprendizado natural', url='https://www.youtube.com/watch?v=GoS29t0xmhY', descricaoAula='Como entender palavras em textos', materia=vocabulario_ingles.materia, assunto=vocabulario_ingles),

        # Espanhol
        Aula(nomeAula='Comprensión de Lectura - Técnicas e exemplos', url='https://www.youtube.com/watch?v=6XZ7yX0yBMs', descricaoAula='Compreensão textual no espanhol do ENEM', materia=leitura_espanhol.materia, assunto=leitura_espanhol),
        Aula(nomeAula='Géneros Textuales - Tipos e finalidades', url='https://www.youtube.com/watch?v=OBbOSACWrCM', descricaoAula='Como identificar textos comuns', materia=generos_textuais_espanhol.materia, assunto=generos_textuais_espanhol),
        Aula(nomeAula='Falsos Cognados em Español', url='https://www.youtube.com/watch?v=3NYmAAhwxYg', descricaoAula='Diferenças entre palavras parecidas', materia=false_cognates_espanhol.materia, assunto=false_cognates_espanhol),
        Aula(nomeAula='Conectores - Uso em textos argumentativos', url='https://www.youtube.com/watch?v=1TKDiADbS6M', descricaoAula='Ligando ideias em espanhol', materia=connectors_espanhol.materia, assunto=connectors_espanhol),
        Aula(nomeAula='Vocabulario en Contexto', url='https://www.youtube.com/watch?v=9sbK9skZPEY', descricaoAula='Entendendo o vocabulário nos textos', materia=vocabulario_espanhol.materia, assunto=vocabulario_espanhol),
    ])

