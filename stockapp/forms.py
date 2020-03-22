# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 01:36:12 2020

@author: Sayantan
"""

from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]