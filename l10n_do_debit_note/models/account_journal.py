from odoo import models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    def _get_journal_ncf_types(self, counterpart_partner=False, invoice=False):
        ncf_types = super(AccountJournal, self)._get_journal_ncf_types(
            counterpart_partner=counterpart_partner, invoice=invoice
        )

        if (
            invoice
            and invoice.debit_origin_id
            or self.env.context.get("internal_type") == "debit_note"
        ):
            ncf_types = ["debit_note"]

        return ["e-%s" % d for d in ncf_types] \
            if self.company_id.l10n_do_ecf_issuer else ncf_types