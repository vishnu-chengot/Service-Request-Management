from odoo import models, fields, api, _
from odoo.exceptions import ValidationError,UserError



class ServiceRequest(models.Model):
    _name = 'service.request'
    _description = 'Service Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, create_date desc'
    _rec_name = 'name'

    name = fields.Char(string='Request Name',help='Request Name will be auto-generated',readonly=True, tracking=True)
    customer_id = fields.Many2one('res.partner', string='Customer',help='Select the customer for this service request',required=True, tracking=True)
    request_date = fields.Date(string='Request Date',help='Date when the service request was created', default=fields.Date.today, tracking=True)
    category = fields.Selection([
        ('repair', 'Repair'),
        ('installation', 'Installation'),
        ('complaint', 'Complaint'),
    ], string='Category',help='Category of the service request',tracking=True)
    description = fields.Text(string='Description', help='Detailed description of the service request',tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='State', help='Current state of the service request', default='draft', tracking=True, group_expand='_expand_states')
    assigned_to = fields.Many2one('res.users', string='Assigned To', help='User assigned to handle this service request', tracking=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority', help='Priority of the service request', default='medium', tracking=True)
    active= fields.Boolean(string='Active', help='Indicates if the service request is active', default=True)

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('service.request') or '/'
        vals['name'] = seq
        record = super(ServiceRequest, self).create(vals)
        return record

    @api.model
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]


    @api.constrains('state', 'assigned_to')
    def _check_assigned_state(self):
        """Validate that assigned_to is required when state is 'assigned'"""
        for record in self:
            if record.state == 'assigned' and not record.assigned_to:
                raise ValidationError(_('Please assign a user before changing the status.'))


    def unlink(self):
        for rec in self:
            if rec.state not in ['draft', 'cancelled']:
                raise UserError(_("You can only delete service requests in Draft or Cancelled state."))
        return super(ServiceRequest, self).unlink()

    def write(self, vals):
        """Override write to handle state changes and send notifications"""
        result = super(ServiceRequest, self).write(vals)

        # Check if state changed to 'assigned' and send email
        if vals.get('state') == 'assigned':
            self._send_assignment_email()
        return result

    def _send_assignment_email(self):
        """Send email notification to assigned user"""
        if not self.assigned_to or not self.assigned_to.email:
            return
        # Get email template
        template = self.env.ref('service_request_management.email_template_service_request_assignment',
                                raise_if_not_found=False)
        if template:
            # Use email template if exists
            template.send_mail(self.id, force_send=True)
        # Also post message in chatter
        self.message_post(
            body=_('Service request has been assigned to %s') % self.assigned_to.name,
            message_type='notification'
        )


