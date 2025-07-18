# Author: Aric Hagberg (hagberg@lanl.gov)

#    Copyright (C) 2005-2019 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

from email.utils import getaddresses, parseaddr
import mailbox
import sys

import matplotlib.pyplot as plt
import networkx as nx

# unix mailbox recipe
# see https://docs.python.org/3/library/mailbox.html

def mbox_graph():
    mbox = mailbox.mbox("unix_email.mbox")  # parse unix mailbox

    G = nx.MultiDiGraph()  # create empty graph

    # parse each messages and build graph
    for msg in mbox:  # msg is python email.Message.Message object
        (source_name, source_addr) = parseaddr(msg['From'])  # sender
        # get all recipients
        # see https://docs.python.org/3/library/email.html
        tos = msg.get_all('to', [])
        ccs = msg.get_all('cc', [])
        resent_tos = msg.get_all('resent-to', [])
        resent_ccs = msg.get_all('resent-cc', [])
        all_recipients = getaddresses(tos + ccs + resent_tos + resent_ccs)
        # now add the edges for this mail message
        for (target_name, target_addr) in all_recipients:
            G.add_edge(source_addr, target_addr, message=msg)

    return G


if __name__ == '__main__':

    G = mbox_graph()

    # print edges with message subject
    for (u, v, d) in G.edges(data=True):
        print("From: %s To: %s Subject: %s" % (u, v, d['message']["Subject"]))     
    pos = nx.spring_layout(G, iterations=10)
    nx.draw(G, pos, node_size=12, alpha=0.4, edge_color='b', font_size=16, with_labels=True)
    plt.show()