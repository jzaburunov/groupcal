# -*- coding: utf-8 -*-

# from datetime import timedelta, date, datetime
#
# import pytz
#
# from openerp import models, fields, api, _, tools
# from openerp.exceptions import Warning
# from openerp.osv import fields, osv, orm

from datetime import date, timedelta, datetime
from odoo import models, fields, api, http
from odoo.http import request

import ipdb

class view(models.Model):
    _inherit = ['ir.ui.view']

    # def __init__(self, pool, cr):
    #     ipdb.set_trace()
    #     super(view, self).__init__(pool, cr)
    #     super(view, self)['type'].selection.append(('groupcal','GrouppedCalendar'))

    # def _check_selection_field_value(self, **args):
    #     print 'here w values'
    #     print args
    #     ipdb.set_trace()
    #     super(view, self)._check_selection_field_value(seld, args)
