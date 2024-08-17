# Monitoring Validations at the TSE - Political Party in Formation MISSAO

[Português](README.md) | **English** 

The goal of this project is to create a report to monitor the validations of support collected by the Political Party in formation MISSAO at the TSE (Tribunal Superior Eleitoral) in the country Brazil. Additionally, a comparative analysis of the validated support for all parties in the formation process was developed. The adopted solution imports data from all parties available on the official TSE website, allowing the exact number of parties to vary as new candidates emerge or existing parties are excluded due to missed deadlines.

The validated support can be obtained through the official website: [Partidos em Formação - TSE](https://www.tse.jus.br/partidos/criacao-de-partido/partidos-em-formacao).

## Summary of the Adopted Solution

Data collection from the TSE website is performed in Python, using the Selenium library. The resulting .csv file from this collection is saved in a directory synchronized with SharePoint, a collaborative repository similar to Microsoft OneDrive. The final report is generated in a tabular data cube in Power BI, using the free solution for web publishing. The data source for the tabular model is the mentioned SharePoint repository.

Publishing on Twitter is done through a Python script using the Tweepy library. Other common libraries were also employed for convenience, and all the libraries used can be found in the file [Modulos.txt](Modulos.txt). The data included in the tweets is obtained by DAX queries on the tabular model, using the Power BI REST API.

## Required Knowledge

- **API Microsoft Entra**
- **API Power BI**
- **Python** (basic language concepts, Tweepy, Selenium, and Requests libraries)
- **Power BI tabular model** (Power Query and DAX language)

These are the required skills to implement the complete solution, but it is entirely possible to adopt a partial implementation. For example, we used the Power BI tabular model for report visualization due to its ease in performing complex calculations. Additionally, Power BI allows free web publishing of the reports. However, you can consume the data using the solution you find most convenient.

## Setting Up the Environment

To fully adopt this solution, you will need:

- A Power BI Service account
- Access to a SharePoint Online repository
- An app in Microsoft Entra for generating access tokens to the Power BI REST API
- A Twitter developer account
- Python version 3.11.1 (more recent versions should not cause issues)

We also used a trigger in Power Automate to automatically update the Power BI tabular model whenever the SharePoint directory is updated.

If you do not have access to some of these services, it is possible to adopt the solution partially and replace components as per your availability. For instance, instead of using the Power Automate trigger, you can use the Power BI REST API itself to update the tabular model.

### Configuring Environment Variables

The first step is to configure the environment variables, which are the credentials to access the services (Microsoft Entra, Power BI, Twitter). All the credentials necessary to adopt the complete solution can be found in the [credenciais.txt](credenciais.txt) file. Save a copy of this file in the root directory with your actual credentials in .env format.

### Additional Documentation

For additional information, the documentation for the APIs and Libraries used can be accessed through the following links:

- [Microsoft Entra](https://learn.microsoft.com/en-us/graph/identity-network-access-overview)
- [REST API Power BI](https://learn.microsoft.com/en-us/rest/api/power-bi/)
- [Selenium](https://www.selenium.dev/documentation/)
- [Tweepy](https://docs.tweepy.org/en/stable/)
- [Twitter API](https://developer.x.com/en/docs/twitter-api)

### Additional Notes

The directory synchronized with SharePoint must contain the [Arquivos](Arquivos) folder, which will be the repository for the .csv outputs of the data scraping. The "Arquivos" folder in this GitHub repository will most likely be outdated compared to the more recent .csv files. The latest .csv files can be obtained through this [link](https://www.dropbox.com/scl/fo/f1unxkrpy8wqh19wm9fbf/ADeOmtksP50NWqRu9T4Gvgs?rlkey=1owwc01plrlycnjgcdxew1bn2&st=fcerw9pp&dl=0).

In the same synchronized directory, the [Parametros](Parametros) folder should be copied. This folder contains files with the basic and unchangeable attributes of the tabular cube, such as flag images, state acronyms, minimum support number per state, validation estimate by Aliança, non-working days, etc. These parameters need to be imported only once into the tabular model, with the option "Include in report refresh" disabled.

The entire structure and metrics of the tabular cube are in the [ContagemMissão.pbit](ContagemMissão.pbit) file. Upon opening it for the first time, configure the access credentials to the SharePoint directory in Power Query, in the connection-only table called "conexão" in the "ConexãoSharePoint" folder.

In the .pbit from this repository, the "Arquivos" and "Parametros" folders are located in a directory called "Validacao TSE" within "Documentos Compartilhados" of the SharePoint Online site. The solution to be adopted is up to you, as long as the final Power Query tables are maintained as they are.

If you use the summary print in the tweet, there must be a public Power BI report on the web that will be the source of the screenshot. The report used for the summary is in the [Imagem.pbit](Imagem.pbit) file. It will also be necessary to modify the [ImageMatriz.py](ImageMatriz.py) script, replacing the link and configuring the screenshot dimensions.

The public Power BI report obtained with this project can be accessed through this [link](https://app.powerbi.com/view?r=eyJrIjoiMmVkZjM0ODEtNjkyMi00NjliLTlkYTgtNDE3ODg0ZTE1NDhlIiwidCI6ImFkY2JiMThhLWE3NzEtNDU5OS04YjllLWFiM2IzNmE3NWY1MSJ9).