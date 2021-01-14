#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:22:17 2021

@author: ralphsec
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.complete_graph(6)
nx.draw(G)
plt.show()
