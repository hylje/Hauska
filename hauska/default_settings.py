# -*- encoding: utf-8 -*-
# Konffattavia juttuja tähän

# polku git-repon juureen
from os.path import dirname, abspath, join
PROJECT_DIR = dirname(dirname(abspath(__file__)))

DATABASE = join(PROJECT_DIR, "hauska.sqlite")
DEBUG = True
