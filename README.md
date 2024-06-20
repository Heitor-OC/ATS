# Ferramenta de ATS

ATS consiste em uma ferramenta de gerenciamento de gestão de processos de recrutamento, ou seja, torna o processo de seleção de candidatos mais ágil devido à filtragem dos currículos por meio de automações.

# REQUISITOS FUNCIONAIS DO PROJETO

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



# ENDPOINTS

# 1. Get Index "/"
Renderiza o arquivo index.html na página web

Parâmetros:
index.html

Exemplo de uso:
Obter a página inicial da API.

# 2. Upload PDF "/uploadpdf/"
Realiza o upload do arquivo pdf (Currículo) e da lista de habilidades (separadas por vírgula) para o Banco de Dados

Parâmetros:
Recebidos do client-side: Arquivo e lista de palavras-chave.
Enviados para o banco de dados:  Conteúdo, id do arquivo, nome do arquivo e lista de palavras.

Exemplo de uso:
Faz o upload do arquivo e lista de habilidades que vão ser analisados pela ATS.


# 3. Display Pdf Content "/pdfcontent/{pdf_content_id}/display"
Visualização do conteúdo do PDF por meio do arquivo pdf_content.html

Parâmetros:
ID do conteúdo do PDF, nome do arquivo.

Exemplo de uso:
Retorna uma string com o conteúdo do PDF.


# 4. Get All Pdfs "/pdfcontent/"
Retorna todos os arquivos cadastrados para criação da lista de PDFs no index.html

Parâmetros:
Lista dos PDFs.

Exemplo de uso:
Carrega todos os PDFs na página principal.


# 5. Delete Pdf Or Search Words "/pdfcontent/{pdf_content_id}/"
Exclui do Banco de Dados um arquivo e a lista de palavras-chave associada ao mesmo. 

Parâmetros:
ID do conteúdo do PDF.

Exemplo de uso:
Deleta os PDFs e a palavras-chave selecionadas.


# 6. Search words in Pdf "/pdfcontent/{pdf_content_id}/search/"
Retorna a lista de habilidades encontradas e não encontradas por meio de JSON para o endpoint "/pdfcontent/{pdf_content_id}/search/results"

Parâmetros:
Recebe: ID do conteúdo do PDF, lista de palavras-chave, conteúdo do PDF.
Retorna: ID do PDF, lista de palavras-chave encontradas e lista de palavras-chave não encontradas

Exemplo de uso:
Busca todas as palavras-chave dentro do conteúdo do PDF e depois retorna uma lista com as que encontrou e outra lista com os que não encontrou

# 7. Search Results Page "/pdfcontent/{pdf_content_id}/search/results"
Renderiza o arquivo search_results.html para visualização dos resultados (gráfico, nota, habilidades encontradas e não encontradas, porcentagem de coerência)

Parâmetros:
ID do PDF, palavras-chave encontradas, palavras-chave não encontradas, porcentagem de coerência de palavras-chave encontradas e nota baseada na porcentagem de coerência.

Exemplo de uso:
Mostra o resultado da analise feita pela ATS, mostrando palavras encontradas, palavras não encontradas, nota e a porcentagem de coerência.  

# TESTES
# 1. Testes envolvendo os PDFs:
Testar se a funcionalidade de upload de PDF, Exibição de PDFs Carregados e deleção de PDF estão funcionando.

# 2. Teste do cálculo de coerência:
Testar se os currículos estão sendo devidamente escaneados.

# 3. Teste de pontuação:
Testar se a nota está coerente com o determinado.

# 4. Teste da porcentagem:
Testar se a porcentagem está coerente com o determinado

# INSTALAÇÃO

Passo 1: Usar o seguinte comando no terminal (certifique-se de que está na raiz do projeto):

pip install uvicorn fastapi sqlalchemy pymupdf motor pymongo jinja2 pydantic alembic

Passo 2: Usar o seguinte comando no terminal na raiz do diretório para rodar o servidor: python -m uvicorn app.main:app --reload

Passo 3: Entrar na URL: http://127.0.0.1:8000/


# CONTRIBUIÇÃO
● Caiky Augusto Souza Abud
● Heitor Oliveira da Costa 
