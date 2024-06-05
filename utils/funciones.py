
# Llenar los valores 0 de 'budget' con la media de la columna

def fill_budget(df, mean_budget):
    df['budget_is_mean'] = 0
    df.loc[df.budget == 0, 'budget _is_mean'] = 1
    df.loc[df.budget == 0, 'budget'] = mean_budget
    return df


# Pasar los formato JSON a nominales
def get_dictionary(s):
    try:
        d = eval(s)
    except:
        d = {}
    return d