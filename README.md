# Ferramenta de ATS

ATS consiste em uma ferramenta de gerenciamento de gestão de processos de recrutamento, ou seja, torna o processo de seleção de candidatos mais ágil devido à filtragem dos currículos por meio de automações.

# Requisitos Funcionais do projeto

# 1. Upload de Currículo
Faz o upload de um currículo no formato de pdf

# 2. Deleção de Currículo
Exclui um currículo do Banco de Dados

# 3. Cadastro de Palavras-Chave
Associa uma lista de palavras-chave, que devem ser separadas por vírgula, a um currículo. As palavras-chave são as habilidades que estão descritas na vaga que deseja analisar, ou seja, são as habilidades que a ferramenta irá procurar no arquivo do currículo.

# 4. Visualização do Conteúdo do Currículo
Demonstra o conteúdo textual do currículo por meio de HTML

# 5. Identificação das Palavras-Chave dentro do arquivo
Realiza a procura de habilidades dentro do texto do arquivo, as habilidades que serão procuradas são as palavras contidas na lista de palavras-chave que estará associada ao currículo.

# 6. Cálculo de Coerência do Currículo com a Vaga
Realiza o cálculo baseado na porcentagem de habilidades que foram encontradas em relação ao total de habilidades que foram repassadas por meio da lista de palavras-chave

#7. Atribuição de nota baseada na porcentagem de coerência do Currículo com a Vaga
Atribui uma nota (A, B, C, D, F) de acordo com a porcentagem de coerência ( >90%, >80%, >70%, >60%, <50% ).

# 7. Listagem das Habilidades Econtradas
Visualização da lista de habilidades encontradas e da lista de habilidades não encontradas



# Endpoints
# 1.
