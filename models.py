# -*- coding: utf-8 -*-
##############################################################################
#
#   Author: J. Zaburunov
#
##############################################################################
from datetime import date, timedelta, datetime
from lxml.builder import E
from odoo import models, fields, api, http
from odoo.http import request
from odoo.tools.translate import _
from odoo.exceptions import UserError
from odoo.models import BaseModel
from odoo.addons.base.ir.ir_ui_view import View

# TODO use amount_type = fields.Selection(selection_add=[('code', 'Python Code')])
VIEW_TYPES = [('tree', 'Tree'),
              ('groupcal', 'GrouppedCalendar'),
              ('form', 'Form'),
              ('graph', 'Graph'),
              ('pivot', 'Pivot'),
              ('calendar', 'Calendar'),
              ('diagram', 'Diagram'),
              ('gantt', 'Gantt'),
              ('kanban', 'Kanban'),
              ('search', 'Search'),
              ('qweb', 'QWeb')]


class view(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(VIEW_TYPES, string='View Type')


class IrActionsActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(VIEW_TYPES, string='View Mode', required=True)


class IrActionsActWindow(models.Model):
    _inherit = 'ir.actions.act_window'
    view_type = fields.Selection(VIEW_TYPES, string='View Type', required=True)


@api.model
def _get_default_groupcal_view(self):
    return self._get_default_calendar_view()


BaseModel._get_default_groupcal_view = _get_default_groupcal_view


@api.model
def _get_default_calendar_view(self):
    """ Generates a default calendar view by trying to infer
    calendar fields from a number of pre-set attribute names

    :returns: a calendar view
    :rtype: etree._Element
    """
    def set_first_of(seq, in_, to):
        """Sets the first value of ``seq`` also found in ``in_`` to
        the ``to`` attribute of the ``view`` being closed over.

        Returns whether it's found a suitable value (and set it on
        the attribute) or not
        """
        for item in seq:
            if item in in_:
                view.set(to, item)
                return True
        return False

    view = E.calendar(string=self._description)
    view.append(E.field(name=self._rec_name_fallback()))

    if self._date_name not in self._fields:
        for dt in ['date', 'date_start', 'x_date', 'x_date_start']:
            if dt in self._fields:
                self._date_name = dt
                break
        else:
            raise UserError(_("Insufficient fields for Calendar View!"))
    view.set('date_start', self._date_name)

    set_first_of(["user_id", "partner_id", "x_user_id", "x_partner_id"],
                 self._fields, 'color')

    # if not set_first_of(["date_stop", "date_end", "x_date_stop", "x_date_end"],
    #                     self._fields, 'date_stop'):
    #     if not set_first_of(["date_delay", "planned_hours", "x_date_delay", "x_planned_hours"],
    #                         self._fields, 'date_delay'):
    #         raise UserError(_("Insufficient fields to generate a Calendar View for %s, missing a date_stop or a date_delay") % self._name)

    return view


BaseModel._get_default_calendar_view = _get_default_calendar_view
