# Extrator de Documentos

Este script foi desenvolvido para extrair conteúdo de texto de diversos tipos de arquivos, incluindo PDFs e imagens. O texto extraído é então processado usando um serviço de IA (neste caso, o `GeminiApi`) para obter informações ou insights adicionais.

## Pré-requisitos

- Python 3.x instalado em sua máquina.
- Os pacotes Python necessários podem ser instalados com o seguinte comando:

  ```bash
  pip install -r requirements.txt
  ```

## Uso

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-nome/extrator-de-documentos.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd extrator-de-documentos
   ```

3. Execute o script com as opções desejadas:

   ```bash
   python main.py -f /caminho/para/seu/arquivo.pdf -t pdf_text
   ```

   Substitua `/caminho/para/seu/arquivo.pdf` pelo caminho real do seu arquivo e `pdf_text` pelo tipo de arquivo desejado.

## Opções da Linha de Comando

- `-f, --file_path`: Especifique o caminho do arquivo que deseja processar.
- `-t, --file_type`: Especifique o tipo de arquivo a ser processado (`pdf_image`, `pdf_text`, `image` ou `text`).

## Exemplo

```bash
python main.py -f arquivo.pdf -t pdf_image
```

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).