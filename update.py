name: IPTV AUTO

on:
  schedule:
    - cron: '0 */6 * * *'
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - run: pip install requests

    - run: python update.py

    - run: |
        git config --global user.name "bot"
        git config --global user.email "bot@github.com"
        git add lista.m3u
        git commit -m "auto update" || echo "no changes"
        git push
