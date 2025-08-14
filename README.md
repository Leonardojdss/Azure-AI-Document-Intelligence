# Azure AI Document Intelligence

Este projeto demonstra como usar o Azure AI Document Intelligence para extrair dados de documentos usando modelos customizados. O Azure Document Intelligence é um serviço de IA que aplica tecnologia avançada de machine learning para identificar e extrair texto, pares chave-valor, tabelas e estruturas de documentos automaticamente.

## 📋 Funcionalidades

- **Análise de Documentos**: Extração automática de dados de documentos usando modelos customizados
- **Detecção de Campos**: Identificação e extração de campos específicos com níveis de confiança
- **Suporte a Múltiplos Formatos**: Compatível com imagens (JPG, PNG) e PDFs
- **Análise em Lote**: Processamento de múltiplos documentos

## 🏗️ Estrutura do Projeto

```
Azure-AI-Document-Intelligence/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências do projeto
├── README.md             # Documentação
├── .env                  # Variáveis de ambiente (não versionado)
├── env/                  # Ambiente virtual Python
└── examples_docs/        # Documentos de exemplo
    ├── training/         # Documentos para treinamento do modelo
    │   ├── Form_1.jpg
    │   ├── Form_2.jpg
    │   ├── Form_3.jpg
    │   ├── Form_4.jpg
    │   └── Form_5.jpg
    └── validation/       # Documentos para teste
        └── test1.jpg
```

## 🚀 Começando

### Pré-requisitos

- Python 3.8 ou superior
- Conta do Azure com acesso ao Azure AI Document Intelligence
- Azure Storage Account para armazenar documentos de treinamento
- Modelo customizado treinado no Azure AI Document Intelligence Studio

### Configuração do Azure

1. **Crie um recurso do Azure AI Document Intelligence**:
   - Acesse o [Portal do Azure](https://portal.azure.com)
   - Crie um novo recurso "Document Intelligence"
   - Anote o endpoint e a chave de API

2. **Configure o Azure Blob Storage para documentos de treinamento**:
   
   a) **Crie uma Storage Account**:
   - No Portal do Azure, crie um novo recurso "Storage Account"
   - Escolha um nome único para sua storage account
   - Selecione a mesma região do Document Intelligence
   
   b) **Crie um container para os documentos**:
   - Acesse sua Storage Account
   - Vá em "Containers" no menu lateral
   - Clique em "+ Container"
   - Nome sugerido: `training-documents`
   - Nível de acesso: **Blob (acesso de leitura anônimo apenas para blobs)**
   
   c) **Faça upload dos arquivos de treinamento**:
   - No Portal do Azure, acesse seu container
   - Clique em "carregar"
   - Selecione todos os arquivos da pasta `examples_docs/training/`
   - Clique em "carregar"


3. **Treine um modelo customizado**:
   - Acesse o [Document Intelligence Studio](https://documentintelligence.ai.azure.com/)
   - Acesse o modelo de extração customizado
   - Crie um novo projeto
   - **Configure a fonte de dados**:
     - Selecione "Azure Blob Storage"
     - Insira a URL do seu container: `https://<sua-storage-account>.blob.core.windows.net/training-documents`
     - Configure as credenciais de acesso se necessário
   - O sistema carregará automaticamente seus documentos do Blob Storage
   - Faça a rotulação dos campos nos documentos, rotule os campos name vendor e total
   - Treine com o build "template"
   - Após treinado o modelo, teste-o com o documento da pasta `examples_docs/validation/`

### Utilizar o code python para extração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Leonardojdss/Azure-AI-Document-Intelligence.git
   cd Azure-AI-Document-Intelligence
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv env
   source env/bin/activate  # No Windows: env\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   DOC_INT_ENDPOINT=https://your-document-intelligence-endpoint.cognitiveservices.azure.com/
   DOC_INT_API_KEY=your-api-key-here
   MODEL_ID=your-custom-model-id
   ```

## 💻 Uso

### Execução Básica

```bash
python app.py
```

### Exemplo de Saída

```
--------Analyzing document #1--------
Document has type model-template:model-template
Document has confidence 0.591
Document was analyzed by model with ID model-template
Found field 'Total' with value '$7350.00' and with confidence 0.994
Found field 'Vendor Name' with value 'Seth Stanley' and with confidence 0.99
-----------------------------------
```