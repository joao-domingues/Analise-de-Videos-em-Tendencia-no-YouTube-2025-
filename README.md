# Análise de Vídeos em Tendência no YouTube (2025)

Projeto de **Análise de Dados / Business Intelligence (BI)** desenvolvido para **portfólio**, utilizando **Python** e **Jupyter Notebook**.  
O foco do projeto é a **exploração, tratamento e análise de dados reais**, com geração de insights sobre **engajamento e desempenho de canais**, especialmente no **Brasil (BR)**.

---

## Objetivo

Demonstrar habilidades práticas essenciais para vagas de **Analista de Dados / BI**, incluindo:

- Limpeza e padronização de dados
- Tratamento de diferentes tipos de dados (texto, numérico e datas)
- Análise exploratória (EDA)
- Geração de métricas de engajamento
- Visualização de dados para apoio à tomada de decisão

---

## 🗂️ Dataset Utilizado

- **Fonte:** Kaggle  
- **Nome:** *YouTube Trending Videos 2025 (Updated Daily)*  
- **Link:**  
  https://www.kaggle.com/datasets/sebastianbesinski/youtube-trending-videos-2025-updated-daily  

O dataset contém registros diários de vídeos em tendência no YouTube, incluindo métricas de visualização, curtidas e comentários por país.

## 🛠️ Tecnologias e Ferramentas

- **Python 3**
- **Pandas** (manipulação e análise de dados)
- **NumPy**
- **Matplotlib** (visualização)
- **Seaborn** (visualização estatística)
- **Jupyter Notebook**

---

## 🧹 Tratamento e Preparação dos Dados

Etapas realizadas no pipeline de dados:

- Conversão dos tipos de arquivo
- Padronização de formatos de data
- Tratamento de valores inválidos e ausentes
- Otimização de memória
- Criação de subconjunto específico para análise do **Brasil (BR)**

---

## Análises Desenvolvidas

### 1. Avaliação de Qualidade dos Dados
- Heatmap para identificação de valores nulos no dataset
<img width="1270" height="699" alt="Examining Missing Values" src="https://github.com/user-attachments/assets/ae2c959f-d7f4-4dc6-8620-a11f4411ec42" />

### 2. Top 10 Canais com Mais Visualizações no Brasil
- Agregação de visualizações por canal
- Identificação de canais com maior alcance
<img width="1400" height="800" alt="10 canais mais assistidos no Brasil" src="https://github.com/user-attachments/assets/f8c90d90-cead-49ac-84f1-1ebf4bd6b184" />

### 3. Top 10 Canais com Mais Likes no Brasil
- Análise de engajamento por canal
- Comparação entre volume de views e curtidas
<img width="1753" height="600" alt="10 canais mais likes no Brasil" src="https://github.com/user-attachments/assets/9a62b325-27df-4896-9f17-4ca9f221fff9" />

### 4. Relação entre Views e Likes
- Scatter plot global
<img width="640" height="480" alt="likes vs views" src="https://github.com/user-attachments/assets/7c576b94-86b4-4e5a-9374-2a34cc0d747e" />

- Scatter plot específico para o Brasil
<img width="640" height="480" alt="likes vs views brasil" src="https://github.com/user-attachments/assets/8e7dd183-cd98-48dd-bae1-30809b5a1782" />

---

##  Como Executar o Projeto

1. Clone o repositório: git clone https://github.com/seu-usuario/nome-do-repositorio.git
2. pip install pandas numpy matplotlib seaborn
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
