#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stocksensecli/stocksense/controllers/base.py

"""

from cement import Controller, ex
from cement.utils.version import get_version_banner
from PyInquirer import Separator, Token, prompt, style_from_dict

from ..controllers.validators import EmptyValidator
from ..core import algorithms as algos
from ..core import helpers as hlprs
from ..core.version import get_version

VERSION_BANNER = """
Performs the magic of stock analysis %s
%s
""" % (get_version(), get_version_banner())

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Performs the magic of stock analysis'

        # text displayed at the bottom of --help output
        epilog = 'Usage: stocksense command <subcommand> <args>'

        # controller level arguments. ex: 'stocksense --version'
        arguments = [
            # add a version banner
            (['-v', '--version'], {
                'action': 'version',
                'version': VERSION_BANNER
            }),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='test command',

        # sub-command level arguments. ex: 'stocksense command1 --foo bar'
        arguments=[
            # add a sample foo option under subcommand namespace
            (['-f', '--foo'], {
                'help': 'notorious foo option',
                'action': 'store',
                'dest': 'foo'
            }),
        ],
    )
    def test(self):
        """Example test command."""

        data = {
            'foo': 'bar',
        }

        # do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo
        self.app.render(data, 'command1.jinja2')


class Analyse(Controller):
    class Meta:
        label = 'analyse'
        description = "Perform your stock analysis in one go"
        stacked_on = 'base'
        stacked_type = 'nested'

    @ex(
        help='Stock analysis ',

        # sub-command level arguments. ex: 'stocksense command1 --foo bar'
        arguments=[
            # add a sample foo option under subcommand namespace
            (['-f', '--foo'], {
                'help': 'notorious foo option',
                'action': 'store',
                'dest': 'foo'
            }),
        ],
    )
    def forward_pe(self):
        """Example test command."""
        forward_pe_info = self.ask_forward_pe_info()

        curr_eps = float(forward_pe_info.get('ending_eps'))
        eps_cagr = algos.calc_eps_cagr(
            float(forward_pe_info.get('initial_eps')), curr_eps,
            float(forward_pe_info.get('span')))
        curr_stock_price = float(forward_pe_info.get('curr_stock_price'))
        estimated_eps = algos.calc_estimated_eps(curr_eps, eps_cagr)
        current_pe = algos.calc_curr_pe(curr_stock_price, curr_eps)
        forward_pe = algos.calc_forward_pe(curr_stock_price, estimated_eps)
        print_col = "red"

        if forward_pe < current_pe:
            print_col = "green"

        hlprs.log("1 Yr. Forward PE: " + str(forward_pe), print_col)

    def ask_forward_pe_info(self):
        """[summary]

        Returns
        -------
        [type]
            [description]
        """

        questions = [{
            'type': 'input',
            'name': 'initial_eps',
            'message': 'Initial EPS',
            'validate': EmptyValidator
        },
                     {
                         'type': 'input',
                         'name': 'ending_eps',
                         'message': 'Ending EPS',
                         'validate': EmptyValidator
                     },
                     {
                         'type': 'input',
                         'name': 'span',
                         'message': 'SPAN (Number of Years)',
                         'validate': EmptyValidator
                     },
                     {
                         'type': 'input',
                         'name': 'curr_stock_price',
                         'message': 'Current Stock Price',
                         'validate': EmptyValidator
                     },
                     {
                         'type': 'confirm',
                         'name': 'calculate',
                         'message': 'Calculate'
                     }]
        return prompt(questions, style=style)
