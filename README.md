# Prediction Markets QTS

Quantitative trading strategy for prediction markets

FINM 33150 QTS Winter 2026 - Final Project Group Live: M

---

## TODO
- [ ] Get data: J Becker's github exposes ~36gb of data from 2021-2024 he collected from kalshi and polymarket's api but is stored in his personal S3. Find a way to get data directly from APIs
- [ ] Implement strategy MVP
- [ ] Write draft ipynb

## Setup

### Installing dependencies

1. Using uv[^1]
[^1]: [Installation](https://docs.astral.sh/uv/getting-started/installation/)
```bash
uv sync
```

2. See 1.

## Development

```bash
make sync      # install dependencies
make test      # run tests
make lint      # ruff check
make clean     # remove caches and build artifacts
```

## Project Structure

```
src/prediction_market_qts/   # logic goes here
scripts/                     # standalone scripts
notebooks/                   # jupyter notebooks
tests/                       # pytest suite
data/                        # gitignored
```

## Acknowledgements
[The Microstructure of Wealth Transfer in Prediction Markets](https://www.jbecker.dev/research/prediction-market-microstructure) - Jonathan Becker


## License

The Unlicense
