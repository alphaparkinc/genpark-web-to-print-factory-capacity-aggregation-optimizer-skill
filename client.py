class WebToPrintFactoryCapacityAggregationOptimizerClient:
    def aggregate_print_job(self, print_type='offset_color_flyers_a4', run_quantity=5000, deadline_days=3):
        return {
            'print_job_id': 'rks_job_7721',
            'print_specification': print_type,
            'run_quantity': run_quantity,
            'assigned_partner_printing_factory': 'KANAGAWA_FACTORY_BAY_04',
            'idle_factory_capacity_utilized_pct': 88.0,
            'cost_savings_vs_standard_print_pct': 48.0,
            'total_print_cost_jpy': 14800.0,
            'guaranteed_dispatch_date': '2026-08-27'
        }
