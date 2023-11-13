# Taxly case

O case da taxly consiste em criar um microserviço em container de uma aplicação responsável por receber arquivos PDF com texto, e a partir destes arquivos extrair informações a fim de serem utilizadas posteriormente para validar pagamentos. O projeto deve ser validado por meio de um token único de segurança e não necessita de front-end.

A linguagem de programação escolhida para o projeto foi o Python devido ao grande número de bibliotecas disponíveis para lidar com arquivos PDF e a facilidade de uso. O framework python selecionado foi o Flask com o uso do banco de dados não relacional mongoDB.

## Configuração do projeto

- Copie o arquivo `.env.example` para o arquivo `.env`.
  - Monte a url do mongoDB e substitua na variável `DATABASE_URI`
- Abra um terminal na raiz do projeto e rode o comando `make up`.
- O projeto deverá estar rodando no endereço http://localhost:5000.
- Opcional: rode o comando `make update` quando atualizar o código para ter efeito.

## Endpoint

### Request

`POST /upload`

    curl --location --request POST 'http://localhost:5000/upload' \
    --header 'Authorization: Bearer my-app-token' \
    --form 'files[]=@"/path-to-file.pdf"'

Este endpoint aceita 1 ou mais arquivos pdf de texto para a extração de dados.

### Response

Este é um exemplo de response contendo um comprovante, um DAS, um DAMSP e um arquivo não PDF.

    [
        {
            "extrated_data": {
                "amount": 1234.56,
                "bar_code": "00000000000 00000000000 00000000000 00000000000",
                "cnpj": "00.000.000/0000-00",
                "payment_date": "12/11/2023",
                "receipt": true
            },
            "filename": "file-comprovante.pdf"
        },
        {
            "extrated_data": {
                "amount": 6543.21,
                "cnpj": "11.111.111/1111-11",
                "doc_month": "Novembro/2023",
                "doc_type": "DAS",
                "due_date": "12/11/2023",
                "receipt": false,
                "social_reason": "TEST COMPANY LTDA"
            },
            "filename": "DAS-file.pdf"
        },
        {
            "extrated_data": {
                "amount": 888.88,
                "bar_code": "11111111111-2 11111111111-2 11111111111-2 11111111111-2",
                "cnpj": "22.222.222/2222-22",
                "doc_month": "11/2023",
                "doc_type": "DAMSP",
                "due_date": "12/11/2023",
                "receipt": false,
                "social_reason": "TEST COMPANY 2 LTDA"
            },
            "filename": "DAMSP-file.pdf"
        },
        {
            "error": "File is not a PDF",
            "filename": "not-a-pdf"
        }
    ]

### Dados extraídos

Os dados estão sendo extraídos de acordo com padrões REGEX configurados de acordo com os documentos utilizados para a criação do microserviço. Os dados são:

- receipt -> Booleano indicando se o arquivo é recibo ou não.
- social_reason -> Razão social no arquivo.
- due_date -> Data de validade para arquivos que não são recibos.
- payment_date -> Data de pagamento para arquivos que são recibos.
- bar_code -> Código de barras no arquivo.
- amount -> Valor total no arquivo.
- cnpj -> CNPJ no arquivo.
- doc_type -> Se o arquivo não for recibo, identifica o tipo de doc_type(DAS ou DAMSP)

Para extração de novos dados, deverão ser mapeados por padrão REGEX e inseridos na response do endpoint.
