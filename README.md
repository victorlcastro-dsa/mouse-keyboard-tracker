# mouse-keyboard-tracker

## Criar e ativar o ambiente virtual

### No Linux/macOS

```bash
python3.11 -m venv venv  # Cria o ambiente virtual com Python 3.11
source venv/bin/activate  # Ativa o ambiente virtual
```

## No Windows

```bash
python3.11 -m venv venv  # Cria o ambiente virtual com Python 3.11
venv\Scripts\activate  # Ativa o ambiente virtual
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar testes

```bash
python -m unittest discover -s tests
```

## Executar o monitoramento

```bash
python main.py
```
