#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
algorithms.py
Performs the required calculations for analysis
"""


def calc_forward_pe(curr_stock_price, estimated_eps):
    """
    Returns the forward PE

    Parameters
    ----------
    curr_stock_price : float
    estimated_eps : float

    Returns
    -------
    float
        forward PE
    """
    return curr_stock_price / estimated_eps


def calc_eps_cagr(initial_eps, ending_eps, span=3):
    """
    Returns CAGR for EPS

    Parameters
    ----------
    initial_eps : float
    ending_eps : float
    span : int, optional
        The default is 3

    Returns
    -------
    float
        EPS CAGR
    """
    return (ending_eps / initial_eps)**(1 / span) - 1


def calc_curr_pe(curr_stock_price, curr_eps):
    """
    Return current PE

    Parameters
    ----------
    curr_stock_price : [type]
        [description]
    curr_eps : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    return curr_stock_price / curr_eps


def calc_estimated_eps(curr_eps, eps_cagr, span=1):
    """[summary]

    Parameters
    ----------
    curr_eps : [type]
        [description]
    eps_cagr : [type]
        [description]
    span : int, optional
        [description] (the default is 1, which [default_description])

    Returns
    -------
    [type]
        [description]
    """

    return (eps_cagr + 1)**span * curr_eps
