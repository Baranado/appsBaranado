class DietOptimizer(object):
    def __init__(self, nutrient_data_filename='nutrients.csv',
        nutrient_constraints_filename='constraints.csv'):
        self.food_table = # load data into a list of dicts
        self.constraints_data = # load data into a list of dicts
        self.solver = pywraplp.Solver('diet_optimizer', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
        self.create_variable_dict()
        self.create_constraints()
        self.objective = self.solver.Objective()
        for row in self.food_table:
            name = row['description']
            var = self.variable_dict[name]
            calories_in_food = row[calories_name]
            self.objective.SetCoefficient(var, calories_in_food)
        self.objective.SetMinimization()
