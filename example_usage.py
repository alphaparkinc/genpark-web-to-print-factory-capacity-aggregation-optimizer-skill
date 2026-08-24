from client import WebToPrintFactoryCapacityAggregationOptimizerClient

def main():
    client = WebToPrintFactoryCapacityAggregationOptimizerClient()
    res = client.aggregate_print_job('business_cards_matte_finish', 2000, 2)
    print('Print Job: ' + res['print_job_id'] + ' (' + str(res['run_quantity']) + ' units)')
    print('Factory: ' + res['assigned_partner_printing_factory'] + ' (Capacity: ' + str(res['idle_factory_capacity_utilized_pct']) + '%)')
    print('Cost: JPY ' + str(res['total_print_cost_jpy']) + ' (-' + str(res['cost_savings_vs_standard_print_pct']) + '% savings, Dispatch: ' + res['guaranteed_dispatch_date'] + ')')

if __name__ == '__main__':
    main()
