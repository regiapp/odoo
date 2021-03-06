# -*- coding: utf-8 -*-
# ######################################################################
# © 2015-2018 Marcos Organizador de Negocios SRL. (https://marcos.do/)
#             Eneldo Serrata <eneldo@marcos.do>
# © 2017-2018 iterativo SRL. (https://iterativo.do/)
#             Gustavo Valverde <gustavo@iterativo.do>
#             Manuel Marquez <buzondemam@gmail.com>

# This file is part of NCF Purchase

# NCF Purchase is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# NCF Purchase is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with NCF Manager.  If not, see <http://www.gnu.org/licenses/>.
# ######################################################################

from odoo import models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.multi
    def action_view_invoice(self):
        result = super(PurchaseOrder, self).action_view_invoice()
        supplier = self.partner_id
        if supplier.purchase_journal_id:
            result['context']['default_journal_id'] = \
                supplier.purchase_journal_id.id
        return result
