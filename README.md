# Acompanhamento das Validações no TSE - Partido Político em Formação MISSAO

**Português** | [English](README-en-us.md)

O objetivo deste projeto é criar um relatório para acompanhar as validações dos apoiamentos coletados pelo partido em formação MISSAO no TSE (Tribunal Superior Eleitoral). Além disso, foi desenvolvido um comparativo dos apoiamentos validados de todos os partidos em processo de formação. A solução adotada importa dados de todos os partidos disponíveis no site oficial do TSE, permitindo que o número exato de partidos varie conforme novos postulantes surjam ou partidos existentes sejam excluídos por perda de prazo.

Os apoiamentos validados podem ser obtidos através do site oficial: [Partidos em Formação - TSE](https://www.tse.jus.br/partidos/criacao-de-partido/partidos-em-formacao). 

## Resumo da Solução Adotada

A coleta de dados do site do TSE é realizada em Python, utilizando a biblioteca Selenium. O arquivo .csv resultante dessa coleta é salvo em um diretório sincronizado com o SharePoint, um repositório colaborativo semelhante ao OneDrive da Microsoft. O relatório final é gerado em um cubo de dados tabular no Power BI, utilizando a solução gratuita de publicação na web. A fonte de dados do modelo tabular é o repositório SharePoint mencionado.

A publicação no Twitter é realizada por meio de um script em Python, utilizando a biblioteca Tweepy. Outras bibliotecas comuns também foram empregadas para maior conveniência, e todas as bibliotecas utilizadas podem ser encontradas no arquivo [Modulos.txt](Modulos.txt). Os dados incluídos nos tweets são obtidos por consultas DAX no modelo tabular, utilizando a REST API do Power BI.

## Conhecimentos Necessários

- **API Microsoft Entra**
- **API Power BI**
- **Python** (conceitos básicos da linguagem, bibliotecas Tweepy, Selenium e Requests)
- **Modelo Tabular do Power BI** (Power Query e linguagem DAX)

Esses são os conhecimentos necessários para implementar a solução completa, porém é perfeitamente possível adotar uma implementação parcial. Por exemplo, utilizamos o modelo tabular do Power BI para a visualização dos relatórios devido à sua facilidade em realizar cálculos complexos. Além disso, o Power BI permite a publicação gratuita dos relatórios na web. No entanto, você pode consumir os dados utilizando a solução que considerar mais conveniente.

## Configurando o Ambiente

Para adotar esta solução de forma completa, você precisará de:

- Uma conta no Power BI Service
- Acesso a um repositório do SharePoint Online
- Um aplicativo no Microsoft Entra para a geração de tokens de acesso à REST API do Power BI
- Uma conta de desenvolvedor do Twitter
- Python na versão 3.11.1 (versões mais recentes não devem causar problemas)

Também utilizamos uma trigger no Power Automate para atualizar automaticamente o modelo tabular do Power BI sempre que o diretório do SharePoint é atualizado.

Caso não tenha acesso a algum desses serviços, é possível adotar a solução de forma parcial e substituir os componentes conforme sua disponibilidade. Por exemplo, em vez de usar a trigger do Power Automate, você pode utilizar a própria REST API do Power BI para atualizar o modelo tabular.

### Configuração das Variáveis de Ambiente

O primeiro passo é configurar as variáveis de ambiente, que são as credenciais para acessar os serviços (Microsoft Entra, Power BI, Twitter). Todas as credenciais necessárias para adotar a solução completa podem ser visualizadas no arquivo [credenciais.txt](credenciais.txt). Salve uma cópia deste arquivo no diretório raiz com suas credenciais reais no formato .env.

### Documentações Adicionais

Para informações adicionais, as documentações das APIs e Bibliotecas utilizadas podem ser acessadas nos links abaixo:

- [Microsoft Entra](https://learn.microsoft.com/pt-br/graph/identity-network-access-overview)
- [REST API Power BI](https://learn.microsoft.com/pt-br/rest/api/power-bi/)
- [Selenium](https://www.selenium.dev/documentation/)
- [Tweepy](https://docs.tweepy.org/en/stable/)
- [Twitter API](https://developer.x.com/en/docs/twitter-api)

### Observações Adicionais

O diretório sincronizado com o SharePoint deverá conter a pasta [Arquivos](Arquivos), que será o repositório dos outputs .csv da raspagem de dados. A pasta Arquivos neste repositório do GitHub muito provavelmente estará desatualizada em relação aos arquivos .csv de datas mais recentes. Os arquivos .csv mais recentes podem ser obtidos por este [link](https://www.dropbox.com/scl/fo/f1unxkrpy8wqh19wm9fbf/ADeOmtksP50NWqRu9T4Gvgs?rlkey=1owwc01plrlycnjgcdxew1bn2&st=fcerw9pp&dl=0).

No mesmo diretório sincronizado, deverá ser copiada a pasta [Parametros](Parametros). Esta pasta contém arquivos com os atributos básicos e inalteráveis do cubo tabular, como imagens das bandeiras, siglas dos estados, número mínimo de apoiamentos por estado, estimativa da validação realizada pelo Aliança, dias não úteis, etc. Esses parâmetros precisam ser importados uma única vez no modelo tabular, podendo ser desativada a opção "Incluir na atualização do relatório".

Toda a estrutura e as métricas do cubo tabular estão no arquivo [ContagemMissão.pbit](ContagemMissão.pbit). Ao abri-lo pela primeira vez, configure as credenciais de acesso ao diretório do SharePoint no PowerQuery, na tabela de somente conexão chamada "conexão" no folder "ConexãoSharePoint".

No .pbit deste repositório, as pastas de "Arquivos" e "Parâmetros" estão localizadas em um diretório chamado "Validacao TSE" dentro de "Documentos Compartilhados" do site do SharePoint Online. A solução a ser adotada fica a seu critério, desde que as tabelas finais do Power Query sejam mantidas como estão.

Caso você utilize o print do resumo no tweet, deverá existir um relatório Power BI público na web que será a fonte do screenshot. O relatório usado para o resumo está no arquivo [Imagem.pbit](Imagem.pbit). Também será necessário alterar o script [ImageMatriz.py](ImageMatriz.py), substituindo o link e configurando as dimensões do screenshot.

O relatório público em Power BI, obtido com este projeto, pode ser acessado com este [link](https://app.powerbi.com/view?r=eyJrIjoiMmVkZjM0ODEtNjkyMi00NjliLTlkYTgtNDE3ODg0ZTE1NDhlIiwidCI6ImFkY2JiMThhLWE3NzEtNDU5OS04YjllLWFiM2IzNmE3NWY1MSJ9).
