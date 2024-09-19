def get_basketball_position(position_code):
    positions = {
        'C': 'Center',
        'PF': 'Power Forward',
        'SF': 'Small Forward',
        'SG': 'Shooting Guard',
        'PG': 'Point Guard'
    }
    return positions.get(position_code.upper(), 'Invalid position')