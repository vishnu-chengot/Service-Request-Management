odoo.define('request_dashboard.status_count', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');

    var RequestStatusDashboard = AbstractAction.extend({
        template: 'RequestStatusDashboard',

        init: function (parent, action) {
            this._super.apply(this, arguments);
            this.action = action;
        },

        start: function () {
            this._loadStatusData();
            console.log('Request Status Dashboard started');
        },

        _loadStatusData: function () {
            var self = this;
            return this._rpc({
                route: '/request/dashboard/status',
                params: {},
            }).then(function (result) {
                console.log(result, 'Request Status Data');
                self._renderStatusCards(result);
            });
        },

        _renderStatusCards: function (data) {
            var $container = this.$('#status_cards_container');
            $container.empty();

            var statusList = data.status_counts || [];

            if (statusList.length === 0) {
                // Show no data message
                var $noDataDiv = $('<div class="no-data-container">');
                $noDataDiv.html(
                    '<div class="no-data-icon">&#128202;</div>' +
                    '<div class="no-data-message">No request data available</div>' +
                    '<div class="no-data-subtitle">Start creating requests to see status overview</div>'
                );
                $container.append($noDataDiv);
                return;
            }

            statusList.forEach(function (status) {
                var $card = $('<div class="status-card" data-status="' + status.state + '">');
                $card.html(
                    '<div class="status-name">' + status.state + '</div>' +
                    '<div class="status-count">' + status.count + '</div>'
                );
                $container.append($card);
            });

            // Add click event for redirection
            this.$('.status-card').on('click', this._onStatusCardClick.bind(this));
        },

        _onStatusCardClick: function (ev) {
            var status = $(ev.currentTarget).data('status');

            this.do_action({
                type: 'ir.actions.act_window',
                name: 'Requests - ' + status,
                res_model: 'service.request',
                view_mode: 'tree,form',
                views: [[false, 'list'], [false, 'form']],
                domain: [['state', '=', status]],
                target: 'current',
            });
        },
    });

    core.action_registry.add('request_status_dashboard', RequestStatusDashboard);

    return RequestStatusDashboard;
});