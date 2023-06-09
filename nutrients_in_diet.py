def create_variable_dict(self):
    '''
        The variables are the amount of each food to include, denominated in units of 100g
    '''
    self.variable_dict = dict(
        (row['description'], self.solver.NumVar(0, 10, row['description']))
        for row in self.food_table)  
