name: python run

on:
    push:
      branches: ["main"]
    workflow_dispatch:

jobs:
    run script:
        runs-on: ubuntu-latest

        steps:
            - name: checkout repository
              uses: actions/checkout@v4

            - name: set up python
              uses: actions/setup-python@v5
              with:
                  python-version: '3.10'

            - name: run python file
              run: python main.py
