# Probabilis

Biblioteca Python para análise de dados e processamento de sinais em ciências da reabilitação.

## Instalação

Após publicação no PyPI:

```bash
pip install probabilis
```

Para desenvolvimento local, na pasta do projeto:

```bash
pip install -e .
```

## Uso

```python
import probabilis as pb

pb.resumo(dados)
```

Também é possível importar módulos diretamente:

```python
from pb import emg, cop, imu, plotting, utils
```

## Módulos

| Módulo | Funções disponíveis |
|---|---|
| `cop` | `computar_freqs`, `computar_area_elipse_cop` |
| `emg` | `filt_emg` |
| `imu` | `calcular_freeacc` |
| `plotting` | `stat_diff` |
| `utils` | `resumo`, `media_movel` |

O notebook `examples/basic_usage.ipynb` e os dados de exemplo foram preservados.

## Desenvolvimento e publicação

1. Edite os módulos em `src/probabilis/` e execute `python -m pytest`.
2. Atualize a versão em `pyproject.toml` e faça commit/push para o GitHub.
3. Crie uma tag igual à versão, por exemplo `git tag v0.1.0`, e envie com `git push origin v0.1.0`.
4. O workflow do GitHub Actions construirá o pacote e publicará no PyPI quando o Trusted Publishing estiver configurado.

**Configuração inicial:** crie um repositório GitHub, configure no PyPI um Trusted Publisher apontando para esse repositório e para `.github/workflows/publish.yml`, e associe o ambiente `pypi` no GitHub. Verifique antes se o nome `probabilis` está disponível no PyPI.

Para verificar o pacote localmente:

```bash
python -m pip install build pytest
python -m build
python -m pytest
```

## Licença

MIT. Consulte `LICENSE`.
