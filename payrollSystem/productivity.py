# Productivity app

class ProductivitySystem:
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }
    
    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('______________________________')
        for employee in employees:
            employee.work(hours)
        print('')


class ManagerRole:
    def perform_duties(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


class SecretaryRole:
    def perform_duties(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


class SalesRole:
    def perform_duties(self, hours):
        print(f'{self.name} expends {hours} on the phone.')


class FactoryRole:
    def perform_duties(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')

