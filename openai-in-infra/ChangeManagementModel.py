import pandas as pd
import matplotlib.pyplot as plt

# Define KPIs
kpi_names = ['Number of Changes', 'Change Success Rate', 'Change Lead Time']
kpis = pd.DataFrame(columns=kpi_names)

# Set up dummy data for changes
changes = [{'id': 1, 'success': True, 'lead_time': 5},
           {'id': 2, 'success': False, 'lead_time': 10},
           {'id': 3, 'success': True, 'lead_time': 3},
           {'id': 4, 'success': True, 'lead_time': 7}]

# Measure KPIs for changes
num_changes = len(changes)
success_rate = sum([c['success'] for c in changes])/num_changes
lead_time = sum([c['lead_time'] for c in changes])/num_changes

# Update KPIs dataframe with current values
kpis.loc[0] = [num_changes, success_rate, lead_time]

# Print KPIs
print(kpis)

# Plot KPIs
plt.plot(kpis['Number of Changes'], label='Number of Changes')
plt.plot(kpis['Change Success Rate'], label='Change Success Rate')
plt.plot(kpis['Change Lead Time'], label='Change Lead Time')
plt.legend()
plt.show()