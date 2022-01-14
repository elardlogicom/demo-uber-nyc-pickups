# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:31:34 2021

@author: Elliot Lard
"""
import seaborn as sns
import streamlit as st
import pandas as pd
from datetime import timedelta
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime


def text_area(label):
    final_comment.append(label)
    inp = st.text_area(label)
    final_comment.append(inp)
    return inp
def radio(label, ls):
    final_comment.append(label)
    inp = st.radio(label, ls)
    final_comment.append(inp)
    return inp
def text_input(label):
    final_comment.append(label)
    inp = st.text_input(label)
    final_comment.append(inp)
    return inp
def write(text):
    final_comment.append(text)
    final_comment.append('\n')
    st.write(text)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
up_down = ('Up', 'Down')
yes_no = ('Yes', 'No')
gro = ('Green', 'Red', 'Off')


with st.sidebar.expander('select ONT info'):
    ont_fiber_aoe = st.selectbox('ONT Fiber', up_down)
    ont_lan_aoe = st.selectbox('ONT LAN', up_down)
    uptime = st.number_input('ONT Uptime', 0, step=1)
    service_status = st.selectbox('Service Status', ['Active', 'Suspended'])
    upstream_BIP = st.number_input('Upstream BIP', 0, step=1)
    downstream_BIP = st.number_input('Downstream BIP', 0, step=1)
    ip = st.text_input('ip address', '192.168.1.1')
    olt_rx = st.number_input('OLT RX Power (RSSI) dBm', -17.2, step = 0.1)
    ont_rx = st.number_input('ONT RX Power (dBm)', -18.2, step = 0.1)
    ont_tx = st.number_input('ONT TX Power (dBm)', 1.5, step = 0.1)
with st.sidebar.expander('ONT Info'):
    st.write('Ticket No. 145828')
    st.write('Name: John Doe')
    st.write('Callback Number: 8188889023')
    st.write('Account Number: 5687413')
    st.write('Service Address: 21 Jump St')
    st.write('ONT fiber: ' + ont_fiber_aoe)
    st.write('ONT LAN: ' + ont_lan_aoe)
    st.write('ONT Uptime: ' + str(uptime))
    st.write('Service Status: ' + service_status)
    st.write('Service Package: Res 300mbps')
    st.write('IP Address: ' + ip)
    st.write('Upstream BIP: ' + str(upstream_BIP))
    st.write('Downstream BIP: ' + str(downstream_BIP))
    st.write('OLT RX Power (RSSI) dBm: ' + str(olt_rx))
    st.write('ONT RX Power (dBm): ' + str(ont_rx))
    st.write('ONT TX Power (dBm): ' + str(ont_tx))
    st.button('Paste to Commnet')
    st.button('Refresh')
    
issues = ['(QOS) Slow Internet Troubleshooting', '(LOS) No Internet All Devices', 'Intermittent Internet', 'Slow Speeds', 'Customer Service', 'Member Equipment', 'Voice', 'Video']

final_comment = []


text_area('Member Description of Issue')

member_issue = st.selectbox("Member Issue", issues)

if member_issue == '(LOS) No Internet All Devices':
    radio('ONT Status:', ['Up', 'Discovering'])
    text_input('ONT Uptime:')
    text_input('Device Location:')
    
    st.write('Reboot ONT and RG [wiki](http://xwiki.logicom.center:8080/xwiki/bin/view/T1/All%20COOPS/Proper%20ONTRG%20Reboot%20Sequence%20%28All%20COOPs%20except%20NAEC%29/)')
    
    write('ONT Status Before Reboot:')
    cols = st.columns(3)
    with cols[0]: radio('ONT Power Before Reboot:', gro)
    with cols[1]: radio('ONT Fiber Before Reboot:', gro)
    with cols[2]: radio('ONT LAN Before Reboot:', gro)
    
    write('Cabling:')

    st.checkbox('Checked Cabling')
    st.checkbox('Reboot ONT:')
    st.checkbox('Reboot RG:')
    # cols = st.columns(3)
    # with cols[0]: radio('Checked Cabling:', yes_no)
    # with cols[1]: ont_reboot = radio('Reboot ONT:', yes_no)
    # with cols[2]: radio('Reboot RG:', yes_no)
    
    # if(ont_reboot=='Yes'):
    #     write('ONT Status After Reboot:')
    #     cols = st.columns(3)
    #     with cols[0]: radio('ONT Power After Reboot:', gro)
    #     with cols[1]: radio('ONT Fiber After Reboot:', gro)
    #     with cols[2]: radio('ONT LAN After Reboot:', gro)
    text_area('Result:')

with st.expander('Resolution Box'):

    col = st.columns(2)
    with col[0]:st.selectbox('Issue Code', ['CS customer service', 'QOS - speed', 'LOS - ONT fiber', 'LOS - damaged fiber'])
    with col[1]: t1_res = st.selectbox('Tier 1 Resolution', ['escalation', 'TS - reboot ONT/RG', 'RG - 2.4ghz/5ghz separation/education'])
    if t1_res == 'escalation': st.selectbox('escalation', ['External Standard - Internet', 'Internal Internet'])
   
    final_notes = '\n'.join(final_comment)

    st.text_area('Final Commnet', final_notes,height = 300)
    st.button('submit')